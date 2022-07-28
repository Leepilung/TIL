

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


# VueX

Vue.js의 상태 관리를 위한 패턴이자 라이브러리이다. 당연히 컴포넌트 간의 통신이나 데이터 전달을 좀 더 유기적으로 관리하기 위해 사용된다.

> 필요성

뷰의 컴포넌트 방식인 props와 event emit으로는 거쳐야할 컴포넌트가 많아지는 경우 로직 자체가 복잡해지고 컴포넌트 간의 데이터 흐름또한 방해된다.

> 상태 관리 패턴

상태 관리 구성요소는 크게 3개로 나뉘는데

- state : 컴포넌트 간에 공유할 data
- view : 데이터가 표현될 template
- actions : 사용자 입력에 따라반응할 methos

```js
new Vue({
  // state
  data() {
    return {
      counter: 0
    };
  },
  // view
  template: `
    <div>{{ counter }}</div>
  `,
  // actions
  methods: {
    increment() {
      this.counter++;
    }
  }
});
```

> state 등록 방법

Vuex에서 state를 등록하는 방법은 아래와 같다.

```js
// store.js
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  // counter라는 state 속성을 추가
  state: {
    counter: 0
  }
});
```

state에 정의된 counter라는 속성에 접근하는 방법은 다음과 같다.

```html
<!-- App.vue(Parent) -->
<div id="app">
  Parent counter : {{ $store.state.counter }} <br />
  <button @click="addCounter">+</button>
  <button @click="subCounter">-</button>

  <!-- 기존 코드 -->
  <!-- <child v-bind:num="counter"></child> -->
  <child></child>
</div>
```

메소드들을 이용해 해당 state를 조절할 수 도 있다.

```js
// App.vue(Parent)
import Child from "./Child.vue";

export default {
  components: {
    child: Child
  },
  methods: {
    addCounter() {
      this.$store.state.counter++;
    },
    subCounter() {
      this.$store.state.counter--;
    }
  }
};
```

## Getter란 ?

Vuex와 같은 중앙 데이터 관리식 구조에서 발생하는 문제점 중 하나는 데이터에 접글할 때 중복된 코드를 반복 호출하는 경우이다.

```js
// 반복 호출 예시

// App.vue
computed: {
  doubleCounter() {
    return this.$store.state.counter * 2;
  }
},

// Child.vue
computed: {
  doubleCounter() {
    return this.$store.state.counter * 2;
  }
},
```
위와 같이 여러 컴포넌트에서 같은 로직을 중복 사용하는 것은 매우 비효율적이다.

Vuex의 데이터(state) 변경을 각 컴포넌트에서 수행하는게 아닌, Vuex에서 수행하도록 하고 각 컴포넌트에서는 해당 수행 로직을 호출한다면 가독성도 올라가고 성능에서의 이점이 발생한다.


```js
// Vuex 활용한 로직

// store.js (Vuex)
getters: {
  doubleCounter: function (state) {
    return state.counter * 2;
  }
},

// App.vue
computed: {
  doubleCounter() {
    return this.$store.getters.doubleCounter;
  }
},

// Child.vue
computed: {
  doubleCounter() {
    return this.$store.getters.doubleCounter;
  }
},
```

위의 예시는 매우 간단한 경우임에도 굉장히 편해진다.

만약
```js
this.store.state.todos.filter(todo => todo.done)...
```
이런 로직이 중복 사용된다면 보기만해도 어지럽다.

> Getters를 위한 코드 정리 

만약 다음과 같은 코드를 정리한다고 쳐보자

```js
<!-- App.vue -->
<div id="app">
  Parent counter : {{ this.$store.state.counter }}
  <!-- ... -->
</div>
```

template 에서의 표현식은 최대한 간소화되는 것이 권장되므로 다음과 같이 바꿀 수 있다.

```js
<!-- App.vue -->
<template>
<div id="app">
  Parent counter : {{ parentCounter }}
  <!-- ... -->
</div>
<template/>

<script>
computed: {
  parentCounter() {
    return this.$store.state.counter;
  }
},
<script/>

<!-- Child.vue -->
<template>
<div>
  Child counter : {{ childCounter }}
  <!-- ... -->
</div>
<template/>

<script>
computed: {
  childCounter() {
    return this.$store.state.counter;
  }
},
<script/>
```

computed를 활용하여 Template 코드를 간결화 시키고 가독성 또한 증가시켰다. 이어서 Getters에 등록과 사용을 할 차례이다.

> Getters 등록

getters에 등록하는 코드이다.
```js

// store.js
export const store = new Vuex.Store({
  // ...
  getters: {
    getCounter: function (state) {
      return state.counter;
    }
  }
});
```

> Getters 사용된다

getters에 사용하는 코드이다.

```js
// App.vue
computed: {
  parentCounter() {
    this.$store.getters.getCounter;
  }
},

// Child.vue
computed: {
  childCounter() {
    this.$store.getters.getCounter;
  }
},
```

getters를 각 컴포넌트에서 사용하려면 this.$store를 이용하여 getters에 접근, key값을 이용하면 된다.

> mapGetters

Vuex 에 내장된 helper 함수인 `mapGetters` 로 이미 위에서 한번 가독성이 올라간 코드를 더 직관적이게 작성할 수 있다.

```js
<!-- App.vue -->
<div id="app">
  Parent counter : {{ parentCounter }}
  <!-- ... -->
</div>

// App.vue
import { mapGetters } from 'vuex'

// ...
computed: mapGetters({
  parentCounter : 'getCounter' // getCounter 는 Vuex 의 getters 에 선언된 속성 이름
}),
```

# Mutations란 ?

