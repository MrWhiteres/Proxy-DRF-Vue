<script setup>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import lodash from 'lodash';

const router = useRouter();
const rows = ref([]);
const old_rows = ref([]);
const deleted = ref([]);
const new_element = ref({
  name: null,
  site: null,
});
const isLoading = ref(false)

const rules = ref({
  required: (val) => !!val || 'Обов’язкове поле',
  min: (val) => val.length >= 5 || 'Мінімум 5 символів',
  max: (val) => val.length <= 100 || `Максимум ${100} символів`,
  url: (val) => validateURL(val) || `Невірна адреса`,
});

const validateURL = (val) => {
  try {
    new URL(val);
    return true;
  } catch (e) {
    return false;
  }
};

const clear = () => {
  Object.keys(new_element.value).forEach((key) => {
    new_element.value[key] = null;
  });

  activate.value = false;
};
const submit = async () => {
  isLoading.value = true
  try {
    await axios.post('/proxy/', { data: rows.value, deleted: deleted.value });
    await get_data_async();
  } catch (e) {
  }
  isLoading.value = false
};

const get_data_async = async () => {
  rows.value = [];
  isLoading.value = true
  try {
    const response = await axios.get('/proxy');
    rows.value = [...response.data.response];
  } catch (e) {
  }
  isLoading.value = false
};
get_data_async();
const activate = ref(false);
const deleteItem = async (value) => {
  isLoading.value = true
  try {
    await axios.delete(`/proxy`, { data: { id: value } });
  } catch (e) {

  }
  await get_data_async();
};

watch(rows.value, () => {
  console.log(lodash.isEqual(rows.value, old_rows.value));
});

const columns = [
  { name: 'name', label: 'Назва', align: 'center', field: 'name', sortable: true },
  { name: 'site', label: 'URL', align: 'center', field: 'site', sortable: true },
  { name: 'transition', label: 'Кількість переходів', align: 'center', field: 'transition', sortable: true },
  { name: 'traffic', label: 'Використано трафіку', align: 'center', field: 'traffic', sortable: true },
  { name: 'created_at', label: 'Дата створення', align: 'center', field: 'created_at', sortable: true },
  { name: 'link', label: 'Дія', align: 'center', field: 'link', sortable: false }
];

watch(activate, () => {
  if (!activate.value) {
    clear();
  }
});

const addSite = async () => {
  try {
    await axios.post('/proxy/', new_element.value);
  } catch (e) {
  }
  clear();
  await get_data_async();
};

const openSite = async (url) => {
  if (url.charAt(url.length -1) === '/') {
    url = url.slice(0, -1);
  }
  await router.push(`/proxy/${url}`);
};
</script>

<template>
  <div class="page">
    <h2 class="list-title">Лист сайтів</h2>
    <q-table
        flat
        bordered
        :rows="rows"
        :columns="columns"
        row-key="id"
        binary-state-sort
        :loading="isLoading"
    >
      <template v-slot:top>
        <q-card-section style="display: flex; justify-content: space-between; align-items: center; width: 100%">
          <q-btn
              icon="add"
              label="Додати новий сайт"
              style="text-transform: capitalize"
              @click="activate = true"
          />
          <q-btn
              icon="mdi-reload"
              style="text-transform: capitalize"
              @click="get_data_async"
          />
        </q-card-section>
      </template>
      <template v-slot:header="props">
        <q-tr :props="props">
          <q-th
              v-for="col in props.cols"
              :key="col.name"
              :props="props"
          >
            {{ col.label }}
          </q-th>
        </q-tr>
      </template>
      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td
              key="name"
              :props="props"
          >
            {{ props.row.name }}
          </q-td>
          <q-td
              key="site"
              :props="props"
          >
            {{ props.row.site }}
          </q-td>
          <q-td
              key="transition"
              :props="props"
          >
            {{ props.row.transition }}
          </q-td>
          <q-td
              key="traffic"
              :props="props"
          >
            {{
              Math.round(props.row.traffic / (
                  1024 * 1024
              ) * 1000) / 1000
            }} МБ

          </q-td>
          <q-td
              key="created_at"
              :props="props"
          >
            {{ props.row.created_at }}
          </q-td>
          <q-td
              key="link"
              style="display: flex; gap: 6px; justify-content: center; align-items: center"
          >
            <q-btn
                color="primary"
                label="Перейти"
                @click="() => openSite(props.row.site)"
            />
            <q-btn
                icon="delete"
                @click="deleteItem(props.row.id)"
            />
          </q-td>
        </q-tr>
      </template>
      <template v-slot:no-data>
        <q-banner
            inline-actions
            rounded
            style="width: 100%"
        >
          Лист сайтів порожній
        </q-banner>
        <q-card-section style="display: flex; justify-content: space-between; align-items: center; width: 100%">
          <q-btn
              icon="mdi-content-save-move-outline"
              label="Зберегти"
              style="text-transform: capitalize"
              @click="submit"
          />
        </q-card-section>
      </template>
    </q-table>
  </div>
  <q-dialog
      v-model="activate"
      position="top"
  >
    <q-card style="margin-top: 5%; width: 700px">
      <q-card-section style="text-align: center">
        <div class="text-h6">Додати новий сайт</div>
      </q-card-section>
      <q-separator />
      <q-card-section>
        <q-form
            style="display: flex; flex-direction: column; gap: 10px;"
            @submit.prevent="addSite"
        >
          <q-card-section style="display: flex; flex-direction: row; gap: 10px; padding: 0; margin: 0">
            <q-input
                outlined
                v-model="new_element.name"
                label="Назва"
                :rules="[rules.required, rules.min, rules.max]"
                class="input-q"
                dense
            />
          </q-card-section>

          <q-input
              outlined
              v-model="new_element.site"
              :rules="[rules.required, rules.min, rules.url]"
              label="URL"
              dense
          />
          <q-btn
              type="submit"
              color="primary"
              label="Додати"
          />
        </q-form>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<style scoped>
.list-title {
  font-size: 20px;
  margin-bottom: 10px;
}

.input-q {
  min-width: 49%;
}

.page {
  padding: 16px;
}
</style>
