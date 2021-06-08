function ChildCompoment(probs) {
  const name = probs.name;
  const age = probs.age;
  return (
    <h3>
      나는 {name}입니다. {age}살입니다.
    </h3>
  );
}

export default ChildCompoment;
