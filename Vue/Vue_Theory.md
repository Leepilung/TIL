

# 이벤트 핸들링

## 이벤트 종류

- click
- change
- keyup

> 문법

v-on:click || @click

## v-on

Vue에선 html 요소에 이벤트를 엮는 방법은 태그에 v-on을 입력하는 방법이 있다.

```vue
<template lang="">
	<div>
		<button tpye="button" @click="increaseFunc">Add +1</button>
		<p>The count is : {{ counter }}</p>
        <!-- 쉼표를 기준으로 아래와 같이 짜면 함수가 동시에 실행됨 -->
		<button tpye="button" @click="one(), two()">One Two</button>
	</div>
</template>

<script>
export default {
	data() {
		return {
			counter: 0,
		};
	},
	methods: {
		increaseFunc() {
            // Vue에서 상태를 참조하려면 this로 바인딩을 해줘야한다.
			this.counter += 1;
		},
		one() {
			alert('One');
		},
		two() {
			alert('Two');
		},
	},
};
</script>
```
v-on:click은 @click등으로 축약이 가능하다.

또한 함수를 여러개 사용할 수 있는 방법은 위의 구문처럼 쉼표를 기준으로 one(), two()와 같이 짜면 순차대로 함수가 실행된다.