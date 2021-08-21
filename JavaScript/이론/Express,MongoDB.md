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

## 서버 구현 부분

테스트용 구문이라 TODOLIST2에선 삭제하고 별도로 정리한 내용.

```js
app.post("/add", (req, res) => {
    console.log(req.body.todo);
    // -> input창 (name=todo) 에 기록한 정보가 터미널에 출력됨.
    console.log(req.body.date);
    // -> input창 (name = date)에 기록한 정보가 터미널에 출력됨.
    console.log(req.body);
    // input창이 포함되있는 form의 정보가 객체 형태로  터미널에 출력됨.
```

---

## DB와 연결하는 부분.

기본적으로 express를 활용하여 서버를 띄우는 기본문법은 다음과 같다.

```js
// express를 활용한 서버 활성 기본 문법
const express = require("express");
const app = express();
let db;
app.use(express.urlencoded({ extended: true }));
```

MongoDB와 연결하는 문법

```js
// MongoDB와 연결하는 부분
const MongoClient = require("mongodb").MongoClient;
const URL = "mongodb://localhost:27017";
```

27017은 MongoDB 기본 할당 url이라고한다. 별도로 지정도 가능함. Test기능으로 연결됐는지도 확인 가능.

그리고 다음과 같은 구문으로 MongoDB와 연결을 성공했을 때 연결시키는 url을 출력시키는 구문

```js
// MongoClient를 따로 선언해줘야함. (위에서 했음)
MongoClient.connect(URL, (err, client) => {
  if (err) return console.log(err);

  db = client.db("TODOLIST"); //TODOLIST라는 데이터베이스에 연결한다는 의미.

  app.listen(3333, () => {
    console.log("listening on http://localhost:" + 3333);
  });   // 3333은 포트번호를 의미.
```

# MongoDB CRUD 파트

## MongoDB Create 파트

DB의 인스턴스 생성자체는 위에서 따로 언급했고 MongoDB와 Express를 활용한 local DB 관리는 Robo 3T라는 GUI를 사용하고 있다. robo3T 자체의 사용법은 대충 숙지했으므로 별도로 정리하지 않음.

Robo 3T를 활용하면 별도로 컬렉션이나 local DB, document를 생성할 수 있고 (가시적으로 구분이 잘 되어있음)

Javascript를 활용해서 local DB의 컬렉션과 연결하여 데이터를 입력할 수 있음.

기본적으로 TODOLIST2를 기준으로 POST라는 컬렉션과 연결하려면 다음과 같은 구문을 사용해야함.

```js
db.collection("POST"); // POST라는 이름의 컬렉션
```

그 후에 post 메소드를 사용하면 db에 데이터를 저장할 수 있다.

```js
// 등록버튼으로 /add 이동시 input창 데이터 서버 저장되게 하기
// /add 버튼은 html에서 form action="/add" 처럼 부여하면된다.
app.post("/add", (req, res) => {
    res.send("전송 완료");
    db.collection("counter").findOne(   //"counter" 컬렉션에서 하나를찾는 메소드
      { name: "numberofPost" }, // "numberofPost"라는 이름을 가진 값을 찾으라는 뜻.
      (err, result) => {    // result는 name의 값이 numberofPost를 가지는 객체 출력됨.
        console.log(result.totalPost);  // 그 객체의 totalPost 값 출력.
        let total_number_of_Post = result.totalPost;  //  해당 값 변수에 지정
```

그 다음에는 POST컬렉션에 값을 입력하는 부분이다.

```js
        //글 발행하는 부분
        db.collection("POST").insertOne(
          {
            할일: req.body.todo,
            날짜: req.body.date,
            _id: total_number_of_Post + 1,
          },
          (err, result) => {
            console.log("저장완료");
            //count라는 콜렉션에 있는 totalPost의 값 수정하는 부분
            db.collection("counter").updateOne( // 업데이트 메소드. 매개변수 3개 가짐.
              { name: "numberofPost" }, // numberofPost라는 네임을 가진 값 찾고
              { $inc: { totalPost: 1 } },   // totalPost라는 값을 1 증가시킨다($inc)
              (err, result) => {    // 에러 발생시 에러 출력하는 부분
                if (err) {
                  return console.log(err);
```

## MongoDB Update 파트

DB 데이터 수정을 원한다면 updateOne()을 사용한다.

> 구문

```js
db.collection('db컬렉션이름').updateOne( {바꾸고싶은 자료명} , {operator($set or $inc등)} , function(에러, 결과){
    console.log('쏼라쏼라')
})
```

updateOne 함수는 세개의 파라미터를 요구한다.

맨 처음엔 `{name:"numberofPost"}`와 같이 자료를 찾을 수 있는 이름이나 쿼리문등을 적어준다.

그 다음부분은 여러 종류가 있는데 totalPost라는 값을

{ $set : { totalPost : 100 } } 이렇게 넣어서 값을 아예 100으로 변경할 수도 있고

{ $inc : { totalPost : 5 } } 이렇게 넣어서 기존 값에 5만큼 더해줄 수도 있다.

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

## MongoDB Delete Method

Router 활용한 delete메소드를 활용하는 방법도 있는거 같은데 리액트를 활용한 부분이라 공부가 필요한 것 같다.

MongoDB 기본적인 메소드를 활용한 get , Post만 이용하면 코듣가 굉장히 길어지고 복잡해진다고 한다.

일단은 그래서 JQuery를 활용하여 구현했다.

EJS 파일안에 별도로 script안에 구현한다.

```html
/* TODOLIST2 에서 list.ejs파일에 다음과 같이 구현한다. /* J쿼리는 사용할 때
다음과 같은 구문을 추가해줘야 한다.
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
// delete 메소드 구현파트
<script>
  $(".delete_button").click((e) => {
    const post_number = e.target.dataset.id;
    $.ajax({
      method: "DELETE",
      url: "/delete",
      data: { _id: post_number },
    })
      //성공시 페이지 새로고침 + 콘솔창에 '성공'출력.
      .done(function (result) {
        console.log("성공");
        location.reload();
      })
      .fail((xhr, textStatus, errorThrown) => {
        console.log(xhr, textStatus, errorThrown);
      });
  });
</script>
```

그 다음 server.js에

```js
// 삭제 리액트 라우터 공부필요함. 우선 j쿼리로 구현.
app.delete("/delete", (req, res) => {
  console.log("req.body", req.body);
  req.body._id = parseInt(req.body._id);
  db.collection("POST").deleteOne(req.body, (err, result) => {
    console.log("삭제완료");
    res.status(200).send({ message: "성공했습니다." });
  });
});
```

처럼 구현하면 기존에 list.ejs에 구현해놓은 delete를 불러다가 사용한다.
