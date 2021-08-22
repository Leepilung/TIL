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
