<script setup>

import { defineProps, ref } from 'vue';

const props = defineProps({
  label: String
});

const pass = ref(true);
</script>

<template>
  <q-input
      outlined
      clearable
      :label="props.label"
      :type="pass ? 'password' : 'text'"
  >
    <template v-slot:append>
      <q-icon
          :name="pass ? 'visibility_off' : 'visibility'"
          class="cursor-pointer"
          @click="pass = !pass"
      />
    </template>
  </q-input>
</template>

<style scoped>

</style>