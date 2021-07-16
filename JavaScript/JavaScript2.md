# JavaScript 2

# 함수

함수를 마스터하는 것은 프로그래밍 언어를 배움에 있어 매우 중요한 기술이다. 자바스크립트는 함수를 많이 사용하고, 언어의 유연성과 표현력의 상당 부분이 함수에서 비롯된다.

## \* 함수란 무엇인가?

함수를 사용하면 코드를 그룹화하고 이름을 지정해 그 이름으로 재사용할 수 있다.

```m
function sum(a,b) {
... var c = a+b;
... return c;
... }
```

함수를 구성하는 부분은 다음과 같다.

- function 키워드
- 함수 이름(위의 경우 sum)
- 함수의 매개변수(위의 경우 a, b). 함수는 매개변수를 사용하지 않거나, 또는 원하는 매개 변수를 사용할 수 있으며, 매개변수는 쉼표로 구분한다.
- 코드 블록 = 함수 본문이라고도 한다.
- return문 = 함수는 항상 값을 반환한다. 값을 명시적으로 반환하지 않으면, 암시적으로 undefined를 반환한다.

함수는 단일 값만 반환할 수 있다. 더 많은 값을 반환해야 하는 경우, 배열을 반환하면 된다.

위의 예제와 같은 구문을 함수 선언이라고 한다.

## \* 함수 호출

함수를 사용하려면 함수를 호출 해야 한다. 간단히 함수의 이름을 사용하여 호출하면 된다. 선택적으로 괄호 안에 매개변수를 제공할 수도 있다.

두 개의 인수를 전달하여 sum() 함수를 호출하고, 함수가 반환하는 값을 변수 result에 할당해 보자.

```m
> var result = sum(1,2);
undefined
> result
3
```

## \* 매개변수

함수를 정의할 때, 함수가 호출될 때 필요한 `매개변수`를 지정할 수 있다. 힘스기 매개변수를 필요로 하지 않을 수도 있지만, 필요한 경우 이를 전달하지 않으면 undefined 값이 지정된다.

다음 예제에선 1과 undefined를 합산하려고 시도하기 때문에 함수는 NaN을 반환한다.

```m
> sum(1)
NaN
```

sum은 저 위에서 정의한 함수이다.

기술적으로 매개변수와 인수(argument)는 서로 다르지만, 두 용어는 종종 같은 의미로 사용된다. 매개변수는 함수와 함께 정의되며, 인수는 호출될 때 함수에 전달된다.

```m
> function sum(a,b) {
... return a + b;
... }
undefined
> sum(1,2)
3
```

위의 예제에서 a와 b는 매개변수이고, 1과 2는 인수다.

자바스크립트는 인수를 받는 데 있어 까다롭지 않다. 함수가 필요로 하는 개수 이상의 인수를 전달하여도 여분의 인수는 무시된다.

```m
> sum(1,2,3,4,5);
3
```

게다가 받아들이는 매개변수의 수에 유연한 함수를 작성할 수 있다. 이는 각 함수 내부에서 자동으로 생성되는 특별한 값인 arguments 덕분에 가능하다.
단순히 전달받은 모든 인수를 반환하는 함수는 다음과 같다.

```m
> function args() {
... return arguments;
... }
undefined
> args();
[Arguments] {}
> args(1,2,3,4,true,'ninja');
[Arguments] { '0': 1, '1': 2, '2': 3, '3': 4, '4': true, '5': 'ninja' }
```

원본은 리스트형태인데 왜 딕셔너리 형태로 나오는지는 모르겠다.

arguments를 사용하면 다음 예제와 같이 sum() 함수를 개선해 여러 개의 인수를 허용하거나 동작하게 만들 수 있다.

ex)

```m
> function sumSteroids() {
... var i
... res = 0,
... number_of_params = arguments.length;
... for (i=0; i<number_of_params; i++) {
..... res += arguments[i];
..... }
... return res;
... }
```

이제 예제를 호출해보자.

