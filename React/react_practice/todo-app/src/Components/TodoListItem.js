import React from 'react';
import {
  MdCheckBoxOutlineBlank,
  MdCheckBox,
  MdRemoveCircleOutline,
} from 'react-icons/md';
import styled, { css } from 'styled-components';

// 각 할 일 항목에 대한 정보를 보여 주는 컴포넌트
const ListItem = styled.div`
  padding: 1rem;
  display: flex;
  align-items: center;
  &:nth-child(even) {
    background-color: rgba(100, 100, 160, 0.5);
  }

  & + & {
    border-top: 1px solid black;
  }
`;

const CheckBox = styled.div`
  cursor: pointer;
  flex: 1;
  display: flex;
  align-items: center;
  svg {
    // react-icons 아이콘 태그
    font-size: 1.5rem;
  }

  ${(props) =>
    props.checked &&
    css`
      svg {
        color: #22b8cf;
      }
    `}
`;

const Text = styled.div`
  margin-left: 0.5rem;
  flex: 1;

  ${(props) =>
    props.checked &&
    css`
      color: rgba(210, 210, 210, 1);
      text-decoration: line-through;
    `}
`;

const Delete = styled.div`
  display: flex;
  align-items: center;
  font-size: 1.5rem;
  color: #ff6b6b;
  &:hover {
    color: rgba(230, 170, 170, 0.9);
  }
`;

const TodoListItem = ({ todo }) => {
  const { text, checked } = todo;
  return (
    <ListItem>
      <CheckBox>
        {checked ? <MdCheckBox /> : <MdCheckBoxOutlineBlank />}
        <Text checked={checked}>{text}</Text>
      </CheckBox>
      <Delete>
        <MdRemoveCircleOutline />
      </Delete>
    </ListItem>
  );
};

export default TodoListItem;
