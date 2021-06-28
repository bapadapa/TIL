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


## 반복문
vector <- 1:200

s <- 0

for(v in vector){
    if(v%%3 == 0){
        s = s+v
    }
}
s

sum(vector)
vector <- 0:200
s<- 0

# 길이를 가지고 하는 것 이니 1:length(vector) 과 같이
# 범위로 해야한다!
for(i in 1:length(vector)){
    if(vector[i]%%3 == 0){
        s = s+vector[i]
    }
}
s 


# m의 열의 합을 구하시오
m <- matrix(1:100,3) 
# 방법 1
ans <- NULL
for(i in 1:dim(m)[2]){
    ans = c(ans,sum(m[,i]))    
}
ans
# 방법 2
ans <- NULL
for(i in 1:dim(m)[2]){
    ans = cbind(ans,sum(m[,i]))
}
ans

# 1:99 ,3인 메트릭스의 열의 합을구하고
# 3,11의 matrix로 만드시오
m <- matrix(1:99,3) 
ans <- NULL
for (i in 1:dim(m)[2]){
    ans = cbind(ans,sum(m[,i]))
}
tmp <- NULL
result <- NULL
for (i in 1:dim(m)[2]){
    tmp <- rbind(tmp,ans[i])
    if(!i%%3){
        result <- cbind(result,tmp)
        tmp<-NULL
    }
}

m_new <- result
m_new
v = sample(20:40 ,10,replace = F)
sort(v,decreasing = T)
v[order(v)]

names(iris)
iris[order(iris$Sepal.Length),]

a <- sample(1:100 , 100,replace =T)
b <- sample(1:100 , 100,replace =T)
c <- sample(1:100 , 100,replace =T)
d <- sample(1:100 , 100,replace =T)
e <- sample(1:100 , 100,replace =T)

df = data.frame(a,b,c,d,e)
col_name = NULL
for(i in 1:nrow(df)){
    tmp <- names(df)[order(as.matrix(df)[i,])[4]]
    col_name <- c(col_name,tmp)
}

df <- data.frame(df,col_name)
df
df[3,]
df[3,which(names(df) == df[3,"col_name"])]

secondScore <-NULL
for (i in 1:nrow(df)){
    secondScore <- c(secondScore, df[i,which(names(df) == df[i,"col_name"])])
}
secondScore <- data.frame(secondScore)
secondScore


# -------------------------------------------------

m <- matrix(1:99,3)
#방법 1
m_col_sum = NULL
for (i in 0:10){
    tmp1 <- NULL
    for (j in 1:3){
        tmp2 <- sum(m[,i*3+j])
        tmp1 <- c(tmp1,tmp2)
    }
    m_col_sum = cbind(m_col_sum,tmp1)
}
m_col_sum
#방법2
matrix(apply(m,2,sum),3)

##로또~
sample(1:45, 6  , replace = FALSE, prob = NULL)
lotto <- NULL
for( i in 1:6){
    x = sample(1:45, 1, replace = FALSE, prob = NULL)
    if( x == lotto or lotto == NULL){
        lotto <- c(lotto,x)
    }
    
}
lotto
install.packages('sqldf')
library(sqldf)
names()

iris2 <- iris
names(iris2) <- gsub('\\.','_',names(iris2))
# sql 문 바로 넣기
sqldf('select Species,avg(Sepal_Length) from iris2 group by Species')
# stmt변수를 만들어서 사용하기
stmt <- 'select Species,avg(Sepal_Length) from iris2 group by Species'
sqldf(stmt)

stmt <- 'select * from iris2 where Sepal_Length > 0.3'
sqldf(stmt)
x <- c('sepal_length','patal_length','sepal_width')
paste(x,collpase = ',')

unique(iris$Species)

iris_cnt <- NULL
for( i in unique(iris$Species)){
    tmp <- data.frame(species=i,cnt = nrow(iris[iris$Species == i,]))
    iris_cnt <- rbind(iris_cnt,tmp)
}
iris_cnt
sqldf('select species, count(*) as cnt from iris group by species')

iris2[iris2$Sepal_Length > mean(iris2$Sepal_Length),'Sepal_Length']
sqldf('select sepal_length from iris2 where sepal_length > (select avg(sepal_length) from iris2)')
stmt <- 'select species , count(sepal_length) as cnt, sum(sepal_length) as sum , avg(sepal_length) as avg , std(sepal_length) as std from iris2'
sqldf(stmt)
sqldf('select species , count(sepal_length) as cnt, sum(sepal_length) as sum , avg(sepal_length) as avg , std(sepal_length) as std from iris2')