```m
> sumSteroids(1,1,1);
3
> sumSteroids(1,2,3,4);
10
> sumSteroids(1,2,3,4,5,5,6,3,1)
30
> sumSteroids(5)
5
> sumSteroids();
0
```

arguments.length 표현식은 함수가 호출될 때 전달받은 인수의 수를 반환하고 res 값에 for문을 통해 arguments의 인덱스에 해당하는 값을 더해 출력한다.

위의 함수 sumSteroids에서 arguments가 배열처럼 보이지만 사실은 배열이 아니라 배열과 비슷한 객체라는 것을 알아야 한다.

그리고 ES6 함수 매개변수는 디폴트 값, 나머지 매개변수를 가질 수 있으며, 구조화가 가능하다.

## 디폴트 매개변수

함수 매개변수에 디폴트 값을 지정할 수 있다. 함수를 호출할 때 매개변수가 생략되면 매개변수에 지정된 디폴트 값이 사용된다.

```mm
> function render(fog_level = 0, spark_level=100) {
... console.log(`Fog Levle : ${fog_level} and spark level : ${spark_level}`)
... }

> render()
Fog Levle : 0 and spark level : 100
> render(15,20)
Fog Levle : 15 and spark level : 20
```

render의 함수에서 매개변수를 별도로 설정하지 않으면 설정해놓은 초기값이 출력되고, 별도로 입력하면 해당 값들을 인수로 받아 출력한다.

매개 변수의 디폴트 값을 제공할때 다른 매개변수도 참조할 수 있다.

```m
> function t(fog_level=1, spark_level=fog_level){
... console.log(`Fog level: ${fog_level} and spark_level:${spark_level}`)
... }
> t()
Fog level: 1 and spark_level:1
```

디폴트 매개변수에는 자체 범위가 없다. 이 범위는 함수의 외부 함수 범위와 함수의 내부 범위 사이에 끼어 있다. 매개변수가 내부 범위의 변수에 의해 가려지면, 내부 변수를 사용할 수 없다.

```m
> var scope = 'outer';

> function scoper(val=scope) {
... var scope = 'inner';
... console.log(val);
... }

> scoper()
outer
```

val이 scope 변수의 내부 정의에 의해 가려질 것으로 예상하겠지만, 디폴트 매개변수가 자체 범위를 가져 val에 할단된 값은 내부 범위에 영향을 받지 않는다.

## 나머지 매개변수

나머지 매개변수를 사용하면 배열 형태로 함수에 임의의 수의 매개변수를 보낼 수 있다.

나머지 매개변수는 반드시 매개변수 목록의 마지막 매개변수여야 하며, 하나의 나머지 매개변수만 가능하다.

마지막 일반 매개변수 앞에 나머지 연산자(...)를 두면 매개변수가 나머지 매개변수임을 타나낸다.

```mm
> function sayThing(tone,...quotes){
... console.log(Array.isArray(quotes));
... console.log(`In ${tone} voice, I say ${quotes}`)
... }

> sayThing("Morgan Freeman", "Something serious","Imploding Univers","Amen");
true
In Morgan Freeman voice, I say Something serious,Imploding Univers,Amen
```

함수에 전달된 첫 번째 매개변수는 tone으로 받는 반면, 나머지 매개변수는 배열로 받는다.

나머지 매개변수는 argument 변수를 대체할 수 있다.

## 스프레드 연산자

스프레드 연산자는 나머지 연산자와 모양은 동일하지만 정반대의 기능을 수행한다. 스프레드 연산자는 함수를 호출하거나 배열을 정의할 때 인수를 제공하는 데 사용된다. 또한 배열을 받아 배열의 요소를 개별 변수로 분리한다.

```m
> function sumAll(a,b,c){
... return a+b+c
... }

> console.log(sumAll(...number))
21
```

sumAll() 함수를 호출할 때, 스프레드 연산자(...)를 사용하고 number 배열을 함수 호출에 전달한다. 그런 다음 배열은 개별 변수 a,b,c로 나뉜다.

