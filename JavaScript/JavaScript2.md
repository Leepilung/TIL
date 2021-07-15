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
