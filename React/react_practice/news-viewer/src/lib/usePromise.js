import { useEffect, useState } from 'react';

// 프로젝트의 다양한 곳에서 사용될 수 있는 유틸 함수들은 보통 이렇게 src 디렉토리에 lib 디렉토리를 만든 후 그 안에 작성한다.
// Promise를 통해 API 호출하는 커스텀 Hook -> 코드의 간결성 확보

export default function usePromise(promiseCreator, deps) {
  // 3가지 상태에 대한 상태 관리
  const [loading, setLoading] = useState(false);
  const [resolved, setResolved] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const process = async () => {
      setLoading(true);
      try {
        const resolved = await promiseCreator();
        setResolved(resolved);
      } catch (e) {
        setError(e);
      }
      setLoading(false);
    };
    process();
    // ↓ eslint 경고 출력되는거 무시해주는 구문
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);

  return [loading, resolved, error];
}
