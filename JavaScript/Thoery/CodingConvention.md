# 코딩 컨벤션

- **indent :** 2칸 공백 사용이 디폴트
- **quotes :** 작은 따옴표가 디폴트
- **no-unused-vars :** 사용하지 않은 변수 정의 금지
- **keyword-spacing :** 예약어 뒤에 공백 추가
    - eslint: `[keyword-spacing](http://eslint.org/docs/rules/keyword-spacing)`
        
        ```jsx
        if (condition) { ... }   // ✓ Good
        if(condition) { ... }    // ✗ Avoid
        ```
        
- **eqeqeq :** 비교 시 항상 일치 연산자(===) 사용 권고
    - 예외: `null || undefined`는 `obj == null`로 확인할 수 있다.
    - eslint: `[eqeqeq](http://eslint.org/docs/rules/eqeqeq)`
        
        ```jsx
        if (name === 'John')   // ✓ Good
        if (name == 'John')    // ✗ Avoid
        ```
        
        ```jsx
        if (name !== 'John')   // ✓ Good
        if (name != 'John')    // ✗ Avoid
        ```
        
- **space-infix-ops :** 공백 사이에 연산자 넣기
    - eslint: `[space-infix-ops](http://eslint.org/docs/rules/space-infix-ops)`
        
        ```jsx
        // ✓ Good
        var x = 2
        var message = 'hello, ' + name + '!'
        ```
        
        ```jsx
        // ✗ Avoid
        var x=2
        var message = 'hello, '+name+'!'
        ```
        
- **comma-spacing :** 쉼표 뒤에 공백
- **barce-style :** else 문은 중괄호와 같은 줄에 둬야 함
    - eslint: `[brace-style](http://eslint.org/docs/rules/brace-style)`
        
        ```jsx
        // ✓ Good
        if (condition) {
          // ...
        } else {
          // ...
        }
        ```
        
        ```jsx
        // ✗ Avoid
        if (condition) {
          // ...
        }
        else {
          // ...
        }
        ```
        
- **culry :** 여러줄의 if 문 사용 시 중괄호 사용
- **err :** 함수 파라미터로 err가 있을 경우 항상 처리 해야함
- **no-multiple-empty-lines :** 여러 줄의 공백을 허용하지 않음
- **operator-linebreak :** 여러 줄의 삼항 연산자를 사용할 경우 ?와 :를 각각의 행으로 처리해야 함
- **one-var :** var선언을 각각의 변수 1개마다 별도로 선언해야 함
- **block-spacing :** 한 줄에 중괄호로 처리할 경우 공백을 추가함
    - eslint: `[block-spacing](http://eslint.org/docs/rules/block-spacing)`
        
        ```jsx
          function foo () {return true}    // ✗ Avoid
          function foo () { return true }  // ✓ Good
        ```
        
- **camelcase :** 변수나 함수 이름 정의 시 카멜케이스(camelcase)를 사용해야 함
- **comma-dangle :** 맨 뒤쪽의 쉼표를 허용하지 않음
    - eslint: `[comma-dangle](http://eslint.org/docs/rules/comma-dangle)`
        
        ```jsx
          var obj = {
            message: 'hello',   // ✗ Avoid
          }
        ```
        
- **comma-style :** 쉼표를 사용할 경우 현재 행 끝에 사용해야 함
    - eslint: `[comma-style](http://eslint.org/docs/rules/comma-style)`
        
        ```jsx
          var obj = {
            foo: 'foo'
            ,bar: 'bar'   // ✗ Avoid
          }
        
          var obj = {
            foo: 'foo',
            bar: 'bar'   // ✓ Good
          }
        ```
        
- **dot-location :** 점(Dot)은 각 속성과 같은 줄에 있어야 한다.
    - eslint: `[dot-location](http://eslint.org/docs/rules/dot-location)`
        
        ```jsx
          console.
            log('hello')  // ✗ Avoid
        
          console
            .log('hello') // ✓ Good
        ```
        
- **func-call-sapcing :** 함수 식별자와 호출 사이에 공백이 없어야 함
    
    ```jsx
    console.log ('hello') // ✗ Avoid
    console.log('hello')  // ✓ Good
    ```
    
- **key-spacing :** key-콜론과 키 값 쌍의 값 사이에 공백을 추가해야 함
    
    ```jsx
    var obj = { 'key' : 'value' }    // ✗ Avoid
    var obj = { 'key' :'value' }     // ✗ Avoid
    var obj = { 'key':'value' }      // ✗ Avoid
    var obj = { 'key': 'value' }     // ✓ Good
    ```
    
