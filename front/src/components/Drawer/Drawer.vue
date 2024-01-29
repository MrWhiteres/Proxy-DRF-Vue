<script setup>
import { useSiteStore } from '@/state/site.js';
import { ref, watch } from 'vue';
import { useUserStore } from '@/state/user.js';
import { useRouter } from 'vue-router';

const store = useSiteStore();
const active = ref(false);
const router = useRouter();
watch(store, () => {
  active.value = store.leftDrawerOpen;
});
const pusher = async (value) => {
  await router.push({
    name: value
  });
};
</script>

<template>
  <q-drawer
      v-if="useUserStore().authorized"
      side="left"
      v-model="active"
      elevated
  >
    <q-scroll-area class="fit">
      <q-item
          clickable
          @click="pusher('profile')"
      >
        <q-item-label
            header
            class="text-h6"
        >
          Профіль
        </q-item-label>
      </q-item>
      <q-item
          clickable
          @click="pusher('proxy')"
      >
        <q-item-label
            header
            class="text-h6"
        >
          Лист серверів
        </q-item-label>
      </q-item>
    </q-scroll-area>
  </q-drawer>
</template>

<style scoped>

</style>