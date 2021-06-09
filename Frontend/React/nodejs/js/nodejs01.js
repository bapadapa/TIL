console.log("hello javascript");

// 변수
// 변수선언과 정의

var name; // 변수선언
name = "그랩";
var name1 = "그랩";

console.log(name + name1);

let num2 = 20;
console.log(num2);
num2 = "hello";
console.log(num2);

var name; // undefined
nam = "bapa"; // string
var age = 30; //number
var isFool = false; // boolean (true/ false)
var nully = null; // null

//array
var productName = ["커피", "글라인더"]; // array
var productIds = [10, 20];
var productNesArray = [
  [0, 1, 2],
  [3, 4, 5],
];
// array 길이 확인
var length = productName.length;
console.log(length);
//2 출력

var firstValue = productName[0];
var secondValue = productName[1];

console.log(typeof firstValue);
// string 출력

//위치값 (인덱스)으로 삽입하기.
productName[2] = "리시버";
console.log(productName[2]);

//push로 삽입하기.
productName.push("Push리시버");
//productName[push : "PA리시버"];
