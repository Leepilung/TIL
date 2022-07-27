import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

createApp(App).use(store).use(router).mount('#app')

// 발급받은 Javascript 앱 키 추가
window.Kakao.init('9f7a0d7eec73ac12905101830b5d94d4')
