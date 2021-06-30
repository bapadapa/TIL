v <- c('a','ab')
v <- c(v,1)

mean(c(1,2,3))
max(1:3)
min(1:3)
range(1:3)
string <- 'I love R and Python'
length(v)
nchar(string)
paste(string,'.',sep='',collapse=',')

#install.packages('ggplot2')
library(ggplot2)
require(ggplot2)
x <- c('a','a','b','c')
mtcars
mpg
qplot(data=mpg,x=hwy)
qplot(data=mpg,x=drv,y=hwy,geom='line')
qplot(data=mpg,x=drv,y=hwy,geom='boxplot')
help(qplot)

##q1
score <- c(80,60,70,50,90)
##q2
mean(score)
##q3
total_mean <- mean(score)
total_mean


library(sqldf)

x = sqldf('select a.* from iris a, iris b')

nrow(iris)
nrow(x)

name <- c('김지훈','이유진','박동현','김민지')
english<- c(90,80,60,70)
math <- c(50,60,100,20)

df_middterm <- data.frame(name,english,math)

class <- c(1,1,2,2)

df_middterm[,'class'] = class

df_middterm$class <- class

df_middterm <- data.frame(df_middterm,class)

df_middterm <- cbind(df_middterm,class)



mean(df_middterm$english)
mean(df_middterm[,'math'])

##data.frame(),c()
df <- data.frame(제품 = c('사과','딸기','수박'),
가격 = c(1800,1500,3000),
판매량 = c(24,38,13))
mean(df$가격)
mean(df$판매량)

install.packages('readxl')
library(readxl)
df_exam <- read_excel('excel_exam.xlsx')

saveRDS(df_exam,'df_exam.rds')
str(df_exam)
dir()
rm(df_exam)
df_exam <- readRDS('df_exam.rds')

View(df_exam$math)
summary(df_exam)

dim(df_exam)

c(nrow(df_exam),length(df_exam))

head(df_exam,1)

class(mpg)

as.data.frame(ggplot2::mpg)

dim(mpg)
head(mpg)
tail(mpg)
names(mpg)
str(mpg)
help(mpg)
summary(mpg)

names(iris) <- gsub('\\.','_',names(iris))
library(dplyr)

df_new <- data.frame(var1 = c(1,2,3),var2=c(2,3,2))
df_new <- rename(df_new,v2 =var2)

as.data.frame(ggplot2::mpg)

df <- data.frame(var1=c(4,3,8),
                 var2=c(2,6,1))
df$var_sum <- df$var1 + df$var2
df$var_sum <- NULL

df$var_sum <- rowSums(df)
df$var_sum <- NULL

df <- df %>% mutate(var_sum=df$var2+df$var1)

mpg$total <- (mpg$cty+mpg$hwy)/2
summary(mpg$total)

library(sqldf)
boxplot(mpg$total)
hist(mpg$total)

mpg[mpg$total >= median(mpg$total),'test'] <- 'pass'
mpg[mpg$total < median(mpg$total),'test'] <- 'fail'

mpg$test <- NULL
mpg$test = ifelse(mpg$total >= median(mpg$total),'pass','fail')

mpg <- mpg %>% mutate(test = ifelse(mpg$total >= median(mpg$total),'pass','fail'))

mpg$class
## 자동차 중에서 클래스가 가장 많은 것

dt <- mpg %>% group_by(class) %>% summarise(cnt = n()) %>%
  arrange(desc(cnt))

barplot(dt$cnt,names.arg=dt$class)


table(mpg$test)


mpg %>% group_by(test) %>% summarise(cnt = n())

qplot(mpg$test)

mpg$grade <- ifelse(mpg$total >= 30,'A',
       ifelse(mpg$total >= 20,'B','c'))

table(mpg$grade)

qplot(mpg$grade)

midwest

data.table(ggplot2::midwest)

midwest <- rename(midwest,
                  total=poptotal,
                  asian = popasian)

