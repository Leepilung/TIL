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

## 객체에서 상속받은 객체

앞에선 생성자 함수를 사용해 객체를 생성하고 상속받는 경우들을 살펴봤다. 그러나 생성자 함수를 사용자히 않고 객체 리터럴만을 사용해 객체를 생성할 수도 있다. 이 경우가 실제로 타이핑도 적다. 그렇다면 상속은 어떨까?

다른 언어에선 클래스를 이용해 상속하지만 자바스크립트에는 클래스가 없으므로 클래스 배경에 익숙한 프로그래머는 생성자 함수에 의존한다.

`모든것은 결국 객체로 통한다.` 라는 말을 기억한 채로 예제를 살펴보자.

```js
Child.prototpye = new Parent();
```

프로토타입 파트의 앞부분 에서 사용한 예제이다. 여기서 Child 생성자(or 클래스)는 Parent에서 상속됐다. 그러나 이것은 new Parent()를 사용해 객체를 생성하고 이를 상속받는 방식으로 수행된다.

클래스가 포함되어 있지는 않지만 클래스 상속과 유사하기 때문에 이를 `의사 클래스 상속 패턴(pseudo-classical inheritance)`이라고 부른다.

그렇다면 왜 중개자(생성자/클래스)를 없애고 객체를 바로 객체에서 상속받지 않을까? extend2()에서 부모 prototype 객체의 속성이 자식 prototype 객체의 속성으로 복사됐다.

두 프로토타입은 본질적으로 객체다. 프로토타입과 생성자 함수에 대해 생각하지 않으면 단순히 객체의 모든 속성을 다른 객체로 복사할 수 있다.

var o = {};를 사용해 자체 속성을 가지지 않는 빈 객체로 시작하고 나중에 속성을 채울 수 있다. 그러나 완전히 새로 작성하는 대신 기존 객체의 모든 속성을 복사하여 시작할 수 있다.

다음 함수는 객체를 받아 이 객체의 새 복사본을 반환하는 예이다.

```js
function extendCopy(p) {
  var c = {};
  for (var i in p) {
    c[i] = p[i];
  }
  c.uber = p;
  return c;
}
```

단순히 모든 속성을 복사하는 것은 쉬운 패턴이며 널리 사용되고 있다. 이 함수의 실제 동작을 살펴보자. 기본 객체를 가지고 시작한다.

```js
var shape = {
  name: "Shape",
  toString: function () {
    return this.name;
  },
};
```

이전 객체를 기반으로 새 객체를 만드려면 새 객체를 반환하는 extendCopy() 함수를 호출하면 된다. 그런 다음 추가 기능으로 새로운 객체를 보강할 수 있다.

```js
var twoDee = extendCopy(shape);
twoDee.name = "2D Shape";
twoDee.toString = function () {
  return this.uber.toString() + " ," + this.name;
};
```

다음은 2D shape 객체를 상속받은 triangle 객체다.

```js
var triangle = extendCopy(twoDee);
triangle.name = "Triangle";
triangle.getArea = function () {
  return (this.side * this.height) / 2;
};
```

다음으로 triangle을 사용해보자.

```js
triangle.side = 5;
triangle.height = 10;
triangle.getArea();
25;
triangle.toString();
("Shape ,2D Shape ,Triangle");
```

이 메소드의 단점은 새 triangle 객체를 초기화하는 다소 장황한 방법이다. 생성자에 값으로 전달하는 것이 아니라 side와 hegiht의 값을 수동으로 설정해야 한다.

그러나 이것은 생성자로 동작하고 초기화 매개변수를 받아들이는 init() 함수(or \_\_constructor())를 사용하면 쉽게 해결할 수 있다.

또는 extendCopy()에서 두 개의 매개변수, 즉 상속할 객체와 반환될 사본에 추가할 다른 속성의 객체 리터럴을 허용한다. 즉, 두 객체를 병합하면 된다.

## 깊은 복사

