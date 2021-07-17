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
