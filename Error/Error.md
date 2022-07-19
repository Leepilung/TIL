# Error: listen EADDRINUSE: address already in use :::8080(포트번호))

포트 사용 문제.

로컬 서버에서 사용하는 서버들은 해당포트를 이미 껐음에도 내부에서 비정상종료 되는 경우나 기타 등등 그 포트가 제대로 꺼지지 않아 발생하는 문제.

> 해결방법

Unbuntu나 터미널창에

```
sudo lsof -i :포트넘버
```

를 사용하여 특정 포느넘버를 입력할 경우

다음과 같이 해당 포트넘버를 차지하고있는 노드가 출력되고
ex)

```
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
node    28326 ek3434   19u  IPv6 741046      0t0  TCP *:http-alt (LISTEN)
```

해당 노드의 PID를 기반으로 노드를 kill명령어로 죽이면 된다.

```
kill -9 28326
```

여기서 -9는 kill명령어의 수행동작중 하나라나 뭐라나..

# Refused to apply style MIME type 에러 이슈

express와 nodejs로 간단한 개인프로젝트 개발 중, html 문서에서 css파일을 분리하던 중 지속적으로 에러 발생. 문제는 크롬에서는 별도로 콘솔창에 표기되는 바가 없었음. 그래서 문법적 오류가 없었음에도 css파일이 적용되지 않아 해결을 못하던 중 파이어폭스로 출력해보았고

파이어폭스 디벨롭 에디션에서 해당 에러가 발생하였음.

원인은 express내에서 static 설정을 추가로 안해줬기 때문에 발생한 에러였음. express 구동시 static 설정을 추가적으로 해주어야 정상적으로 css 및 asset들에 대한 import가 가능함.
x
실제로 TODOLIST2 프로젝트에서 해당 구문을 추가하니 정상적으로 로컬네트워크에서 불러옴을 확인할 수 있었음.

> 해결방법

```js
app.use(express.static(__dirname + "/static"));
```

의 형태로 추가해줘야함.

별것도 아닌 문제였는데 오류 해결을 위해 구글링을 시도 했을 때의 키워드가 잘못됐음을 깨닳음.

> 복기해야할 부분

에러나 오류사항을 해결하고자 구글링할 때에는 하나의 키워드에 매몰되서 시간낭비하지말고 시간을 나눠서 키워드를 검색하는 방향으로 사고하자.

# Node.js Cannot find module 에러

단순히 경로지정이 잘못됐을 경우 나타나는 에러.

> 해결방법

package.json 파일에서 main 경로가 제대로 기입되있는지, script부분 경로가 제대로 되있는지 확인하면 된다.

# Cannot find module

아주 간단한 에러. 모듈 경로가 잘못 지정되면 출력됨. 어차피 ./ ../와 같이 입력하면 자동으로 현재 파일 위치를 기준으로 알아서 선택가능함


# NPM -global 경로 설정

NPM으로 패키지 설정 시 경로가 잘못되어 있는 경우가 있는데

기본적으로 cli를 통해 global 패키지들의 설치 위치를 변경할 수 있다.

```
npm config set prefix {변경하려는 경로}
```

그리고 전역으로 명령어를 인식시키기 위해서 .zshrc를 수정해야 한다.

~/.zshrc에 

```
export PATH=$PATH:~/.npm-global/bin
```
등으로 수정 구문 삽입하면 해결.