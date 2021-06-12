console.log("hello Parcel!!!");
console.log("hello parcel");

async function test() {
  const promise = Promise.resolve(123);
  console.log(await promise);
}
test();