names(midwest)

midwest$totalperasian <- (midwest$asian/midwest$total)*100

names(midwest)

midwest$state

hist(midwest$state)

dt <- midwest %>% group_by(state) %>% summarise(cnt = n())

barplot(dt$cnt,names.arg=dt$state)

midwest$scale = ifelse(midwest$totalperasian >mean(midwest$totalperasian),
                       'large','small')

table(midwest$scale)

dt <- midwest %>% group_by(scale) %>% summarise(cnt = n())

barplot(dt$cnt,names.arg=(dt$scale))



library(readxl)
df_exam <- read_excel('excel_exam.xlsx')
head(df_exam)

df_exam.class.unique()

unique(df_exam$class)

df_exam[df_exam$class !='1',]

df_exam %>% filter(class == 1)

df_exam %>% filter(class == 1 & math >= 50)

df_exam %>% filter(class == 1 | math >= 50)

df_exam %>% filter(class == 1 | class == 2 | class == 3)

class_123 <- df_exam %>% filter(class %in% c(1,2,3))


# %/% 몫
 
# %% 나머지
# %in%

displ_4 <- mpg[mpg$displ <= 4,'hwy']
displ_5 <- mpg[mpg$displ >= 5,'hwy']

mean(displ_4$hwy)
mean(displ_5$hwy)

displ_4 <- mpg %>% filter(displ <= 4) %>% mutate(m = mean(hwy))
displ_5 <- mpg %>% filter(displ >= 5) %>% mutate(m = mean(hwy))

names(mpg)

mpg %>% group_by(manufacturer) %>%
  summarise(m = mean(cty)) %>%
  filter(manufacturer %in% c('audi','toyota'))

mpg %>% filter(manufacturer %in% c('chevrolet','ford','honda')) %>%
  group_by(manufacturer) %>% summarise(m = mean(hwy))


df_exam %>% select(class, math, english)

df_exam %>% head

mpg %>% filter(class %in% c('suv','compact')) %>%
  group_by(class) %>% summarise(m = mean(cty)) %>%
  arrange(m)

new_mpg <- mpg %>% filter(manufacturer == 'audi') %>%
  arrange(desc(hwy))

head(new_mpg$model,5)

df_exam <- df_exam %>%
  mutate(total = math+english+science)
df_exam$total <- NULL
df_exam$mean <- NULL
df_exam <- df_exam %>%
  mutate(total = math+english+science,
         avg = total/3,
         test = ifelse(avg>50,'pass','fail'))

df_exam

new_mpg <- mpg %>% mutate(total=hwy+cty)

new_mpg$avg <- new_mpg %>% mutate(avg=total/2)


new_mpg %>% arrange(desc(avg)) %>%
  select(model,avg) %>%
  head(2)


mpg %>% mutate(avg = (hwy+cty)/2) %>%
  arrange(desc(avg)) %>% select(model,avg) %>% head(3)

df_exam %>% summarise(m=mean(math))

df_exam %>% group_by(class) %>%
  summarise(class_mean=mean(math))

mpg %>% group_by(manufacturer,drv) %>%
  summarise(mean = mean(cty)) %>% names %>% length


df_exam


df_exam1 <- df_exam %>% select(id,class,math)
df_exam2 <- df_exam %>% select(id,class,english,science)


left_join(df_exam1,df_exam2)

df_exam3 <- df_exam1[1:10,]

left_join(df_exam3,df_exam2)
df_exam3[1,2] <- 2
left_join(df_exam3,df_exam2)
left_join(df_exam2,df_exam3)


fl = sort(unique(mpg$fl))
price_fl = c(2.35,2.38,2.11,2.76,2.22)
fuel = data.frame(fl,price_fl)
new_mpg = left_join(mpg,fuel,by='fl')

new_mpg$price_fl

new_mpg %>% select(fl,price_fl) %>% head(5)

