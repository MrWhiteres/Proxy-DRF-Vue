import { createRouter, createWebHistory } from 'vue-router';
import IndexPage from '../views/IndexPage.vue';
import { useUserStore } from '@/state/user.js';
import Profile from '@/views/Profile.vue';
import ProxyList from '@/views/ProxyList.vue';
import ProxyView from '@/views/ProxyView.vue';

import { getToken } from '@/handler/auto_login.js';

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexPage,
    props: true,
    beforeEnter: async (to, from, next) => {
      if (localStorage.getItem('refreshToken')) {
        await getToken();
      }
      if (useUserStore().authorized) {
        next('/profile');
      } else {
        next();
      }
    }
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
  },
  {
    path: '/proxy',
    name: 'proxy',
    component: ProxyList,
    props: true,
    beforeEnter: (to, from, next) => {
      if (useUserStore().authorized) {
        next();
      } else {
        next('/');
      }
    },
  },
  {
    path: '/proxy/:catchALL(.*)',
    component: ProxyView,
    beforeEnter: async (to, from, next) => {
      if (localStorage.getItem('refreshToken')) {
        await getToken();
      }
      if (useUserStore().authorized) {
        next();
      } else {
        next('/');
      }
    },
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
