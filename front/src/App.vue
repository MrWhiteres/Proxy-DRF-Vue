<script setup>

import Header from './components/Header/Header.vue';
import Drawer from './components/Drawer/Drawer.vue';
import { useUserStore } from '@/state/user.js';
import { watch } from 'vue';
import axios from 'axios';
import { getToken } from '@/handler/auto_login.js';

const userStore = useUserStore();
watch(userStore, () => {
  if (userStore.accessToken)
    axios.defaults.headers.common['Authorization'] = `Bearer ${userStore.accessToken}`;
  else
    delete axios.defaults.headers.common['Authorization'];
});

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
