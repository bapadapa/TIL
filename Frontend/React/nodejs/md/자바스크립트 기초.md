# 변수

## var,let,const 차이

- var은 같은 이름의 변수를 다시 사용할 수 <font color = 'red'>있다. </font>
  - 권장하지는 않지만, 브라우저( 과거와의 호환성 )에서는 사용한다.
- let은 같은 이름의 변수를 다시 사용할 수 <font color = 'red'>없다. </font>
  - 최근에 사용을 많이 한다.
- const는 선언된 변수에 새로운 값을 정의 할 수 없다.

```javaScript
let num2 = 20;
num2 = 'hello';
//let num2 = 'bob';
```

## 주석

- // 한줄 주석
- /_ 여러줄 주석 _/

## 기본 자료형

- string , number , boolean
- null 값 이 없을 때 자료형
- undefined 변수 선언만 하고 정의하지 않은 상태

```javaScript
var name; // undefined
nam = 'bapa'; // string
var age = 30; //number
var isFool = false; // boolean (true/ false)
var nully = null; // null
```

### array ( 배열 )

- 실제로 array는 object의 종류 중 하나로 object 자료형이다.

### 객체 ( Object )

- 객체는 자료들을 key : value 형태로 저장하는 자료형
- {}안에 key:value를 순차적으로 넣는다.
- 파이썬의 dict타입과 비슷

```javaScript
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
```

### 연산자

- 기본연선자
  - - , - , \* , /
- 비교 연산자
  - > , < , >= , <= , ==, !=
    - ===는 변수의 값을 비교한다.

```javascript
var name = "bapa";
console.log(name == "bapa");
console.log(name === "bapa");
console.log(name !== "jim");
```

- 논리 연산자
- || : OR
- && : AND

### 조건문

- if (조건) { 로직 }

```javascript
if (조건){
  //코드
}else if{
  //코드
}else{
  //코드
}
```

## 반목문

### for문

```javascript
for (var i = 0; i < 10; i++) {
  //로직
}
```

## 함수

- 자바스크립트에서는 함수가 중요하다 . 자바스크립트의 꽃이라고 말함.
- 함수는 변수처럼 선언 후 사용 할 수 있다.
- 함수 선언은 선언식, 표현식 두가지 방법이 있다.
  - 표현식이 2가지가 있는 것 이고, 동일하게 함수를 선언해준다.

```javascript
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
// 함수를 변수에 담아서 사용 할 수 있다.
var a = helloFunction();
var b = hiFunction();
```

### 함수의 인자

- 파라미터가 있는 함수
- 함수 파라미터 변수명 문자 + 숫자 형태로 적을 수 있다.

```javascript
//인자값 1개
function calculate(x) {
  var result = 3 * x * 5;
  console.log("결과값  : " + result + "입니다.");
}
var result = calculate(5);

// 인자값 1개, return 사용하기.
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

// 인자값 n개 , return값 n개( object타입으로 반환.)
function getProfile(profileName, profileAge) {
  return { name: profileName, age: profileAge };
}
var profile = getProfile("bapa", 20);
console.log(profile.name, profile.age);
```

- 아래와 같은 구조면 에러가 나야하지만, javascript는 알아서 찾아줘서 에러가 안 난다.
  - 선언은 왠만하면 위에 묶어서 하자. 나중에 에러찾기 어렵다.

```javascript
function getName1() {
  console.log(name1);
}
var name1 = "bapa";
getName();
```
