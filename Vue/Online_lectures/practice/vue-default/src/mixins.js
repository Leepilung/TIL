import axios from 'axios';

// Mixin용 파일
export default {
  // mixin의 mounted가 우선적으로 실행됨
  mounted() {
    console.log('mixins moutned() :D');
  },
  unmounted() {},
  methods: {
    // $를 붙이는 이유는 충돌을 방지하기 위한 prefix개념. 아무렇게나 써도 상관없을듯
    async $api(url, method, data) {
      return (
        await axios({
          method: method,
          url: url,
          data: data,
        }).catch(e => {
          console.log(e);
        })
      ).data;
    },
  },
};
