import React, { useState } from 'react';

const Counter = () => {


    function increase() {
        setCount(count + 1);
    }
    const [count, setCount] = useState(3);


    return (

        <div>
            <h1>{count}</h1>
            <button onClick = {increase}>Вротэнд</button>
        </div>
    )
}

export default Counter;