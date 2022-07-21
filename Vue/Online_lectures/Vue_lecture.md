# Vue3

# Vue CLI를 활용한 프로젝트 생성 방법

1. Default 옵션으로 생성
2. Manually select features 옵션으로 생성
3. Vue 프로젝트 매니저로 생성

# Default 옵션 활용

```
vue create {생성할 프로젝트 명}
```

입력 시 아래와 같은 선택지 등장

```
Vue CLI v5.0.8
? Please pick a preset: (Use arrow keys)
❯ Default ([Vue 3] babel, eslint)
  Default ([Vue 2] babel, eslint)
  Manually select features
```

Manually로 vue 프로젝트를 생성하면

preset으로 다음번 vue CLI로 프로젝트를 생성할 때

preset이 저장된다.

```
vue-basic 이란 이름으로 Manually 옵션으로 만든 preset

Vue CLI v5.0.8
? Please pick a preset:
❯ vue-basic ([Vue 3] babel, router, vuex, eslint)
  Default ([Vue 3] babel, eslint)
  Default ([Vue 2] babel, eslint)
  Manually select features
```

## 파일 구조

- node_modules : npm으로 설치된 패키지 파일이 모여있는 디렉토리

- public : 웹팩을 통해 관리되지 않는 정적 리소스가 모여 있는 디렉토리

- src/assets : 이미지, css, 폰트 등을 관리하는 디렉토리

- src/components : Vue 컴포넌트 파일이 모여 있는 디렉토리

- App.vue : 최상위(root) 컴포넌트

- main.jsd가장 먼저 실행되는 자바스크립트 파일, Vue 인스턴스의 생성을 담당한다.

- babel.config.js : 바벨(babel) 설정 파일

- package-lock.json : 설치된 package의 디펜던시 정보를 관리하는 파일

- package.json : 프로젝트에 필요한 package를 정의하고 관리하는 파일

# vue 프로젝트 매니저 이용하여 프로젝트 생성 방법

명령어는

```
vue ui
```

입력 시 localhost:8000 링크로 프로젝트를 선택하여 만들 수 있는 화면이 나온다.

온갖 대시보드 의존성, 플러그인, 설정, 작업목록 등을 GUI로 구동하고 자세한 파라미터들 까지 확인이 가능하다.

# Vue Router 설치 방법

vue cli등으로 생성한 프로젝트 디렉토리로 이동하여

```
vue router
```

를 입력하면 된다.

---

# computed

script 태그 안에서 사용되며

데이터 필드에 입력한 변수를 가지고 내부에 함수를 선언할 수 있음

> 예시

```vue
<template lang="">
	<div>
		<input type="text" v-model="lastName" />
		<input type="text" v-model="firstName" />
		<h1>Hello, {{ fullName }}</h1>
		<h1>Hello, {{ fullName }}</h1>
		<h1>Hello, {{ fullName }}</h1>
		<h1>Hello, {{ fullName }}</h1>
		<h1>Hello, {{ fullName }}</h1>
		<h1>Hello, {{ fullName }}</h1>
	</div>
</template>
<script>
export default {
	data() {
		return {
			firstName: '재석',
			lastName: '유',
		};
	},
	// computed의 경우 연산 자체를 단 한번만 한다.
	// 또한 computed는 안에 사용된 데이터 필드의 변경사항을 항상 감시하고 반영한다.
	computed: {
		fullName() {
			return this.lastName + this.firstName;
		},
	},
	// 그러나 getFullname()으로 매번 호출하면 매번 연산을 반복
	methods: {
		getFullName() {
			return this.lastName + this.firstName;
		},
	},
};
</script>
<style lang=""></style>
```

# Watch

computed와 굉장히 유사하지만 computed에 비해 코스트가 굉장히 큰 녀석

watch 안에 data에 선언된 데이터들을 함수 형태로 선언이 가능한데 그렇게 되면 해당 값들이 바뀔때 마다 값의 변경을 감지한다.


```vue
<template lang="">
	<div>
		<!-- input type을 바꿔도되고 v-model에 .number 추가해도 됨 -->
		<input type="number" v-model="x1" />
		<input type="text" v-model.number="x2" />
		<button type="button" @click="plusNumber">계산</button>
		<input type="text" v-model="y" />
	</div>
</template>
<script>
export default {
	data() {
		return {
			x1: 0,
			x2: 0,
			y: 0, // computed 사용할 시에는 함수명과 중복 안됨.
		};
	},
	// watch는 입력한 데이터 값의 변수를 계속해서 참조하기 떄문에 코스트가 꽤 큰 기능이라
	// 꼭 필요한 부분에서만 사용해야 한다.
	watch: {
		x1() {
			this.y = this.x1 + this.x2;
		},
		x2() {
			this.y = this.x1 + this.x2;
		},
	},
	computed: {
		y() {
			return this.x1 + this.x2;
		},
	},
	methods: {
		plusNumber() {
			this.y = this.x1 + this.x2;
		},
	},
};
</script>
```