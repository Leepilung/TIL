module.exports = {
  root: true,
  // env : 프로젝트 사용 환결 설정으로 browser, es2021이 대표적
  env: {
    node: true,
  },
  // extends : 정의되어 있는 ESLINT 설정을 가져와 적용.
  extends: [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
    'prettier',
    'plugin:prettier/recommended',
  ],
  parserOptions: {
    parser: '@babel/eslint-parser',
  },
  // ESLint는 써드파티를 지원하여 prettier등을 추가하여 사용이 가능하다.
  plugins: ['prettier'],
  // 프로젝트에서 사용하는 세부 규칙 적용 구문
  rules: {
    indent: ['error', 2],
    'prettier/prettier': [
      'error',
      {
        singleQuote: true, // 따옴표
        semi: true, // 세미콜론
        trailingComma: 'all', // 후행 쉼표 추가 구문
        printWidth: 80, // 줄바꿈 길이 설정
        arrowParens: 'avoid', // 화살표 함수 괄호 사용 방식
        bracketSpacing: true, // 객체 리터럴의 괄호 사이 공백 출력
        htmlWhitespaceSensitivity: 'css',
      },
    ],
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
  },
};
