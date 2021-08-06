# 상속

객체는 데이터와 수단(메소드)를 캡슐화해서 모두 데이터로 처리한다. 집합도 마찬가지이다. 객체는 다른 객체를 포함할 수 있다. 메소드는 함수이고, 함수 역시 객체이기 때문이다.

이제 `상속(inheritance)`에 대해 알아보자. 상속은 가장 흥미로운 특징 중 하나이다. 상속은 기존 코드를 재사용할 수 있게 해주며 인간의 특징을 컴퓨터 프로그래밍으로 가져온 것이다.

자바스크립트는 동적인 언어이며, 주어진 작업을 수행하는 방법이 여러 가지가 있다. 상속도 예외는 아니다. 상속을 구현하는 몇 가지 일반적인 패턴을 알아보자. 이런 패턴들을 잘 이해하면, 작업이나 프로젝트, 스타일에 따라 적합한 패턴을 선택하는 데 도움이 된다.

# 프로토타입 체인

상속을 구현하는 가장 기본 방법인 프로토타입을 통한 상속 체인부터 알아보자.

모든 함수는 객체를 가리키는 prototype 속성을 가지고 있다. 함수가 new 연산자를 사용해 호출되면, 객체를 생성하여 반환한다. 이 새 객체는 prototype 객체에 대한 비밀 링크를 가진다. 비밀 링크(일부 환경에선 `__proto__`로 불린다.)를 사용하면 prototype 객체의 메소드와 속성을 마치 새로 생성한 객체의 메소드와 속성인 것처럼 사용할 수 있다.

prototype 객체도 일반적인 객체이므로 이 객체 역시 프로토타입에 대한 비밀 링크를 가지고 있다. 따라서 프로토타입 체인(prototype chain)으로 불리는 체인이 만들어진다.

<img src="https://github.com/Leepilung/TIL/blob/main/img/%EC%83%81%EC%86%8D%20%EC%84%A4%EB%AA%85%EC%98%B9%20%EA%B7%B8%EB%A6%BC(%EC%9E%90%EC%9E%91)%20%EC%88%98%EC%A0%95.png?raw=true">

이 그림에서 객체 A는 여러 속성을 가진다. 이 속성 중 다른 객체인 B를 가리키는 숨겨진 `__proto__` 속성이 있다.
객체 B의 `__proto__`속성은 다시 C를 가리킨다. 이 체인은 부모의 부모인 Object.prototype 객체에서 끝나고, 모든 객체는 여기서 상속된다.

실용적인 측면에서 보면 객체 A에는 속성이 없지만, B에는 있는 경우 A는 B의 속성을 자신의 속성처럼 접근할 수 있다. 또한 B에는 필요한 속성이 없지만 C가 가진 경우도 마찬가지이다. 이것이 상속이 일어나는 방식이다. 객체는 상속 체인 중 어딘가에 있는 모든 속성에 접근할 수 있다.

앞으로의 상속파트에선 다음과 같은 계층 구조를 사용하는 다양한 예제를 다뤄볼 것이다. 하나의 예로 일반 Shape 부모는 2D shape에서 상속되며, 삼각형과 사각형 같은 특정 2차원 모양(shape)의 개수로 상속된다.

## 프로토타입 체인 예제

프로토타입 체인은 상속을 구현하는 가장 기본적인 방법이다. 계층 구조를 구현하기 위해 다음과 같이 세 개의 생성자 함수를 정의해보자.

```js
function Shape() {
  this.name = "Shape";
  this.toString = function () {
    return this.name;
  };
}

function TwoDShape() {
  this.name = "2D Shape";
}

function Triangle(side, height) {
  this.name = "Triangle";
  this.side = side;
  this.height = height;
  this.getArea = function () {
    return (this.side * this.height) / 2;
  };
}
```

상속의 마법을 수행하는 코드는 다음과 같다.

```js
TwoDShape.prototype = new Shape();
Object { name: "Shape", toString: toString() }

Triangle.prototype = new TwoDShape();
Object { name: "2D Shape" }
```

TwoDShape의 prototype 속성에 포함된 객체를 가져와서 개별 속성으로 보강하는 대신, new와 함께 Shape() 생성자를 호출해 만든 다른 객체로 완전히 덮어 쓴다. Triangle에 대해서도 도일한 과정을 수행할 수 있다.

