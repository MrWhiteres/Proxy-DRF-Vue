<script setup>
import { useRoute } from 'vue-router';
import axios from 'axios';
import { ref } from 'vue';

const route = useRoute();
const site = ref(null);

const get_site_data = async () => {
  try {
    const response = await axios.post(`${route.fullPath}`);
    if (response.data.site)
    {
      site.value = response.data.site;
    }
    site.value = response.data.site;
  } catch (e) {
    console.log(e)
  }
};
get_site_data();
</script>

<template>
  <q-card-section>
    <div v-html="site"/>
  </q-card-section>
</template>

<style scoped>

</style>