import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// 최상위 컴포넌트 옵션
const app = createApp(App);

app.use(router);

// 앱 인스턴스는 mount()가 호출되기 전까지 아무 것도 렌더링 하지 않는다.
app.mount("#app");
