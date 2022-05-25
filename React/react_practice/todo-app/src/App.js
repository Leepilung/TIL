import React, { useState, useCallback, useRef } from 'react';
import TodoTemplate from './Components/TodoTemplate';
import TodoInsert from './Components/TodoInsert';
import TodoList from './Components/TodoList';

const createBulkTOdos = () => {
  const array = [];
  for (let i = 1; i <= 2500; i++) {
    array.push({
      id: i,
      text: `할 일 ${i}`,
      checked: false,
    });
  }
  return array;
};

const App = () => {
  const [todos, setTodos] = useState(createBulkTOdos);

  // 렌더링과 관련 없는 변수 사용 시 -> useRef 사용.
  const nextId = useRef(2501);

  // 세터 함수를 사용할 때 앞에 변경하려는 상태를 화살표함수로 엮어줌 'Todos => '
  // 상태를 참조하는 모든 함수를 화살표함수 사용하게 바꿔 최적화함으로써 useCallback의 의존성 제거 가능 + 속도 20배정도 개선.

  // input 입력 시 내용 추가
  const onInsert = useCallback((text) => {
    const todo = { id: nextId.current, text, checked: false };
    setTodos((todos) => todos.concat(todo));
    nextId.current += 1;
  }, []);

  // 내용 삭제
  const onRemove = useCallback((id) => {
    setTodos((todos) => todos.filter((todo) => todo.id !== id));
  }, []);

  const onToggle = useCallback((id) => {
    setTodos((todos) =>
      todos.map((todo) =>
        todo.id === id ? { ...todo, checked: !todo.checked } : todo,
      ),
    );
  }, []);

  return (
    <>
      <TodoTemplate>
        <TodoInsert onInsert={onInsert} />
        <TodoList todos={todos} onRemove={onRemove} onToggle={onToggle} />
      </TodoTemplate>
    </>
  );
};

export default App;
