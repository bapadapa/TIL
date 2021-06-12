// 실제 선언 및 정의
var product = {
  title: "농구공",
  description: "농구의 황제 조던이 사용했던 농구공",
  price: 50000000,
};

var productNmae = product["title"];
var productDescription = product.description;

product["title"] = "축구공"; // 값 변경
product.title = "축구공"; //값 변경
product["seller"] = "그랩"; //값 추가
product.seller = "그랩"; //값 추가

var name = "bapa";
console.log(name == "bapa");
console.log(name === "bapa"); // 값 비교시에는 3개를 사용한다.
console.log(name !== "jim");

//선언식
function helloFunction() {
  console.log("hello javascript function");
}
//표현식
const hiFunction = function () {
  console.log("hi javascript function");
};
//함수 실행
helloFunction();
hiFunction();

//인자값 1개
function calculate(x) {
  var result = 3 * x * 5;
  console.log("결과값  : " + result + "입니다.");
}
var result = calculate(5);

function calculate2(x) {
  var result = 3 * x * 5;

  return result;
}
console.log("결과값  : " + calculate2(5) + "입니다.");

// 인자갑 n개
var getAge = function (name, age) {
  console.log(name + "은 " + age + "살입니다.");
};
getAge("bapa", 28);

function getProfile(profileName, profileAge) {
  return { name: profileName, age: profileAge };
}
var profile = getProfile("bapa", 20);
console.log(profile.name, profile.age, typeof profile);
