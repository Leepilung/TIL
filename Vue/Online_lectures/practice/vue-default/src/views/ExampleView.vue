<template lang="">
  <div>
    <select v-model="city">
      <!-- 위와 같이 해놓으면 city에 해당하는 값이 셀렉트 되어있음 -->
      <option value="02">서울</option>
      <option value="032">강원도</option>
      <option value="031">경기도</option>
    </select>
    <hr />
    <label>
      <input type="checkbox" value="서울" v-model="checked" />서울
      <!-- 체크 박스의 경우 checked 값이 설정된다. -->
    </label>
    <label>
      <input type="checkbox" value="강원도" v-model="checked" />강원도
    </label>
    <label>
      <input type="checkbox" value="경기도" v-model="checked" />경기도
    </label>
    <br />
    <span> 체크한 지역 : {{ checked }} </span>
    <!-- chcked 활용 방법 -->
    <hr />
    <label
      ><input
        type="radio"
        v-model="picked"
        v-bind:value="radio[0]"
      />서울</label
    >
    <label
      ><input
        type="radio"
        v-model="picked"
        v-bind:value="radio2"
      />강원도</label
    >
    <label
      ><input
        type="radio"
        v-model="picked"
        v-bind:value="radio3"
      />경기도</label
    >
    <br />
    <span>선택한 지역 : {{ picked }}</span>
    <!-- 속성 데이터 바인딩 파트 -->
    <hr />
    <!-- 이미지 데이터 바인딩 -->
    <img v-bind:src="url" style="height: 150px; width: auto" />
    <br />
    <input type="text" v-model="textValue" />
    <button type="button" v-bind:disabled="textValue === ''">Click</button>
    <hr />
    <!-- 클래스, 스타일 바인딩 -->
    <div class="container" v-bind:class="[activeClass, redClass]">
      Class Binding
    </div>
    <div v-bind:style="[baseStyle, addStyle, styleObject]">
      인라인 스타일 Binding
    </div>
    <hr />
    <select>
      <!-- v-for (~prama) in options 하면  -->
      <option :value="city.v" :key="i" v-for="(city, i) in options">
        {{ city.t }}
      </option>
    </select>
  </div>
</template>
<script>
export default {
  data() {
    // 데이터 () 안에 바인딩되는 태그들은
    return {
      city: '031',
      checked: [],
      picked: '',
      radio: ['서울', '강원도', '경기도'],
      radio1: '서울',
      radio2: '강원도',
      radio3: '경기도',
      url: 'https://dimg.donga.com/ugc/CDB/WEEKLY/Article/5b/b3/22/85/5bb32285000ed2738de6.jpg',
      textValue: '',
      activeClass: 'active',
      redClass: 'text-red',
      styleObject: {
        // inline 스타일은 카멜케이스로 해야함.
        backgroundColor: 'blue',
        color: 'red',
        fontWeight: 'bold',
      },
      baseStyle: 'background-color : gray; width : 100%; height : 150px;',
      addStyle: 'color : purple; font-weight: bold',
      options: [
        { v: '02', t: '서울' },
        { v: '031', t: '경기도' },
        { v: '032', t: '강원도' },
      ],
    };
  },
  setup() {},
  created() {}, // 뷰 컴포넌트가 생성되는 순간 실행
  mounted() {
    // DOM이 실제 로딩이 되는순간 실행
  },
  unmounted() {}, // 특정 컴포넌트에서 다른 컴포넌트로 이동되는 순간
  methods() {}, //
};
</script>
<style scoped>
.container {
  width: 100%;
  height: 200px;
}

.active {
  background-color: yellow;
  font-weight: bold;
}
.text-red {
  color: red;
}
</style>
