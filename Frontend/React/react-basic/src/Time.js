import React from "react";

function TimeComponent() {
  const [Time, setTime] = React.useState(0);
  const [abc, setAbc] = React.useState(1);
  console.log("Component Update");
  function updateTime() {
    setTime(Time + 1);
  }
  return (
    <div>
      <h3>{Time}초</h3>
      <button onClick={updateTime}>버튼을 누르면 1씩올라가유</button>
    </div>
  );
}
export default TimeComponent;
