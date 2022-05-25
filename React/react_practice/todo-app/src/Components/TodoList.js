import React from 'react';
import { List } from 'react-virtualized';
import TodoListItem from './TodoListItem';
import styled from 'styled-components';

// todos 배열을 props로 받아 온 후, 이를 배열 내장 함수 map을 사용해서 여러 개의 TodoListItem 컴포넌트로 변환하여 보여준다.

const List = styled.div`
  min-height: 320px;
  max-height: 513px;
  overflow-y: auto;
`;

const TodoList = ({ todos, onRemove, onToggle }) => {
  return (
    <List>
      {todos.map((todo) => (
        <TodoListItem
          todo={todo}
          key={todo.id}
          onRemove={onRemove}
          onToggle={onToggle}
        />
      ))}
    </List>
  );
};

// 리스트 관련 컴포넌트 최적화 시 리스트 내부에서 사용하는 컴포넌트도 최적화해야 하고,
// 리스트로 사용되는 컴포넌트 자체도 최적화 해주는 것이 좋다.
// 내부 데이터가 100개를 안넘으면 굳이 할 필요가 없음.

export default React.memo(TodoList);
