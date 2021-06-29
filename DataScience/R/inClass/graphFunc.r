workspace = "D:\\workspace\\TIL\\DataScience\\R\\inClass"
setwd(workspace)
setRepositories(ind = c(1:8))
getwd()


install.packages(c('e1071','randomForest','stringr','stringi','sqldf','data.table','plyr','dplyr','hflights'))
install.packages('MASS')
install.packages('RColorBrewer')
install.packages('ggplot2')
install.packages('canvasXpress')


library('e1071')
library('randomForest')
library('stringr')
library('stringi')
library('sqldf')
library('data.table')
library('plyr')
library('dplyr')
library('hflights')
library('MASS')
library('RColorBrewer')
library('ggplot2')
library('canvasXpress')
## Scatter plot
x <- 1:10
y <- rnorm(10)
plot(x,y)
plot(rnorm(100))

title(main = 'Test Graph', xlab = 'index', ylab = 'value')
grid()

# 아래 2개 동일
plot(iris$Sepal.Length, iris$Petal.Width, pch= (as.integer(iris$Species)+1))
with(iris,plot(Sepal.Length,Petal.Width , pch = (as.integer(Species)+1)))
# 범례 추가
plot(iris$Petal.Length, iris$Petal.Width, pch= (as.integer(iris$Species)))
legend(1.5,2.4,unique(iris$Species),pch = c(1,2,3))
title(main = 'Iris-Polt', xlab = 'Petal Length' , ylab=('Petal Width'))

plot(iris[,4])
height <- seq(120,135,3)
grade <- paste0(1:6,'학년')
df <- data.frame(grade,height)

barplot(df$height, names.arg = df$grade)

#임의의 grade를 생성하여 barplot 띄우기!
grade1 <- sample(120:140,100,replace=T)
grade2 <- sample(130:150,100,replace=T)
grade3 <- sample(140:160,100,replace=T)
grade4 <- sample(150:170,100,replace=T)
grade5 <- sample(160:180,100,replace=T)
grade6 <- sample(170:190,100,replace=T)

height <- c(grade1,grade2,grade3,grade4,grade5,grade6)
grade <- rep(1:6, each =100)
df <- data.frame(grade,height)
dt <-df %>% group_by(grade) %>% summarise(height = mean(height)) %>% select(height)
dt <- as.data.frame(dt)
barplot(dt$height ,names.arg =paste0(1:6,'학년'))

#Box Plot
# MASS에서 Cars93 데이터 가져오기
data(Cars93)
boxplot(Cars93$MPG.city)
# breaks : 분할하기
hist(Cars93$MPG.city,breaks=20)

x <- rnorm(10000)
# runif(개수) 개수만큼의 0~1 사이의 난수
x <- runif(1000) 
hist(x, breaks = 30)

#shell명령 cmd명령어이다.
shell('dir')

colors <- c('#FF0000','#FFFF00','#00FF00','#00FFFF','#FF00FF','#0000FF')

pie(rep(1,6), col = colors, lables = colors)
par(new=T)
pie(rep(1,6), col = 'white',radius=0.5,labels='')

diplay.brewer.all(type='seq')
# 편하게 plotting 할 수 있음

# ggplot띄우기
plot(mtcars$wt,mtcars$mpg)
qplot(mtcars$wt,mtcars$mpg)
# ggplot(data, aes(x축,y축))
ggplot(mtcars,aes(x=wt,y=mpg) ) +geom_point()
mtcars %>%  group_by(cyl) %>% summarise(m = mean(mpg)) 
df <- mtcars %>%  group_by(cyl) %>% summarise(m = mean(mpg)) 

barplot(df$m, names.arg=df$cyl)

ggplot(mtcars,aes(x = cyl,y=mpg))+ geom_bar(stat ='identity')

# 아래와 같이 연쇄적으로 삽입할 수 있다.
# 순서는 ggplot만 먼저 나오면 상관 없다
ggplot(mtcars) + geom_point()+
    ggtitle('Test ggplot2') + aes(x=wt,y=mpg)
