# 프로토타입

프로토타입이 어떻게 동작하는지 이해하는 것은 자바스크립트 언어 학습에 있어서 중요한 부분이다.

자바스크립트는 프로토타입 기반 객체 모델로 분류되는 경우가 많다.

이번 프로토타입에서 다룰 주제들은 다음과 같다.

- 모든 함수는 prtototype 속성을 가지고 있으며 객체를 포함한다.
- 프로토타입 객체에 속성 추가하기
- 프로토타입에 추가된 속성 사용하기
- 자체 속성과 프로토타입 속성간의 차이점
- 모든 객체가 프로토타입을 유지하는 비밀링크인 **proto** 속성
- isPrototypeOf()와 hasOwnProperty(), propertyIsEnumerable() 메소드
- 배열과 문자열 같은 내장 객체 확장하기와 이것이 좋지 않은 이유

# 프로토타입 속성

자바스크립트의 함수는 객체이며, 메소드와 속성을 포함한다. 여기에는 이미 여러번 사용한 apply()와 call() 같은 메소드와 length나 constructor 같은 속성등이 대표적인 예이다.

그리고 함수 객체에는 또 다른 속성인 prototype이 있다.

간단한 함수 foo()를 정의하면, 다른 객체와 마찬가지로 함수의 속성에 접근할 수 있다.

```js
function foo(a, b) {
  return a + b;
}
foo.length
2
foo.constructor;
function Function()
```

prototype 속성은 함수를 정의하자마자 사용할 수 있는 속성이다. 초기값은 빈 객체이다.

```js
typeof foo.prototype;
("object");
```

또한 다음과 같이 속성을 직접 추가할 수 있다.

```js
foo.prototype = {};
Object {  }
```

이 빈객체를 속성과 메소드로 보강할 수 있다. 이것들은 foo() 함수 자체에는 아무런 영향을 미치지 않고, foo()를 생성자로 호출할 때만 사용한다.

## 프로토타입을 사용하여 메소드와 속성 추가하기

앞에서 객체를 생성하는데 사용할 수 있는 생성자 함수를 정의하는 방법을 알아봤다. 주된 개념은 new로 호출된 함수 내에서 생성자가 반환하는 객체를 참조하는 this값에 접근할 수 있다는 내용이었다. this에 메소드와 속성을 추가하는 `보강(augmenting)`은 생성되는 객체에 기능을 추가할 수 있는 방법이다.

생성자 함수인 Gadget()을 살펴보자. 다음과 같이 this를 사용해 두 개의 속성과 하나의 메소드를 이 함수가 생성하는 객체에 추가해보자.

```js
function Gadget(name, color) {
  this.name = name;
  this.color = color;
  this.whatAreyou = function () {
    return "I am a " + this.color + " " + this.name;
  };
}
```

생성자 함수의 prototype 속성에 메소드와 속성을 추가하는 것은 이 생성자가 생성하는 객체에 기능을 추가하는 또 다른 방법이다.

getInfo() 메소드와 함께 price, rating의 두개의 속성을 더 추가해보자. prototype이 이미 객체를 가리키고 있으므로 다음과 같이 속성과 메소드를 계속 추가할 수 있다.

```js
Gadget.prototype.price = 100;
Gadget.prototype.rating = 3;
Gadget.prototype.getInfo = function () {
  return "Rating: " + this.rating + ", price: " + this.price;
};
```

또는 prototype 객체에 속성을 하나씩 추가하는 대신, 다음 예제와 같이 prototype을 완전히 덮어 쓰고 원하는 객체로 대체할 수도 있다.

# 프로토 타입의 메소드와 속성 사용하기

prototype에 추가된 모든 메소드와 속성은 생성자를 사용해 새 객체를 만드는 즉시 사용할 수 있다.

Gadget() 생성자를 사용해 newtoy 객체를 만든 경우, 다음 코드에서 볼 수 있듯이 이미 정의된 모든 메소드와 속성에 접근할 수 있다.