위에서 설명한 extendCopy() 함수는 extend2()와 같이 객체의 얕은 복사본을 만든다.

앞에서 `참조로 복사할 때의 문제점` 파트에서 다뤘던 내용처럼 객체를 복사하면 객체가 저장된 메모리의 위치를 가리키는 포인터만 복사 한다. 이것은 얕은 복사에 해당한다. 복사본에서 객체를 수정하면 원본도 수정된다. 깊은 복사는 이 문제를 방지해준다.

깊은 복사는 얕은 복사와 동일한 방법으로 구현된다. 속성을 반복하여 하나씩 복사한다. 그러나 객체를 가리키는 속성을 만나면 다시 deepcopy 함수를 호출한다.

```js
function deepCopy(p, c) {
  c = c || {};
  for (var i in p) {
    if (p.hasOwnProperty(i)) {
      if (typeof p[i] === "object") {
        c[i] = Array.isArray(p[i]) ? [] : {};
        deepCopy(p[i], c[i]);
      } else {
        c[i] = p[i];
      }
    }
  }
  return c;
}
```

배열과 하위객체를 속성으로 가지는 객체를 생성한다.

```js
var Parent = {
  number: [1, 2, 3],
  letters: ["a", "b", "c"],
  obj: {
    prop: 1,
  },
  bool: true,
};
```

깊은 복사와 얕은 복사를 생성해 테스트해 보자. 얕은 복사와 달리, 깊은 복사의 numbers 속성을 업데이트해도 원본은 영향을 받지 않는다.

```js
var mydeep = deepCopy(parent);
var myshallow = extendCopy(parent);
mydeep.numbers.push(4, 5, 6);
6;
mydeep.numbers;
Array(6)[(1, 2, 3, 4, 5, 6)];
parent.numbers;
Array(3)[(1, 2, 3)];
myshallow.numbers.push(10);
4;
myshallow.numbers;
Array(4)[(1, 2, 3, 10)];
parent.numbers;
Array(4)[(1, 2, 3, 10)];
mydeep.numbers;
Array(6)[(1, 2, 3, 4, 5, 6)];
```

다음은 deepCopy() 함수에 대한 두 가지 참고 사항이다.

- hasOwnProperty()로 자체 속성이 아닌 속성을 필터링하면 다른 사람이 핵심 프로토타입을 추가하지 못하게 할 수 있다.
- Array.isArray()는 실제 배열을 객체와 구분하는 것이 놀랄 정도로 어렵기 때문에 ES5부터 존재한다.

## Object() 메소드 사용하기

객체가 객체를 상속한다는 개념에 기반하여, 객체를 받아 프로토타입을 부모로 가진 새로운 객체를 반환하는 Object() 함수의 사용을 알아보자.

```js
function object(o) {
  function F() {}
  F.prototype = o;
  return new F();
}
```

uber 속성에 접근이 필요한 경우, object() 함수를 다음과 같이 수정한다.

```js
function object(o) {
  function F() {}
  F.prototype = o;
  n = new F();
  n.uber = o;
  return n;
}
```

this 함수를 사용하는 것은 extendCopy()를 사용하는 것과 동일하다. twoDee와 같은 객체를 받아 새 겍체를 만든 다음, 새 객체를 보강하는 것으로 진행한다.

```js
var triangle = object(twoDee);
triangle.name = "Triangle";
triangle.getArea = function () {
  return (this.side * this.height) / 2;
};
```

새로운 triangle은 여전히 같은 방식으로 동작한다.

```js
triangle.toString();
("Shape ,2D Shape ,Triangle");
```

이 패턴은 부모 객체를 자식 객체의 프로토타입으로 사용하기 때문에 프로토타입 상속(prototype inheritance)라고도 한다. 또한 ES5에서 채택되어 Object.create()로 호출된다. 예제는 다음과 같다.

```js
var square = Object.create(triangle);
```