midwest <- midwest %>% mutate(popminor = (1-popadults/total)*100)

midwest %>% arrange(desc(popminor)) %>%
  select(county,popminor) %>% head(5)

midwest %>%
  mutate(grade = ifelse(popminor >= 40,'large',
                                  ifelse(popminor >=30,
                                         'middle','small'))) %>%
  group_by(county,grade) %>%
  summarise(cnt = n())

df = data.frame(gender = c('M','F',NA,'M','F'),
                score = c(5,4,3,4,NA))


table(!is.na(df))

table(is.na(df$gender))

df[!is.na(df$gender) & !is.na(df$score),]

cl_df <- df %>% filter(!is.na(score) & !is.na(gender))

na.omit(df)
df_exam[c(3,8,15),'math'] <- NA


sum(is.na(df_exam))

apply(is.na(df_exam),2,sum)

df_exam[is.na(df_exam$math),'math'] <- mean(df_exam$math,na.rm=T)


df_exam$math <- df_exam %>% mutate(new_math = ifelse(is.na(math),mean(math,na.rm=T),math)) %>%
  select(new_math)

sum(is.na(df_exam$math))


x <- sample(1:200,200,replace=T)

x <- c(x,1000)

boxplot(x)


x[x > mean(x) + 1.5*sd(x) | x <mean(x) - 1.5*sd(x)]

x[x > mean(x) + 1.5*sd(x)] <- mean(x) + 1.5*sd(x)
x[x > mean(x) - 1.5*sd(x)] <- mean(x) - 1.5*sd(x)

x = ifelse(x >mean(x) + 1.5*sd(x),mean(x) + 1.5*sd(x),
       ifelse(x < mean(x) - 1.5*sd(x),mean(x) - 1.5*sd(x),x))

boxplot(mpg$hwy)

install.packages('foreign')

library(foreign)

shell('dir')

raw_wellfare <- read.spss(file = 'Koweps_hpc10_2015_beta1.sav',
                          to.data.frame = T)

wellfare <- raw_wellfare


head(wellfare)
tail(wellfare)
dim(wellfare)
names(wellfare)
str(wellfare)

apply(is.na(wellfare),2,sum)

welfare <- rename(wellfare, gender = h10_g3,
                  birth = h10_g4,
                  marriage = h10_g10,
                  religion = h10_g11,
                  income = p1002_8aq1,
                  code_job = h10_eco9,
                  code_region = h10_reg7)


welfare <- welfare %>%
  select(gender,birth,marriage,religion,income,
         code_job,code_region)

apply(is.na(welfare),2,sum)

welfare_gender_income <- welfare %>%
  filter(!is.na(income)) %>% select(gender,income)


qplot(welfare_gender_income$gender)


hist(welfare_gender_income$income)

dt <- welfare_gender_income %>%  
  group_by(gender) %>% summarise(m = mean(income))

barplot(dt$m,names.arg=dt$gender)


names(welfare)



code_job <- read_excel('Koweps_Codebook.xlsx',sheet=2)
welfare[is.na(welfare$code_job),'code_job'] <- 9999

welfare <- left_join(welfare,code_job,by='code_job')

welfare[welfare$code_job==9999,'income'] <- 0

sum(is.na(welfare[welfare$code_job==9999,'income']))


welfare[is.na(welfare$income),'job']


missing_df <- welfare %>% group_by(code_job) %>%
  summarise(m=mean(income,na.rm=T))

welfare <- left_join(welfare,missing_df)

welfare <- welfare %>% mutate(incomes = ifelse(is.na(income),m,income)) %>%
  select(gender,birth,marriage,code_job,job,religion,incomes,
         code_region)

apply(is.na(welfare),2,sum)

View(welfare[is.na(welfare$incomes),])


welfare <- na.omit(welfare)

sum(is.na(welfare))

welfare %>%
  filter(code_job != 9999) %>%
  group_by(gender) %>%
  summarise(m = mean(incomes))