import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import mixins from './mixins';
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import i18nPlugin from './plugins/i18n';
import store from './store';
import vClickOutside from 'v-click-outside';

const i18nStrings = {
  en: {
    hi: 'Hello',
    save: 'Save',
  },
  ko: {
    hi: '안녕하세요!',
    save: '저장',
  },
};

createApp(App)
  .use(router)
  .mixin(mixins)
  .use(vClickOutside)
  .use(VueSweetalert2)
  // 글로벌 하게 사용할 수 도 있음.
  .directive('focus', {
    mount(el) {
      el.focus();
    },
  })
  .use(i18nPlugin, i18nStrings)
  // store 삽입 구문
  .use(store)
  .mount('#app');
