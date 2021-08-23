# Express와 MongoDB 활용한 DB구축 관련 내용 정리 MD 문서

## MongoDB

라이브러리 설치 명령어로 우선 설치 필요함.

```js
npm i mongodb
```

그 다음 nodemon 등으로 server.js나 index.js 같은 구동파일 실행시 mongodb를 킬거라면

터미널 입력창에서

```js
mongod;
```

입력해서 켜주는것 잊지말기.

## MongoDB 연결

> MongoDB 설치

WSL (Ubuntu 20.04)에 MongoDB (버전 5.0)를 설치 하려면 다음을 수행 합니다.

1. WSL 터미널을 엽니다 (ie. Ubuntu)로 이동 하 고 루트 디렉터리로 이동 합니다. cd ~
2. Ubuntu 패키지를 업데이트합니다. sudo apt update
3. MongoDB 패키지 관리 시스템에서 사용 하는 공개 키를 가져옵니다. wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
4. MongoDB에 대 한 목록 파일을 만듭니다. echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
5. 로컬 패키지 데이터베이스 다시 로드: sudo apt-get update
6. MongoDB 패키지를 설치 합니다. sudo apt-get install -y mongodb-org
7. 설치를 확인하고 버전 번호(mongod --version)를 가져옵니다.
8. 홈 디렉터리로 이동 합니다. cd / && cd home
9. 데이터를 저장할 디렉터리를 만듭니다. mkdir -p data/db

<가장 중요한 부분>

10. `Mongo 인스턴스를 실행 합니다. sudo mongod --dbpath ~/data/db`

11. `MongoDB 인스턴스가 실행 되 고 있는지 확인 합니다. ps -e | grep 'mongod'`

12. `MongoDB 셸을 종료 하려면 바로 가기 키 (Ctrl + C)를 사용 합니다.`

포트사용 오류 발생시 -> 삭제하기.

## node.js 경로 확인 방법

node.js에서는 \_filename으로 현재 파일의 정보, \_\_dirname으로 현재 디렉터리의 정보를 확인할 수 있다.

> `__filename` => 현재 파일 경로 확장자

```js
console.log(__filename);
// /home/ek3434/Project/express-test/src/index.js
```

> `__dirname` => 현재 디렉토리(폴더) 경로 확장자

```js
console.log(__dirname);
// /home/ek3434/Project/express-test/src
```

## Express 정적 파일 적용

이미지, CSS 파일 및 JavaScript 파일과 같은 정적 파일을 제공하려면 Express의 기본 제공 미들웨어 함수인 express.static을 사용해야 한다.

정적 자료들이 포함된 디렉토리의 이름을 express.static 미들웨어 함수에 전달하면 파일의 직접적인 제공이 가능하다. 예를 들면, 다음과 같은 코드를 이용하여 public이라는 이름의 디렉토리에 포함된 이미지, CSS 파일 및 JavaScript 파일을 제공할 수 있다.

```js
app.use(express.static("public"));
```

또한 여러 개의 정적 자산 디렉토리를 이용하려면 다음과 같이 express.static 미들웨어 함수를 여러 번 호출해야 한다.

```js
app.use(express.static("public"));
app.use(express.static("files"));
```

그리고 Express는 express.static 미들웨어 함수를 이용해 정적 디렉토리를 설정한 순서대로 파일을 검색한다.

또한 express.static 함수를 통해 제공되는 파일에 대한 가상 경로 URL(파일 시스템 내에 해당 경로가 실제로 존재하지 않는 경우)을작성하려면 다음과 같이 작성하면 된다.

```js
app.use("/static", express.static("public"));
```

이러면 이제 다음과 같은 경로를 통해 public 디렉토리에 포함된 파일을 로드시킬 수 있다.

```
http://localhost:3000/static/css/style.css
```

그러나 express.static 함수에 제공되는 경로는 node 프로세스가 실행되는 디렉토리에 대해 상대적이기 때문에 Express 앱을 다른 디렉토리에서 실행하는 경우에는 다음과 같이 제공하기 원하는 디렉토리의 절대 경로를 사용하는 것이 더 안전하다.

```js
app.use("/static", express.static(__dirname + "/public"));
```

## 서버 구현 부분

## DB와 연결하는 부분.

기본적으로 express를 활용하여 서버를 띄우는 기본문법은 다음과 같다.

# MongoDB CRUD 파트

## MongoDB Create 파트

## MongoDB Update 파트

## MongoDB Delete Method

---

# 에러부분

## Express Style.css 적용 관련 에러

```js
app.use(express.static(__dirname + "/static"));
```

해당 구문을 사용하지 않으면 백날 문법적 오류가 없어도 css파일을 분리시켜도 html에서 로드를 못해서 적용되질 않음.

> EJS 파일에서의 CSS.style 적용 에러

보통 다른 파일에서 css.style같은 파일을 참조하려면

```js
<link type="text/css" rel="stylesheet" href="style.css" />
```

같은 태그를 사용하는데 같은폴더안에 있어도 경로지정을 다르게 해야 해결되는 문제점이 생길 수도 있다.

---

# 모듈

## path 모듈

Node.js가 기본으로 제공하는 path 모듈은 파일/폴더/디렉토리 등의 경로를 편리하게 설정할 수 있는 기능을 제공한다.

path모듈의 대표적 메소드는 join(), resolve()등이 있다.

### path 모듈 사용방법

path는 node의 내장 모듈이므로 별도 설치 없이, 바로 추출하여 사용할 수 있다.

> 모듈 추출 방법

```js
const path = require("path");
```

### 주요 메소드

> path.join('경로','경로',...)

- 여러개의 경로를 알아서 합쳐준다.

- 상위경로(..), 현재경로(.)등도 알아서 처리해준다.

- 중간에 `/`를 만나면 앞의 경로에 이어서 '상대경로'로 처리해준다.

```js
console.log("join : ", path.join(__dirname, "/a/b", "..", "./b", "c", "/d"));

// join 경로 :  /home/ek3434/Project/express-test/src/a/b/c/d
```

> path.resolve('경로','경로',...)

- join과 마찬가지로 여러개의 경로를 자동으로 합쳐준다.

- join과 마찬가지로 동시에 상위경로(..), 현재경로(.)등도 똑같이 알아서 처리해준다.

- Join()과의 차이점 : 중간에 `/`를 만나면 앞에 경로 다 무시하고, 맨 처음부터 다시 시작한다.

```js
console.log(
  "resolve : ",
  path.resolve(__dirname, "/a/b", "..", "./b", "c", "/d"),
);

// resolve 경로 :  /d
```
