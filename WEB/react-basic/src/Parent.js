import ChildCompoment from "./Child";
function ParentComponent(probs) {
  const name = probs.name;
  return (
    <div>
      <h3>나는 {name} 입니다.</h3>
      <div>
        <h1>내 자식을 소개 합니다.</h1>
        <ChildCompoment name="민수" age={27} />
        <ChildCompoment name="승현" age={28} />
        <ChildCompoment name="BAPA" age={28} />
      </div>
    </div>
  );
}
export default ParentComponent;