Triangle의 프로토타입은 new TwoDShape()로 생성한 객체로 대체된다. 자바스크립트가 클래스가 아닌 객체로 동작한다는 사실을 기억해야 한다.

new Shape() 생성자를 사용해 인스턴스를 사용해야 하며, 그래야 속성을 상속받을 수 있다. Shape()에서 직접 상속받지 않는다. 또한 상속한 후 Shape() 생성자를 수정하거나 덮어쓰거나 삭제할 수 있으며, 상속할 하나의 인스턴스만 필요하기 때문에 이는 TwoDShape에 영향을 미치지 않는다.

앞의 프로토타입 파트에서 봤듯이 프로토타입을 덮어 쓰는 것은(단순히 속성을 추갛하는 것과는 대조적으로) constructor 속성에 부작용이 발생할 수 있다. 따라서 constructor 속성을 상속한 후 재설정하는 것이 좋다.

다음 예제를 통해 이 부분에 대해 자세히 살펴보자.

```js
TwoDShape.prototype.constructor = TwoDShape;
function TwoDShape()

Triangle.prototype.constructor = Triangle;
function Triangle(side, height)
```

지금까지 무슨일이 일어났는지 테스트해 보자. Triangle 객체를 생성해보고 자체 getArea() 메소드를 호출하면 예상한대로 동작한다.

```js
var my = new Triangle(5, 10);
my.getArea();
25;
```

my 객체에는 toString()메소드가 없지만, 상속받은 객체에서 이 메소드를 호출할 수 있다. 상속된 toString() 메소드가 this 객체를 my에 바인딩 하는 방법에 대해 주목해보자.

```js
my.toString();
("Triangle");
```

my.toString()을 호출할 때 자바스크립트 엔진이 어떤 작업을 수행하는지 알아보자.

- 자바스크립트 엔진은 my의 모든 속성을 조회하고 toString() 메소드를 찾지 못한다.
- 자바스크립트 엔진은 my.\_\_proto\_\_가 가리키는 this 객체를 상속하는 과정에서 생성된 new TwoDShape() 인스턴스로 본다.
- 이제 자바스크립트 엔진은 TwoDShape의 인스턴스를 조회하고 toString() 메소드를 찾지 못한다. 그런 다음 해당 객체의 \_\_proto\_\_를 확인한다. 이번에는 \_\_proto\_\_가 new Shape()에 의해 생성된 인스턴스를 가리킨다.
- new Shape() 인스턴스를 검사하고 결국 toString()이 발견된다.
- 이 메소드는 my 컨텍스트에서 호출된다. 즉, this는 my를 가리킨다.

my의 생성자가 누구인지를 물어보면, 상속 후 constructor 속성을 재설정했기 때문에 올바르게 보고한다.

```js
my.constructor;
function Triangle(side, height)
```

또한 instanceof 연산자를 사용하면 my가 세 생성자 모두의 인스턴스인지 확인할 수 있다.

```js
my instanceof Shape;
true;
my instanceof TwoDShape;
true;
my instanceof Triangle;
true;
my instanceof Array;
false;
```

my를 전달하여 생성자의 isPrototype()을 호출할 때도 마찬가지이다.

```js
Shape.prototype.isPrototypeOf(my);
true;
TwoDShape.prototype.isPrototypeOf;
true;
my instanceof Triangle;
true;
my instanceof Array;
false;
```

다른 두 생성자를 사용하여 객체를 생성할 수도 있다.
new TwoDShape()로 생성된 객체 역시 Shape()에서 상속된 toString() 메소드를 가져온다.

```js
var td = new TwoDShape();
td.constructor === TwoDShape;
true;
td.toString();
("2D Shape");

var s = new Shape();
s.constructor === Shape;
true;
```

## 공유 속성을 프로토타입으로 이동

생성자 함수를 사용해 객체를 생성하면, 자체 속성은 this를 사용해 추가한다. 그러나 이것은 인스턴스간에 속성이 변경되지 않는 경우 비효율적일 수 있다.
앞의 예제에서 Shape()는 다음과 같이 정의됐다.

```js
function Shape() {
  this.name = "Shape";
}
```

new Shape()를 이용해 새 객체를 생성할 때마다, 새 name 속성이 만들어져 메모리 어딘가에 저장된다. 다른 선택사항은 name속성을 프로토타입에 추가해 모든 인스턴스에서 공유하는 것이다.