스프레드 연산자는 자바스크립트의 배열 기능을 향상시킨다. 다른 배열로 구열된 배열을 생성하려고 하면 기존 배열 구문은 이를 지원하지 않는다. push, splice, conact등을 사용해야 한다. 그러나 스프레드 연산자를 사용하면 간단하다.

```mm
> var mideweek = ['Wed','Thu'];
undefined
> var weekend = ['Sat','Sun'];
undefined
> var week = ['Mon','Tue',...mideweek, 'Fri', ...weekend];
undefined
> console.log(week)
[
  'Mon', 'Tue',
  'Wed', 'Thu',
  'Fri', 'Sat',
  'Sun'
]
```

# 사전 정의된 함수

자바 스크립트의 내장 함수들 중엔 유용한 함수가 많다.

- parseInt()
- parseFloat()
- isNaN()
- isFinite()
- encodeURI()
- decodeURI()
- encodeURIComponent()
- decodeURIComponent()
- eval()

## ParseInt()

ParseInt() 함수는 모든 유형의 입력(대부분 문자열)을 받아 정수로 만든다. 실패하면 NaN을 반환한다.

```mm
> parseInt('abc123');
NaN
> parseInt('1abc23');
1
> parseInt('123abc');
123
```

그리고 이 함수는 선택적인 두 번째 매개변수인 기수(radix)를 사용해 숫자의 유형(10,16,2진수 등)을 알려준다. 예를 들어 FF 문자열에서 10진수를 추출하려고 하면 의미가 없다.
결과는 NaN이지만, FF를 16진수로 시도하면 255가 된다.

```mm
> parseInt('FF',10);
NaN
> parseInt('FF',16);
255
```

또 다른 예는 베이스 10(10진수)와 베이스 8(8진수)인 문자열을 파싱(parsing -> parseInt랑 여관있는듯?)하는 것이다.

```mm
> parseInt('0377', 10);;
377
> parseInt('0377', 8);;
255
```

parseInt()를 호출할 때 두 번째 인수를 생략하면 함수는 다음 예외를 제외하고 모두 10(10진수)로 가정한다.

- 0x로 시작하는 문자열을 전달하면 기수는 16(16진수)로 가정한다.
- 전달한 문자열ㅇ이 0으로 시작하면 기수를 8(8진수)로 가정한다.

```mm
> parseInt('377'); // 아무것도 없어 10진수로 가정한 경우
377
> console.log(0o377); // 8진수로 가정한 경우
255
undefined
> parseInt('0x377'); // 16진수로 가정한 경우
887
```

가장 안전한 방법은 기수를 지정해 주는 것이다.

## parseFloat()

parseFloat() 함수는 parseInt() 함수와 비슷하지만, 입력에서 숫자를 추추할 때 10진수를 찾는다.

```mm
> parseFloat('123');
123
> parseFloat('1.23');
1.23
> parseFloat('1.23.00');
1.23
> parseFloat('1.23abc.00');
1.23
> parseFloat('a.bc1.23.00');
NaN
```

parseInt()와 마찬가지로 parseFloat()는 예상치 못한 문자가 나타나면 준자열의 나머지 부분에 사용할 수 있는 숫자가 있더라도 이를 무시한다.

그리고 parseFloat()함수는 parseInt()함수와 달리 입력값의 지수를 이해한다.

```mm
> parseFloat('123e-2');
1.23
> parseFloat('1e10');
10000000000
> parseInt('1e10'); // parseInt는 지수를 문자열로 인식함.
1
```

## isNaN()

isNaN을 사용하면 산술 연산에서 안전하게 사용할 수 있는 유효한 숫자인지 확인할 수 있다.

이 함수는 parseInt(), paresFloat() 또는 산술 연산이 성공했는지 여부를 확인하는 편리한 방법이기도 하다.

```mm
> isNaN(NaN);
true
> isNaN(123);
false
> isNaN(1.23);
false
> isNaN(parseInt('abc123'));
true
```

이 함수는 또한 입력을 숫자로 변환하려고 시도한다.

