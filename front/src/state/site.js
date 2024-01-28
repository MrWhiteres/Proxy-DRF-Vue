import { defineStore } from 'pinia';

export const useSiteStore = defineStore({
  id: 'site',
  state: () => (
    {
      leftDrawerOpen: false
    }
  ),
  actions: {
    changeLeftDrawer() {
      this.leftDrawerOpen = !this.leftDrawerOpen;
    }
  }
});