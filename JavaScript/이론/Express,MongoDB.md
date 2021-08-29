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

## MongoDB Read 파트

MongoDB에서 Read부분에 해당하는 파트이다. 대표적인 조회 메소드로 find가 있다.

## MongoDB Update 파트

CURD에서 U를 담당하는 Update 메소드들 중에서 가장 유명한 메소드는 Update가 있다.

### Update
단적인 예로 monster라는 db에 Slime이라는 자료형의 hp 값을 바꿔보려고 한다.

```js
db.monsters.update({ name: 'Slime' }, { $set: { hp: 30 } });
```
그럼 다음과 같이 $set을 써줘야만 원하는 필드값만을 변경한다. 만약 $set을 넣지 않고 그냥 { hp : 30 } 이라는 값만 넣으면 'Slime'이라는 name의 다큐먼트가 다 지워지고 { hp : 30 } 이라는 객체만 남게 된다.

그 다음엔 hp라는 필드 값을 내려보고자 한다. 그럴땐 다음과 같은 구문을 사용하면 된다.

```js
db.monsters.update({ name: 'Slime' }, { $inc: { hp: -5 } });
```

$inc를 사용하면 그 필드값의 숫자를 올리거나 내릴 수 있다. 음수를 넣으면 내리고 양수를 넣으면 올린다. 

### UpdateOne

몽고DB의 일정 버전부터 update를 대체하는 메소드이다. 위에 서술한 양식과 기능은 전부 동일하나 차이점이라면 updateOne은 매칭되는 다큐먼트 중 첫 번째 다큐먼트만을 수정하고, UpdateMany는 매칭되는 모든 다큐먼트를 수정한다.


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

# Node.js + Express 개념

Node.js와 express를 사용하면 가장 기본적이고 많이 사용되는 객체중 하나이다.

## req 객체

- `req.body` : POST 정보를 가진다. 파싱을 위해서 body-parser와 같은 패키지가 필요하다. 요청 정보가 url에 들어있는 것이 아니라 Request(req)의 본문에 들어있기 때문이다.

- `req.query` : GET 정보를 가집니다. 즉, url로 전송된 쿼리 스트링 파라미터를 담고 있다.

- `req.params` : 내가 이름 붙인 라우트 파라미터 정보를 가진다.

- `req.headers` : HTTP의 Header 정보를 가진다.

이 외에도 req.route, req.cookies, req.acceptedLanguages, req.url, req.protocol, req.host, req.ip 등이 존재한다.

## res 객체

- `res.send` : 다양한 유형의 응답을 전송한다.

- `res.redirect` : 브라우저를 리다이렉트 한다.

  - `리다이렉트` : 한 페이지에 접속시 자동으로 다른 페이지로 넘어가는 것

- `res.render` : 설정된 템플릿 엔진을 사용해서 views 폴더를 렌더링한다.

- `res.json` : JSON 응답을 전송한다.

- `res.end` : 응답 프로세스를 종료한다.

## res.send / res.json / res.end 비교

### res.send

`res.send([body])`의 body에는 Buffer, String, Object, Array가 올 수 있다.

그리고 response Header에는 Body의 Content-Type이 자동으로 정의된다고 한다.

```js
res.send({ name: "SSibal" });
```

key에는 name, value에는 'SSibal'이라는 object를 body에 넣어서 response 응답을 전달하면 response Header 내 Content-Type은 자동으로 json(JavaScript Object Notation)으로 정의된다고 한다.

참고로 이 response Header는 response 객체 내 set메소드로 제어가 가능하다고 한다. 간단한 예로 res.set('Content-Type', 'text/html'); 같은 형태를 들 수 있다.

### res.json

res.json은 JSON을 응답으로 보낸다.

그러나 res.send도 Object를 응답으로 보낼 수 있으니까 res.json이 굳이 필요할까 라는 의문이 들 수 있는데, res.json은 JSON 정보를 전달하는데 더 특화된 기능을 가지고 있다.

더 자세히 이해하기 위해선 Object와 JSON은 비슷하게 생기긴 했지만 확연한 차이점을 가지고 있다는걸 짚고 넘어가야 한다.

JSON은 String, Number, Object, Array, Boolean, Null을 지원하지만, Function, Date, Undefined 등과 같은 타입은 지원하지 않는다.

그렇기 때문에 우리가 { x: [10, undefined, function(){}, Symbol('')] } 같은 파라미터를 입력하면 undefined, function(){}, Symbol(") 는 JSON이 지원하지 않는 타입이기에 JSON이 지원하는 타입으로 바꾸는 작업이 요구된다.

이를 해결하기 위한 방법이 JSON.stringfy() 메소드이다.

res.json을 사용하면 JSON.stringfy() 메소드를 호출하여 파라미터를 JSON string 형태로 먼저 변환 한 뒤, res.send()를 호출하여 응답을 내보낸다.

JSON.stringfy() 메소드는 replacer와 spaces라는 두 가지 파라미터를 가질 수 있는데 이를 Express에서는 아래와 같은 옵션을 통해 제어 가능하다.

### res.end

res.end는 위에서 언급한 것 처럼 응답 프로세스를 종료하는 데 사용된다.

하지만 응답 데이터를 res.json이나 res.send 같은 형태로 전송하는 경우에는 이들이 일부 데이터를 보낸 뒤에 자동으로 응답 종료처리를 하기 때문에 굳이 res.end()를 호출 할 필요가 없다.

## Request Properties

### req.params

예로 /user/:name등의 경로가 있으면 "name"속성을 req.params.name으로 사용할 수 있다.

https://params/user/12341234 일 경우 12341234를 받는다.

### req.body

JSON 등의 데이터를 담을때 사용한다. (주로 POST로 유저의 정보 또는 파일 업로드를 보냈을 때가 해당됨 )

요청 본문에 제출 된 키-값 데이터 쌍을 포함한다. 기본적으로 이는 정의되어 있지 않으며 express.json(), express.urlencoded()와 같은 미들웨어를 사용해야한다.

쉽게 말하자면 req.body는 body-parser를 사용하기 전에는 default 값으로 Undefined 설정되기 때문에 body-parser를 사용하여 해결해야 오류를 뿜지 않는다.

Express 4.16.0버전 부터 body-parser의 일부 기능이 익스프레스에 내장되어 있어서

```js
app.use(express.json());
app.use(express.urlencoded({ extends: true }));
```

다음과 같은 구문을 사용하면 된다.

# Express () 함수

- express.json() : 들어오는 request를 JSON 데이터로 파싱하며, body-parser를 기반으로 한다.

- express.static() : 정적 파일을 제공하며, serve-static를 기반으로 한다.

- express.Router() : 새 router 객체를 생성한ㄷ다.

- express.urlencoded() : 들어오는 request를 urlencoded 데이터로 파싱하며, body-parser를 기반으로 한다.