```mm
> isNaN('1.23');
false
> isNaN('a1.23');
true
```

isNaN() 함수는 특별 값 NaN이 NaN을 포함한 어떤 값과도 같지 않기 때문에 유용하다.
즉 NaN === NaN은 false다.

## isFinite()

isFinite() 함수는 입력 값이 Infinity나 NaN이 아닌 숫자인지 확인한다.

```mm
> isFinite(Infinity);
false
> isFinite(-Infinity);
false
> isFinite(12);
true
> isFinite(1e308);
true
> isFinite(1e309);
false
```

Javascript.md에서 살펴본 바와 같이 자바스크립트에서 가장 큰 숫자는 1.7976931348623157e+308임을 기억하자. 1e309는 따라서 무한대가 된다.

# 변수 범위 ( 매우 중요 )

자바 스크립트의 변수는 블록 범위가 아닌 `함수 범위`에 정의된다는 점을 기억해야 한다. 즉 변수가 함수 내에 정의된 경우, 함수 외부에서 변수가 보이지 않는다.

그러나 if 또는 for 코드 블록 내부에 정으된 경우에는 블록 외부에서도 볼 수 있다. `전역(global) 변수`가 함수외부에서 정의하는 변수를 의미한다. 반면 `지역(local)`변수는 함수 내에서 정의된 변수다. 함수 내부의 코드는 지역 변수뿐만 아니라 모든 전역 변수에도 접근할 수 있다.

다음 예제에서

- f() 함수는 global 변수에 접근할 수 있다.
- f() 함수 외부에 local 변수는 존재하지 않는다.

```mm
> var global = 1;
undefined
> function f() {
... var local = 2;
... global++
... return global;
... }
undefined
> f()
2
> global
2
> f()
3
> global
3
> local
Uncaught ReferenceError: local is not defined
```

또한 변수를 선언할 때 var문을 사용하지 않으면, 이 변수는 자동으로 전역 범위로 할당 된다는 점에 유의하자.

```m
> function a () {locala =2}
undefined
> locala
Uncaught ReferenceError: locala is not defined
> a()
undefined
> locala
2
```

함수 a()는 locala 변수를 포함하고 있다. 함수를 호출하기 전에는 변수가 존재하지 않는다. 함수를 처음 호출하면 local 변수가 전역 범위로 생성된다. 그 다음에 함수 밖에서 locala 변수에 접근하면 사용이 가능하다.

## 변수 호이스팅

```mm
var a = 123;

> function f() {
... alert(a);
... var a = 1;
... alert(a);
... }
```

첫번째 alert() 함수는 123을 표시하고 두 번째는 1을 표시할 것으로 기대할 것이다. 그러나 다르다.

첫번째 alert()는 undefined를 표시한다. 이는 함수 내에서 지역 범위가 전역 범위보다 더 중요하기 때문이다. 다라서 지역 변수는 같은 이름의 전역 변수를 덮어 쓴다.

첫번째 alert() 당시 a 변수는 아직 지정되지 않았지만(따라서 undefined 값), 호이스팅(hoisting)이라는 특별한 동작으로 인해 여전히 지역 공간에 존재한다.

자바스크립트 프로그램 실행이 새 함수로 들어가면, 함수에서 선언된 모든 변수가 함수의 맨 위로 이동하거나 호이스팅(위로 올라간다) 된다. 또한 선언만 호이스팅되는데, 이는 변수의 존재만 맨 위로 이동함을 의미한다.
모든 할당은 원래 위치 그대로 남아있는다.

위의 예제에서 지역 변수 a의 선언은 맨 위로 호이스팅 됐다. 선언만 호이스팅 됐고 1로 할당은 아니다.
다음 예제와 같이 써있다고 생각하면 된다.

```mm
> function f() {
... var a;
... alert(a)
... a =1;
... alert(a);
... }
```

## 블록 범위

ES6에서는 범위를 선언할 때 추가 범위를 제공한다. 또한 변수를 선언할 수 있는 let과 const 키워드를 도입했다.

