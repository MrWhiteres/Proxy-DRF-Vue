<script setup>

import { ref, watch } from 'vue';
import { useUserStore } from '@/state/user.js';
import BaseInput from '@/components/FormComponent/BaseInput.vue';
import PasswordInput from '@/components/FormComponent/PasswordInput.vue';
import axios from 'axios';

const userStore = useUserStore();
const active = ref(false);
const tab = ref('auth');

watch(userStore, () => {
  active.value = userStore.showModal;
});
watch(active, () => {
  userStore.showModal = active.value;
});

const baseForm = {
  email: null,
  password: null,
};

const loading = ref(false);
const rules = ref({
  required: (val) => !!val || 'Обов’язкове поле',
  email: (val) => /.+@.+\..+/.test(val) || 'Невірний емейл',
  min: (val) => val.length >= 6 || 'Мінімум 6 символів',
  sameAs: (val) => val === regForm.value.password || 'Паролі не співпадають',
  max: (val) => val.length <= 20 || 'Максимум 20 символи',
});
const authForm = ref({ ...baseForm });

const regForm = ref({
  ...baseForm,
  username: null,
  password2: null,
});

watch(tab, () => {
  if (tab.value === 'auth') {
    authForm.value = { ...baseForm };
  } else if (tab.value === 'reg') {
    regForm.value = {
      ...baseForm,
      username: null,
      password2: null,
    };
  }
});
const submit = async () => {
  loading.value = true;
  const activeForm = tab.value === 'auth' ? authForm.value : regForm.value;
  try {
    const response = await axios.post(
        tab.value === 'auth' ? '/login/' : '/register/',
        activeForm
    );
    userStore.changeAuthorized();
    userStore.accessToken = response.data.access;

    localStorage.setItem('refreshToken', response.data.refresh);
    userStore.showModal = false;
  } catch (e) {
    console.log(e);
  }
  loading.value = false;
};
</script>

<template>
  <q-dialog
      v-model="active"
      position="top"
  >
    <q-card style="margin-top: 20%; width: 700px">
      <q-form @submit.prevent="submit" autocomplete="off" autocorrect="off">
        <q-card-section>
          <q-tabs
              narrow-indicator
              align="center"
              v-model="tab"
          >
            <q-tab
                name="auth"
                label="Авторизація"
            />
            <q-tab
                name="reg"
                label="Рєєстрація"
            />
          </q-tabs>
          <q-separator />
        </q-card-section>
        <q-card-section>
          <q-tab-panels
              v-model="tab"
              animated
          >
            <q-tab-panel name="auth">
              <base-input
                  label="Email"
                  type="email"
                  v-model="authForm.email"
                  :disable="loading"
                  :rules="[
                    rules.required,
                    rules.email,
                  ]"
              />
              <password-input
                  v-model="authForm.password"
                  label="Пароль"
                  :rules="[
                    rules.required,
                    rules.min
                  ]"
                  :disable="loading"
              />
            </q-tab-panel>
            <q-tab-panel name="reg">
              <base-input
                  label="Email"
                  type="email"
                  :rules="[
                    rules.required,
                    rules.email,
                  ]"
                  v-model="regForm.email"
                  :disable="loading"
              />
              <base-input
                  label="Username"
                  type="text"
                  :rules="[
                    rules.required,
                    rules.min,
                    rules.max
                  ]"
                  v-model="regForm.username"
                  :disable="loading"
              />
              <password-input
                  v-model="regForm.password"
                  label="Пароль"
                  :rules="[
                    rules.required,
                    rules.min,
                  ]"
                  :disable="loading"
              />
              <password-input
                  v-model="regForm.password2"
                  label="Підтвердіть пароль"
                  :rules="[
                    rules.required,
                    rules.min,
                    rules.sameAs
                  ]"
                  :disable="loading"
              />
            </q-tab-panel>
          </q-tab-panels>

        </q-card-section>

        <q-card-actions
            align="center"
            style="margin-bottom: 10px"
        >
          <q-btn
              type="submit"
              color="primary"
              :loading="loading"
          >
            {{ tab === 'auth' ? 'Авторизуватись' : 'Рєєстрація' }}
          </q-btn>
        </q-card-actions>
      </q-form>
    </q-card>
  </q-dialog>
</template>

<style scoped>

</style>