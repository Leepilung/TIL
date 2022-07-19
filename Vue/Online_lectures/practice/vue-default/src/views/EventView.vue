<!-- 이벤트 처리 : v-on (click, change, keyup ) -->
<template lang="">
	<div>
		<!-- vue에서 event를 주는 방법은 v-on을 하면 된다. -->
		<!-- v-on: 은 @로 축약이 가능하다.  -->
		<button tpye="button" @click="increaseFunc">Add +1</button>
		<p>The count is : {{ counter }}</p>
		<!-- 쉼표를 기준으로 아래와 같이 짜면 함수가 동시에 실행됨 -->
		<button tpye="button" @click="one(), two()">One Two</button>
		<hr />
		<select v-model="city" @change="changeSelect">
			<option value="서울">서울</option>
			<option value="부산">부산</option>
			<option value="제주">제주</option>
		</select>
		<p>{{ city }}</p>
		<hr />
		<!-- keyup중 enter가 keyup될때 실행됨. -->
		<input type="text" v-model="textValue" @keyup.enter="showValue" />
	</div>
</template>
<script>
export default {
	data() {
		return {
			counter: 0,
			city: '아직 도시 선택 안됨',
			textValue: '',
		};
	},
	methods: {
		increaseFunc() {
			this.counter += 1;
		},
		one() {
			alert('One');
		},
		two() {
			alert('Two');
		},
		changeSelect() {
			alert(this.city);
		},
		showValue() {
			alert(this.textValue);
			this.city = this.textValue;
		},
	},
};
</script>
<style lang=""></style>
