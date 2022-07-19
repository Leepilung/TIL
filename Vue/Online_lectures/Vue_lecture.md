# Vue3

# Vue CLI를 활용한 프로젝트 생성 방법

1. Default 옵션으로 생성
2. Manually select features 옵션으로 생성
3. Vue 프로젝트 매니저로 생성

# Default 옵션 활용

```
vue create {생성할 프로젝트 명}
```

입력 시 아래와 같은 선택지 등장

```
Vue CLI v5.0.8
? Please pick a preset: (Use arrow keys)
❯ Default ([Vue 3] babel, eslint)
  Default ([Vue 2] babel, eslint)
  Manually select features
```

Manually로 vue 프로젝트를 생성하면

preset으로 다음번 vue CLI로 프로젝트를 생성할 때

preset이 저장된다.

```
vue-basic 이란 이름으로 Manually 옵션으로 만든 preset

Vue CLI v5.0.8
? Please pick a preset:
❯ vue-basic ([Vue 3] babel, router, vuex, eslint)
  Default ([Vue 3] babel, eslint)
  Default ([Vue 2] babel, eslint)
  Manually select features
```

## 파일 구조

- node_modules : npm으로 설치된 패키지 파일이 모여있는 디렉토리

- public : 웹팩을 통해 관리되지 않는 정적 리소스가 모여 있는 디렉토리

- src/assets : 이미지, css, 폰트 등을 관리하는 디렉토리

- src/components : Vue 컴포넌트 파일이 모여 있는 디렉토리

- App.vue : 최상위(root) 컴포넌트

- main.jsd가장 먼저 실행되는 자바스크립트 파일, Vue 인스턴스의 생성을 담당한다.

- babel.config.js : 바벨(babel) 설정 파일

- package-lock.json : 설치된 package의 디펜던시 정보를 관리하는 파일

- package.json : 프로젝트에 필요한 package를 정의하고 관리하는 파일

# vue 프로젝트 매니저 이용하여 프로젝트 생성 방법

명령어는

```
vue ui
```

입력 시 localhost:8000 링크로 프로젝트를 선택하여 만들 수 있는 화면이 나온다.

온갖 대시보드 의존성, 플러그인, 설정, 작업목록 등을 GUI로 구동하고 자세한 파라미터들 까지 확인이 가능하다.

# Vue Router 설치 방법

vue cli등으로 생성한 프로젝트 디렉토리로 이동하여

```
vue router
```

를 입력하면 된다.
