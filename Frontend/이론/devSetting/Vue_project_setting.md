# 새 프로젝트 시작 시  개발 환경 세팅 (작성 중)

> 목표

1. 프로젝트 생성 방식의 정리
2. 프로젝트 생성 순서 및 개발 환경 세팅 순서에 맞게끔 작성
3. 특정 라이브러리 or 패키지에 대한 설치 과정 및 유의 사항, 설명등 정리 

## 0. 프로젝트 생성

간단한 CLI로 프로젝트를 생성하는 경우

> Vue.js의 경우

```js
vue create '생성할 프로젝트 이름'
```

> Nuxt.js의 경우

```js
npm init nuxt-app '생성할 프로젝트 이름'
```

## 1. EsLint 및 Prettier

프로젝트 시작 시 eslint, prettier등의 설정 필요하다.

Vscode에서 실행 시 Prettier 확장은 비활성화, ESLint의 경우에는 활성화가 필요함.

Vue의 경우 eslintrc.js에서 해당 설정 extends에 적용할 코드 컨벤션 룰셋 및 prettier 설정 추가하면 된다.

```js
// .eslintrc.js
module.exports = {
  root: true,
  env: { // 개발 환경에 대한 설정
    browser: true,
    node: true,
  },
  parserOptions: {
    parser: '@babel/eslint-parser',
    requireConfigFile: false,
  },
  extends: [ // 익스텐션 적용할 플러그인들 목록
    '@nuxtjs',
    '@vue/eslint-config-standard',
    'plugin:nuxt/recommended',
    'prettier',
  ],
  plugins: ['prettier'], // 프리티어 적용 시킬 시 플러그인에 삽입
  rules: { // ESLint 관련 설정 룰 삽입 부분
    'vue/multi-word-component-names': [  // VUE 멀티워드 관련 설정
      'error',
      {
        ignores: ['error', 'index', 'default'],
      },
    ],
    'prettier/prettier': [ // 프리티어 관련 룰 
      'error',
      {
        singleQuote: true,
        semi: false,
        useTabs: false,
        tabWidth: 2,
        trailingComma: 'all',
        printWidth: 80,
        bracketSpacing: true,
        arrowParens: 'always',
      },
    ],
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
  },
}
```

> ESLint 동작 설정 관련 User.setting 설정

eslint에서 디렉토리나 워크스페이스에 추가하는 설정 (settings.json)의 경우 

```json
{
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
}
```

vscode 자체에 존재하는 유저 설정의 setting.json에 추가하는 방법 존재

# Nuxt

## @nuxtjs/style-resources

[참조](https://junglast.com/blog/nuxt-style-resources)

별도의 import 구문 없이 전역 스타일링(변수, Mixin 등) 로직 사용하는 방법

Vue의 단일 컴포넌트 환경에서는 Sass-loader를 통해 `<style>`영역에 확장 CSS문법을 사용할 수 있어, SCSS등에서 지원하는 변수, 믹스인, 함수 등의 문법을 그대로 사용할 수 있다.

그러나 이러한 로직이 많아지면 해당 style 문구를 import하여 사용이 가능한데 이 역시도 컴포넌트의 개수가 많아지면 번거로워진다.

이를 해결하기 위한 패키지가 `@nuxtjs/style-resources` 이다.

이 때 사용하고자 하는 CSS 확장 문법에 알맞는 loader또한 미리 설치되어야 한다.

```js
npm i @nuxtjs/style-resources // 메인 설치

// 아래 것들 중 쓰는 문법에 맞게 1개 설치
npm i sass-loader sass // SASS
npm i less-loader less // LESS
npm i stylus-loader stylus // Stylus
```

해당 모듈을 설치하고, Nuxt.config.js에 아래와 같이 사용하면 된다.

```js
// Nuxt.config.js
{
  buildModules: [
    '@nuxtjs/style-resources',
  ],

  styleResources: {
   scss: [
     '@/assets/ styles/사용할 css 파일 1',
     '@/assets/styles/사용할 css 파일 2',
   ],
  }
}
```

### 작동 방식과 주의점

`@nuxtjs/style-resources`의 역할은, 빌드 과정에서 css를 번들링하기 이전에 nuxt.config.js의 styleResources에 추가했던 파일들을 각각의 .vue 파일의 `<style>` 영역에 `자동으로 import하는 것`이다. 이렇게 자동으로 import를 한 이후에는 일반적인 빌드와 동일한 과정을 거친다.

주의할 점은 모든 컴포넌트의 `<style>`영역에 `동일한 css를 모두 import`하므로, 만약 styleResources에 변수/믹스인/함수가 아닌 일반적인 스타일 규칙이 있을 경우 번들 사이즈와 HMR 성능에 문제를 일으킬 수 있다.

`@nuxtjs/style-resources`의 레포지토리에도 모듈로 사용할 css 파일에 "actual style"을 절대 사용하지 말라는 주의사항이 언급되어 있다.

> nuxt.config.js의 css 속성과의 차이점

nuxt.config.js의 css 속성은 css, scss, sass, less 파일을 프로젝트의 글로벌 영역에 추가해주는 역할을 한다.

```js
// nuxt.config.js
{
  ...
  css: ['@/styles/wrapper.scss', '@/styles/normalize.css'],
  ...
}
```

그러나 css 속성과 @nuxtjs/style-resources를 사용하는 것 간에는 명확한 차이가 있다. 

css 속성에 추가한 파일은 글로벌 영역에 추가되긴 하지만, 각각의 vue 컴포넌트에서 별도의 import를 거치지 않는 이상 css 속성에 추가한 파일의 변수, 믹스인, 함수등에 접근할 수 없다.

<img src="https://junglast.com/static/images/nuxt-style-resources/diagram.png"/>

