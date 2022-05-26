# React-router

```js
<Routes>
    <Route path="주소규칙" element={<보여줄컴포넌트/>}>
</Routes>
```

```js
    <Route path="/" element={<보여줄컴포넌트/> exact={true}}>
```

경로가 "/" 일경우 어떤 주소던 포함되는 것으로 알고 있었으나 실제 테스트 결과 홈페이지에서만 동작하고 다른 페이지에서 중복렌더링 안됨.

패키지가 업데이트되서 그런듯. 책(V5기준인듯?)과는 문법 자체도 많이 다름.

exact 옵션 삭제됨(V6에서)

# Link 컴포넌트 사용

웹 애플리케이션에선 a태그 사용하나 리액트 라우터를 사용할 때에는 a 태그 사용하면 안됨.

a 태그는 페이지 전환과정에서 페이지를 전부 새로 불러와 `상태를 전부 초기화`시켜버림.

Link 컴포넌트를 사용해 페이지를 전환하면, 페이지를 새로 불러오지 않고 어플을 유지한 상태에서 HTML5 History API를 사용해 페이지의 주소만 변경해줌

```Js
<Link to="주소">내용</Link>
```

다른경로 같은 컴포넌트 렌더링 -> 따로따로 해야될듯. props 배열설정은 이제 안된다는듯.

파라미터 -> 특정 아이디, 이름 사용하여 조회할 떄 사용
쿼리 -> 어떤 키워드 검색 or 페이지에 필요한 옵션 전달 시 사용.

강제된건 아니고 일반적인 사용 예시.

# URL 파라미터 match 객체 -> URL Params로 변경

기존에 파라미터 받아서 Match를 사용하는 방법 -> v6에서 UseParams로 변경됨

```Js
// v5
const Profile = ({ match }) => {
	// v5에선 파라미터를 받아올 땐 match 안에 들어있는 params 값을 참조
	const { username } = match.params;
}

<Route path="/profiles/:username" component={Profile} />



// v6
import { useParams } from 'react-router-dom';

const Profile = () => {
	const { username } = useParams();
}

<Route path="/profiles/:username" element={<Profile />} />
```

# URL 쿼리 읽는법( 기존 : location 객체)

v5 에서는 라우트 컴포넌트에게 전달되는 location 객체에 있는 search 값에서 읽어올 수 있고, 문자열을 객체 형태로 변환하기 위해서 qs라는 라이브러리를 사용해야만 했는데

```js
// v5
import qs from 'qs'

const About = ({ location }) => {
	const query = qs.parse(location.search, {
		ignoreQueryPrefix: true   //쿼리 접두사 무시
	}

	const detail = query.detail === 'true'; // 쿼리의 파싱 결과값은 문자열

	return (
		<div>
			{detail && <p>해당 경로로 들어오면 보이는 텍스트입니다</p>}
		</div>
	)
}
```

이젠 `useLocation`을 사용해야함

```js
// v6
import { useLocation } from "react-reuter-dom";

const About = () => {
    const { search } = useLocation();

    //현재 지금 경로가(search) '?detail=true' 인지 확인
    const detail = search === "?detail=true";

    return (
        <div>{detail && <p>해당 경로로 들어오면 보이는 텍스트입니다</p>}</div>
    );
};
```

# 서브 라우팅
```js
// v5
// Profiles 컴포넌트에 있는 Route 
return (
  <div>
    <Route
      path="/profiles"
      exact
      render={() => <div>유저를 선택해주세요.</div>}
    />
    <Route path="/profiles/:username" component={Profile} />
  </div>
);

// App.js
const App = () => {
  return (
    <div>
      <Route path="/" exact={true} component={Home} />
      <Route path="/about" component={About} />
      <Route path="/profiles" component={Profiles} />
    </div>
  );
};
```

App.js에서는 `<Profiles /> `컴포넌트를 렌더링하고, Profiles 주소로 들어오면 render안에 작성한 `<div>` 태그를 렌더링, 그리고 `<Profiles />` 컴포넌트를 렌더링하는 해줬음.

```js
// v6
// Profiles 컴포넌트에 있는 Route 
return (
  <Routes>
			<Route path="/*" element={<div>유저를 선택해주세요.</div>} />
      <Route path=":username" element={<Profile />} />
  </Routes>
);

// App.js
const App = () => {
  return (
    <Routes>
      <Route path="/" exact={true} component={Home} />
      <Route path="/about" component={About} />
      <Route path="/profiles/*" element={<Profiles />} />
    </Routes>
  );
};
```

- Routes로 무조건 감싸줘야하고
- 하위 페이지가 있으면 부모 Rotue에 '/*' 추가해줘야함(exact가 대체된 것이라 함.
- path에 부모경로까지 적을 필요 없이 :username만 적어도된다.



# render -> element

그리고 IIFE 구조 안해도됨.

# history, useHistory 대신 useNavigate로 교체