```js
function Shape() {}
Shape.prototype.name = "Shape";
```

이제 new Shape()을 사용해 객체를 생성할 때마다 이 객체는 자체 name 속성을 가지지 못하지만, 프로토타입에 추가된 속성을 사용할 수 있다. 좀 더 효율적인 방법이지만, 인스턴스간 변경되지 않는 속성에 대해서만 사용해야 한다.

다음으로 prototype에 모든 메소드와 적절한 속성을 추가해보자.

```js
// 생성자
function Shape() {}

// 보강된 프로토타입
Shape.prototype.name = "Shape";
Shape.prototype.toString = function () {
  return this.name;
};

// 다른 생성자
function TwoDShape() {}

// 상속 처리
TwoDShape.prototype = new Shape();
TwoDShape.prototype.constructor = TwoDShape;

// 보강된 프로토타입
TwoDShape.prototype.name = "2D Shape";
```

위의 예제에서 알 수 있듯이 프로토타입을 보강하기 전에 상속을 먼저 처리해야 한다. 그렇지 않으면 상속할 때 TwoDShape.prototype에 추가한 항목이 모두 지워진다.

다음 예제로 사용할 Triangle 생성자는 생성하는 모든 객체가 서로 다른 크기를 가질 수 있는 새로운 삼각형 이기 때문에 약간 다르다. 따라서 side와 height는 자체 속성으로 유지하고 그외 나머지는 공유하는 것이 좋다. 예를 들어 getArea() 메소드는 각 삼각형의 실제 크기에 관계없이 동일하다.

거듭 반복하지만 상속을 수행한다음 프로토타입을 보강해야 하는 것을 잊지 말아야한다.

```js
function Triangle(side, height) {
  this.side = side;
  this.height = height;
}
// 상속 처리
Triangle.prototype = new TwoDShape();
Triangle.prototype.constructor = Triangle;

// 보강된 프로토타입
Triangle.prototype.name = "Triangle";
Triangle.prototype.getArea = function () {
  return (this.side * this.height) / 2;
};
```

이제 위의 코드들을 사용한 예제를 살펴보자.

```js
var my = new Triangle(5, 10);
my.getArea();
25;
my.toString();
("Triangle");
```

my.toString()을 호출할 때 백그라운드에서 약간의 차이가 있다. 차이점은 앞의 예제의 new Shape()인스턴스와 달리, Shape.prototype에서 메소드를 찾기 전에 수행할 조회가 한번 더 있다는 것이다.

또한 hasOwnProperty()를 사용해 자신의 속성인지 프로토타입 체인에서 온 속성인지 비교할 수 있다.

```js
my.hasOwnProperty("side");
true;
my.hasOwnProperty("name");
false;
```

앞의 예제의 isPrototypeOf()와 instanceof 연산자에 대한 호출은 정확히 동일한 방식으로 동작한다.

```js
TwoDShape.prototype.isPrototypeOf(my);
true;
my instanceof Shape;
true;
```

## 프로토타입만 상속

효율성을 위해 재사용 가능한 속성과 메소드를 프로토타입에 추가해야 한다. 이렇게 하면, 모든 재사용 가능한 코드가 프로토타입에 있기 때문에 프로토타입만 상속하는 것이 좋다.

즉, 앞에서 사용한 Shape.prototype 객체를 상속하는 것이 new Shape()로 생성한 객체를 상속하는 것보다 낫다. 결국 new Shape()는 재사용할 수 없는 자체 shape 속성만 제공한다. 또한 다음과 같은 방법으로 효율성을 좀더 높일 수 있다.

- 상속만으로 새 객체를 생성하지 않는다.
- 런타임 중 조회를 적게 수행한다(toString()을 검색할 때).

예제를 통해 알아보자.

```js
function Shape() {}
// 보강된 프로토타입
Shape.prototype.name = "Shape";
Shape.prototype.toString = function () {
  return this.name;
};

function TwoDShape() {}
// 상속 처리
TwoDShape.prototype = Shape.prototype;
TwoDShape.prototype.constructor = TwoDShape;
// 보강된 프로토타입
TwoDShape.prototype.name = "2D shape";

function Triangle(side, height) {
  this.side = side;
  this.height = height;
}
// 상속 처리
Triangle.prototype = TwoDShape.prototype;
Triangle.prototype.constructor = Triangle;
// 보강된 프로토타입
Triangle.prototype.name = "Triangle";
Triangle.prototype.getArea = function () {
  return (this.side * this.height) / 2;
};
```

