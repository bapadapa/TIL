workspace = "E:\\GoogleDrive\\SeungHyuen\\Korea_uni\\Class\\4-2\\ClassMeterials\\Convergence_Infomatics\\R_workspace"
setwd(workspace)
##getwd()

## which server you wanna use
setRepositories( ind = 1:8 )

## install "gglplot2" package
## download package
install.packages("ggplot2")
## set package // include, using ....
library(ggplot2)


A <- 1 
B <- 2
C <- 3

numericVector <-c(1,2,3,4,5)
numericVector

class(numericVector)

charVector <- c("One" , "Two" , "Three" , "Four"  , "Five")
class(charVector)

## TRUE,T / FASLE,F  로만 사용 가능.. t,f 는 사용 불가.
logicalVector <-c(TRUE,FALSE,T,F,F)
class(logicalVector)


data(iris)
iris

fix(iris)

## 현재 사용중인 Objects들 확인 할 수있음.
ls()


## 클래스(변수) 자료형 확인.
class(logicalVector)


## str != string , str == structure
str(iris)


## 한개의 벡터를 Data Frane 으로 묶을 수 있다.
## 이때 벡터의 갯수는 통일 시켜야한다.
exampleData <- data.frame(numericVector,charVector,logicalVector)
exampleData


## row(행) 갯수 == Data, element 갯수
nrow(exampleData)
## col(열) 갯수 == vector 갯수.
ncol(exampleData)

## 다른 프로그램은 배열등의 데이터가 0부터 시작하는 반면
## R은 1부터 시작한다..
## exampleData 의 구성은 아래와 같다.
## 이떄 one을 찾고싶다면, 1,2로 찾아야한다.
##
#    numericVector charVector logicalVector
# 1             1        One          TRUE
# 2             2        Two         FALSE
# 3             3      Three          TRUE
# 4             4       Four         FALSE
# 5             5       Five         FALSE
 
##exampleData[1,2]
# > exampleData[1,2]
# [1] "One"

## head , tail은 시작과 끝 기준으로 출력해주는 역할을 한다.
head(exampleData,2)
tail(exampleData,2)

     











