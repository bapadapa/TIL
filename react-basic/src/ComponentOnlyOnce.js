import React from "react";

function ComponentOnlyOnce() {
  const [time, setTime] = React.useState(0);
  React.useEffect(() => {
    setTime(time + 1);
    console.log("Component가 화면에 처음 랜더링될 때 한번만 실행됩니다..");
  }, []);
  return <h3>{time}</h3>;
}
function NeverDoThisComponent() {
  const [time, setTime] = React.useState(0);
  //아래와 같이 사용하면 무한 랜더링이 걸린다.
  React.useEffect(() => {
    setTime(time + 1);
    console.log("Component가 화면에 처음 랜더링될 때 한번만 실행됩니다..");
  }, [time]);

  return <h3>{time}</h3>;
}
export default ComponentOnlyOnce;
