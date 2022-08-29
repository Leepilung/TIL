import React, { useState } from 'react';

const State = () => {
  // 리액트에서 상태 선언 방법
  const [state, setState] = useState('');

  const inputEventHandler = (e) => {
    setState(e.target.value)
  }
  return (
    <div>
      <input value={state} onChange={inputEventHandler}/>
    </div>
  );
};

export default State;