<template>
  <div>
    <button type="button" @click="getProductList">데이터 조회하기</button>
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
import axios from 'axios';
export default {
  data() {
    return {
      productList: [],
    };
  },
  methods: {
    async getProductList() {
      this.productList = await this.api(
        'https://8e6bbca8-7c9b-41c0-b91c-b932b245a118.mock.pstmn.io/productList',
        'GET',
        {},
      );
      console.log(this.productList);
    },
    async api(url, method, data) {
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
</script>
<style lang=""></style>
