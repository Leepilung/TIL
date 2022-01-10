# OS 단어장

- Mutitasking

  하나의 프로그램이 끝나기 전에 다른 프로그램이 실행 되는 것.

- MultiProgramming

  메모리에 여러 프로그램이 동시에 올라가는 방식.(Multitasking)이 되려면 메모리에 여러가지가 올라가야 하긴 함.

- Time sharing

  시 분할. CPU를 쪼개서 진행.

- Multiprocess

  여러 프로세스가 동시에 실행된다.

4가지 용어가 전부 다 비슷비슷하다.
구분 짓는 방법은

- 위의 용어들은 컴퓨터에서 여러 작업을 동시에 수행하는 것을 뜻한다.
- Multiprogramming은 여러 프로그램이 메모리에 올라가 있음을 강조한다.
- Time Sharing은 CPU의 시간을 분할하여 나누어 쓴다는 의미를 강조한다.

> 🌟 Multiprocessor(다중 처리기)

CPU가 여러개 달린 녀석을 말하기도 한다.

이 녀석은 다른 의미인데 하나의 컴퓨터에 CPU(processor)가 여러 개 붙어 있음을 의미한다.

> 엔트리 포인트(entry point)

`엔트리 포인트(entry point)` 또는 `진입점(進入點)`은 제어가 운영 체제에서 컴퓨터 프로그램으로 이동하는 것을 말하며, 프로세서는 프로그램이나 코드에 진입해서 실행을 시작한다.

> 파일 디스크립터(File Descriptor)란 ?

쉽게 말하자면, `시스템으로부터 할당받은, 파일(File)을 대표하는 음수가 아닌 정수`이다.

시스템이 파일을 사용할 때, 단순히 파일명으로 접근하기에는 불편함이 있다. 만약 사용할 파일이 길고 복잡한 파일명이면 쓸 때마다 길고 복잡한 파일명을 참조해야 한다.

그렇기 때문에 리눅스에서는 프로세스가 파일을 사용할 때, 파일에다가 별명을 붙여 사용하기 쉽게 한 것이다.

여기서 `별명`이 `파일 디스크립터`라고 이해하면 된다.

프로그램이 메모리에 탑재되어 실행이 될 때, 기본적으로 할당되는 파일 디스크럽터가 있다.

바로 0(stdin, 표준 입력), 1(stdout, 표준 출력), 2(stderr, 표준 에러) 이다. 이들은 프로그램이 실행되면, 기본적으로 할당되는

파일 디스크립터이다. 그래서 파일 디스크립터는 3부터 할당된다.

`파일 디스크립터`는 프로세스마다 같을 수도, 다를 수도 있다.

<img src="https://postfiles.pstatic.net/MjAxODA2MDJfMTk4/MDAxNTI3ODY2NTI2NTgw.PQA5v6qv5-DCXxjSTW4HmYDXnL6OT2_2buXtrl5Ao9Qg.yBTwImXMTDqM2Rw_5Or2-k9waUdWlwPRmYtdrZoErtog.PNG.songblue61/1.PNG?type=w966">

서로 같은 파일을 써도 프로세스가 다르면, 다른 파일 디스크립터를 가질 수 있고

<img src="https://postfiles.pstatic.net/MjAxODA2MDJfMTg4/MDAxNTI3ODY2NjE0MjMw.7VYL-ZtpPbqxdrNxdmsTri8xhNm-P7GCEv0N3LLJbDog.UDk_wD-XSDXShlJeXNl5Dj_hDFcaJtCWLpTXuwvn2qUg.PNG.songblue61/2.PNG?type=w966">

서로 다른 프로세스가 서로 다른 파일을 사용해도, 파일 디스크립터는 같은 값일 수 있다.

위의 설명을 한문장으로 간단히 표현하자면, `프로세스는 자기만의 파일 디스크립터 테이블을 하나씩 갖고 있다`

> 파일 디스크립터가 할당되는 과정

- 파일 디스크립터 테이블(File Descriptor Table)

  프로세스가 현재 사용중인 파일을 관리하기 위한 테이블이며, 프로세스마다 하나씩 가지고 있다.

  File Table을 가리키는 포인터를 담고있는 배열이고, 이 배열의 index가 fd이다.

- 파일 테이블((Open) File Table)

  프로세스에 의해 open된 파일의 읽기/쓰기 동작을 지원하기 위한 테이블. 파일이 열릴 때마다 하나씩 할당된다.

  따라서, 만약 하나의 프로세스가 A라는 파일을 3번 open한다면, A의 File Table Entry가 3개 생성된다.

  이 테이블 Entry 안에는 open_flag, file_offset, ref_cnt, VFS table을 가리키는 포인터가 들어있다.

- VFS i-node Table (Virtual File System i-node Table)

  프로세스들이 사용하고 있는 파일의 i-node를 담고 있는 테이블이다. File Table과는 달리, 만약 하나의 프로세스가 A라는 파일을 3번 open해도 i-node Table Entry는 하나밖에 할당되지 않는다.

  i-node 안에는 i-node 번호, 파일 종류와 권한, 크기, 데이터 블록을 가리키는 포인터 등의 파일 정보가 들어있다.

  i-node Table Entry에는 i-node, ref_cnt가 들어있다.

- 할당 과정

  만약 프로세스가 fileA라는 파일을 쓰기권한으로 open한다고 하자. fd = open("fileA", O_WRONLY);

  1. 커널은 File System에서 fileA를 찾아, 해당 파일의 i-node를 가져와 VFS i-node table의 빈 공간(Entry)에 할당.

     만약 fileA의 i-node가 이미 할당되어있는 경우, ref_cnt(reference counter)만 하나 증가시킨다.

  2. i-node 정보에 담겨있는 접근 권한을 찾아, 쓰기 권한(O_WRONLY)을 허용하는지 확인한다.

  3. 권한이 있다면 file table의 Entry에 open_flag, file_offset, ref_cnt, VFS i-node table entry 포인터 등의 정보를 할당한다.

  4. File descriptor table을 index 0부터 탐색해서, 빈 공간에 file table entry를 가리키는 포인터를 저장한다.

  5. 저장한 곳의 index를 반환한다.

  그림을 보면서 이해하면 쉽다.

<img src="https://mblogthumb-phinf.pstatic.net/MjAxODExMDVfMTE0/MDAxNTQxMzg2ODkwMTc4.TA2Lnn4dC70OSSCQkf2YqUXTgv8FD5_3fTxQfPC87Dwg.W-672W6OlWYtFFHeM7Isolm-UjnAGsZcgN1IQ1FChbwg.PNG.songblue61/%EC%BA%A1%EC%B2%98.PNG?type=w800">