# 모든 칼럼에

install.packages('data.table')
library(data.table)

DF <- data.frame(x = c(rep('b',3),rep('a',2)),v=rnorm(5))
DT <- data.table(x = c(rep('b',3),rep('a',2)),v=rnorm(5))
DT2 <- as.data.table(DF)
class(DT2)

DF2 <- as.data.frame(DT2)
DT[,sd(v),by=a]

DF2[DF2$v>0,]
DT2[v>0,]

iris2 <- iris

DT<- data.table(a = c(rep('b',3),rep('a',2)),v=rnorm(5))
DT <- data.table(a = LETTERS[c(1,1,3)],b=4:7,key='a')
DF <- as.data.frame(DT)
DF <- data.frame(DF,c=8)

# c칼럼에 삽입
DT[,c :=7]
# 칼럼 삭제
DT[,c :=NULL]
# 아래 연산은 동일하다!
DF[DF$a == 'A',]
DT[a=='A',]

# a 가 'A'인 것중 칼럼이 'b','c'인 것들을 추출
# select b,c from DF where a == 'A'
DF[DF$a =='A',c('b','c')]

## 출력 결과 길이
options(sipen = 999999999)

# ceiling 올림
ceiling(3.444)

grpsize <-ceiling(1e7/26^2)
system.time(DF <- data.frame(x = rep(LETTERS,each = 26*grpsize),
                            y = rep(letters,each = grpsize),
                            v = runif(grpsize*26^2),
                            stringAsFactors = F))


## 생성한 변수들 모두 삭제
rm(list = ls())



# 실습 문제 1
# 1. iris 데이터를 data.table 형식으로 변경하라.
# 2. data.table형식으로 바꾼 iris데이터에서 컬럼 Species를 키값으로 정의하라
# 3. 컬럼 Species내의 값에서 setosa인 값을 추출하여 새로운 data.table를 생성하라.
# (생성된 data.table내의 컬럼은 Sepal.Length, Petal.Length, Species 컬럼만 존재)
irisDT <- as.data.table(iris)
setkey(irisDT,Species)
tables()
irisDT2 <- irisDT[Species == 'setosa',list(Sepal.Length, Petal.Length, Species)]
irisDT2

DT <- as.data.table(DF)
setkey(DT,x,y)
# aggregate사용 sum()
tt <- system.time(sum_DF <- aggregate(DF$v, by = list(DF$x),sum))
sum_DF
# select sum(x) from DT group by x
ss <- system.time(sum_DF <- DT[,sum(v),by = x])
head(sum_DF)

tt/ss

# iris데이터를 종별로 speal.length의 합
# Sepal.Length Sepal.Width Petal.Length Petal.Width   Species
irisDT <- as.data.table(iris)
names(irisDT) = gsub('\\.','_',names(irisDT))
sl <- irisDT[,sd(Sepal_Length),by = Species]
sl <- aggregate(iris[1:4],by = list(irisDT$Species),sum)
sqldf('select species, sum(sepal_length) from irisDT group by species')
irisDT[,list(sum(Sepal_Length),mean(Sepal_Length)),by = Species]

sl


# 실습 문제 2
# 1. iris 데이터를 data.table 형식으로 변경하여 Species 컬럼 기준으로 Sepal.Length컬럼 값에
# 대하여 기초통계량(평균, 최대값, 최소값, 중앙값) 값을 구하라

irisDT <- as.data.table(iris)
names(irisDT) = gsub('\\.','_',names(irisDT))
# ver.01
irisDT[,list(mean(Sepal_Length),max(Sepal_Length),min(Sepal_Length),median(Sepal_Length)),by = Species]
# ver.02
sqldf('select species,avg(Sepal_Length) as mean,max(Sepal_Length) as max,min(Sepal_Length) as min,median(Sepal_Length) as median from irisDT group by Species')

DF_1 <- data.frame(AA = letters[1:5], BB = rnorm(5))
DF_2 <- data.frame(AA = letters[1:10], CC = c(1:10))
DF_3 <- data.frame(EE = LETTERS[1:5], DD = sample(1:100, 5))
DF_4 <- data.frame(AA = letters[6:8], BB = rnorm(3))

DT_1 <- as.data.table(DF_1)
DT_2 <- as.data.table(DF_2)
DT_3 <- as.data.table(DF_3)
DT_4 <- as.data.table(DF_4)

