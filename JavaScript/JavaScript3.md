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