## 프로토타입 상속과 속성 복사의 혼합 사용

상속을 사용할 때는 대부분 이미 존재하고 있는 기능에 새로운 기능을 추가해 사용하려는 것이다. 이것은 존재하는 객체로부터 상속받고 새로운 메소드와 속성을 추가해 새로운 객체를 생성하는 것을 의미한다.

방금 두 가지 방법을 조합하여 하나의 함수호출로 이 작업을 수행할 수 있다.

- 프로토타입 상속을 사용하여 기존 객체를 새로운 객체의 프로토타입으로 사용한다.
- 새로 만든 객체에 다른 객체의 모든 속성을 복사한다.

```js
function objectPlus(o, stuff) {
  var n;
  function F() {}
  F.prototpye = o;
  n = new F();
  n.uber = o;
  for (var i in stuff) {
    n[i] = stuff[i];
  }
  return n;
}
```

이 함수는 stuff 객체로부터 o 객체를 상속받아 추가 메소드와 속성을 추가한ㄷ마. 실제로 작성해보자.

기본 Shape 객체로 시작한다.

```js
var Shape = {
  name: "Shape",
  toStirng: function () {
    return this.name;
  },
};
```

shape를 상속하고 속성을 추가하여 twoDee라는 객체를 생성해보자. 추가 속성은 객체 리터럴을 사용해 간단히 만들 수 있다.

```js
var twoDee = objectPlus(Shape, {
  name: "2D shape",
  toString: function () {
    return this.uber.toString() + "," + this.name;
  },
});
```

이제 twoDee에서 상속받고 속성을 추가하여 triangle객체를 생성해 보자.

```js
var triangle = objectPlus(twoDee, {
  name: "Triangle",
  getArea: function () {
    return (this.side * this.height) / 2;
  },
  side: 0,
  height: 0,
});
```

side와 height를 정의해 구체적인 상각형 객체 my를 만들어 어떻게 동작하는지 테스트해보자.

```js
var my = objectPlus(triangle, {
  side: 4,
  height: 4,
});
my.getArea();
8;
my.toString();
("Shape, 2D Shape, Triangle, Triangle");
```

여기서 toString()을 실행할 때 차이점은 Triangle 이름이 두번 반복된다는 것이다.
구체적인 인스턴스는 triangle을 상속받아 생성됐기 때문에 더 많은 수준의 상속이 있기 떄문이다.

## 다중 상속

다중 상속은 하나 이상의 부모로부터 상속받는 것을 의미한다. 다중 속성은 장단점에 대한 의견 대립이 많다. 그러나 여기서는 자바스크립트로 이를 어떻게 구현하는지에 대해 알아보자.

속성을 복사하고 확장하여 입력 객체의 수를 무제한으로 상속받을 수 있도록 한 상속의 아이디어를 사용하면 간단하게 구현할 수 있다.

여러 개의 입력 객첼를 받는 multi() 함수를 만들어 보자. 함수에 arguments로 전달된 모든 객체를 반복해 다른 루프의 속성을 복사하는 루프를 래핑할 수 있다.

```js
function multi() {
  var n = {},
    stuff,
    j = 0,
    len = arguments.length;
  for (j = 0; j < len; j++) {
    stuff = arguments[j];
    for (var i in stuff) {
      if (stuff.hasOwnProperty(i)) {
        n[i] = stuff[i];
      }
    }
  }
  return n;
}
```

shape와 twoDee, 그리고 세 번째로 이름없는 세 개의 객체를 만들어 이를 테스트해 보자. 그런 다음 triangle 객체를 생성하는 것은 mulit()를 호출하고 새 객체를 모두 전달하는 것을 의미한다.

```js
var shape = {
  name: "Shape",
  toString: function () {
    return this.name;
  },
};

var twoDee = {
  name: "2D shape",
  diemsions: 2,
};

var triangle = multi(shape, twoDee, {
  name: "Triangle",
  getArea: function () {
    return (this.side * this.height) / 2;
  },
  side: 5,
  height: 10,
});
```

