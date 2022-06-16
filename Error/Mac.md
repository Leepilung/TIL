# Homebrew -> brew install CL 입력시 No similarly named formulae found 에러

해당 에러 해결법은 간단함.

우선 brew 코어 디렉토리 삭제 이후 brew를 다시 설치하면 된다.

```
# brew 코어 디렉토리 삭제 명령어
$ rm -fr $(brew --repo homebrew/core)
```

# 맥북 5000 포트 점유(address already in use :::5000)

macOS Monterey 이상으로 업데이트 했을 시 AirPlay 모드 기능이 켜져있으면 5000번 포트를 점유하고 있음.

lsof ~ kill 명령어로는 해결할 수 없고


시스템 환경 설정 - 공유 -> AirPlay 수신 모드 항목의 체크를 해제하면 된다.