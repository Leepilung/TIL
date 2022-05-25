import React from 'react';
import styled from 'styled-components';

// 화면 가운데 정렬 + 앱 타이틀(일정 관리) 표시하는 컴포넌트.

const Template = styled.div`
  width: 512px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 6rem;
  border-radius: 4px;
  overflow: hidden;
  border: 3px solid black;
`;

const AppTitle = styled.div`
  background: #22b8cf;
  color: white;
  height: 4rem;
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const Content = styled.div`
  background: white;
`;

const TodoTemplate = ({ children }) => {
  return (
    <>
      <Template>
        <AppTitle>일정 관리</AppTitle>
        <Content>{children}</Content>
      </Template>
    </>
  );
};

export default TodoTemplate;
