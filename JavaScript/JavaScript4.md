# JavaScript 4

## 내장 객체

앞에서 Object() 생성자 함수를 살펴봤다. 객체 리터럴 표기법을 사용해 객체를 생성하고 해당 constructor 속성에 접근할 때 반환된다. Object()는 내장된 생성자 중 하나다.

내장 객체는 세 그룹으로 나눌 수 있다.

- 데이터 랩퍼 객체 : Object, Array, Function, Boolean, Number, String등이 있다. 이들 객체는 자바스크립트에서 각각의 데이터 유형에 해당된다. Undefined와 null을 제외하고는 typeof 값에 대한 데이터 래퍼 객체가 있다.

- 유틸리티객체 : Math, Date, RegExp등이 있으며 편리하게 사용할 수 있다.

- 오류 객체 : 일반적인 Error 객체뿐만 아니라 예기치 않은 상황이 발생할 때 프로그램이 동작 상태를 복구하는데 도움디 되는 여러 특정 객체가 포함된다.
