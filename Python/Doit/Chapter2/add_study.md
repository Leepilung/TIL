# 모듈 가져오기(import)

import 명령문을 사용하면 모듈을 가져올 수 있다.

방법에는 두 가지 방법이 있다.

```m
1. import 모듈
```

```m
2. from 모듈 import 이름
```

첫 번째 방법으로 불러올 경우 모듈 전체를 가져온다

```m
>>> import tkinter
>>> tkinter.widget = tkinter.Label(None, text='I love Python!')
>>> tkinter.widget.pack()
```

그러나 이방법은 `모듈.변수`의 형식으로 써줘야 하기 때문에 번거롭다.