```js
function Gadget(name, color) {
  this.name = name;
  this.color = color;
  this.whatAreyou = function () {
    return "I am a " + this.color + " " + this.name;
  };
}

Gadget.prototype.price = 100;
Gadget.prototype.rating = 3;
Gadget.prototype.getInfo = function () {
  return "Rating: " + this.rating + ", price: " + this.price;
};

var newtoy = new Gadget("webcam", "black");
newtoy.name;
("webcam");
newtoy.color;
("black");
newtoy.whatAreyou();
("I am a black webcam");
newtoy.price;
100;
newtoy.rating;
3;
newtoy.getInfo();
("Rating: 3, price: 100");
```

prototype은 살아있다는 점에 유의하자. 자바스크립트에서 객체는 참조로 전달되므로 prototype은 모든 새 객체 인스턴스에 복사되지 않는다. 이것이 실제 무엇을 의미하는가? 이것은 언제든지 prototype을 수정할 수 있고, 모든 객체(심지어 수정 전에 생성된 객체도)에서 변경 내용을 볼 수 있다는 것을 의미한다.

prototype에 새로운 메소드를 추가하여 예제를 계속 작성해 보자.

```js
Gadget.prototype.get = function (what) {
  return this[what];
};
function get(what)
```

newtoy 객체가 get() 메소드가 정의되기 전에 생성되었음에도 불구하고, newtoy 객체는 다음과 같이 새로운 메소드에 접근할 수 있다.

```js
newtoy.get("price");
100;

newtoy.get("color");
("black");
```

## 자체 속성 대 프로토타입 속성

앞의 예제에서, getInfo()는 내부적으로 객체의 속성에 접근하는데 사용되었다. 다음과 같이 Gadget.prototype을 사용하여 동일한결과를 얻을 수 있다.

```js
Gadget.prototype.getInfo = function () {
  return 'Rating: ' + Gadget.prototype.rating + ', price: ' + Gadget.prototype.price;
}
function getInfo()
```

차이점이 무엇일까? 이것을 알아보기 위ㅏ해선 prototype이 어떻게 동작하는지 자세히 살펴보자.

newtoy 객체를 다시 사용해보자.

```js
var newtoy = new Gadget("webcam", "black");
```

newtoy 속성인 newtoy.name에 접근하려고 하면, 자바스크립트 엔진은 객체의 모든 속성에서 name을 찾고, 발견하면 다음과 같이 해당 값을 반환한다.

```js
newtoy.name;
("webcam");
```

rating 속성에 접근하면 무슨 일이 생길 것 같은가? 자바스크립트 엔진은 newtoy 객체의 모든 속성을 검사하지만 rating이라는 속성을 찾지 못한다. 그러면 자바스크립트 엔진은 이 객체를 만드는 데 사용된 생성자 함수의 prototype을 식별한다.(newtoy.constructor.prototype을 수행하는 것과 동일). prototype 객체에서 속성이 발견되면, 이 속성이 사용된다.

```js
newtoy.rating;
3;
```

prototype에 직접 접근할 수 있다. 모든 객체는 객체를 생성한 함수에 대한 참조인 constructor 속성을 가진다.

```js
newtoy.constructor === Gadget;
true;
newtoy.constructor.prototype.rating;
3;
```

이제 한 단계 더 들어가 보자. 모든 객체는 생성자가 있다.

prototype은 객체이므로 이것 역시 생성자가 있어야 한다. 즉 prototype을 가진다. 프로토타입 체인을 올라가다보면, 결국 최상위 수준 부모인 내장 Object() 객체에 도달한다.

실제로 이는 newtoy.toString()을 호출할 때, newtoy에 자체 toString() 메소드가 없고 prototype에도 없으면, 결국 Object 객체의 toString() 메소드를 사용한다는 것을 의미한다.

```js
newtoy.toString();
("[object Object]");
```

## 프로토타입 속성을 자체 속성으로 덮어 쓰기

앞에서 살펴본 것처럼, 어떤 객체에서 자체 속성을 가지고 있지 않으면, 프로토타입 체인 어딘가에 있는 속성을 사용할 수 있다. 객체가 자체 속성을 가지고 있고 프로토타입에도 동일한 이름을 가진 속성이 있는 경우는 어떨까? 이 경우 자체 속성이 프로토타입 속성보다 우선된다.

속성 이름이 자체 속성과 prototype 객체의 속성에 모두 존재하는 시나리오를 생각해 보자.

```js
function Gadget(name) {
  this.name = name;
}
Gadget.prototype.name = "mirror";
("mirror");
```