# DF_1 , DF_3 옆으로 붙이기
cbind(DF_1,DF_3)
cbind(DT_1,DT_3)
# DF_1 , DF_4 아래로 붙이기
rbind(DF_1,DF_4)
rbind(DT_1,DT_4)

merge(DT_1,DT_2, by = 'AA', all.x=T)
merge(DT_1,DT_2,all.x=T)

setkey(DT_1,AA)
setkey(DT_2,AA)
# 키값 기준 merge
merge(DT_1,DT_2)

# 키값 삭제
# setkey(DT_1,NULL)

#실습 문제 3
# 1. data.table로 변경된 iris데이터를 가지고 Species 컬럼내의 값 기준으로 
#    그룹하여 Sepal.Length 컬럼의 요약통계량을 구하여라.(평균, 최대값, 최소값)
# 2. data.table로 변경된 iris데이터와 요약통계량값과 결합하여 새로운 data.table을 생성하라.

irisDT <- as.data.table(iris)
summeryIris <-irisDT[,list(mean(Sepal.Length),max(Sepal.Length),min(Sepal.Length)),by = Species]

merge(irisDT,summeryIris,by ='Species')
merge(irisDT,summeryIris)

# 데이터를 분할하고, 분할된 데이터에 특정 함수를 적용하여 데이터를 분석 및 처리한 후 
# 그 결과를 재조함 하는 세 단계로 진행하는 함수를 제공한다.
install.packages('plyr')
library(plyr)

# adply : 함수는 행렬 배열 또는 데이터 프레임을 받아 데이터 프레임을 반환하는 함수이다.
#형식 : adply(data,margins,fun)
adply(iris[,1:4],1,function(x){data.frame(Mean = rowMeans(x))})

# ddply : 데이터 프레임을 받아 데이터 프레임을 반환하는 함수이다.
# 형식 : ddply( data, variables, fun)
ddply(iris,.(Species),function(x){data.frame(Mean1 = mean(x$Sepal.Length))})

# mdply : 데이터 프레임 또는 배열을 받아 데이터 프레임을 반환하는 함수이다.
# 형식 : mdply( data, fun)
x_df <- data.frame(m = 1:5, sd = 1:5)
x_df
mdply(x_df,rnorm,n =3)

data.frame(species=unique(iris$Species),max_length = c(10,20,30))
aggregate(iris$Sepal.Length, by = list(iris$Species),max)
aggregate(iris$Sepal.Length, by = list(iris$Species),min)
aggregate(iris$Sepal.Length, by = list(iris$Species),mean) 

ddply(iris, .(Species),function(x){data.frame(me=mean(x$Sepal.Length),mi=min(x$Sepal.Length),ma=max(x$Sepal.Length))})


install.packages('dplyr')
library('dplyr')

# 아래 2개는 동일함
filter(iris,Species == 'setosa' & Sepal.Length ==5.1)
# 파이프 연산
iris %>% filter(Species == 'setosa' & Sepal.Length ==5.1)
# data.table에도 동일하게 연산 가능
irisDT <- data.table(iris)
filter(irisDT,Species == 'setosa' & Sepal.Length ==5.1)

# 데이터가 많은 라이브러리라고함
install.packages('hflights')
library('hflights')

names(hflights)
# arrange : 데이터를 정렬하는 기능을 제공한다
# 형식 : arrange(data, 정렬할 컬럼명)
system.time(order(hflights$Year,hflights$Month,hflights$DayOfWeek,hflights$ActualElapsedTime))
system.time(arrange(hflights, Year,Month,DayOfWeek,ActualElapsedTime))

# select  : 사용자가 원하는 컬럼을 추출할 때 사용한다.
# 형식 : select(data, 추출할 컬럼명)
# 컬럼명 앞에 (-)를 입력하면 입력한 컬럼명을 제외한 나머지 컬럼을 추출한다.
iris[,c("Sepal.Length", 'Sepal.Width')]
select(iris,  -(Sepal.Length:Sepal.Width))

# mutate : 열을 추가하는 기능을 제공한다.
# 형식 : mutate(data, 추가할컬럼명)
mutate(iris, New1 = Sepal.Length - mean(Sepal.Length))

mutate(iris,New1 = mean(Sepal.Length),New2 = New1 - Sepal.Length)

