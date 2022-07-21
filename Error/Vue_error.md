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