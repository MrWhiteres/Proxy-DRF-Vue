import { createRouter, createWebHistory } from 'vue-router';
import IndexPage from '../views/IndexPage.vue';
import { useUserStore } from '@/state/user.js';
import Profile from '@/views/Profile.vue';

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexPage,
    props: true,
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile,
    beforeEnter: (to, from, next) => {
      if (useUserStore().authorized) {
        next();
      } else {
        next('/');
      }
    }
  }
];

const router = createRouter({

  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;