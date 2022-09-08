# Web-server && WAS의 차이점

> 목표

1. Static Page, Dynamic Pages의 과정 이해
2. Web Server와 WAS의 차이 이해
3. Web 서비스 구조에 대한 이해

# Static Pages && Dynamic Pages
<img src="https://gmlwjd9405.github.io/images/web/static-vs-dynamic.png"/>

## Static Pages
- Web Server는 파일 경로 이름을 받아 경로와 일치하는 files contents를 반환한다.
- 항상 동일한 페이지를 반환한다.
  - ex: image, html, css, javascript 파일과 같이 컴퓨터에 저장되어 있는 파일들

## Dynamic Pages
- 인자의 내용에 맞게 동적인 contents를 반환한다.
- 웹 서버에 의해 실행되는 프로그램을 통해 만들어진 결과물을 의미

# Web Server && WAS(Web Application Server)의 차이

<img src="https://gmlwjd9405.github.io/images/web/webserver-vs-was1.png"/>

## Web server
- 웹 서버는 소프트웨어와 하드웨어로 구분된다.
- 하드웨어 : 웹 서버가 설치되어 있는 컴퓨터
- 소프트웨어 : 웹 브라우저 클라이언트로부터 HTTP 요청을 받아 정적인 컨텐츠(.html .jpeg .css 등)을 제공하는 컴퓨터 프로그램

- 기능
  - HTTP 프로토콜을 기반으로 클라이언트의 요청을 서비스 하는 기능을 담당함
  - 요청에 따라 두 가지 기능 중 적절하게 선택하여 수행한다.
  - 기능 1
    - 정적인 컨텐츠 제공
    - WAS를 거치지 않고 바로 자원을 제공
  - 기능 2
    - 동적인 컨텐츠 제공을 위한 요청 전달
    - 클라이언트의 요청을 WAS에 보내고, WAS의 처리 결과를 클라이언트에게 전달(응답, response) 한다.
  - Web Server의 ex : Apache Server, NginX, IIS(window 전용 웹 서버)

## WAS (Web Application Server)
- WAS란 DB 조회나 다양한 로직 처리를 요구하는 동적인 컨텐츠를 제공하기 위해 만들어진 Application Server이다.
- HTTP를 통해 컴퓨터나 장치에 애플리케이션을 수행해주는 미들웨어이기도 하다.
- 웹 컨테이너(Web Container) 혹은 서블릿 컨테이너(Servlet Container)라고도 불린다.
  - 여기서 컨테이너(Container)란 JSP, SErvlet등을 실행시킬 수 있는 소프트웨어를 의미한다.
  - 즉, WAS는 JSP, Servlet(`서블릿`이란 Dynamic Web Page를 만들 때 사용되는 자바 기반의 웹 애플리케이션 프로그래밍 기술) 구동 환경을 제공한다.

- 역할
  - WAS = Web Server + Web Container
  - Web Server 기능들을 구조적으로 분리하여 처리하고자 하는 목적으로 제시되었다.
    - 분산 트랜잭션, 보안, 메시징, 쓰레드 처리등의 기능을 처리하는 분산 환경에서 사용된다.
    - 주로 DB 서버와 같이 수행된다.
  - 현재는 WAS가 가지고 있는 Web Server또한 정적인 컨텐츠를 처리하는 데 있어 성능상 큰 차이가 없다.

- WAS의 주요 기능
  - 프로그램 실행 환경과 DB 접속 기능 제공
  - 여러 개의 트랜잭션(논리적인 작업 단위) 관리 기능
  - 업무를 처리하는 비즈니스 로직 수행

- WAS의 ex : Tomcat, JBoss, Jeus, Web Sphere 등

## Web Serverd와 WAS를 구분하는 이유

<img src="https://gmlwjd9405.github.io/images/web/webserver-vs-was2.png"/>

- Web Server가 필요한 이유?
  - 클라이언트(웹 브라우저)에 이미지 파일(정적 컨텐츠)를 보내는 과정을 생각해 보자
    - 이미지 파일과 같은 정적 파일은 웹 문서(HTML 문서)가 클라이언트로 보내질 때 함께 가는 것은 아니다.
    - 클라이언트는 HTML 문서를 먼저 받고 그에 맞게 필요한 이미지 파일들을 다시 서버로 요청하면 그때서야 이미지 파일을 받아온다.
    - Web Server를 통해 이런 정적인 파일들을 Application Server까지 가지 않고 앞단에서 빠르게 보내줄 수 있다.
  - 따라서 Web Server에서는 정적인 컨텐츠만 처리하도록 기능을 분배하여 서버의 부담을 줄일 수 있다.
  
- WAS가 필요한 이유?
  - 웹 페이지는 정적 컨텐츠와 동적 컨텐츠가 모두 존재한다.
    - 이러한 특징 떄문에 사용자의 요청에 맞게 적절히 동적 컨텐츠를 만들어 제공해야 한다.
    - 이때, Web Server만을 이용한다면 사용자가 원하는 요청에 대한 결과값을 모두 미리 만들어 놓고 서비스를 해야 한다.
    - 하지만 이렇게 수행하기에는 자원이 절대적으로 부족하다.
  - 따라서 WAS를 통해 요청에 맞는 데이터를 DB에서 가져와 비즈니스 로직에 맞게 그때 그때 결과를 만들어 제공함으로써 자원의 효율적 사용이 가능하다.