새 객체를 만들고 이 객체의 name 속성에 접근하면 다음과 같이 객체 자체의 name 속성이 제공된다.

```js
var toy = new Gadget("camera");
toy.name;
("camera");
```

다음과 같이 hashOwnProperty()를 사용해 속성이 정의된 위치를알 수 있다.

```js
toy.hasOwnProperty("name");
true;
```

만일 toy 객체의 자체 name 속성을 삭제하면, 동일한 이름을 가진 프로토타입의 name 속성이 다음과 같이 등장한다.

```js
delete toy.name;
true;

toy.name;
("mirror");

toy.hasOwnProperty("name");
false;
```

물론 다음과 같이 객체 자체 속성을 언제든지 만들 수 있다.

```js
toy.name = "camera";

toy.name;
("camera");
```

특정 속성의 출저를 찾으려면 hasOwnProperty() 메소드를 사용하면 된다. 앞에서 toString() 메소드를 사용했다. 그럼 과연 이 메소드는 어디서 온 것일까?

```js
toy.toString();
("[object Object]");
toy.hasOwnProperty("toString");
false;
toy.constructor.hasOwnProperty("toString");
false;
toy.constructor.prototype.hasOwnProperty("toString");
false;
Object.hasOwnProperty("toString");
false;
Object.prototype.hasOwnProperty("toString");
true;
```

## 속성 열거하기

객체의 모든 속성을 나열하려면 for ...in 루프를 사용할 수 있다. 앞에서 다뤘듯이 for는 배열에 적합하고, for..,in은 객체에 더 적합하다. 객체의 URL에 대한 쿼리 문자열을 생성하는 예제를 살펴보자.

```js
var params = {
  productid: 666,
  section: "products",
};
var url = "http://example.org/page.php?",
  i,
  query = [];

for (i in params) {
  query.push(i + "=" + params[i]);
}

url += query.join("&");
```

이렇게 하면 다음과 같은 url 문자가 생긴다.

    "http://example.org/page.php?productid=666&section=products"

다음 몇 가지 사항에 주의해야 한다.

- 모든 속성이 for ...in 루프에 표시되는 것은 아니다. 예를 들어, length(배열의 경우) 및 생성자 속성은 표시되지 않는다. 표시되는 속성을 열거 가능(enumerable)하다고 말한다. propertyIsEnumerable() 메소드의 도움으로 어떤 속성이 열거 가능한지 확인할 수 있다.
- 프로토타입 체인을 통해 온 프로토타입도 열거 가능한 경우 표시된다. 객체의 자체 속성인지 프로토타입의 속성인지 여부는 hasOwnProperty() 메소드를 사용하여 확인할 수 있다.
- PropertyIsEnumerable() 메소드는 열거 가능하고 for...in 루픙에 표시될지라도, 모든 프로토타입의 속성에 대해 false를 반환한다.

이제 위의 메소드들을 실제로 사용해보자.

```js
function Gadget(name, color) {
  this.name = name;
  this.color = color;
  this.getName = function () {
    return this.name;
  };
}
Gadget.prototype.price = 100;
Gadget.prototype.rating = 3;
```

이 다음 새 객체를 생성해 보자.

```js
var newtoy = new Gadget("webcam", "black");
```

이제 for...in 루프를 사용해 반복하면 프로토타입에서 온 속성을 포함, 모든 객체의 속성을 볼 수 있다.

```js
for (var prop in newtoy) {
  console.log(prop + " = " + newtoy[prop]);
}
```

메소드는 결국 함수인 속성이다 결과 또한 객체의 메소드를 포함한다.

```js
name = webcam;
color = black;
getName = function () {
  return this.name;
};
price = 100;
rating = 3;
```

객체의 자체 속성과 프로토타입의 속성을 구분하려면 hasOwnProperty()를 사용한다.

```js
newtoy.hasOwnProperty("name");
true;
newtoy.hasOwnProperty("price");
false;
```

다시 루프를 반복하되 이번에는 객체의 자체 속성만 표시한다.

```js
for (var prop in newtoy) {
  if (newtoy.hasOwnProperty(prop)) {
    console.log((prop = "=" + newtoy[prop]));
  }
}
```

결과는 다음과 같다.

```js
name = webcam;
color = black;
getName = function () {
  return this.name;
};
```

