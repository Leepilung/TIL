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

## Uber - 자식 객체에서 부모에 접근하기

고전 OO언어는 대개 슈퍼클래스라고 하는 부모 클래스에 접근할 수 있는 특수 구문을 제공한다. 이것은 자식이 부모 메소드에 추가 기능을 추가하는 경우에 편리하다. 이런 경우, 자식은 부모의 메소드를 동일한 이름으로 호출하여 결과를 가지고 작업한다.

자바스크립트에 이런 특별한 구문은 없지만, 동일한 기능을 구현하는 것은 어려운 일이 아니다. 상속을 처리할 때 부모의 prototype 객체를 가리키는 uber 속성을 만들어 보자.

```js
function Shape() {}
// 보강된 프로토타입
Shape.prototype.name = "Shape";
Shape.prototype.toString = function () {
  const c = this.constructor;
  return c.uber ? c.uber.toString() + ", " + this.name : this.name;
};

function TwoDShape() {}
// 상속 처리
var F = function () {};
F.prototype = Shape.prototype;
TwoDShape.prototype = new F();
TwoDShape.prototype.constructor = TwoDShape;
TwoDShape.uber = Shape.prototype;
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
Triangle.uber = TwoDShape.prototype;
// 보강된 프로토타입
Triangle.prototype.name = "Triangle";
Triangle.prototype.getArea = function () {
  return (this.side * this.height) / 2;
};
```

여기서 새로운 것은 다음과 같다.

- 부모의 prototype을 가리키는 새로운 uber 속성
- 업데이트된 toString() 메소드

앞에서 toString()은 this.name만을 반환했다. 이제 이외에도 this.constructor.uber가 있는지 확인하고, 있는 경우 toString()을 먼저 호출한다. this.constructor는 함수 자체이며, this.constructor.uber는 부모의 prototype을 가리킨다.

결과로 Triangle 인스턴스의 toString()을 호출하면 프로토타입 체인 위의 모든 toString() 메소드가 호출된다.

```js
var my = new Triangle(5, 10);
my.toString();
("Shape, 2D shape, Triangle");
```

uber 속성의 이름을 superclass로 할 수도 있지만, 자바스크립트는 클래스가 없기 때문에 적합하지 않다.

## 상속 부분을 함수로 분리하기

Uber 부분에서 상속의 모든 세부사항을 처리하는 코드를 extend()라 명명한 재사용 가능한 함수로 옮겨보자.

```js
function extend(Child, Parent) {
  var F = function () {};
  F.prototype = Parent.prototype;
  Child.prototype = new F();
  Child.prototype.constructor = Child;
  Child.uber = Parent.prototype;
}
```

이 함수를 사용하면, 반복 상속 관련 작업의 코드를 깨긋하게 유지할 수 있다. 이렇게 하면 다음 두 줄의 코드를 사용해 간단하게 상속받을 수 있다.

```js
extend(TwoDShape, Shape);
extend(Triangle, TwoDShape);
```

전체적인 예제 코드는 다음과 같다.

```js
// 상속 헬퍼(helper)
function extend(Child, Parent) {
  var F = function () {};
  F.prototype = Parent.prototype;
  Child.prototype = new F();
  Child.prototype.constructor = Child;
  Child.uber = Parent.prototype;
}

// 정의 -> 보강
function Shape() {}
Shape.prototype.name = "Shape";
Shape.prototype.toString = function () {
  return this.constructor.uber
    ? this.constructor.uber.toString() + " , " + this.name
    : this.name;
};

// 정의 -> 상속 -> 보강
function TwoDShape() {}
extend(TwoDShape, Shape);
TwoDShape.prototype.name = "2D Shape";

// 정의
function Triangle(side, height) {
  this.side = side;
  this.height = height;
}

// 상속
extend(Triangle, TwoDShape);

// 보강
Triangle.prototype.name = "Triangle";
Triangle.prototype.getArea = function () {
  return (this.side * this.height) / 2;
};
```

다음 코드를 테스트 해보면 값이 다르게 나옴을 알 수 있다.

```js
new Triangle().toString();
("Shape , 2D Shape , Triangle");
```

---

## 속성 복사

상속은 모두 코드 재사용에 관한 것이므로 하나의 객체에서 원하는 속성을 다른 객체로 간단히 복사하거나 부모 객체에서 자식객체로 복사하는것은 어떨지 생각해보자.

앞에서 extend() 함수와 동일한 인터페이스를 유지하면서 두 개의 생성자 함수를 사용하고 부모의 prototype에서 모든 속성을 자식의 prototype으로 복사하는 extend2() 함수를 만들 수 있다. 메소드는 함수인 속성일 뿐이므로 이것은 메소드에도 동일하다.

```js
function extend2(Child, Parent) {
  var p = Parent.prototype;
  var c = Child.prototype;
  for (var i in p) {
    c[i] = p[i];
  }
  c.uber = p;
}
```

보다시피 속성을 반복하는 간단한 루프만 있으면 된다. 앞의 예제와 마찬가지로, 자식에서 부모의 메소드에 편리하게 접근하려면 uber 속성을 설정하면 된다.

그러나 앞의 예제와 달리 여기서는 자식의 prototype이 완전히 덮어 쓰이지 않고 보강되어 Child.prototype.constructor를 재설정할 필요는 없다. 따라서 constructor 속성은 초기 값을 가리킨다.

