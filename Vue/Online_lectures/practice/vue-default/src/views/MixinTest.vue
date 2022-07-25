<template>
  <div>
    <div>
      <PageTitle :title="title" />
      <ChildComponents
        :likes="likes"
        :isOk="true"
        :isArray="isArray"
        :isObject="isObject"
      />
    </div>
    <button type="button" @click="getProductList">데이터 조회하기</button>
    <button type="button" @click="getMixinProductList">
      Mixin으로 조회하기
    </button>
    <table>
      <thead>
        <tr>
          <th>이름</th>
          <th>나이</th>
          <th>직업</th>
        </tr>
      </thead>
      <tbody>
        <tr :key="i" v-for="(product, i) in productList">
          <td>{{ product.name }}</td>
          <td>{{ product.age }}</td>
          <td>{{ product.job }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import ApiMixin from '../api.js';
import MonitoringTest from '../monitoring.js';

// 컴포넌트 삽입 구문
import PageTitle from '../components/PageTitle';
import ChildComponents from '@/components/ChildComponents.vue';

export default {
  name: 'NaNi',
  mixins: [ApiMixin, MonitoringTest],
  components: { PageTitle, ChildComponents },
  data() {
    return {
      productList: [],
      title: '부모 컴포넌트에서 보낸 제목',
      likes: 23,
      isArray: [1, 5, 2, 3],
      isObject: { Author: '수박장수', title: '수박을 누가 먹었는가?' },
    };
  },
  mounted() {
    console.log('컴포넌트 mounted:D');
  },
  methods: {
    async getProductList() {
      this.productList = await this.$callApi(
        'https://8e6bbca8-7c9b-41c0-b91c-b932b245a118.mock.pstmn.io/productList',
        'GET',
        {},
      );
      console.log(this.productList);
    },

    async getMixinProductList() {
      this.productList = await this.$api(
        'https://8e6bbca8-7c9b-41c0-b91c-b932b245a118.mock.pstmn.io/productList',
        'GET',
        {},
      );
      console.log(this.productList);
    },
  },
};
</script>
<style lang=""></style>
