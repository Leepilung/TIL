import React, { useState, useCallback } from 'react';
import { MdAdd } from 'react-icons/md';
import styled from 'styled-components';

// 새로운 항목을 입력하고 추가할 수 있는 컴포넌트

const InsertForm = styled.form`
  display: flex;
  background: #495057;
`;

const TodoInput = styled.input`
  background: none;
  outline: none;
  border: none;
  padding: 0.5rem;
  font-size: 1.125rem;
  line-height: 1.5;
  color: white;
  // 1로 선언하면 다른 요소가 차지하는 영역 제외하고 혼자 다먹음.
  flex: 1;

  &::placeholder {
    color: #dee2e6;
  }
`;

const TodoButton = styled.button`
  // 기본 스타일 초기화 구문들
  background: none;
  outline: none;
  border: none;

  // 스타일 정의 구문
  background: #868e96;
  color: white;
  padding: 0 1rem 0 1rem;
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: 0.2s ease-in;
  &:hover {
    background: #adb5bd;
  }
`;

const TodoInsert = ({ onInsert }) => {
  const [value, setValue] = useState('');

  const onChange = useCallback((e) => {
    setValue(e.target.value);
    console.log(e.target.value);
  }, []);

  const onSubmit = useCallback(
    (e) => {
      onInsert(value);
      setValue('');
      e.preventDefault();
    },
    [onInsert, value],
  );

  return (
    <>
      <InsertForm onSubmit={onSubmit}>
        <TodoInput
          placeholder="할 일을 입력하시오"
          value={value}
          onChange={onChange}
        />
        <TodoButton type="submit">
          <MdAdd />
        </TodoButton>
      </InsertForm>
    </>
  );
};

export default TodoInsert;
