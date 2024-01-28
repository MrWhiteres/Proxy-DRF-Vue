import { Dialog, Loading, LoadingBar, Meta, Notify, Quasar } from 'quasar';
import axios from 'axios';
import VueAxios from 'vue-axios';
import pinia from '../state/index.js';
import router from '../router/index.js';

import 'quasar/src/css/index.sass';
import '@quasar/extras/material-icons/material-icons.css';
import '@quasar/extras/material-icons-outlined/material-icons-outlined.css';
import '@quasar/extras/material-icons-round/material-icons-round.css';
import '@quasar/extras/material-icons-sharp/material-icons-sharp.css';
import '@quasar/extras/material-symbols-outlined/material-symbols-outlined.css';
import '@quasar/extras/material-symbols-rounded/material-symbols-rounded.css';
import '@quasar/extras/material-symbols-sharp/material-symbols-sharp.css';
import '@quasar/extras/mdi-v7/mdi-v7.css';
import '@quasar/extras/fontawesome-v5/fontawesome-v5.css';
import '@quasar/extras/fontawesome-v6/fontawesome-v6.css';
import '@quasar/extras/ionicons-v4/ionicons-v4.css';
import '@quasar/extras/eva-icons/eva-icons.css';
import '@quasar/extras/themify/themify.css';
import '@quasar/extras/line-awesome/line-awesome.css';

export function registerPlugins(app) {
  axios.defaults.baseURL = 'http://localhost:8000/api/';
  app.use(Quasar, {
    plugins: {
      Notify,
      LoadingBar,
      Meta,
      Loading,
      Dialog,
    },
  }).use(VueAxios, axios).use(router).use(pinia).use(router);
}

