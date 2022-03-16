# Homebrew -> brew install CL 입력시 No similarly named formulae found 에러

해당 에러 해결법은 간단함.

우선 brew 코어 디렉토리 삭제 이후 brew를 다시 설치하면 된다.

```
# brew 코어 디렉토리 삭제 명령어
$ rm -fr $(brew --repo homebrew/core)
```
