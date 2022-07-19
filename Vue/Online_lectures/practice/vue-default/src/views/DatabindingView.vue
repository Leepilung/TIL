<template lang="">
	<div>
		<h1>
			{{ sampleData }}
		</h1>
		<div>
			{{ sampleData2 }}
		</div>
		<div v-html="htmlString"></div>
		<!-- v-html : html태그안에 데이터바인딩-->
		<input type="text" v-model="valueModel" />
		<br />
		<input type="number" v-model.number="valueModel2" />
		<!-- 숫자로 받고싶다면 .number를 붙여줘야 한다 -->
		<br />
		<textarea v-model="textAreaModel"></textarea>
	</div>
</template>
<script>
export default {
	components_name: '',
	components: {},
	data() {
		// 데이터 () 안에 바인딩되는 태그들은
		return {
			textAreaModel: '테스트',
			valueModel: 'South Korea',
			valueModel2: 12,
			sampleData: 'Hi',
			sampleData2: 'Hi134',
			htmlString: '<p style="color:red;"> This is a red string. </p>',
		};
	},
	setup() {},
	created() {}, // 뷰 컴포넌트가 생성되는 순간 실행
	mounted() {
		// mounted 란 화면이 다 실행되고 실행되는 메소드
		console.log(this.valueModel2);
		let a = 3;
		console.log(a);
	}, // DOM이 실제 로딩이 되는순간 실행
	unmounted() {}, // 특정 컴포넌트에서 다른 컴포넌트로 이동되는 순간
	methods() {}, //
};
</script>
<style lang="" scoped></style>