테스트 코드는 동일한 결과를 보인다.

```js
var my = new Triangle(5, 10);
my.getArea();
25;
my.toString();
("Triangle");
```

my.toString()을 호출할 때 조회에 어떤 차이가 있을것 같은가? 먼저 자바스크립트 엔진은 평소처럼 my 객체 자체의 toString() 메소드를 찾는다. 엔진은 이 메소드를 찾지 못하기 때문에 프로토타입을 검사하게 된다. 프로토타입은 TwoDShape의 프로토타입이 가리키는 객체와 Shape.prototype이 가리키는 객체와 동일한 객체를 가리킨다. 객체는 값으로 복사되지 않고 참조에 의해서만 복사된다는 점을 기억하자. 따라서 조회는 두 단계의 프로세스를 거치게 된다.

간단히 프로토타입만 복제하는 것이 더 효율적일 순 있지만 이것은 자식과 부모의 프로토타입이 모두 동일한 객체를 가르키기 때문에 부작용이 크다.

또한 자식이 프로토타입을 수정하면 부모는 변경사항을 가져오고 형제또한 변경사항을 가지고 온다.

다음 코드를 보자.

```js
Triangle.prototype.name = "Triangle";
```

riangle의 name속성을 변경하면 Shape.prototype.name도 효과적으로 변경된다. new Shape()를 사용해 인스턴스를 생성하는 경우에도 name 속성은 'Triangle'이 된다.

```js
var s = new Shape();
s.name;
("Triangle");
```

## 임시 생성자 - new F()

앞에서 설명한 모든 프로토타입이 동일한 객체를 가리키고 부모가 자식의 속성을 가져오는 문제에 대한 해결책은 중재자(intermediary)를 사용해 체인을 끊는 것이다.

중재자는 임시 생성자 함수의 형태를 가지고 있다. 빈 함수 F()를 생성하고 이 함수의 prototype을 부모 생성자의 프로토타입으로 설정하면, new F()를 호출할 때 자체 속성을 가지지 않지만 부모의 prototype의 모든 것을 상속받는 객체를 생성할 수 있다.

수정된 코드를 통해 살펴보자.

```js
function Shape() {}
// 보강된 프로토타입
Shape.prototype.name = "Shape";
Shape.prototype.toString = function () {
  return this.name;
};

function TwoDShape() {}
// 상속 처리
var F = function () {};
F.prototype = Shape.prototype;
TwoDShape.prototype = new F();
TwoDShape.prototype.constructor = TwoDShape;
// 보강된 프로토타입
TwoDShape.prototype.name = "2D shape";

function Triangle(side, height) {
  this.side = side;
  this.height = height;
}
// 상속 처리
var F = function () {};
F.prototype = TwoDShape.prototype;
Triangle.prototype = new F();
Triangle.prototype.constructor = Triangle;
// 보강된 프로토타입
Triangle.prototype.name = "Triangle";
Triangle.prototype.getArea = function () {
  return (this.side * this.height) / 2;
};
```

이제 my 라는 변수를 Triangle 생성자를 통해 생성하고 테스트해보자.

```js
var my = new Triangle(5, 10);
my.getArea();
25;
my.toString();
("Triangle");
```

이 접근 방식을 사용하면, 프로토타입 체인이 그대로 유지된다.

```js
my.__proto__ === Triangle.prototype;
true;
my.__proto__.constructor === Triangle;
true;
my.__proto__.__proto__ === TwoDShape.prototype;
true;
my.__proto__.__proto__.__proto__.constructor === Shape;
true;
```

또한 부모의 속성을 자녀가 덮어 쓰지도 않는다.

```js
var s = new Shape();
s.name;

"I am a " + new TwoDShape(); // calling toString()
("I am a 2D shape");
```

동시에 이 접근방식은 자체 속성이 아닌 프로토타입에 추가된 속성과 메소드만 상속받아야 한다는 개념을 지원한다. 자체 속성은 재사용하기엔 너무 구체적이기 때문이다.
