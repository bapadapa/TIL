setRepositories(ind = c(1:8))
#install.packages(c("tidyverse","datarium","caret","dplyr","rpart","rpart.plot","kknn"))
#install.packages("e1071")
library(tidyverse)
library(datarium) # for data
library(caret) # for cross-validation algorithms
library(dplyr)
library(rpart)
library(rpart.plot)
library(kknn)
library(data.table)
library(e1071)
library(caret)


## Set Working Dir.
workspace = "E:/GoogleDrive/SeungHyuen/Korea_uni/Class/4-2/ClassMeterials/Convergence_Infomatics/Homework/Homework3"
setwd(workspace)
getwd()

trainSet <- data.frame(fread("TrainSet.txt" , head = T, stringsAsFactors = T))
testSet  <- data.frame(fread("TestSet.txt" , head = T, stringsAsFactors = T))

############
# [Step 1] #
############

dataCleansing <- function(data){
  cleanData <- data%>%
    select(-"ID") %>% 
    mutate(Gender = factor(Gender, levels = c(1, 2), labels = c('Male', 'Female')), 
           Race = factor(Race, levels = c(1, 2), labels = c('White', 'Black')),
           HaveCough = factor(HaveCough, levels = c(1, 0), labels = c('Yes', 'No'))) %>%
    na.omit()
  
  return(cleanData)
}

## Generating function
create_train_test <- function(data, size = 0.8, train = TRUE) {
  n_row <- nrow(data)
  total_row <- size * n_row
  train_sample <- 1:total_row
  if (train == TRUE) {
    return (data[train_sample, ])
  } else {
    return (data[-train_sample, ])
  }
}

# 인덱스 나누기.
dtTrain <- create_train_test(dataCleansing(trainSet),0.6,train=TRUE)
dtTest <- create_train_test(dataCleansing(trainSet),0.6,train = FALSE)

fix(dtModel)

dtModel <- rpart(Disease~., data = dtTrain,method = "class")
rpart.plot(dtModel)

dtPredictResult <- predict(dtModel,dtTest,type = "class")

confusionMatrix(dtPredictResult,dtTest$Disease)

confusion<- table(dtTest$Disease,dtPredictResult)
confusion

############                                                                                                                                                     
# [Step 3] #
############

dtData <- dataCleansing(testSet)
dtDataPredict <- predict(dtModel,dtData,type = "class")

# I will save at bottom
#write.csv(dtDataPredict,"dtDataPredict.csv")


#### KNN Function #####################################################################
myKnnConfusionMatrix <- function(trainData, nn){
  knnTrain <- create_train_test(dataCleansing(trainData),0.7,train=TRUE)
  knnTest <- create_train_test(dataCleansing(trainData),0.7,train = FALSE)
  
  knnModel <-  kknn(Disease~., train = knnTrain, test = knnTest,k = nn)
  return(confusionMatrix(fitted(knnModel),knnTest$Disease)) 
  
}

############
# [Step 4] #
############

 myKnnConfusionMatrix(trainSet, 7)
 
############
# [Step 5] #
############

myKnnConfusionMatrix(trainSet, 5)

############
# [Step 6] #
############

myKnnConfusionMatrix(trainSet, 3)

############
# [Step 7] #
############
myKnn <- function(trainData, testData, nn){
  ID <- testData$ID  
  
  knnTrain <- trainData
  knnTrain <- dataCleansing(knnTrain)
  
  knnTest <- dataCleansing(testData)
  knnTest[,"Disease"] <- c(rep("",nrow(knnTest)))
  
  knnDF <- structure(list(character()),class = "data.frame")
  for(i in nn){
    knnModel <- kknn(Disease~., train = knnTrain, test = knnTest, k=i)  
    data <- knnModel$fitted.values
    data <- gsub('1L','COVID19',data[])
    data <- gsub('2L','Healthy',data[])
    knnDF <- rbind(knnDF,data) 
  }
  
  knnDF <- t(knnDF)
  rownames(knnDF) <- ID
  colnames(knnDF) <- nn
  return(knnDF)
}

