# JavaScript 4

## 내장 객체

앞에서 Object() 생성자 함수를 살펴봤다. 객체 리터럴 표기법을 사용해 객체를 생성하고 해당 constructor 속성에 접근할 때 반환된다. Object()는 내장된 생성자 중 하나다.

내장 객체는 세 그룹으로 나눌 수 있다.

- 데이터 랩퍼 객체 : Object, Array, Function, Boolean, Number, String등이 있다. 이들 객체는 자바스크립트에서 각각의 데이터 유형에 해당된다. Undefined와 null을 제외하고는 typeof 값에 대한 데이터 래퍼 객체가 있다.

- 유틸리티객체 : Math, Date, RegExp등이 있으며 편리하게 사용할 수 있다.

- 오류 객체 : 일반적인 Error 객체뿐만 아니라 예기치 않은 상황이 발생할 때 프로그램이 동작 상태를 복구하는데 도움디 되는 여러 특정 객체가 포함된다.

# Object

Object는 모든 자바스크립트 객체들의 부모다. 즉 생성한 모든 객체는 여기서 상속됐음을 의미한다. 새로운 빈 객체를 생성하려면, 리터럴 표기법이나 Object() 생성자 함수를 사용한다.

```js
var o = {};
var o = new Object();
```

위의 두 줄은 동일하다. 위에서 언급했듯이 빈 객체는 이미 여러 상속된 메소드와 속성을 가지고 있기 때문에 바로 사용이 가능하다. 여기서 빈 객체라는 것은 `{ }` 같은 객체로, 자동으로 받은 것 이외의 자체 속성을 가지지 않는 객체를 의미한다.

- o.constructor 속성은 생성자 함수의 참조를 반환한다.
- o.toString()은 객체를 표현하는 문자열을 반환하는 메소드다.
- o.valueOf()은 객체의 단일 값 표현을 반환한다. 이것은 종종 객체 자체로 취급된다.

메소드들의 실제 동작을 살펴보자. 우선 객체를 생성한다.

```
var a = new Object();
```

그 다음 toString()을 호출하면 객체의 문자열 표현식이 반환된다.

```js
a.toString();
("[object Object]");
```

toString() 메소드는 객체가 문자열 컨텍스트에서 사용될 때 자바스크립트에 의해 내부적으로 호출된다. 예를 들어 alert()는 문자열에서만 동작하므로 alert()함수를 호출할 때 객체를 전달하면, toString() 메소드가 자동으로 호출된다.

그렇기 때문에 다음 두 줄의 결과는 동일하다.

```js
alert(a); // [object Object]
alert(a.toString()); // [object Object]
```

문자열 컨텍스트의 또 다른 유형은 문자열 연결이다. 객체를 문자열과 연결하려고 하면 객체의 toString() 메소드가 먼저 호출된다.

```js
"An obejct" + o;
("An obejct[object Object]");
```

valueof() 메소드는 모든 객체가 제공하는 메소드 중 하나다. 생성자가 Object()인 단순 객체인 경우, valueof() 메소드는 객체 자체를 반환한다.

```js
o.valueOf() === o;
true;
```

요약하면 다음과 같다.

- var o = {}; 또는 var o = new Object();로 객체를 생성할 수 있다.
- 아무리 복잡한 객체더라도 Object 객체를 상속하므로 toString() 같은 메소드와 constructor 같은 속성을 제공한다.
