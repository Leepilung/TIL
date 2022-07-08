# 맥 개발환경 세팅

설치 과정 블로그나 Md에 자세히 기록 필요.

0. brew 설치
1. iterm2 설치
2. zsh -> Oh my zsh 설치
   - syntaxhighlighting
   - autosuggestion
   - neofetch

# 하나의 맥 환경에서 2개 계정 설정

- SSH 키 발급 각각 다르게 받기(key name 다르게)
- SSH 키 등록
- 디렉토리마다 다르게 설정(git config global && local)
  - .git/config에서 해도 무관
- ~/.ssh/config -> Host, Name 설정 다르게
- ssh -T git@github.com-{설정값} 으로 연결 테스트