# I will save at bottom
# write.csv(myKnn(trainSet,testSet,c(7,5,3)),"KnnPredict.csv")

# myKnn(trainSet,testSet,c(1,2,3,4,5,6,7,8,9,10))


############
# [Step 9] #
############

dtData <- dataCleansing(testSet)
dtDataPredict <- predict(dtModel,dtData,type = "class")
dtDataPredict <- as.data.frame(dtDataPredict)

combinedData <- dtDataPredict

combinedData <- cbind(combinedData , myKnn(trainSet,testSet,c(7,5,3)))


fix(combinedData)  



##Code for Finanl predicted value##
#Cleansing Myself
tModel<- as.data.frame(trainSet[,12:14])
FEV1_FVC <- tModel$FEV1/tModel$FVC
tModel <- cbind(FEV1_FVC , tModel)
tTrain <- create_train_test(tModel,0.6,train=TRUE)
tTest <- create_train_test(tModel,0.6,train = FALSE)

#TestSet Cleansing
realTest<- as.data.frame(testSet[,12:13])
FEV1_FVC <- realTest$FEV1/realTest$FVC
realTest <- cbind(FEV1_FVC , realTest)
realTest[,"Disease"] <- c(rep("",nrow(testSet)))

#Desition Tree
tDTModel <- rpart(Disease~., data = tTrain,method = "class")
#rpart.plot(tDTModel)
tDTModelPredictResult <- predict(tDTModel,tTest,type = "class")

#for accuracy check
confusionMatrix(tDTModelPredictResult,tTest$Disease)

##Apply on Real Data
desitionTree <- predict(tDTModel,realTest,type = "class")
desitionTree <- as.data.frame(desitionTree)
#fix(desitionTree)




#for accuracy check
myKnnConfusion <- function(trainData, nn){
  knnTrain <- create_train_test(trainData,0.7,train=TRUE)
  knnTest <- create_train_test(trainData,0.7,train = FALSE)
  knnModel <-  kknn(Disease~., train = knnTrain, test = knnTest,k = nn)
  print(confusionMatrix(fitted(knnModel),knnTest$Disease))
  return(confusionMatrix(fitted(knnModel),knnTest$Disease)) 
  
}

myKnnConfusion(tModel, 7)
myKnnConfusion(tModel, 5)
myKnnConfusion(tModel, 3)


#KNN
tmpDF <- structure(list(character()),class = "data.frame")

Lastresult<- desitionTree
for(i in c(7,5,3)){
  knnModel <- kknn(Disease~., train = tModel, test = realTest, k=i)
  tmp <-as.data.frame(knnModel$fitted.values)
  colnames(tmp) <- as.character(i)
  Lastresult  <- cbind(Lastresult,tmp)
}

FinalValue <- as.data.frame(rep("",nrow(Lastresult)))
colnames(FinalValue) <- "FinalValue"
Lastresult <-cbind(Lastresult,FinalValue)

for(i in 1:nrow(Lastresult)){
  cnt = 0
  for(j in 1:4){
    if(Lastresult[i,j] == "Healthy"){
      cnt = cnt+1;
    }
  }
  if(cnt > 2){
    Lastresult[i,5] <- "Healthy"
    #FinalValue <- c(FinalValue,"Healthy")
  }
  else{
    Lastresult[i,5] <- "COVID19"
    #FinalValue <- c(FinalValue,"COVID19")
  }
}


fix(Lastresult)

combinedData <- cbind(testSet$ID,combinedData,Lastresult$FinalValue)
colnames(combinedData)<- c("ID","Predictive value from Decision Tree",	"Predictive value from 7-NN",
                "Predictive value from 5-NN"	,"Predictive value from 3-NN",	"Final predicted value")

fix(combinedData)
write.csv(combinedData,"combinedData.csv")


