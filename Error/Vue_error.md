# Vue 에러 처리

# Cannot use JSX unless the '--jsx' flag is provided.ts(17004) 오류

jsconfig 이나 tsconfig에서 "jsx": "preserve" 구문을 빼먹어서 생기는 오류.

config 파일에 들어가서 해당 구문 한줄만 추가해주면 해결.

```conf
"jsx": "preserve" 
```

# sh: vue-cli-service: command not found

vue cli로 생성한 프로젝트를 npm run serve로 실행 시 발생하는 에러

```
npm ci
npm run serve
```
위 순서대로 진행하여 ci를 새로 설치하고 다시 시작하면 해결.

# Syntax Error: TypeError: this.getOptions is not a function

위와 같은 에러는 vue 2.6 버젼대에서 sass-loader 를 11 버젼을 사용할 경우에 호환되지않아 발생한다.

따라서 sass-loader 를 아래와 같이 10 버젼을 설치하면 해결된다.

기존 sass-loader 를 삭제하고 10 버젼을 설치하는 명령어는 아래와 같다.

```js
// 기존 모듈 삭제
npm uninstall sass-loader

// 10번대 버젼 설치
npm install --save sass-loader@10
```