#SQL사용하기
library(sqldf)
irisSql <- as.data.table(iris)
names(irisSql) = gsub('\\.','_',names(irisSql))
stmt <- 'select * , (select avg(Sepal_Length) from irisSql)as avg from irisSql'
stmt <- 'select sepal_length - sepal_width as minus from irisSql'
# 아래 2개 동일
stmt <- 'select * , (select avg(Sepal_Length) from irisSql)as new1, (select avg(Sepal_Length) from irisSql) - Sepal_Length as new2 from irisSql'
stmt <- 'select a.* ,a.new1 - sepal_length as new2 from (select a.* ,(select avg(sepal_length) from irisSql) as new1 from irisSql a) a'
sqldf(stmt)


iris %>% group_by(Species) %>% summarise(s = sum(Sepal.Width), m = mean(Sepal.Width),sd = sd(Sepal.Length)) %>% select(s,m,sd,Species)
summarise(group_by(iris,), zMean =mean(Sepal.Length), Sum = sum(Sepal.Length))
names(iris)

# 아래 2개 동일
filter(iris,Sepal.Length > mean (Sepal.Length))
iris %>% filter(Sepal.Length >  mean(Sepal.Length))
# 아래 2개 동일
select(iris,Sepal.Length,Petal.Width)
iris %>% select(Sepal.Length, Petal.Width)

mutate(iris,new = mean(Sepal.Length))
arrange(iris,Sepal.Length)
summarise(group_by(iris,Species),m=mean(Sepal.Length))


# 아래 2개 동일
iris[order(iris[iris$Sepal.Length > mean(iris$Sepal.Length),'Sepal.Length']),c('Species','Sepal.Length')]
iris %>% filter(Sepal.Length >  mean(Sepal.Length)) %>% arrange(Sepal.Length) %>% select(Species,Sepal.Length)

#Setosa인 것만 뽑아서 Sepal.Length의 평균과 
#   Sepal.Length와 Sepal.Length의 값을 차이를 보이시오

iris %>% filter(Species =='setosa' | Species == 'versicolor') %>% select(Species, Sepal.Length)


##실습 문제 1
#   chain()함수를 활용하여 다음과 같은 순서로 hflights패키지에 내장되어진 데이터 
#      hflights를 가지고 그룹별 평균값을 구하라
#   1. filter함수를 사용하여 Month 컬럼의 값이 1부터 3월까지 값을 추출
#   2. hflights데이터에서 컬럼 Year, Month, ArrDelay, DepDelay컬럼 추출
#   3. group_by함수를 사용하여 그룹정의를 Year, Month로 정의
#   4. summarise함수를 사용하여 ArrDelay와 DepDelay 각각 평균값을 구하라
names(hflights)
dt <- hflights


hflights %>% 
filter(Month < 4) %>% 
select(Year, Month, ArrDelay, DepDelay) %>% 
group_by(Year,Month) %>% 
summarise(arr = mean(ArrDelay,na.rm =T) , dep = mean(DepDelay,na.rm =T))

sqldf('select Year,Month, avg(ArrDelay),avg(DepDelay) from hflights  where Month < 4 group by Year,Month')
# apply : 모든 값에 적용시키기
# 형식 : apply(input : array,margin, output : array)
apply(matrix(1:33,3),1,function(x){2*x})
apply(matrix(1:33,3),1,sum)
apply(matrix(1:33,3),1,max)

# lapply : 
#형식 lapply(input : list or vector, Output : list)
lapply(1:3, function(x) x*2)

minMax <- function(x){(x-min(x))/max(x)-min(x)}

minMax(sample(2:30,12))
l <- lapply(1:3, function(x) x*2)
# do.call(func,l)
# l 을 func으로 묶는다.
do.call(data.table,l)

# sapply : 조건을
# 형식 : sapply(list : list or vector, output : vector or array)

sapply(iris[,1:4],function(x) {x>3})

# vapply  
# 형식 : vapply(list : list or vector, output : vector or array)
vapply(iris[,1:4],function(x) {x>3} , numeric(length(iris[,1])))

#tapply
# 형식 : tapply(list : list or vector and factor, output : vector or array)
tapply(1:10, rep(c(1,2),each= 5),sum)
tapply(iris$Sepal.Length, iris$Species, sum)

#mapply
# 형식 : mapply(list or vecotr, output : vector or array)
mapply(`+`,iris$Sepal.Length,iris$Sepal.Width)
mapply(function(i,s) { sprintf("%d%s",i,s)} , 1:3 ,  c('a','b','c'))
mapply(function(x,y){x*y},1:4,5:8)

x <- sample(letters,100,replace = T)

