# HTML 궁금점 정리

> `<script type="text/javascript">` 의 의미

`<script type="text/javascript">` 는 보통 HTML에서 `<body>` 부분에 주로 입력되는 사항인데 텍스트를 통해 자바스크립트를 구현하겠다는 의미로 해석하면 된다.

HTML 문서에 자바스크립트를 로딩하는 방법에는 3가지 정도가 있는데

1. `<script type="text/javascript">`

2. `<script language="javascript">`

3. `<script>`

보통 1을 많이 쓰는 것 같고, 3으로만 작성하더라도 대부분 큰 문제는 없다.

3의 경우처럼 script 선언은 브라우저 기본 설정에 맞추어 가는데, 대부분의 브라우저가 기본 설정이 javascript로 되어있기 때문에 3처럼만 써도 크게 상관은 없다.

총 정리 하면 표준의 형태는 1.번과 같지만 HTML5 이상부터는 대부분 브라우저가 JavsScript가 기본설정값으로 되어 있기 때문에 3.으로 작성하여도 무관하다.