이제 propertyIsEnumerable()을 사용해 보자. 이 메소드는 내장되지 않은 객체의 자체 속성에 대해 true를 반환한다.

```js
newtoy.propertyIsEnumerable("name");
true;
```

대부분의 내장된 속성과 메소드는 열거할 수 없다.

```js
newtoy.propertyIsEnumerable("constructor");
false;
```

프로토타입체인을 따라오는 모든 속성은 열거할 수 없다.

```js
newtoy.propertyIsEnumerable("price");
false;
```

그러나 prototype에 포함된 객체에 도달하여 propertyisEnumerable() 메소드를 호출하면, 이 경우 속성을 열거할 수 있다.

```js
newtoy.constructor.prototype.propertyIsEnumerable("price");
true;
```

## IsPrototypeOf() 메소드 사용하기

객체는 또한 IsPrototypeOf() 메소드도 가지고 있다. 이 메소드는 특정 객체가 다른 객체의 프로토타입으로 사용되는지 여부를 알려준다.

monkey를 예로 들어보자.

```js
var monkey = {
  hair: true,
  feeds: "bananas",
  breathes: "air",
};
```

이제 Human 생성자 함수를 만들고 monkey를 가리키도록 prototype 속성을 설정한다.

```js
function Human(name) {
  this.name = name;
}

Human.prototype = monkey;
Object { hair: true, feeds: "bananas", breathes: "air" }
```

그 다음, george라는 새로운 Human 객체를 생성하고, monkey가 george의 프로토타입인지 확인해 보면 true가 나온다.

```js
var george = new Human("George");

monkey.isPrototypeOf(george);
true;
```

프로토타입이 무엇인지 알고 있어야 프로토타입이 monkey인 것이 사실인지 확인해 볼 수 있다. 아는 것이 아무것도 없다면, 프로토타입이 맞는지 물어볼 수가 없다.

그렇다면 객체에 직접 프로타타입이 무엇인지 물어볼 수는 없을까? 대답은 모든 브라우저에서까진 아니지만 대부분의 브라우저에선 Object.getPrototypeOf()의 사용이 가능하다는 것이다.

```js
Object.getPrototypeOf(george).feeds;
("bananas");
Object.getPrototypeOf(george) === monkey;
true;
```

getPrototypeOf()를 지원하지 않는 일부ES5 이전 환경에서는 `__proto__` 라는 특별 속성을 사용할 수 있다.

## secret `__proto__` link

prototype 속성은 현재 객체에 없는 속성에 접근하려고 할 때 사용된다.

monkey라는 객체를 가정해보고, 이를 Human() 생성자로 객체를 만들 때 프로토타입으로 사용해 보자.

```js
var monkey = {
  hair : true,
  breathes: 'air'
};

function Human(name) {}
Human.prototype = monkey;
Object { hair: true, breathes: "air" }
```

이제 developer 객체를 만들고 다음과 같은 속성을 지정해 보자.

```js
var developer = new Human();
developer.feeds = "pizza";
developer.hacks = "JavaScript";
```

이제 이 속성에 접근해보자.(예를 들어, hacks는 developer 객체의 속성이다.)

```js
developer.hacks;
("JavaScript");
```

feeds 속성은 다음과 같이 객체에서도 찾을 수 있다.

```js
developer.feeds;
("pizza");
```

breathes 속성은 developer 객체의 속성으로 존재하지 않으므로, prototype 객체로 연결되는 비밀 링크나 통로가 있는 것처럼 프로토타입이 조회된다.

```js
developer.breathes;
("air");
```

비밀 링크는 대부분의 최시니 자바스크립트 환경에서 `__proto__` 속성으로 노출된다.

```js
developer.__proto__ === monkey;
true;
```

이 비밀 속성을 학습 목적으로 사용할 수는 있지만, 실제 스크립트에서 사용하는것은 좋지 않다. 모든 브라우저에서 지원하지 않기 때문에 스크립트가 정상 동작하지 않을 것이다.

prototype은 해당 객체를 만드는데 사용되는 생성자 함수의 속성인 반면, `__proto__`는 인스턴스의 속성이므로 `__proto__`는 prototype과 동일하지 않다.

```js
typeof developer.__proto__;
("object");
typeof developer.prototype;
("undefined");
typeof developer.constructor.prototype;
("object");
```