# 아래와 같이 x 에 삽입하면 위에 처럼 연쇄 작업을 할 수 있다.
x <- ggplot(mtcars)
x + geom_point()+ ggtitle('Test ggplot2') + aes(x=wt,y=mpg)
# 뭔지 모르겠음
# x + theme(panel.grid.major = element_blank())
# x + theme(panel.grid.minor = element_blank())

plot(iris$Sepal.Length, iris$Sepal.Width ,pch = as.integer(iris$Species)) 
ggplot(iris) + ggtitle('Iris-Plot') + geom_point() + aes(x = Sepal.Length,y=Sepal.Width, shape = Species)

iris2 <- data.frame(sl=c(2,3),sw=c(2,4),sp=c('king','queen'))
ToothGrowth

x <- iris[iris$Species == 'setosa', 'Sepal.Length']
y <- iris[iris$Species == 'versicolor', 'Sepal.Length']
z <- iris[iris$Species == 'virginica', 'Sepal.Length']
boxplot(x,y,z)

ggplot(mtcars) + aes(x = mpg) + geom_histogram(bandwidth = 20)

cal_sum <- function(x){
    return(sum(x))    
}
cal_sum(1:10)

x <- c('akf 2lkdaf')
grep('dd', x)
substring(x,1,3)
gsub('2','',x)
strsplit(x,' ')


x <- c('melon2513245pear','apple123413296banana')
# d : digital
y <- str_extract_all(x,'\\D') 
y<- do.call(c,y)
str_c(y,collpase = '')

clean_number <- function(x){
    return(str_c(do.call(c,str_extract_all(x,'\\D') ),collpase = ''))    
}
clean_number('백승현의 전화번호는 01091102413')

paste0(sample(1990:2000,520), sample(111111111111))
regit_number_generator <- function(x){

}

reg_number <- paste0(sample(1990:2020,520, replace =T),'-',sample(1111111:2222222,520))
length(rep(letters,20))
df <- data.frame(name = rep(letters,20),reg_number)
str_replace_all(df$reg_number,'\\d','*')



mail = c('rlagustjr855@naver.com',
'rlagustjr85@gmail.com',
'rlagustjr85@hanmail.net',
'rlagustjr85@nate.com',
'rlagustjr85@korea.ac.kr',
'intern1813@krihs.re.kr',
'yongmi333@naver.com',
'mymlee1@gmail.com',
'1305989354@qq.com',
'ari95@naver.com',
'140121821@pku.edu.cn',
'1305989354@qq.com',
'lym333@kbsi.re.kr')


library(stringr)
str_locate('kangwook.lee@kbu.ac.kr','@')[1]
substring('kangwook.lee@kbu.ac.kr',14,22)
x = 'kangwook.lee@kbu.ac.kr'

mail_check = function(x){
  start = str_locate(x,'@')[1]+1
  end = nchar(x)
  address = substring(x,start,end)
  return(address)
}
df = as.data.frame(do.call(rbind,lapply(mail,mail_check)))

dt <- df %>% group_by(V1) %>% summarise(cnt = n()) 

barplot(dt$cnt,names.arg=dt$V1)
ggplot(dt) + geom_bar(stat='identity') + aes(x=V1,y=cnt)


Summary_Fn <- function(x){
    return(data.frame(names(x),mean(x),min(x) , max(x) ,count(x)))
}
Summary_Fn(rnorm(100))
data.frame ( 컬럼명, Mean, Min, Max, Cnt) 




sample_df <- data.frame(AA = rep(letters[1:5],10), BB = sample(60:70,50,replace  <- T)) 
sample_df[sample_df$AA=='a',]
subset(sample_df,AA =='a')

result_df <- NULL

for (i in 1:nrow(sample_df)){
    if(sample_df[i,"AA"] == "a") {
        tmp = sample_df[i,]
        result_df = rbind(result_df,tmp)
    }
}
result_df

sample_df$CC <- ifelse(sample_df$AA == "a", 1,ifelse(sample_df$AA == "b", 2, 3 )  )

sample_df$DD <- sample_df$BB * sample_df$CC

#아래 n개 동일
sample_df[,c('AA','CC','DD')]
sample_df[,names(sample_df)[c(1,3,4)]]
sample_df[,which(names(sample_df) != 'BB')]