- 그렇다면 WAS와 Web Server를 분리하는 이유는?
  - 1. 기능을 분리하여 서버의 부하를 방지
    - WAS는 DB 조회나 다양한 로직을 처리하느라 바쁘기 때문에 단순 정적 컨텐츠는 Web Server에서 빠르게 클라이언트에게 제공하는 것이 좋다.
    - WAS는 기본적으로 동적 컨텐츠를 제공하기 위해 존재하는 서버이다.
    - 만약 정적 컨텐츠 요청까지 WAS가 처리한다면 정적 데이터 처리로 부하가 커지게 되고, 동적 컨텐츠의 처리가 지연됨에 따라 수행 속도가 느려진다.
    - 즉 페이지 노출 시간이 늘어나는 문제가 발생한다.

  - 2. 물리적으로 분리하여 보안을 강화
    - SSL(Secure Sockets Layer : 보안 소켓 계층)에 대한 암복호화 처리에 Web Server를 사용한다.

  - 3. 여러 대의 WAS 연결 가능
    - 로드 밸런싱을 위해 Web Server를 사용한다.
    -  Fail Over(장애 극복), Fail Back 처리에 유리하다.
    -  대용량 웹 어플리케이션(여러 대의 서버 사용)의 경우에는 Web Server와 WAS를 분리하여 무중단 운영을 위한 장애 극복에 쉽게 대응할 수 있다.
    -  예를 들어, 앞 단의 Web Server에서 오류가 발생한 WAS를 이용하지 못하도록 한 후 WAS를 재시작함으로 사용자는 오류를 느끼지 못하고 이용할 수 있다.

  - 4. 여러 웹 어플리케이션 서비스 가능
    - 예를 들어, 하나의 서버에서 PHP, Java등의 동시 사용 가능

  - 5. 기타
    - 접근 허용 IP 관리, 2대 이상의 서버에서의 세션 관리 등도 Web Server에서 처리하면 효율적이다.

  - 즉, 자원 이용의 효율성 및 장애 극복, 배포 및 유지보수의 편의성을 위해 Web Server와 WAS를 분리한다.
  - Web Server를 WAS 앞에 두고 필요한 WAS들을 Web Server에 플러그인 형태로 설정하면 더욱 효율적인 분산 처리가 가능하다.

## Web Service Architecture

- 다양한 구조를 가질 수 있다.
  - Client -> Web Server -> DB
  - Client -> WAS -> DB
  - Client -> Web Server -> WAS -> DB

<img src="https://gmlwjd9405.github.io/images/web/web-service-architecture.png"/>

위의 이미지는 3번 구조의 예시인데 해당 구조의 동작 과정은 다음과 같다.

- 동작 과정
  - Web Server는 웹 브라우저 클라이언트로부터 HTTP 요청을 받는다.
  - Web Server는 클라이언트의 요청(Request)을 WAS에 보낸다.
  - WAS는 관련된 Servlet을 메모리에 올린다.
  - WAS는 web.xml을 참조하여 해당 Servlet에 대한 Thread를 생성한다.
    - Thread는 Servlet의 service() 메서드를 호출한다
    - service() 메서드는 요청에 맞게 doGet() 또는 doPost() 메서드를 호출한다.
  - doGet() 또는 doPost() 메서드는 인자에 맞게 생성된 적절한 동적 페이지를 Response 객체에 담아 WAS에 전달한다.
  - WAS는 Response 객체를 HttpResponse 형태로 바꾸어 Web Server에 전달한다.
  - 생성된 Thread를 종료하고, HttpServletRequest와 HttpServletResponse 객체를 제거한다.

# DBMS와 MiddleWare의 개념 차이점

## DMBS (Database Management System)
  - 다수의 사용자들이 DB 내의 데이터를 접근할 수 있도록 해주는 소프트웨어
  - DMBS는 보통 Server의 형태로 서비스를 제공한다.
    - ex : MySQL, MariaDB, Oracle, PostgreSQL 등
  - DBMS Server에 직접 접속해서 동작하는 Client Program의 문제점
    - Client에 로직이 많아지고, 이에 따라 Client Program의 크기가 자연스레 커진다.
    - 로직이 변경될 때마다 매번 배포가 진행되어야 한다.
    - Client에 대부분의 로직이 포함되어 배포가 되기 때문에 보안에 굉장히 취약하다.
  - 이러한 문제를 해결하기 위해 MiddleWare가 생겨났다.

## MiddleWare
  - Client - MiddleWare - DB Server(DBMS)
  - 동작 과정
    - 1. Client는 단순히 요청만 중앙에 있는 MiddleWare Server에 보낸다.
    - 2. MiddleWare Server에서 대부분의 로직이 수행된다.
    - 3. 이때, 데이터를 조작할 일이 생기면 DBMS로 요청을 보낸다.
    - 4. 로직의 결과를 응답으로 Client에게 전송한다.
    - 5. Client는 그 결과를 화면에 보여준다.
  - 즉, 비즈니스 로직을 Client와 DBMS 사이의 MiddleWare Server(통상의 백엔드(?))에서 동작하도록 함으로써 Client는 입력과 출력만 담당하게 된다.