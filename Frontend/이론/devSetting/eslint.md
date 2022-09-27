# ESLINT(린트) 및 프리티어 설정 (작성 중)


> 목표

1. ESLint 및 Prettier에 대한 개념 정리
2. 설정 방법
3. 룰에 대한 정리

기본적으로 Vscode 기준으로 내용 서술됨

Vscode 확장 프로그램 기준으로 Prettier는 비활성화 해야함.

ESLint의 경우에는 설치 및 활성화 해야함.

WorkSapce Setting.json이나 User Setting.json에서 아래와 같이 프리티어 및 ESLint 설정 적용해줘야 함.

```json
  "editor.formatOnSave": false,
  "editor.codeActionsOnSave": {
      "source.fixAll.eslint": true
  },
  "eslint.alwaysShowStatus": true,
  "eslint.workingDirectories": [
      {"mode": "auto"}
  ],
  "eslint.validate": [
      "javascript",
      "typescript"
  ]
```