workspace = "D:\\workspace\\TIL\\DataScience\\R\\inClass"
setwd(workspace)
getwd()

## which server you wanna use
setRepositories(ind = c(1:8))
install.packages('matrixStats')
library('matrixStats')

# 간단하게 벡터 생성하기!
#아래 2개는 동일한 의미! (R에선 <- 를 권장함)
i = 0
i <- 0`
i
## Vector 만들기!
# c() : concatenate
c(c(dir() , 'sh',dir()))
# 연속값
# 시작 : 끝
c(1:10 , 11:20)
c(1:10 , 11:20) +3 #벡터 연산 (BroadCast)이된다!
# 반복
#rep (var,time)
rep(3,6)
# c()로 반복하기
rep(c(3:5),3, )
# seq(var,time,step)
seq(10,100,5)
((1:20)*5)

x <- ((1:7)*10)
x[3:4] <- 100
x[3:4] <- c(50,60)
x
?rep

mat <- c(1:5) c(1:5)*100
letters= c(    'a',   'b',    'c',    'd',    'e')
# 행 붙이기
mat <- rbind(letters[1:5],c(1:5)*100)
mat
mat2 <- matrix(c(1:10), 5,2 ,byrow = T)
length(mat2) #전체 크기
dim(mat2) # 차원
head(mat2) # 앞 (default = 10개)
tail(mat2) # 뒤 (default = 10개)
str(mat2)
## Hetrogeneous
li <- list(c(1:10),matrix(1:10,2))
class(li) # list
class(li[0]) #list
class(li[[1]]) # Integer
class(li[[2]]) # "matrix" "array"

li[[1]][2:7]
#데이터 확인
is.data.frame(li)
#데이터 변경
# as.자료형.(대상)
# as.vector.(값(변수))

## Homogeneous

# data.frame : 데이터 분석시 가장 많이 사용하는 데이터 객체.

id <- c('A001','A002','A003','A004','A005');id
gender <- c('F','F','F','M','M')
wei <- c(58,60,63,68,70)
hei <- c(155,160,165,170,175)
age <- c(23,24,38,43,40)
dataf01 <- data.frame(id,gender,wei,hei,age); 
dataf01

df01 <- data.frame(weight = wei,height= hei,age)
df01
# 속성값 확인 -> 상세 정보
attributes(df01)

dim(df01)[1]
nrow(df01)
length(df01)

# 칼럼 명 병경
names(df01) <- paste0(names(df01),'_1')

is.vector(df01[,3])
class(df01[,3])

df01[,c('weight_1','age_1')]
df01$weight_1
bmi <- wei/hei
df01 <- data.frame(id,gender,weight = wei,height= hei,age); 
df01 <- cbind(df01,bmi)
names(df01) <- paste0(names(df01),'_1')
df01

rbind(df01,data.frame(  id_1 = 'A006', gender_1 = 'M', weight_1=50 ,height_1=170, age_1=30 ,bmi_1 = 50/170))

# 환경설정
getwd()

df <- data.frame(a = c(1,2,3,4))
write.csv(iris, file = "data.csv", append = FALSE, quote = TRUE, sep = ",")
df2 <- data.frame(iris[,1])
df2 
df1


c(T,T,F,F) & c(T,F,T,F)
c(T,T,F,F) | c(T,F,T,F)

a <- 3
4 -> b
a
b
# 변수 목록
ls()
# 변수 삭제
rm('b')
# 여러개 삭제
rm(list = c('bmi','a'))
x <- c(3:7)

sum(x)/length(x)
mean(x)
max(x)
min(x)
range(x)[2] == max(x)
range(x)[1] == min(x)
# var = sd^2
sd(x)
var(x)
# VAR 공식
sqrt(sum((x-mean(x))^2)/(length(x)-1))

# 패키지 설치
install.packages('dplyr')
install.packages(c('e1071','randomForest','stringr','stringi'))

#패키지 사용
library(dplyr)
library(e1071)
library(randomForest)
library(stringr)
library(stringi)

# 메모리에 로드된 패키지 목록
search()

data()
names(swiss)
#값 확인
View(swiss)
# 값 변경
swiss1 <- edit(swiss)
head(swiss)

data(package = "MASS")
# Factor 생성
iris2 <-iris
x <- iris2$Species
class(x)

x <- as.character(x)
class(x)
x <- c(x,'k')

df <- read.csv('./Data/data_2.csv')

eng <- sample(50, 100,10 )
math <- sample(50, 100,10)
sci <- sample(50, 100,10 )
kor <- sample(50, 100,10 )
# 1~100번째 값 추출!
eng[c(1:100)]
# 3번째 값만 100번 추출!
eng[rep(3,100)]
# 평균보다 큰 값만 추출
eng[eng>mean(eng)]


eng[-which(eng>max(eng))]
-which(eng<max(eng))

subset(eng,eng > mean(eng))
df = data.frame(id,eng,math,sci,kor)
rowSums(df[,2:length(df)])
df <- data.frame(df,total=rowSums(df[,2:length(df)]))
df[,2:(length(df)-1)]
# 아래 2개는 동일하다!
avg = apply(df[,2:(length(df)-1)], 1, mean)
rowMeans(df[,2:(length(df)-1)])
avg
df <- data.frame(df,avg)

## 평균이 가장 높은 사람의 영어성적과 수학 성적의 차이
abs(df[df$avg ==max(df$avg),]$eng - df[df$avg ==max(df$avg),]$math)
abs(subset(df,df$avg ==max(df$avg))$eng - subset(df,df$avg ==max(df$avg))$math)
## 평균이 가장 낮은 사람의 영어성적과 영어 성적 평균의 차이는 표준편차와 몇배 차이나는가?
sd(df$eng)/df[min(df$avg) == df$avg,]$eng


summary(df$eng)
str(df)

## 각 과목별에서 median값과 mean 값의 차이가 
## 가장 많이 나는 과목의 가장 점수가 높은 사람의 평균과 전체 평균을 구하시오
summary(df[,2:(length(df)-2)])[3,]
summary(df[,2:(length(df)-2)])[4,]
?rowMeans

## if 문
x <- sample(20:30,10)
if(25 > x){
    print(x)
}else{
    print('No')
}

# 두 변수를 랜덤하게 만들어 앞의 변수가 크면 '크다' , 뒤에 변수가 크면 '작다'를 출력하시오

x <- sample(1:10,1)
y <- sample(1:10,1)

if(x > y){
    print('크다')
}else{
    print('작다')
}

#  for 문을 이용해 data= sample(10,20,30) 의 홀수값은 더하고 짝수는 뺀 값의 결과
data= sample(10,20,30)
sum <- 0
for (i in length(data)){
    sum <- sum+ ifelse(i %% 2 == 0,data[i],-data[i])
}
