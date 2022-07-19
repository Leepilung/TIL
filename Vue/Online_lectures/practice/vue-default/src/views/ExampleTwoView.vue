<template lang="">
	<div>
		<select>
			<!-- v-for (~prama) in options 하면  -->
			<option :value="city.v" :key="i" v-for="(city, i) in options">
				{{ city.t }}
			</option>
		</select>
		<hr />
		<table>
			<thead>
				<tr>
					<th>제품명</th>
					<th>제품가격</th>
					<th>배송비</th>
					<th>제품 카테고리</th>
				</tr>
			</thead>
			<tbody>
				<!-- 리스트 렌더링 -->
				<tr :key="i" v-for="(product, i) in productList">
					<td>{{ product.product_name }}</td>
					<td>{{ product.price }}</td>
					<td>{{ product.delivery_price }}</td>
					<td>{{ product.category }}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>
<script>
export default {
	data() {
		return {
			options: [
				{ v: '02', t: '서울' },
				{ v: '031', t: '경기도' },
				{ v: '032', t: '강원도' },
			],
			productList: [
				{
					product_name: '기계식 키보드',
					price: 25000,
					delivery_price: 5000,
					category: '전자제품',
				},
				{
					product_name: '마우스',
					price: 45000,
					delivery_price: 5000,
					category: '전자제품',
				},
			],
		};
	},
	setup() {},
	created() {},
	mounted() {},
	unmounted() {},
	methods() {},
};
</script>
<style scoped></style>
