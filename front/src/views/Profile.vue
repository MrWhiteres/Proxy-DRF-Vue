<script setup>
import { onMounted, ref, watch } from 'vue';
import lodash from 'lodash';
import axios from 'axios';

const profile = ref({
  username: '',
  email: ''
});
const oldUsername = ref(null);
const isEditing = ref(false);
const isLoading = ref(false);
const isDisable = ref(true);

const loadUserProfile = async () => {
  isLoading.value = true;
  try {
    const response = await axios.get('/profile/');
    profile.value = response.data;
    oldUsername.value = profile.value.username;
  } catch (e) {

  }
  isLoading.value = false;
};

const saveUserProfile = async () => {
  isLoading.value = true;
  try {
    await axios.post('/profile/', profile.value);
  } catch (e) {

  }
  await loadUserProfile();
  isEditing.value = false;
};

watch(profile, () => {
  isDisable.value = lodash.isEqual(profile.value.username, oldUsername.value);
}, { deep: true });

onMounted(() => {
  loadUserProfile();
});
</script>

<template>
  <div class="profile-container">
    <q-card class="profile-card">
      <q-card-section>
        <h4>Профіль користувача</h4>
      </q-card-section>

      <q-card-section>
        <q-input
            filled
            outlined
            label="Ім'я користувача"
            v-model="profile.username"
            :loading="isLoading"
            :readonly="!isEditing"
        />
        <q-input
            filled
            outlined
            label="Email"
            :loading="isLoading"
            v-model="profile.email"
            readonly
        />
      </q-card-section>
      <q-card-section class="action">
        <q-btn
            color="primary"
            label="Редагувати"
            :loading="isLoading"
            @click="isEditing = !isEditing"
        />
        <q-btn
            v-if="isEditing"
            color="primary"
            :disable="isDisable"
            label="Зберегти"
            @click="saveUserProfile"
        />
      </q-card-section>
    </q-card>
  </div>
</template>

<style scoped>
.profile-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.profile-card {
  max-width: 400px;
  margin: 20px;
  padding: 20px;
  width: 700px;
  text-align: center;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.profile-card h4 {
  margin-bottom: 20px;
  font-size: 1.5em;
}

.action {
  display: flex;
  justify-content: space-between;
}
</style>
