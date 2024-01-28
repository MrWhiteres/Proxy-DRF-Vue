<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  label: String
});
</script>

<template>
  <q-input
      style="margin-bottom: 5px"
      outlined
      clearable
      counter
      type="text"
      :label="props.label"
  />
</template>

<style scoped>

</style>