`__proto__`는 학습이나 디버깅 목적으로만 사용해야 한다.

# 내장 객체 보강

Array, String, 그리고 Object와 Function 같이 내장된 생성자 함수로 만든 객체는 프로토타입을 사용해 보강(또는 향상)시킬 수 있다. 예를 들면, Array 프로토타입에 새 메소드를 추가하고, 모든 배열에서 이 메소드를 사용할 수 있다.

PHP에는 배열에 값이 있는지 여부를 알려주는 in_array()라는 함수가 있다. 자바스크립트에 in_array() 메소드는 없지만, 동일한 목적으로 사용할 수 있는 indexOf()가 있다. 예제를 통해 알아보고 Array.prototype에 추가해 보자.

```js
Array.prototype.inArray = function (needle) {
  for (var i = 0, len = this.length; i < len; i++) {
    if (this[i] === needle) {
      return true;
    }
  }
  return false;
};
```

이제 모든 배열은 새 메소드에 접근할 수 있다. 다음 코드를 테스트해 보자.

```js
colors.inArray("red");
true;
colors.inArray("yellow");
false;
```

어플리케이션에서 자주 단어를 역순으로 입력해야 하는 경우가 이싸고 가정해 보자. 문자열 객체에 내장된 reverse() 메소드가 있으면 좋을 것이다. Array.prototype.reverse()를 빌려서 String 프로토타입에 reverse() 메소드를 쉽게 추가할 수 있다.

```js
String.prototype.reverse = function () {
  return Array.prototype.reverse.apply(this.split("")).joint("");
};
```

이 코드는 split() 메소드를 사용해 문자열에서 배열을 만든 다음, 이 배열에서 reverse()메소드를 호출해 역순으로 배열을 생성한다. 그런 다음 결과 배열을 join() 메소드를 사용해 문자열로 되돌린다.

```js
"bumblebee".reverse();
("eebelbmub");
```

## 내장 객체 보강

프로토타입을 통해 내장 객체를 보강하는 것은 강력한 기술이며, 자바스크립트를 ㅇ우리가 원하는 모양으로 만들 수 있게 해준다. 그러나 이 방법을 사용하기 전에 우리는 항상 우리의 선택을 다시 한 번 고민해야 한다.

그 이유는 우리가 사용중인 서드 파티 라이브러리나 위젯에 관계없이 동일한 방식으로 동작하기를 기대하기 때문이다. 핵심 객체를 수정하면, 사용자와 관리자를 혼란스럽게 할 수 있으며, 오류또한 발생할 수 있따.

자바스크립트가 발전하고 브라우저 벤더는 지속적으로 더 많은 기능을 지원하고 있다. 우리가 프로토타입에 추가한 메소드가 향후에 내장 메소드가 될 수도 있다. 이 경우 우리가 ㅊ추가한 메소드는 더 이상 필요하지 않게 된다. 또한 이렇게 추가한 메소드를 사용해 이미 많은 코드를 작성했는데 이 메소드가 새롭게 내장된 메소드의 구현과 다르다면 어떻게 해야할까?

내장 프로토타입을 보강하는 가장 보편적이고 수용할 수 있는 유스 케이스는 구형 브라우저에 새로운 기능(ECMA에서 이미 표준화 됐고 새로운 브라우저에 구현된 기능)을 지원할 수 있도록 추가하는 것이다. 이러한 확장은 `심(shim)`또는 `폴리필(polyfill)`로 알려져 있다.

프로토타입을 보강할 때, 구현하기 전에 먼저 메소드가 있는지 확인해야 한다. 메소드가 있다면 브라우저의 네이티브 구현을 사용할 수 있다.

예를 들어 문자열에 trim() 메소드를 추가해 보자. 이 메소드는 ES5에는 있지만, 구형 브라우저에서는 지원하지 않는 메소드이다.

```js
if (typeof String.prototype.trim !== "function") {
  String.prototype.trim = function () {
    return this.replace(/^\s+|s+$/g, "");
  };
}

" hello ".trim();
("hello");
```

## 프로토타입 따라잡기

프로토타입을 다룰 때 고려해야할 두 가지 중요한 사항은 다음과 같다.

- prototype 객체를 완전히 대체할 때를 제외하고는 프로토타입 체인은 살아있다.
- prototype.constructor 메소드는 안정적이지 않다.