잘 동작하는지 살펴보자. getArea() 메소드는 자체 속성이며, dimesions는 twoDee에서, toString()은 shape에서 상속받은 것이여야 한다.

```js
triangle.getArea();
25;
triangle.diemsions;
2;
triangle.toString();
("Triangle");
```

multi()는 입력된 객체를 순서대로 반복하며, 두 객체가 동일한 속성을 가진 경우 마지막 속성을 우선시 한다.

> 믹스인

믹스인(mixin)이라는 용어에 대해 알아보자. 믹승인은 유용한 기능을 제공하지만 하위 객체에 상속되고 확장되지는 않는 객체로 생각하면 된다. 앞에서 설명한 다중 속성을 믹스인 아이디어의 구현으로 생각할 수 있다. 새로운 객체를 생성할 때 다른 객체를 선택하여 새로운 객채에 혼합할 수 있다. 모든 객체를 multi()로 전달하면, 상속 트리에 포함시키지 않으면서 모든 객체의 기능을 사용할 수 있다.

## 기생 상속

자바스크립트에서 상속을 구현하는 데 또다른 방법이 있다. 바로 기생 상속(parasitic inheritance)이다. 이것은 다른 객체의 모든 기능을 가져와 새로운 객체를 보강하고, 이를 반환하여 객체를 생성하는 함수이다.

다음은 곧 기생 상속의 희생양이 될 객체 리터럴로 정의된 일반 객체이다.

```js
var twoD  = {
  name : '2D shape',
  dimensions :
```

triangle 객체를 생성하는 함수는,

- twoD 객체를 that(편의상 this와 유사한) 이라는 객체의 프로토타입으로 사용한다. object()함수를 사용하거나 모든 속성을 복사하는 등 앞에서 봤던 어떤 방법으로도 이 작업을 수행할 수 있다.
- that을 추가 속성으로 보강한다.
- that을 반환한다.

```js
// 프로토타입 파트 위에서 사용한 object 함수가 필요함.
function object(o) {
  function F() {}
  F.prototype = o;
  return new F();
}

function triangle(s, h) {
  var that = object(twoD);
  that.name = "Triangle";
  that.getArea = function () {
    return (this.side * this.height) / 2;
  };
  that.side = s;
  that.height = h;
  return that;
}
```

tirangle()은 생성자가 아닌 일반 함수이기 때문에, new 연산자가 필요하지 않다. 그러나 객체를 반환하기 때문에 실수로 new 연산자를 사용해서 호출해도 잘 동작한다.

```js
// triangle 함수 내부에서 object() 함수를 필요로 하는데 이는 위에서 구현해놓은 함수이므로 따로 갖다써야함.
var t = triangle(5, 10);
t.dimensions;
2;

var t2 = new triangle(5, 5);
t2.getArea();
12.5;
```

this와 마찬가지로, that은 단순히 이름일 뿐이며 특별한 의미를 가지지 않는다.

## 생성자 빌리기

상속을 구현하는 또 다른 방법은 직접 객체를 다루지 않고 생성자 함수를 다시 사용하는 것이다. 이 패턴에서 자식의 생성자 call() 또는 apply() 메소드를 사용해 부모의 생성자를 호출한다.

이것은 `생성자 훔치기(stealing a constructor)` 혹은 `생성자 빌리기를 통한 상속(inheritance by borrowing a constructor)`라고 불린다.

call()과 apply() 메소드는 앞의 Javascript3.md에 정리되어있다. 그러나 왔다갔다 하는 번거러움을 방지하기 위해 다시 한번 정리해 보자.

이들 함수는 함수를 호출하고 this 값에 바인딩할 객체를 전달할 수 있다. 따라서 상속 목적으로 자식 생성자는 부모의 생성자를 호출하고 새로 생성된 자식의 this 객체를 부모의 this로 바인딩한다.

