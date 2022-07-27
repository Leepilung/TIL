export default {
  install: (app, options) => {
    // app.config.globalProperties.$~~ 처럼 등록하면 글로벌하게 모든 컴포넌트에서 사용이 가능함
    app.config.globalProperties.$translate = key => {
      return key.split('.').reduce((o, i) => {
        if (o) return o[i];
      }, options);
    };
  },
};
