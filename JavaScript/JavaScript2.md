# JavaScript3 내용 정리

# 객체

자바스크립트는 고전적인 객체지향 프로그래밍을 변형해 사용한다. 객체지향 프로그래밍은 가장 널리 사용되는 프로그래밍 패러다임 중 하나이며, 자바와 C++같은 대부분의 프로그래밍 언어의 주류가 됐다.

앞에서 알아봤듯, 배열은 값의 목록일 뿐이다. 각 값은 0에서 시작하여 각 값에 대해 1씩 증가하는 인덱스(숫자 키)를 갖고 있다.

객체는 배열과 비슷하지만, 직접 키를 정의한다는 점이 다르다. 숫자 인덱스만 사용할 수 있는 것은 아니며, first_name, age등과 같이 친숙한 키를 사용할 수 있다.

```mm
var hero = {
  breed : 'Turtle',
  occupation : 'Ninja'
};
```

위의 코드에서

- 객체를 참조하는 변수의 이름은 hero다.
- 배열을 정의하는데 사용하는 '[' 과 ']' 대신, 객체에는 '{' 와 '}'를 사용한다.
- 객체에 포함된 요소(속성 Property)는 쉼표로 구분한다.
- 키 / 값의 쌍은 key:value와 같이 콜론으로 나눈다.

키는 선택적으로 따옴표로 묶을 수 있다. 예를 들어 다음 키는 모두 동일하다.

```mm
var hero = {occcpation : 1}
var hero = {"occupation": 1}
var hero = {'occupation': 1}
```

속성의 이름에 따옴표를 사용하지 않는 것이 좋다(입력이 줄어들기 때문) 하지만 따옴표를 사용해야 하는 경우가 있다.

- 속성 이름이 자바스크립트 예약어(reserve word)중 하나인 경우
- 공백이나 특수문자(`문자`,`숫자`,`_`,`$` 이 이외의 문자)가 포함된 경우
- 숫자로 시작되는 경우

즉 속성의 이름으로 선택한 이름이 자바스크립트 변수로 유효한 이름이 아니면, 따옴표로 묶어야 한다.

```mm
var o = {
  $somthing : 1,
  'yesorno' : 'yes',
  '!@)#!@()' : true
};
```

위의 예제들로 사용한것들 전부 유효한 객체이다. 두 번째, 세 번째 속성에는 따옴표가 필요하다. 그렇지 않을경우 오류가 발생한다.

## 요소, 속성, 메소드 및 멤버

배열에 대해 말할 때, 배열에 요소(element)가 들어 이싿고 말한다. 객체에 대해선 객체에 속성(property)이 들어있다고 말한다. 자바스크립트에서는 큰 차이가 없으며 사람들에게 익숙한 용어들이다.

함수는 데이터일 뿐이므로, 객체의 속성은 함수를 가르킬 수 있다. 함수를 가리키는 속성을 `메소드(method)`라고 한다.

다음 예제에서 talk는 메소드이다.

```mm
var dog = {
  name : 'Benji',
  talk : function() {
    alert('Woof, woof!');
  }
};
```

## 해시와 연관 배열

일부 프로그래밍 언어에는 다음 둘 사이에 차이가 있다.

- 일반 배열, 인덱스 배열 또는 열거 배열로도 불린다.
- 연관 배열, 해시 또는 딕셔너리로도 불린다.

자바스크립트는 배열을 사용해 인덱스 배열과 객체를 표시해서 연관배열을 나타낸다. 자바스크립트에서 해시를 원한다면 객체를 사용하면 된다.

## 객체의 속성 접근

객체의 속성에 접근하는 방법은 두 가지가 있다.

