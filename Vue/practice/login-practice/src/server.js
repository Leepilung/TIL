// /server.js
const express = require('express');
const jwt = require('jsonwebtoken');
const cors = require('cors');
const bodyParser = require('body-parser');
const fs = require('fs');
const events = require('./db/events.json');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// 단순 get 요청
app.get('/', (req, res) => {
  res.json({
    message: 'Welcome to the API.',
  });
});

// 대쉬보드 get 요청
app.get('/dashboard', (req, res) => {
  res.json({
    events: events,
  });
});

// 회원가입
app.post('/register', (req, res) => {
  if (req.body) {
    const user = {
      name: req.body.name,
      email: req.body.email,
      password: req.body.password,
      // 패스워드 암호화는 일단 추후에 진행하기
    };

    const data = JSON.stringify(user, null, 2);
    var dbUserEmail = require('./db/user.json').email;

    if (dbUserEmail === req.body.email) {
      res.sendStatus(400);
    } else {
      fs.writeFile('./db/user.json', data, err => {
        if (err) {
          console.log(err + data);
        } else {
          const token = jwt.sign({ user }, 'the_secret_key');
          // 시크릿 키 환경변수로 뺴기 -> 나중에
          res.json({
            token,
            email: user.email,
            name: user.name,
          });
        }
      });
    }
  } else {
    res.sendStatus(400);
  }
});

app.post('/login', (req, res) => {
  const userDB = fs.readFileSync('./db/user.json');
  const userInfo = JSON.parse(userDB);
  if (
    req.body &&
    req.body.email === userInfo.email &&
    req.body.password === userInfo.password
  ) {
    const token = jwt.sign({ userInfo }, 'the_secret_key');
    // 시크릿 키 환경변수로 뺴기 -> 나중에
    res.json({
      token,
      email: userInfo.email,
      name: userInfo.name,
    });
  } else {
    res.sendStatus(400);
  }
});

// 토큰 검증 미들웨어
function verifyToken(req, res, next) {
  const bearerHeader = req.headers['authorization'];

  if (typeof bearerHeader !== 'undefined') {
    const bearer = bearerHeader.split(' ');
    const bearerToken = bearer[1];
    req.token = bearerToken;
    next();
  } else {
    res.sendStatus(401);
  }
}

// 린트 에러로 인한 임시 구문
console.log(verifyToken);

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