Mutations는 Vuex의 데이터(state)를 변경하는 로직들을 의미한다.

Getters와의 차이점은

1. 인자를 받아 Vuex에 넘겨줄 수 있고
2. computed가 아닌 methods에 등록해야 한다는 점

Mutations 에는 순차적(동기적) 로직만 선언하고 Actions 에는 비 순차적, 비동기 처리 로직들을 주로 선언한다.

Mutations 의 성격상 안에 정의한 로직들이 순차적으로 일어나야 각 컴포넌트의 반영 여부를 제대로 추적할 수가 있기 때문이다.

동작 방식이 다소 특잏란데 commit을 이용하여 state를 변경한다.

<img src="https://joshua1988.github.io/images/posts/web/vuejs/vuex-2/vuex-mutations.png">

> Mutations 등록

getters와 마찬가지로 Vuex에 추가한다.

```js
// store.js
export const store = new Vuex.Store({
  // ...
  mutations: {
    addCounter: function (state, payload) {
      return state.counter++;
    }
  }
});
```

> Mutations의 사용

위의 getters의 예시에서는 state의 counter 값을 바로 접근하여 1을 올렸다.

```js
<!-- App.vue -->
<div id="app">
  Parent counter : {{ parentCounter }} <br>
  <button @click="addCounter">+</button>
  <!-- ... -->
</div>

methods: {
  addCounter() {
    this.$store.state.counter++;
  }
}
```
펴
methods: {
  addCounter() {
    // this.$store.state.counter++;
    this.$store.commit('addCounter');
  }
},
```

물론 위와 같은 형태에서도 addCounter라는 mutations를 추가해야 한다.

하나 확실하게 알고가야될 부분은 

```js
this.$store.mutations.addCounter;
```
의 형태와 같은 접근은 불가능하고, commit을 이용하여 mutations 이벤트를 호출해야 한다는 점이다.


> Mutations에 인자값 넘기기

각 컴포넌트에서 Vuex의 state를 조작하는데 필요한 특정 값들을 넘기고 싶을 때에는 `commit()` 에 두 번째 인자를 추가한다.

```js
this.$store.commit('addCounter', 10);
this.$store.commit('addCounter', {
  value: 10,
  arr: ["a", "b", "c"]
});
```

이를 Vuex에서 받는다면 다음과 같이 받을 수 있다.

```js
mutations: {
  // payload 가 { value : 10 } 일 경우
  addCounter: function (state, payload) {
    state.counter = payload.value;
  }
}
```

## Actions란 ?

Mutations에는 순차적 로직만 선언하고 Actions에는 비 순차적 로직이나 비동기 처리 로직을 주로 선언한다.

이렇게 나뉘어진 이유는 Mutations 에 대해 짚어봐야 하는데 Mutations 의 역할 자체가 State 관리에 주안점을 두고 있다.
 
상태관리 자체가 한 데이터에 대해 여러 개의 컴포넌트가 관여하는 것을 효율적으로 관리하기 위함인데 Mutations 에 비동기 처리 로직들이 포함되면 같은 값에 대해 여러 개의 컴포넌트에서 변경을 요청했을 때, 그 변경 순서 파악이 어렵기 때문이다.

이렇기 때문에 Actions와 Mutations로 로직을 나눠 `setTimeout()`이나 서버와의 http 통신 처리 같이 결과를 받아올 타이밍이 예측되지 않는 로직들을 Actions에 선언한다.

> Actions 등록

Vuex에 Actions를 등록하는 방법은 다른 속성과 유사하다. actions를 선언하고 action method를 추가해준다.

```js
// store.js
export const store = new Vuex.Store({
  // ...
  mutations: {
    addCounter: function (state, payload) {
      return state.counter++;
    }
  },
  actions: {
    addCounter: function (context) {
      // commit 의 대상인 addCounter 는 mutations 의 메서드를 의미한다.
      return context.commit('addCounter');
    }
  }
});
```

상태가 변화하는 걸 추적하기 위해 actions는 결국 mutations의 메소드를 호출(commit) 하는 구조가 된다.

그렇기 때문에  HTTP get 요청이나 setTimeout 과 같은 비동기 처리 로직들은 actions에 선언한다.

```js
// store.js
export const store = new Vuex.Store({
  actions: {
    getServerData: function (context) {
      return axios.get("sample.json").then(function() {
        // ...
      });
    },
    delayFewMinutes: function (context) {
      return setTimeout(function () {
        commit('addCounter');
      }, 1000);
    }
  }
});
```

> Actions 사용

actions를 호출할 때에는 아래와 같이 dispatch()를 이용한다.

```js
// App.vue
methods: {
  // Mutations 를 이용할 때
  addCounter() {
    this.$store.commit('addCounter');
  }
  // Actions 를 이용할 때
  addCounter() {
    this.$store.dispatch('addCounter');
  }
},
```

동작을 그림으로 나타낸다면 다음과 같다.

<img src="https://joshua1988.github.io/images/posts/web/vuejs/vuex-3/vuex-actions.png">

> Actions에 인자 값 넘기기

actions에 인자를 넘기는 방법은 Mutations와 유사하다.

```html
<!-- by 와 duration 등의 여러 인자 값을 넘길 경우, 객체안에 key - value 형태로 여러 값을 넘길 수 있다 -->
<button @click="asyncIncrement({ by: 50, duration: 500 })">Increment</button>
```

```js
// 인자를 받는 store.js
export const store = new Vuex.Store({
  actions: {
    // payload 는 일반적으로 사용하는 인자 명
    asyncIncrement: function (context, payload) {
      return setTimeout(function () {
        context.commit('increment', payload.by);
      }, payload.duration);
    }
  }
})
```s