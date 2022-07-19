# Vue 에러 처리

# Cannot use JSX unless the '--jsx' flag is provided.ts(17004) 오류

jsconfig 이나 tsconfig에서 "jsx": "preserve" 구문을 빼먹어서 생기는 오류.

config 파일에 들어가서 해당 구문 한줄만 추가해주면 해결.

```conf
"jsx": "preserve" 
```