### let

let으로 선언된 변수는 블록 범위를 가진다. 변수는 현재 블록 내에만 존재한다. var로 선언된 변수는 앞에서 살펴본 것과 같이 함수 범위를 가진다.

```mm
> var a = 1;

> {
... let a = 2;
... console.log( a );
... }
2

> console.log( a )
1
```

중괄화 '{' '}' 사이의 범위가 블록이다.

자바스크립트에서는 블록이 범위와 관련이 없어 관용적으로 사용해야할 필요가 있다. 그리고 let키워드를 사용해 블록 범위 변수를 생성할 수 있다. 블록 내부에서 생성된 변수 a는 블록 내에서 사용할 수 있다. 블록 범위 변수를 선언할 때, 일반적으로 let 선언을 블록의 맨 위에 추가하는 것이 좋다.

```mm
> function swap(a,b) {
... if (a>0 && b>0) {
..... let tmp=a;
..... a=b;
..... b=tmp;
..... }
... console.log(a,b);
... console.log(tmp);
... reutrn [a,b];
... }

> swap(1,2);
2 1
Uncaught ReferenceError: tmp is not defined
    at swap (REPL80:8:13)
```

보다시피 .tmp는 let으로 선언되어 정의된 블록에섬나 사용이 가능하다. 실제 코드를 작성할 때에는 블록 범위 변수 사용을 최대화해야 한다. var 선언을 사용해야 하는 아주 특별한 이유가 있지 않는 한, 블록 범위 변수를 사용해야 한다.

그러나 let 키워드를 잘못 사용했을 때의 문제점이 있다.

let 키워드를 사용해 동일한 함수 또는 블록 범위 내에서 동일한 변수를 재선언할 수 없다.

```mm
> function blocker(x){
... if(x){
..... let f;
..... let f;
let f;
    ^

Uncaught SyntaxError: Identifier 'f' has already been declared
```

ES7에서 let 키워드로 선언된 변수는 블록 범위로 호이스팅된다. 그러나 선언 전에 변수를 참조하면 오류가 발생한다.

## const

const 키워드로 선언된 변수는 값에 대한 읽기 전용 참조를 생성한다. 이것은 참조의 값이 변경 불가능하다는 것을 의미하지는 않는다. 그러나 변수 식별자는 다시 할당할 수 없다. 상수는 let키워드를 사용하여 생성된 변수와 마찬가지로 블록 범위다. 또한 선언할 때 변수에 값을 할당해야 한다.

```mm
> const car = {}
undefined
> car.tyres =4
4
> car
{ tyres: 4 }
```

예제에서 상수 car에 {}값을 할당했다. 한번 할당되면 이 참조는 변경할 수 없다.

```mm
> const car = 123
Uncaught SyntaxError: Identifier 'car' has already been declared
```

- 가능하다면 const를 사용해라. 값이 변하지 않는 모든 변수에 이 키워드를 사용한다.
- var의 사용은 최대한 피해라.

## 함수는 데이터

자바스크립트의 함수는 실제로 데이터다. 그러므로 다음과 같이 함수를 만들어 변수에 함수를 할당할 수 있다.

```mm
> var f = function() {
... return 1;
... }
```

함수를 정의하는 이런 방식을 함수 리터럴 표기법 이라고 한다.

function() { return 1;} 부분은 `함수 표현식`이다. 함수 표현식은 선택 사항으로 이름을 가질 수 있으며, NFE(Named Function expression) = 이름있는 함수 표현식이 된다.

따라서 자바스크립트 함수는 데이터지만 다음과 같은 두 가지 중요한 특징을 가진 특별한 종류의 데이터다.

- 코드를 포함한다
- 실행 가능하다.

함수를 실행하는 방법은 이름 뒤에 괄호를 추가하는 것이다.

```mm
> var sum = function (a,b) {
... return a + b;
... };

> var add = sum;
> typeof add;
'function'
> add(1,2)
3
```

