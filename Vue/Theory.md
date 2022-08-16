# Vue에서 data()에 있는 이미지 전달 시

```vue
<script>
export default {
  data() {
    return {
      people: [
        {
          // ... 생략
          profileUrl: require("../../assets/images/person1.jpg")
        },
        {
          // ... 생략
          profileUrl: require("../../assets/images/person2.jpg")
        },
        {
          // ... 생략
          profileUrl: require("../../assets/images/person3.jpg")
        },
        {
          // ... 생략
          profileUrl: require("../../assets/images/person4.jpg")
        }
      ],
    }
  }
}
</script>
```
위와 같이 require 구문을 사용하지 않으면 단순 String 취급이 되기 떄문에 사용해줘야 함