- 대괄호 표기법을 사용하는 방법(ex : hero['occupation']0
- 도트 표기법을 사용하는 방법(ex : hero.occupation)

도트 표기법은 읽고 쓰기에 더 쉽지만, 언제나 사용할 수 있는 것은 아니다.

왜냐하면 속성 이름을 인용하는 경우에도 동일한 규칙이 적용되기 때문이다. 또한 속성의 이름이 유효한 변수 이름이 아닌 경우, 도트 표기법을 사용할 수 없다.

다음의 hero 객체를 통해 살펴보자.

```mm
var hero = {
  breed : 'Turtle',
  occupation : 'Ninja'
};
```

도트 표기법으로 속성에 접근하는 예이다.

```mm
hero.breed;
"Turtle"
```

대괄효 표기법으로 속성에 접근하는 예도 살펴보자

```mm
hero['occupation'];
"Ninja"
```

존재하지 않는 속성에 접근하면 다음과 같이 undefined를 반환한다.

```mm
'Hair color is' + hero.hair;
"Hair color isundefined"
```

또한 객체는 다른 객체를 포함한 모든 데이터를 포함할 수 있다.

```mm
var book = {
  name : 'Catch',
  publish : 1961,
  author : {
    firstname : 'Joseph',
    lastname : 'Hellen'
  }
};
```

book 객체의 author 속성에 포함된 객체의 firstname 속성을 가져오려면 다음과 같은 코드를 사용한다.

```mm
book.author.firstname
"Joseph"
```

대괄호 표기법을 사용한 예제를 살펴보자.

```mm
book['author']['firstname']
"Joseph"
```

그리고 두 표기법을 혼합해도 동작한다.

```mm
book.author['firstname']
"Joseph"

book.publish
1961

book['author'].lastname
"Hellen"
```

그리고 대괄호과 필요한 또 다른 경우는 접근해야 하는 속서으이 이름을 미리 알 수 없는 경우이다.
런타임시 동적으로 변수에 저장되는 경우가 해당된다.

```mm
var key = 'firstname';
book.author[key];
"Joseph"
```

예제에서 key값은 변수값으로 주어지며 미리 지정되지 않는다.

## 객체의 메소드 호출

메소드는 함수의 속성 중 하나일 뿐이므로 속성에 접근하는 것과 동일한 방법으로 메소드에 접근할 수 있다. 메소드 호출은 다른 함수 호출과 동일하다. 메소드 이름 뒤에 괄호를 추가하면 실행된다.

```mm
var hero = {
  breed : 'Turtle',
  occupation : 'Ninja',
  say : function () {
    return ' I am ' + hero.occupation;
  }
};

hero.say();
"I am Ninja"
```

메소드에 전달할 매개변수가 있으면 일반 함수처럼 처리할 수 있다.

```mm
hero.say('a', 'b', 'c');    // " I am Ninja"
```

배열과 유사한 대괄호를 사용하여 속성에 접근할 수 있기 때문에, 대괄호를 사용해 메소드에 접근하고 호출할 수 있다.

```mm
hero['say'] // " I am Ninja"
```

그러나 이 방법은 코드 작성시에는 메소드 이름을 알 수 없고 런타임시에 정의되는 경우가 아니라면, 일반적인 관행은 아니다.

```mm
var method = 'say';
hero[method](); // " I am Ninja"
```

## 속성 / 메소드 변경

자바스크립트를 사용하면 언제든지 기존 객체의 속성과 메소드를 변경할 수 있다. 새로운 속성의 추가, 삭제도 포함된다. 빈 객체로 시작하고 나중에 속성을 추가할 수도 있다.

속성이 없는 객체는 다음과 같다.

```
var hero ={};
```

> "빈" 객체

이 색션에서 "빈(blank)" 객체인 var hero = {}으로 시작했다. 이 객체가 실제로 비어 있고 쓸모 없는 것은 아니기 때문에, 따옴표 안에 공백이 있다.

1. 존재하지 않는 속성에 접근하는 코드는 다음과 같다.
   ```mm
   typeof hero.breed;
   "undefined"
   ```
2. 두 개의 속성과 메소드를 추가한다.
   ```mm
   hero.breed = 'turtle';
   hero.name = 'Leonardo';
   hero.sayName = function () {
       return hero.name;
   };
   ```
3. 메소드를 호출한다.
   ```mm
   hero.sayName();
   "Leonardo"
   ```
4. 속성을 삭제한다.
   ```mm
   delete hero.name;
   true
   ```
5. 메소드를 다시 호출하면 더 이상 삭제된 name속성을 찾을 수 없다.
   ```mm
   hero.sayName();
   "undefined"
   ```

## this 값 사용

앞의 예제에서 sayName() 메소드는 hero.name을 사용해 hero 객체의 name 속성에 접근했다.

그러나 메소드 내부에 있을 때 메소드가 속한 객체에 접근할 수 있는 또 다른 방법이 있다. 이 메소드는 특별한 값 this를 사용한다.

- this는 -> 선언이 실행 되는 시점의 나의 문맥을 나타낸다.

```mm
var hero ={
  name : 'Rafaelo',
  sayName :  function () {
    return this.name;
  }
};
hero.sayName();
"Rafaelo"
```

따라서 this를 사용하면 실제로 이 객체 또는 현재 객체에 접근할 수 있다.

## 생성자 함수

객체를 생성하는 방법에는 생성자 함수를 사용하는 방법도 있다. 예제를 통해 살표보자.

```mm
function Hero() {
  this.occupation = 'Ninja'
}
```

이제 이 함수를 사용해 객체를 생성하려면, 다음과 같이 new 연산자를 사용한다.

```mm
var hero = new Hero();
hero.occupation;
"Ninja"
```

생성자 함수를 사용하면 새로운 객체를 만들 때 매개변수를 사용할 수 있는 이점이 있다.
하나의 매개변수를 받아 이것을 name 속성에 할당하도록 생성자를 수정해 보자.

```mm
function Hero(name) {
	this.name = name;
  this.occupation = 'Ninja';
  this.whoAreYou = function () {
    return "I'm " +
      this.name +
      " and I'm a " +
      this.occupation;
	};
}
```

이제 동일한 생성자를 사용해 서로 다른 객체를 생성할 수 있다.

```mm
var h1 = new Hero('Michelangelo');
var h2 = new Hero('Donatello');

h1.whoAreYou();
"I'm Michelangelo and I'm a Ninja"

h2.whoAreYou();
"I'm Donatello and I'm a Ninja"
```

생성자로 설계된 함수를 new 연산자를 생략해 호출해도 오류가 아니다. 하지만 기대했던 결과를 제공하지는 않는다.

```mm
var h = Hero('Leonardo')
typeof h;
"undefined"
```

new 연산자가 없으므로 새로운 객체가 생성되지 않앗다. 함수가 다른 일반 함수처럼 호출됐으므로 변수 h에는 함수가 반환하는 값이 포함된다. 이 함수는 아무것도 반환하지 않는다(return 문이 없다). 따라서 실제로 h에 할당된 undefined를 반환한다. 이 경우 this는 전역 개체를 참조한다.

## 전역 개체

앞에서 전역 변수에 대해(그리고 가급적 사용하지 말 것) 조금 알아보았다. 그리고 자바스크립트 프로그램은 호스트 환경에서 실행된다는 것도 알고 있다. 호스트 환경은 전역 객체를 제공하고, 모든 전역 변수는 전역 객체의 속성으로 접근할 수 있다.

호스트 환경이 웹브라우저인 경우, 전역 객체는 window로 호출된다. 전역 객체에 접근하는 또 다른 방법은(대부분의 환경에서도 동일) 생성자 함수 바깥에서 this 키워드를 사용하는 것이다.

예를 들어, 다음과 같이 함수 외부에서 전역 변수를 선언할 수 있다.

```mm
var a = 1;
```

그런 다음, 이 전역 변수에 다양한 방법으로 접근할 수 있다.

- 변수 a로
- 전역 객체의 속성으로(ex, window['a'] = 1 or window.a = 1 )
- this로 참조되는 전역 객체의 속성으로 (this.a = 1)

생성자 함수를 정의하고 new 연산자 없이 호출하는 경우로 돌아가 보자. 이 경우, this는 전역 객체를 참조하고 this에 설정된 모든 속성은 window의 속성이 된다.

생성자 함수를 선언하고 new 없이 호출하면 "undefined"를 반환한다.

```mm
function hero(name) {
  this.name = name;
}

var h = Hero('Leonardo')
typeof h;
"undefined"
typeof h.name;
TypeError: can't access property "name", h is undefined
```

Hero 함수 안에 this 키워드가 있기 때문에, name이라는 전역 변수(전역 객체의 속성)이 생성됐다.

```mm
name;
"Leonardo"
window.name;
"Leonardo"
```

new를 사용해 동일한 생성자 함수를 호출하면, 새 객체가 반환되고 this가 이 객체를 참조한다.

```mm
var h2 = new Hero('Michelangelo');
typeof h2;
"object"
h2.name;
"Michelangelo"
```

앞에서 봤던 내장된 전역 함수 역시 window 객체의 메소드로 호출할 수 있다. 따라서 다음 두 호출의 결과는 같다.

```mm
parseInt('101 dalmatians');
101
window.parseInt('101 dalmatians');
101
```

## 생성자 속성

객체가 생성되면 특별한 constructor 속성이 백그라운드로 객체에 할당된다. 이것은 this 객체를 생성하는데 사용되는 생성자 함수의 참조를 포함한다.

```mm
h2.constructor;
function Hero(name) {
  this.name = name;
}
```

constructor 속성이 함수에 대한 참조를 포함하고 있으므로, 이 함수를 호출해 새 객체를 생성할 수도 있다. 다음 코드는 "객체 h2가 어떻게 생성됐는지 모르겠지만. 이와 비슷한 다른 객체가 필요하다"고 말한다.

```mm
var h3 = new h2.constructor('Rafaello');
h3.name;
"Rafaello"
```

객체 리터럴 표기법을 사용해 객체를 만든 경우, 객체의 생성자는 내장된 Object() 생성자 함수다.

```mm
var o = {};
o.constructor;
function Object()
typeof o.constructor;
"function"
```

## instanceof 연산자

instanceof 연산자를 사용하면 객체가 constructor 함수로 생성됐는지 테스트할 수 있다.

```mm
function Hero() {}
var h = new Hero();
var o = {};
h instanceof Hero;
true
h instanceof Object;
true
o instanceof Object;
true
```

함수 이름 뒤에 괄호를 넣지 않도록 주의하자(h instanceof Hero()를 사용하지 않는다.) 이것은 이 함수를 호출하지 않고 다른 변수와 마찬가지로 이름으로 참조하기 때문이다.

## 객체를 반환하는 함수

constructor 함수와 new 연산자를 사용해 객체를 생성하는 방법 외에도 일반 함수를 사용해서 new 연산자 없이 객체를 생성할 수도 있다. 약간의 준비 작업을 수행하면 반환 값으로 객체를 가지는 함수를 만들 수 있다.

다음은 객체를 생성하는 간단한 factory() 함수다.

```mm
function factory(name) {
  return {
    name : name
  };
}
```

factory() 함수를 사용하는 다음 예제를 살펴보자.

```mm
var o = factory('one');
o.name;
"one"
o.constructor;
function Object()
```

constructor 함수와 함께 this 키워드 대신 return 객체를 사용할 수도 있다. 즉, constructor 함수의 디폴트 행동을 수정할 수 있음을 의미한다.

```mm
function C() {
  this.a = 1;
}
var c = new C();
c.a;

function C2() {
  this.a = 1;
  return {b: 2};
}
var c2 = new C2();
typeof c2.a
"undefined"
c2.b;
2
```

a 속성을 포함하는 this 객체를 반환하는 대신, 생성자는 b 속성을 포함하는 다른 객체를 반환했다. 이것은 반환 값이 객체인 경우에만 가능하다. 그렇지 않고 객체가 아닌 것을 반환하려고 시도할 경우, 생성자는 일반적인 동작을 수행하고 this를 반환한다.

생성자 함수 안에서 객체를 생성하는 방법을 생각해 보면 this라는 변수는 함수의 맨 위에서 정의된 다음 마지막에 반환된다고 생각할 수 있다.

```mm
function C() {
  // var this = {}; // 의사 코드, 수행할 수 없다.
  this.a = 1;
  // return this
}
```

## 객체 전달

객체를 다른 변수에 할당하거나 함수에 전달하려면 해당 객체에 대한 참조만 전달하면 된다.

또한 참조를 변경하면 실제로는 원본 객체를 수정하는 것이다.

```mm
var original = {home : 1};
var mycopy = original;
mycopy.home;
1
mycopy.home = 100;
100
original.home;
1
```

객체를 함수에 전달할 때도 똑같이 적용된다.

```mm
var original = {home : 100};
var nullify = function (o) { o.home = 0; };
nullify(original);
original.home
0
```

## 객체 비교

객체를 비교할 때, 동일한 객체에 대한 두 개의 참조를 비교할 때만 true가 된다. 똑같은 메소드와 속성을 가지고 있는 서로 다른 두 개별 객체를 비교하면 결과는 false가 된다.

예를 들어

```mm
var fido = {breed : 'dog'}
var benji = {breed : 'dog'}

benji === fido;
false
benji == fido;
false
```

로 서로 다르다. 그러나 여기서 mydog라는 변수를 만들어 비교하면

```mm
var mydog = benji;

mydog === benji
true
mydog == benji
true
mydog == fido
false
mydog === fido;
false
```

가 출력된다.

# ES6 객체 리터럴

ES6에서는 속성 초기화및 함수 정의에 대한 몇 가지 약식 구문을 제공한다.

```mm
let a =1
let b =2
let val = {a : a, b: b}

console.log(val)
Object { a: 1, b: 2 }
```

속성값을 할당하는 일반적인 방법이다. 변수의 이름과 속성 키가 같은 경우 ES6에서는 약식 구문을 사용할 수 있다.

메소드 정의에서도 비슷한 구문을 사용할 수 있다. 메소드는 단순히 값이 함수인 객체의 속성이다.

```mm
let vehicle = "car"
function vehicleType () {
  return "truck"
}
let car = {
  [vehicle + '_model'] : "Ford"
}
let truck = {
  [vehicleType + '_model'] : 'Merecedz'
}

console.log(car) // {"car_model":"Ford"}
console.log(truck) // {"truck_model":"Mercedez"}
```

car 객체를생성할 때 변수 vehicle의 값을 고정된 문자열과 연결해 속성키를 만든다. 두 번째 코드에서는 함수가 반환한 값을 고정된 문자열과 연결하여 속성을 생성한다. 이 속성 키 게산 방법은 객체를 생성할 때 많은 유연성을 제공해서 보일러플레이트와 반복 코드를 제거할 수 있게 해준다.

## 객체 속성과 어트리뷰트

각 객체는 몇 가지 속성을 가지고 있다. 각각의 속성은 키와 어트리뷰트로 구성된다. 속성의 상태는 이들 어트리뷰트에 저장된다. 모든 속성은 다음과 같은 어트리뷰트를 가진다.

- Enumerable(부울) : 객체의 속성을열거할 수 있는지 여부를 나타낸다. 시스템 속성은 열거 가능하지 않지만 사용자 특성은 열거 가능하다. 특별한 이유가 없는 한 이 속성은 변경하지 않는다.

- Configurable(부울) : 이 속성이 false이면, 속성을 삭제하거나 편집할 수 없다.

Object.getOwnPropertyDescriptor() 메소드를 사용하면 객체의 속성을 검색할 수 있다.

```mm
let obj = {
  age : 25
}

console.log(Object.getOwnPropertyDescriptor(obj, 'age'));
Object { value: 25, writable: true, enumerable: true, configurable: true }
```

또한 Object.dfineProperty() 메소드를 사용하여 속성을 정의할 수 있다.

```mm
let obj = {
  age : 25
}

Object.defineProperty(obj,'age', { configuralbe: false })

console.log(Object.getOwnPropertyDescriptor(obj,'age'));
Object { value: 25, writable: true, enumerable: true, configurable: true }
```

이런 메소드를 실제로 사용하지는 않지만 개체 속성과 어트리뷰트를 이해할 필요가 있어서 사용했다.

## ES6 객체 메소드

ES6는 객체에 대한 몇 가지 정적 헬퍼 메소드를 도입했다. Object.assign은 인기있는 믹스인(mixin)을 대체하여 객체의 얕은 복사를 수행하는 헬퍼 메소드이다.

### Object.assign을 사용하여 속성 복사

```mm
let a = {}
Object.assign(a, { age : 25 })
console.log(a)
Object { age: 25 }
```

Object.assign의 첫 번째 매개변수는 원본 속성이 복사되는 대상이다. 동일한 대상 객체가 호출자에게 반환된다. 원본 객체에 포함되지 않은 속성은 무시되지만 기존 속성은 덮어 쓰여진다.

```mm
let a = {age : 23, gender : 'male'}
Object.assign(a, { age:25})
console.log(a)
Object { age: 25, gender: "male" } // age는 덮어씌여지지만, gender는 무시.
```

Object.assign은 복수의 소스 객체를 받을 수 있다.

```mm
console.log(Object.assign({a:1,b:2},{a:2},{c:4},{b:3}))
Object { a: 2, b: 3, c: 4 }
```

주의할 점은 열거 가능한 속성만 Object.assign()을 사용해 복사할 수 있다는 점이다.

## Object.is와 값 비교

앞에서 동등 연산자 ===에 대해 알아봤따. 그러나 NaN이나 -0, +0의 경우 엄격한 동등 연산자 `===`가 일관성 없이 동작한다.

```mm
console.log(NaN===NaN)
false
console.log(+0===-0)
true
console.log(Object.is(NaN,NaN))
true
console.log(Object.is(+0,-0))
false
```

위 두가지 경우를 제외하고는 Object.is()는 === 연산자로 안전하게 바꿀 수 있다.

## 디스트럭처링

자바스크립트 객체 및 배열 표기법은 JSON 포맷과 유사하다. 객체와 배열을 정의한 다음 여기에서 요소를 검색한다. ES6는 객체 및 배열의 속성/멤버에 접근하는 방식을 크게 향상시키는 편리한 구문을 제공한다.

```mm
var config = {
  server : 'localhost',
  port : '8080'
}
var server = config.server;
var port = config.port;
```

위의 예제에서 config 객체에서 server와 port 값을 추출하여 지역 변수에 할당했다. 하지만 이 객체에서 많은 속성이 있고, 그 중 일부가 중첩된 경우 간단한 작업은 매우 지루해질 수 있다.

ES6 디스트럭처링(분할 할당)구문을 사용하면 할당문의 왼쪽에 객체 리터럴을 사용할 수 있다. 다음 예제에서 몇 개의 속성과 config 객체를 정의한다. 뒤에서 디스트럭처링을 사용하여 할당문의 왼쪽에 있는 개별 속성에 객체 config을 할당한다.

```mm
let config = {
  server : 'localhost',
  port : '8080',
  timeout : 900,
}

let {server,port} = config
console.log(server, port)
```

보다시피 server와 port는 속성 이름이 지역 변수와 동일하기 때문에 config 객체에서 할당된 속성을 가진 지역 변수다.

지역 변수에 할당할 때 특정 속성을 선택할 수도 있다.

```mm
let {timeout : t} = config
console.log(t) // 900
```

예제에서는 config 객체에서 timeout을 선택해 지역 변수 t에 할당한다.

디스트럭처링 구문을 사용해서 이미 선언된 변수에 값을 할당할 수도 있다. 이 경우 할당하는 주변에 괄호를 써야 한다.

```mm
let config = {
  server : 'localhost',
  port : '8080',
  timeout : 900,
}

let server = '127.0.0.1';
let port = '80';
({server,port} = config)  // 할당하는 주변을 ( )로 둘러싼다.
console.log(server,port); // 'localhost 8080'
```

디스트럭처링 표현식이 표현식의 오른쪽으로 평가되기 때문에 값을 할당하는 어느 곳이든 사용할 수 있다.

```mm

let config = {
  server : 'localhost',
  port : '8080',
  timeout : 900,
}

let server = '127.0.0.1';
let port = '80';
let timeout = '100';

function startserver(configValue){
  console.log(configValue)
}
startserver({server,port,timeout} = config)
Object { server: "localhost", port: "8080", timeout: 900 }
```

객체에 존재하지 않는 속성 이름을 가진 변수를 지정하면, 지역변수는 undefined 값을 가지게 된다. 그러나 디스트럭처링 할당에서 변수를 사용할 때, 선택적으로 디폴트 값을 지정해 줄 수 있다.

```mm
let config = {
  server : 'localhost',
  port : '8080'
}

let {server,port,timeout =0} = config
console.log(timeout)  // 0 출력
```

위 예에서 존재하지 않는 속성 timeout에 대해 디폴트값을 제공해 지역 변수에 undefined 값이 할당되지 않도록 한 것이다.

디스트럭처링은 배열에서도 동작하며 구문도 객체의 구문과 아주 유사하다. 객체 리터럴 구문을 array : literals로 대체하기만 하면 된다.

```mm
const arr = ['a','b']
const [x,y] = arr
console.log(x,y) // 'a','b' 출력
```

보다시피 위의 구문들이랑 완전히 똑같은 구문들이다. 배열 arr을 정의한 다음 나중에 디스트럭처링 구문으 사용하여 해당 배열의 요소를 두 개의 지역 변수 x, y에 할당했다.

여기에서 할당은 배열의 요소 순서에 따라 진행된다. 요소의 위치만 신경쓰면, 원하는 경우 일부를 건너뛸 수도 있다.

```mm
const days = ['Thursday','Friday','Saturday','Sunday']
const[,,sat,sun] = days
console.log(sat,sun) // Saturday Sunday 출력
```

위 예제에서 인덱스 2,3의 요소가 필요하다. 따라서 인덱스 0, 1의 요소는 무시하고 출력된다.

또한 배열 디스트럭처링은 두 변수의 값을 교환할 때 temp 변수를 사용하지 않아도 되게 해준다.

```mm
let a = 1, b=2;
[b,a] = [a,b]
console.log(a,b); // 2 1 출력
```

그리고 나머지 연산자(...)를 사용해서 나머지 요소를 추출하고 배열에 할당할 수 있다. 나머지 연산자는 디스트럭처링에서 마지막 연산자로만 사용할 수 있다.

```mm
const [x, ...y] = ['a', 'b', 'c'];
console.log(x,y) // x = a 출력 , y = Array [ "b", "c" ] 출력
```