변수의 이름 지정 규칙과 동일한 규칙이 함수의 이름 지정에도 적용된다. 함수 이름은 숫자로 시작할 수 없고 문자 ,숫자, 밑줄 문자 및 달러 기호의 조합을 포함할 수 있다.

## 익명 함수

```mm
var f = function (a) {
    return a;
};
```

함수 표현식을 변수에 지정하지 않고 사용되는 경우 `익명 함수`라고도 불린다.

- 익명 함수를 매개변수로 다른 함수에 전달할 수 있다. 수신 함수는 전달받은 함수로 유용한 작업을 할 수 있다.
- 익명 함수를 정의하고 바로 실행할 수 있다.

## 콜백 함수

함수는 변수에 할당된 다른 데이터와 마찬가지로, 정의되고 복사되어 다른 함수의 인수로 전달할 수 있다.

두 개의 함수를 매개 변수로 받아 실행하고, 각각의 합계를 반환하는 함수의 예를 보여준다.

```mm
> function invokeAdd(a,b) {
... return a() + b();
... }
```

이제 하드 코딩된 값만 반환하는 함수 선언 패턴을 사용하여 두 가지 간단한 추가 함수를 정의해 보자.

```mm
> function one() {
... return 1;
... }

> function two() {
... return 2;
... }

> invokeAdd(one,two);
3
```

그렇게 하면 다음과 같은 결과를 얻을 수 있다.

함수를 매개 변수로 전달하는 또 다른 예제는 익명 함수를 사용하는 것이다.

```mm
> invokeAdd(function () {return 1;}, function() {return 2;});
3
```

함수 A를 다른 함수 B에 전달하고 B가 A를 실행하면, A를 롤백 함수라고 말한다.

만약 A에 이름이 없으면 익명 콜백 함수라고 말할 수 있다.

콜백 함수는 언제 유용할까?

- 이름을 지정할 필요 없이 함수를 전달할 수 있다. 즉 변수가 적어진다.
- 함수를 호출하는 책임을 다른 함수에 위임할 수 있다. 즉, 작성할 코드가 적어짐을 의미한다.
- 실행 연기 또는 호출 차단 해제로 성능을 향상시킬 수 있다.

> 콜백 예제

값을 반환하고 다른 함수로 전달하는 함수가 있다. 예제에서 첫 번째 함수인 multiplyByTwo()는 세 개의 매개변수를 받아 2를 곱하는 루프를 돌은 다음, 결과가 들어있는 배열을 반환한다.

두 번째 함수 addOne()은 값을 받아 1을 더한 다음 반환한다.

```mm
> function multiplyByTwo(a,b,c) {
... var i, ar = [];
... for ( i=0; i<3; i++) {
..... ar[i] =arguments[i] * 2;
..... }
... return ar;
... }
undefined
> function addOne(a) {
... return a +1;
... }
```

다음 함수를 테스트 해보자.

```mm
> multiplyByTwo(1,2,3);
[ 2, 4, 6 ]
> addOne(100)
101
```

이제 세 개의 요소를 가진 myarr 배열이 있고, 각 요소가 두 함수에 전달되어야 한다고 가정해 보자. 먼저 multiplyByTwo()를 호출한다.

```mm
> var myarr = [];
undefined
> myarr = multiplyByTwo(10,20,30);
[ 20, 40, 60 ]
```

이제 루프를 돌아 각 요소를 addOne()에 전달한다.

```m
> for (var i = 0; i < 3; i++) {
...     myarr[i] = addOne(myarr[i]);
... }

> myarr
[ 21, 41, 61 ]
```

보다시피 잘 동작하지만 개선의 여지가 있다. 이를 개선하여 콜백 함수를 받고 모든 반복에서 콜백을 호출하도록 바꿔보자.

```mm
> function multiplyByTwo(a, b, c, callback) {
... var i, ar = [];
... for (i = 0; i < 3; i++) {
..... ar[i] = callback(arguments[i] * 2);
..... }
... return ar;
... }
```

