# Error: listen EADDRINUSE: address already in use :::8080

포트 사용 문제.

로컬 서버에서 사용하는 서버들은 해당포트를 이미 껐음에도 내부에서 비정상종료 되는 경우나 기타 등등 그 포트가 제대로 꺼지지 않아 발생하는 문제.

## 해결방법

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