부모 생성자 Shape()를 먼저 만들어보자.

```js
function Shape(id) {
  this.id = id;
}
Shape.prototype.name = "Shape";
Shape.prototype.toString = function () {
  return this.name;
};
```

이제 apply()를 사용해 Shape() 생성자를 호출하고 this(new Triangle()로 생성한 인스턴스)와 추가 인수를 전달해 Triangle()을 정의해 보자.

```js
function Triangle() {
  Shape.apply(this, arguments);
}
Triangle.prototype.name = "Triangle";
```

Triangle()과 Shape() 모두 프로토타입에 몇 가지 추가 속성을 추가했다.

이제 새로운 triangle 객체를 생성하여 테스트해 보자.

```js
var t = new Triangle(101);
t.name;
("Triangle");
```

새로운 Tirangle 객체는 부모로부터 id 속성을 상속받지만, 부몽의 prototypeㅇ에 추가된 다른 어떤 것도 상속받지 않는다.

```js
t.id;
101;
t.toString();
("[object Object]");
```

Triangle은 new Shape() 인스턴스가 생성되지 않기 때문에 Shape 함수의 프로토타입 속성을 가져오지 못한다. 따라서 프로토타입은 결코 사용되지 못한다.

그러나 이 프로토타입 파트의 시작 부분에서 이 작업을 수행하는 방법을 배웠다. Triangle을 다음과 같이 재정의할 수 있다.

```js
function Triangle() {
  Shape.apply(this, arguments);
}
Triangle.prototype = new Shape();
Triangle.prototype.name = "Triangle";
```

이 상속 패턴에서 부모의 자체 속성은 자식의 자체 속성으로 다시 생성된다. 자식이 배열이나 다른 객체를 상속받는 경우, 이는 완전히 새로운 값(참조가 아닌)이며, 부모를 변경해도 영향을 주지 않는다.

단점은 부모의 생성자가 한번은 apply()로 자체 속성을 상속할 때, 그리고 한번은 new로 프로토타입을 상속받을 때, 총 두 번 호출된다는 것이다. 실제로 부모의 자체 속성은 두 번 상속된다.

```js
function Shape(id) {
  this.id = id;
}
function Triangle() {
  Shape.apply(this, arguments);
}
Triangle.prototype = new Shape(101);
```

여기에서 새로운 인스턴스를 생성해보자.

```js
var t = new Triangle(202);
t.id;
202;
```

자체 속성인 id가 있지만, 프로토타입 체인에서 나와 빛을 발할 준비가 된 속성들도 있다.

```js
t.__proto__.id;
101;
delete t.id;
true;
t.id;
101;
```

## 생성자 빌리기와 프로토타입 복사하기

생성자가 두 번 호출돼서 수행되는 이중 작업 문제는 쉽게 해결할 수 있다. 부모 생성자의 apply()를 호출해 모든 자체 속성을 가져온 다음, 간단한 반복(앞에서 사용한 extend2()등을 사용하여) 프로토타입의 속성을 복사할 수 있다.

```js
function extend2(Child, Parent) {
  var p = Parent.prototype;
  var c = Child.prototype;
  for (var i in p) {
    c[i] = p[i];
  }
  c.uber = p;
}

function Shape(id) {
  this.id = id;
}

Shape.prototype.name = "Shape";
Shape.prototype.toString = function () {
  return this.name;
};

function Triangle() {
  Shape.apply(this, arguments);
}
extend2(Triangle, Shape);
Triangle.prototype.name = "Triangle";
```

다음 코드를 테스트해 보자.

```js
var t = new Triangle(101);
t.toString();
("Triangle");
t.id;
101;
```

이중 상속이 발생하지는 않는다.

```js
typeof t.__proto__.id;
("undefined");
```

extend2() 메소드는 필요한 경우 uber에 대한 접근도 제공한다.

```js
t.uber.name;
("Shape");
```

## 사례 연구 - 도형 그리기