```mm
> multiplyByTwo(1, 2, 3, function (a) {
... return a + 1;
... });
[ 3, 5, 7 ]
```

## 즉시실행 함수

익명함수의 또 다른 응용으로 함수가 정의되는 즉시 호출된다.

```mm
(
function (){
  alert('boo');
}
)();
```

단순히 괄호 안에 함수 표현식을 작성한 다음, 뒤에 또 다른 괄호를 나열하면 된다. 두 번째 괄호는 지금 실행하도록 지시하며 익명 함수가 받을 인수를 지정한다.

즉시실행 함수의 좋은 응용 예는 추가 전역 변수를 생성하지 않고 작업을 하고 싶을 때다.

단점은 물론 동일한 함수를 두 번 실행할 수 없다는 것이다. 즉 즉시실행 함수는 일회성 또는 초기화 작업에 적합하다.

## 내부(비공개) 함수

다른 값들과 마찬가지로 함수 안에서 함수를 정의할 수 있다.

```mm
function outer(param){
  function inner(theinput){
    return theinput * 2;
  }
  return 'The result is ' + inner(param);
}
```

함수 표현식을 사용하면

```mm
var outer = function (param){
  var inner = function (theinput){
    return theinput * 2;
  }
  return 'The result is ' + inner(param);
}
```

다음과 같이 작성할 수 있다.

전역 outer() 함수를 호출하면, 내부적으로 지역 inner() 함수가 호출된다. inner() 함수가 지역이어서 outer()의 밖에서 접근할 수 없기 때문에 비공개 함수라고 말할 수 있다.

```mm
outer(2);
"The result is 4"
outer(8);
"The result is 16"
inner(2);
Uncaught ReferenceError: inner is not defined
```

비공개 함수를 사용하면 다음과 같은 이점이 있다.

- 전역 네임스페이스를 깨끗하게 유지할 수 있어 이름 충돌이 발생할 가능성이 줄어든다.
- 개인 정보 보호 - 필요한 함수만 외부에 노출시키고, 사용하지 않는 나머지 함수는 보이지 않게 유지한다.

## 함수를 반환하는 함수

함수는 항상 값을 반환하고, 명시적으로 return을 기술하지 않으면 undefined를 반환한다.

함수는 하나의 값만 반환할 수 있으며, 함수 역시 반화할 수 있다.

```mm
function a() {
  alert('A!')
  return function () {
    alert('B!')
  }
}
```

위 예제에서 a() 함수는 작업을 수행(A! 출력)하고, 또 다른 작업을 수행(B! 출력)하는 다른 함수를 반환한다. 반환 값을 변수에 할당한 다음, 이 변수를 일반 함수로 사용할 수 있다.

```mm
var newFUnc = a(); // A! 출력
newFUnc();  // B! 출력
```

변환된 함수를 새 변수에 할당하지 않고 즉시실행하려면 다른 괄호 세트를 사용하면 된다.

```mm
a()();  // A! 출력 -> B! 출력
```

## 사용자 정의 함수

함수는 함수를 반환할 수 있으므로 새 함수로 이전의 함수를 대체할 수 있다. 앞의 예제를 계속 사용하여 a()함수를 호출할 때 반환된 값을 가지고 실제 a()함수를 덮어쓸 수 있다.

```mm
a = a();
```

앞의 코드는 A!를 출력하지만, 다음에 a()를 출력할 때는 B!를 출력한다. 이 기능은 함수가 일회성 작업을 수행할 때 유용하다. 이 함수는 호출될 때 불필요한 반복 작업을 피하기 위해 첫 번쨰 호출 후에 스스로를 덮어 쓴다.

함수는 외부에서 재정의 됐고, 반환된 값은 함수에 다시 할당됐다. 그러나 함수는 다음 예젱와 같이 실제로는 내부에서 스스로를 재작성할 수 있다.

```mm
function a() {
  alert('A!');
  a = function () {
    alert('B!')
  };
}
```

이 함수를 처음 호출하면 다음이 수행된다.