간단한 생성자 함수와 두 개의 객체를 생성해 보자.

```js
function Dog() {
  this.tail = true;
}
var benji = new Dog();
var rusty = new Dog();
```

benji와 rusty 객체를 생성한 후에도, Dog() 프로토타입에 속성을 추가할 수 있으며 기존 객체에서도 새 속성에 접근할 수 있다. say() 메소드를 추가해보자.

```js
Dog.prototype.say = function () {
  return "Woof!";
};
```

이제 두 객체 모두 메소드에 접근할 수 있다.

```js
benji.say();
("Woof!");
rusty.say();
("Woof!");
```

이 시점에서 객체를 생성하는 데 사용된 생성자 함수가 무엇인지 확인해 보면 제대로 보고할 것이다.

```js
benji.constructor === Dog;
true;
rusty.constructor === Dog;
true;
```

이제 prototype 객체를 새로운 객체로 완전히 덮어 씌워 보자.

```js
Dog.prototype = {
  paws : 4,
  hair : true
};
Object { paws: 4, hair: true }
```

이전 객체가 새로운 프로토타입의 속성에 접근하지 못한다. 다음과 같이 이전 프로토타입 객체를 가리키는 비밀 링크를 여전히 유지하고 있다.

```js
typeof benji.paws;
("undefined");
benji.say();
("woof!");
typeof benji.__proto__.say;
("function");
typeof benji.__proto__.paws;
("undefined");
```

지금부터 새로 만들 객체는 다음과 같이 업데이트된 프로토타입 객체를 사용한다.

```js
var lucy = new Dog();

lucy.say();
TypeError: lucy.say is not a function

lucy.paws;
4
```

비밀 `__proto__` 링크는 다음 코드 행에 표시된 대로 새 프로토타입 객체를 가리킨다.

```js
typeof lucy.__proto__.say;
("undefined");
typeof lucy.__proto__.paws;
("number");
```

이제 새 객체의 constructor 속성은 더 이상 올바르게 보고하지 않는다. Dog()를 가리킬 것으로 기대하지만, 다음 예제에서 볼 수 있듯이 대신 Object()를 가리킨다.

```js
lucy.constructor;
function Object()

benji.constructor;
function Dog() {
    this.tail = true
}
```

다음과 같이 프로토타입을 완전히 덮어 쓴 후 constructor 속성을 다시 설정하면, 이 혼란을 쉽게 방지할 수 있다.

```js
function Dog() {}
Dog.prototype = {};
new Dog().constructor === Dog;
false;

Dog.prototype.constructor = Dog;
new Dog().constructor === Dog;
true;
```

## 프로토타입 요약

- 모든 함수에는 prototype 이라는 속성이 있다. 처음에는 빈 객체, 즉 자체 속성이 없는 객체를 포함한다.
- prototype 객체에 속성ㅇ과 메소드를 추가할 수 있다. 또한 다른 객체로 완전히 대체할 수도 있다.
- 생성자 함수(new와 함께)를 사용해 객체를 생성하면, 객체는 생성자의 프로토타입을 가리키는 비밀 링크를 가져와서 프로토타입의 속성에 접근할 수 있다.
- 객체의 자체 속성이 동일한 이름의 프로토타입 속성보다 우선한다.
- hasOwnProperty() 메소드를 사용해 객체 자체의 속성과 prototype 속성을 구별한다.
- 프로토타입 체인이 있다. foo.bar를 실행했는데 foo 객체에 bar 속성이 없으면, 자바스크립트 인터프리터는 프로토타입에서 bar 속성을 찾는다. 그래도 발견되지 않으면, 프로토타입의 프로토탕입을 검색하고 이런 검색을 Object.prototype에 도달할 때까지 계속한다.
- 내장된 생성자 함수의 프로토타입을 보강할 수 있으며, 모든 객체는 추가된 내용에 접근할 수 있다. Array.prototype.flip에 함수를 할당하면, 모든 배열은 [1,2,3].flip()과 같이 즉시 flip() 메소드를 사용할 수 있다. 그러나 반드시 추가하고자 하는 메소드/속성이 이미 있는지 확인해서 우리의 스크립트를 미래에 대비할 수 있도록 한다.