이 메소드는 자식 prototype의 속성이 실행 중에 프로토타입 체인을 통해 단순히 조회되는 것이 아니라 복제되는 방식이어서 앞의 메소드에 비해 비효율 적인 방법이다. 이것은 원시 유형을 가지는 속성에 대해서만 유효하다. 모든 객체는 참조로만 전달되므로 복제되지 않는다.

Shape()와 TwoDShape()의 두 생성자 함수를 사용하는 예제를 살펴보자. Shape() 함수의 prototype 객체는 원시(primitive) 속성인 name과 비원시 메소드인 toStirng()을 가진다.

```js
var Shape = function () {};
var TwoDShape = function () {};
Shape.prototype.name = "Shape";
Shape.prototype.toString = function () {
  return this.uber ? this.uber.toString() + "," + this.name : this.name;
};
```

extend()로 상속한 경우, TwoDShape()로 생성한 객체나 이 객체의 프로토타입은 자체 name 속성을 갖ㅈ ㅣ않지만, 상속한 속성에 접근할 수 있다.

```js
extend(TwoDShape, Shape);
var td = new TwoDShape();
td.name;
("Shape");
TwoDShape.prototype.name;
("Shape");
td.__proto__.name;
("Shape");
td.hasOwnProperty("name");
false;
td.__proto__.hasOwnProperty("name");
false;
```

그러나 extend2()로 상속하는 경우, TwoDShape()의 프로토타입은 name 속성의 자체 복사본을 가져 온다. toString()의 자체 복사본도 가져오지만, 참조뿐이기 때문에 두 번째에는 함수가 다시 생성되지 않는다.

```js
extend2(TwoDShape, Shape);
var td = new TwoDShape();
td.__proto__.hasOwnProperty("name");
true;
td.__proto__.hasOwnProperty("toString");
true;
td.__proto__.toString === Shape.prototype.toString;
true;
```

보다시피 두 개의 toString() 메소드는 동일한 함수 객체다. 이는 불필요한 메소드 중복이 발생하지 않기 때문에 유용하다.

따라서 extend2()는 프로토타입의 속성을 다시 생성하기 때문에 extend() 보다 효율적이지 않다. 그러나 원시 데이터 유형만 복제되기 때문에 그리 나쁜 것만은 아니다. 또한 속성을 찾기전에 따라가야 하는 체인 연결이 적기 때문에 프로토타입 체인 조회 시 유용하다.

uber 속성을 살펴보자. 이번에는 변경을 위해 Parent 생성자가 아닌 Parent 객체의 프로토타입 p에 설정한다. 이것이 toString()이 this.constructor.uber가 아닌 this.uber를 사용하는 이유이다. 우리가 원하는 대로 상속 패턴을 형성할 수 있음을 보여주는 것이다.

```js
td.toString();
("Shape,Shape");
```

TwoDShape는 name속성을 재정의하지 않으므로 반복된다. 이것은 언제든지 가능하며, 프로토타입 체인이 살아있으므로 모든 인스턴스가 업데이트를 확인할 수 있다.

```js
TwoDShape.prototype.name = "2D Shape";
("2D Shape");
td.toString();
("Shape,2D Shape");
```

## 참조로 복사할 때의 문제점

객체(함수와 배열 포함)가 참조로 복사된다는 사실은 때때로 예상치 못한 결과를 가져오기도 한다.

예로 두 개의 생성자 함수를 생성하고 첫 번째 프로토타입에 속성을 추가해 보자.

```js
function Papa() {}
function Wee() {}
Papa.prototype.name = "Bear";
Papa.prototype.owns = ["porridge", "chair", "bed"];
```

다음으로 Wee가 Papa로부터 상속받도록 해보자.(extend() 혹은 extend2() 사용)

```js
function extend2(Child, Parent) {
  var p = Parent.prototype;
  var c = Child.prototype;
  for (var i in p) {
    c[i] = p[i];
  }
  c.uber = p;
}

extend2(Wee, Papa);
```

extend2()를 사용하면 Wee 함수의 프로토타입이 Papa.prototype의 속성을 자체 속성으로 상속 받는다.

```js
Wee.prototype.hasOwnProperty("name");
true;
Wee.prototype.hasOwnProperty("owns");
true;
```

name 속성은 원시(primitive)값이므로 새 복사본이 만들어진다. owns 속성은 배열 객체이므로 참조로 복사된다.

```js
Wee.prototype.owns;
Array(3)[("porridge", "chair", "bed")];
Wee.prototype.owns === Papa.prototype.owns;
true;
```

또한 Wee 함수의 name 복사본을 변경해도 Papa에는 영향을 미치지 않는다.

```js
Wee.prototype.name += ",Litte Bear";
("Bear,Litte Bear");
Papa.prototype.name;
("Bear");
```

그러나 Wee 함수의 owns 복사본을 기존 객체를 수정하는 것과는 반대로 아예 다른 객체로 완전히 덮어 쓰면 이야기가 달라진다.

이 경우, Wee.owns는 새 객체를 가리키는 반면 Papa.owns는 이전 객체를 가리키게 된다.

```js
Wee.prototype.owns = ["empty bowl", "broken chair"];
Papa.prototype.owns.push("bed");
Papa.prototype.owns;
Array(6)[("porridge", "chair", "bed")];
```

객체가 메모리의 물리적 위치에 생성되고 저장되는 것으로 생각해 보자.

변수와 속성은 이 위치를 가리키기만 하므로 새로운 객체를 Wee.prototype.owns에 할당하면 본질적으로 이전 객체는 잊어버리고 포인터를 이 새로운 객체로 옮기는 것이다.
