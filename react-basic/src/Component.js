import React from "react";

function Component() {
  const [time, setTime] = React.useState(0);
  setTime(time + 1);
  console.log("Rendering이 됩니다.");
  return <h3>{time}</h3>;
}
export default Component;