- A! 출력 (일회성 예비 작업으로 간주됨)
- 전역 변수 a를 재정의하고 이 변수에 새 함수를 할당함.

다음에 함수가 호출되면 B!를 출력한다.

```mm
var a = (function () {

  function someSetup() {
    var setup = 'done';
  }

  function actualWork() {
    alert('Worky-Worky');
  }

  someSetup();
  retrun actualWork;

}());
```

앞에서 설명한 몇 가지 기술을 결합한 예제이다.

- 비공개 함수 someSetup()과 acutalWork()가 있다.
- 즉시실행 함수가 있다. 함수 정의에 괄호를 사용해 자체적으로 호출하는 익명 함수다.
- 함수가 실행되면, someSetup()을 호출한 당음 함수인 acutalWork 변수에 대한 참조를 반환한다.
  이 함수를 호출한 결과가 아니라 함수 참조를 반환하기 때문에 retrun문에 괄호가 없다는 점에 유의하자.
- 전체가 var a = 로 시작하기 때문에 자기 실행 함수의 반환 값은 a에 할당된다.

## 범위 체인

자바스크립트에는 중괄호 범위가 없고 대신 함수 범위가 있다. 함수에 정의된 변수는 함수 밖에서는 볼 수 없지만, 코드 블록(ex if, for 루프)에 정의된 변수는 블록 외부에서도 볼 수 있다.

EX)

```mm
var a = 1;
function f() {
  var b = 1;
  return a
}
f()
1
b;
Uncaught ReferenceError: b is not defined
```

a 변수는 전역 공간에 있고 b는 함수 f()의 범위 내에 속해있다. 따라서

- f() 안에서는 a와 b가 모두 보인다.
- f() 밖에서는 a는 보이지만 b는 보이지 않는다.

outer() 내부에 중첩된 inner()함수를 정의하자면, 자체 범위뿐 아니라 부모의 범위에 있는 변수에 접근할 수 있다. 이는 범위 체인으로 알려져 있으며, 체인은 필요한 만큼 길어질 수 있다.

```mm
var global =1;
function outer() {
  var outer_local = 2;
	function inner() {
    var inner_local = 3;
    return inner_local + outer_local + global;
  }
  return inner();
}
```

outer() 실행시 6이 출력된다.

## 화살표 함수

자바 스크립트는 거의 모든 종류의 화살표 함수를 사용한다.

```mm
$(#submit-ntn").click(function (event) {
  validateForm();
  submitMessage();
});
```

위의 코드는 전형적인 제이쿼리 이벤트 핸들러라고 한다. 정확히 뭔지는 아직 배우지 않았지만, 이벤트 핸들러인 click()함수는 함수를 매개 변수를 받아들여 인라인 익명 함숲 현식을 만들어 click 함수에 전달한다. 이렇게 익명 함수 표현식을 작성하는 스타일을 람다 함수라고 한다. 그러나 자바스크립트의 람다 구문은 간결하지 않았다.

화살표 함수는 전통적인 함수 표현식보다 더 간결한 구문을 제공한다.

```mm
const num = [1,2,3]
const squares = num.map(function(n){
  return n*n
});
console.log(squares); // [ 1, 4, 9 ]
```

화살표 힘수 구문을 사용하면 함수를 다음 코드 행으로 단순화할 수 있다.

```mm
const squares_6 = num.map( n => n*n)
```

보다시피 어디에도 function이나 return 키워드가 없다. 함수의 인수가 하나뿐이라면 결국 함수를 identifer => expression으로 작성하게 될 것이다.

여러 개의 인수가 필요할 때는 중괄호 안에 인수 목록을 래핑한다.

- 매개변수 없음 : () => {...}
- 1개의 매개변수 : a => {...}
- 여러 개의 매개변수 : (a,b) => {...}

화살표 함수는 표현식 본문뿐만 아니라 코드 블록 본문을 모두 가질 수 있다.

```mm
n => { return n+n} // 블록문
n -> n+n // 표현식
```
