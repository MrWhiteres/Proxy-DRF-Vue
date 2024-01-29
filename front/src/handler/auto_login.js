import axios from 'axios';
import { useUserStore } from '@/state/user.js';

export const getToken = async () => {
  try {
    const response = await axios.post(
      '/new_token/',
      {
        refresh: localStorage.getItem('refreshToken')
      }
    );

    useUserStore().accessToken = response.data.access;
    localStorage.setItem('refreshToken', response.data.refresh);
    useUserStore().authorized = true;
  } catch (e) {

  }
};