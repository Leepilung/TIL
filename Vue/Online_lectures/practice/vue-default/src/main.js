import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import mixins from './mixins';

import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

createApp(App)
  .use(router)
  .mixin(mixins)
  .use(VueSweetalert2)
  // 글로벌 하게 사용할 수 도 있음.
  .directive('focus', {
    mount(el) {
      el.focus();
    },
  })
  .mount('#app');