- **no-cond-assign :** 조건부 할당을 추가적으로 괄호로 묶는다.
    - 이것은 표현식이 등호 (`===`)에 대한 오타보다는 의도적으로 할당 (`=`)이라는 것을 분명히해야 한다.
    - 식이 하나일 때보다 2개일 경우 매우 직관적으로 바뀜
    - eslint: `[no-cond-assign](http://eslint.org/docs/rules/no-cond-assign)`
        
        ```
        // ✓ Good
        while ((m = text.match(expr))) {
          // ...
        }
        
        // ✗ Avoid
        while (m = text.match(expr)) {
          // ...
        }
        ```
        
- **no-class-assign :** 클래스로 선언된 변수의 수정 금지
- **no-const-assign :** const를 사용해 선언되 변수 수정 금지
- **no-constant-condition :** 조건문(반복문 제외)에서 상수 표현식 사용 금지
    
    ```jsx
    if (false) {    // ✗ Avoid
      // ...
    }
    
    if (x === 0) {  // ✓ Good
      // ...
    }
    
    while (true) {  // ✓ Good
      // ...
    }
    ```
    
- **no-delete-var :** 변수에 delete 연산자 사용 금지
    
    ```jsx
    var name
    delete name     // ✗ Avoid
    ```
    
- **no-dupe-args :** 함수 정의 시 중복된 파라미터 사용 금지
- **no-dupe-class-members :** 클래스 멤버에 중복된 이름 사용 금지
- **no-dupe-keys :** 객체 리터럴에 중복된 키 값 사용 금지
- **no-duplicate-case :** switch문에서 중복된 case 라벨 사용 금지
- **no-duplicate-imports :** 모듈 당 하나의 import 문 사용하기
- **no-empty-character-class :** 정규식에서 빈 문자 클래스가 없어야 함
- **no-empty-pattern :** 비어있는 구조의 패턴이 없어야 함
- **no-eval :** eval()을 사용하지 않습니다.
- no-path-content
    - __dirname과 filename을 사용할 때 문자열 연결을 피한다.
    
    ```jsx
    const pathToFile = __dirname + '/app.js'            // ✗ Avoid
    const pathToFile = path.join(__dirname, 'app.js')   // ✓ Good
    ```
    
- no-throw-literal : throw는 반드시 Error 객체 이어야 한다.
    
    ```jsx
    throw 'error'               // ✗ Avoid
    throw new Error('error')    // ✓ Good
    ```
    
- no-trailing-sapces : 줄 끝에서 공백을 사용할 수 없습니다.
- no-undef-init : ‘undefined’로 초기화하는 것은 허용되지 않습니다.
    
    ```jsx
    let name = undefined    // ✗ Avoid
    
    let name
    name = 'value'          // ✓ Good
    ```
    
- no-unneeded-ternary : 더 간단한 대안이 있을 경우 삼항 연산자를 사용하지 않음
    
    ```jsx
    let score = val ? val : 0     // ✗ Avoid
    let score = val || 0          // ✓ Good
    ```
    

---

# 의논이 필요한 부분

- no-undef
    - **불편하고 불필요하다고 생각**
    - 항상 브라우저 전역 접두어에는 `window`를 붙여야 한다.
    - 예외의 경우: `document`, `console`, `navigator`.
        
        eslint: `[no-undef](http://eslint.org/docs/rules/no-undef)`
        
        ```
        window.alert('hi')   // ✓ Good
        ```
        
- no-array-constructor
    - 그러나 리스트의 길이를 사전 설정해야 하는 경우 무조건 생성자를 사용 해야 하므로 해당 옵션은 불필요하다고 생각함
    - 배열 생성자 대신 배열 리터럴을 사용해야 하는 설정
    - 스킵
    - eslint: `[no-array-constructor](http://eslint.org/docs/rules/no-array-constructor)`
        
        ```jsx
        var nums = new Array(1, 2, 3)   // ✗ Avoid
        var nums = [1, 2, 3]            // ✓ Good
        ```
        
- no-return-assign
    - return의 결과문을 감싸는 형태인데 호불호가 많이 갈릴듯한 설정
    - 반환 내용(return)에 대한 대입 값을 괄호로 묶어야 함
    - eslint: `[no-return-assign](http://eslint.org/docs/rules/no-return-assign)`
    
    ```jsx
    function sum (a, b) {
      return result = a + b     // ✗ Avoid
    }
    
    function sum (a, b) {
      return (result = a + b)   // ✓ Good
    }
    ```
    
- no-this-before-super
    - this를 사용하기 전에 super()를 호출해야 하는 구문
    - class에서 한정되는 것 같음..?
    - eslint: `[no-this-before-super](http://eslint.org/docs/rules/no-this-before-super)`
    
    ```jsx
    class Dog extends Animal {
      constructor () {
        this.legs = 4     // ✗ Avoid
        super()
      }
    }
    ```