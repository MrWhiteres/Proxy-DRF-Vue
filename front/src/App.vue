<script setup>

import Header from './components/Header/Header.vue';
import Drawer from './components/Drawer/Drawer.vue';
import { useUserStore } from '@/state/user.js';
import { watch } from 'vue';
import axios from 'axios';

const userStore = useUserStore();
watch(userStore, () => {
  if (userStore.accessToken)
    axios.defaults.headers.common['Authorization'] = `Bearer ${userStore.accessToken}`;
  else
    delete axios.defaults.headers.common['Authorization'];
});
const getToken = async () => {
  try {
    const response = await axios.post(
        '/new_token/',
        {
          refresh: localStorage.getItem('refreshToken')
        }
    );

    userStore.accessToken = response.data.access;
    localStorage.setItem('refreshToken', response.data.refresh);
    userStore.authorized = true;
  } catch (e) {

  }
};
if (localStorage.getItem('refreshToken')) {
  getToken();
}
</script>

<template>
  <q-layout view="hhh lpr fff">

    <Header />
    <Drawer />

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<style scoped>
</style>
