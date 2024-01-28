import { defineStore } from 'pinia';

export const useUserStore = defineStore({
  id: 'user',
  state: () => (
    {
      showModal: false,
      authorized: false,
      user: {
        username: null,
        email: null,
      },
      accessToken: null,
    }
  ),
  actions: {
    changeAuthorized() {
      this.authorized = true;
    },
    clearData() {
      this.authorized = false;
      this.user = {
        username: null,
        email: null,
      };
      this.accessToken = null;
    },
    showModalHandler() {
      this.showModal = !this.showModal;
    }
  }
});