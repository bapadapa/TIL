//예시 1
function SayHelloComponent() {
  const test = "안녕";
  return (
    <div>
      <h3>Bapa가 얘기합니다 : {test}</h3>
    </div>
  );
}
//예시 2
function SayHelloComponent2() {
  const getHello = function () {
    return <h3>bapa가 얘기합니다.</h3>;
  };
  return <div>{getHello()}</div>;
}
//예시 3
function SayHelloComponent3() {
  const sayHello = function () {
    alert("안녕 나는 bapa야");
  };
  return (
    <div onClick={sayHello}>
      <h3>클릭 해보세요</h3>
    </div>
  );
}

export default SayHelloComponent3;
