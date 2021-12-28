# PintOS 문법 정리 단어장

# 
## Semaphores

추상자료형 : Object와 Operation으로 구성됨 

앞의 방식들을 추상화 시킴

공유자원을 획득하고 반납하는 것을 Semaphore가 처리해줌

Semaphore S : 정수값(integer variable)을 가질 수 있는데 그것이 자원의 개수라고 생각(즉 S가 5면, 자원이 5개있는것)

P연산은 값을 획득하는 과정이고, V연산은 반납하는 과정

P(S) : while (S≤0)do no-op; //lock을 거는과정
   
                                   //S값이 0이하인 경우 아무것도 안하고 기다림 자원을 다가져가고 없는 상태니까,

                                  //여기서도 busy wait 문제는 발생함 (계속해서 자원이 없으면 기다리기만하니까)

    s—; // 기다리다가 양수값이되면 자원을 1빼고 획득!

V(S) : S ++; //lock을 푸는 과정

mutex : CS이 1개인것

semaphore : CS이 1개이상 들어갈 수 있다


# Project 1

in thread.h

```c
struct thread {
	/* Owned by thread.c. */
	tid_t tid;                          /* Thread identifier. */
	enum thread_status status;          /* Thread state. */
	char name[16];                      /* Name (for debugging purposes). */
	int priority;                       /* Priority. */

	/* Shared between thread.c and synch.c. */
	struct list_elem elem;              /* List element. */
```

스레드를 위한 구조체 형태

스레드는 구조체의 스택 영역에 존재한다 -> 힙영역으로 커진다.

`struct thread`가 너무 크면 커널 스택을 위한 영역이 없을 것이다. 그래서 몇 바이트 정도의 공간만 가지게 된다. (반드시 1kB 미만으로 잡아준다)

커널 스택도 너무 커지면 안된다. 커널에서 스택 오버플로우가 발생하면 스레드 상태를 변이시킬 가능성이 있다.

그렇기에 커널 함수는 큰 사이즈의 structure나 non-static 지역 변수를 가지면 안된다.

malloc이나 palloc_get_page()같은 동적할당을 활용해야 한다.

---
```c
tid_t tid
```

스레드의 식별자이다.

모든 스레드는 스레드의 수명동안 고유한 식별자를 갖는다.

tid_t는 정수이며, 새로 생기는 스레드는 더 높은 숫자의 tid를 갖게 된다. (ex 1, 2, 3, 4와 같이 오름차순으로 커짐)

type이나 순서 매기는 방식을 변경이 가능하다.

---

```c
enum thread_status status;
```

스레드의 상태를 바꿔주는 녀석

1. THREAD_RUNNING

   - 기동(running) 중.

   - 오직 한 스레드가 주어진 시간동안 기동하고 있다.

   - thread_current()는 현제 기동중인 스레드를 반환한다.

2. THREAD_READY

   - 스레드가 기동할 준비가 되었지만 기동하지 않는 상태

   - 스케줄러에 의해 기동될 수 있다.

   - ready thread는 ready_list라는 이중연결리스트 안에 보관된다.

3. THREAD_BLOCKED

   - 대기(or 일시정지) 중인 상태이다. (ready와는 다름)

   - 이 스레드는 thread_unblock() 으로 상태가 THREAD_READY 로 바뀌기 전에는 스케줄에 할당되지 않는다.

   - 원시적 synchronization 방법이다.

   - Blocked thread가 무엇을 기다리고 있는지 알 수 있는 방법은 없다. (하지만 backtrace가 도움이 될 수도 있다.)

4. THREAD_DYING

   - 다음 스레드가 온다면 스케줄러에 의해 사라질 스레드라는 것을 나타낸다.

---

```c
char name[16]
```
스레드의 이름이나 축약어를 기록하는 부분

---

```c
struct intr_frame tf;
```
문맥 교환(context switching)을 위해 정보를 저장한다.

스택 포인터나 레지스터가 주로 담긴다.

---

```c
struct list_elem elem;
```
스레드를 이중연결 리스트에 넣기 위해서 쓰인다. 

이중연결리스트라 하면, ready_list (run을 위해 ready중인 스레드의 리스트), sema_down()에서 세마포어에서 waiting중인 스레드 리스트를 말한다.

이 두 경우에서 쓸 수 있는 이유는 세마포어에 있는 스레드는 ready상태가 될 수 없고, 반대로 ready인 스레드는 세마포어일 수가 없다. 그래서 이 두 리스트에 대해서 같은 list_elem을 사용할 수 있는 것이다.


---------------------

# Thread Functions
