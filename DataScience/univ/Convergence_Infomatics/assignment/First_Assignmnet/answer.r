setRepositories()

laptop_workspace = "D:\\GoogleDrive\\SeungHyuen\\Korea_uni\\Class\\4-2\\ClassMeterials\\Convergence_Infomatics\\Homework\\Homework_1.Convergence_Informatics"
setwd(laptop_workspace)
#workspace = "E:\\GoogleDrive\\SeungHyuen\\Korea_uni\\Class\\4-2\\ClassMeterials\\Convergence_Infomatics\\Homework\\Homework_1.Convergence_Informatics"
#setwd(workspace)

getwd()
library("ggpubr")
library("ggplot2")
library("dplyr")
#custom Function


#dataFrame mean
dfmean <- function(df,rowN){
  
  output <-  data.frame(matrix(nrow=0, ncol=1)) 
  for(i in 1 : ncol(df)){
    columName <- names(df[i])
    eachMean <- mean(df[,i])
    output <- rbind(output,eachMean)
  }
  output <- t(output)
  colN <- names(df)
  #rownames(output) <- rowN
  colnames(output) <- colN
  output <- cbind(output, data.frame(calcMethod = "ave",Species = rowN ))
  return(output)
}

#dataFrame variance
dfvar <- function(df,rowN){
  
  output <-  data.frame(matrix(nrow=0, ncol=1))
  for(i in 1 : ncol(df)){
    columName <- names(df[i])
    eachMean <- var(df[,i])
    output <- rbind(output,eachMean)
  }
  output <- t(output)
  colN <- names(df)
  #rownames(output) <- rowN
  colnames(output) <- colN
  output <- cbind(output, data.frame(calcMethod = "var",Species = rowN ))
  return(output)
}

#dataFrame standard deviation
dfSd <- function(df,rowN){
  
  output <-  data.frame(matrix(nrow=0, ncol=1))
  for(i in 1 : ncol(df)){
    columName <- names(df[i])
    eachMean <- sd(df[,i])
    output <- rbind(output,eachMean)
  }
  output <- t(output)
  colN <- names(df)
  #rownames(output) <- rowN
  colnames(output) <- colN
  output <- cbind(output, data.frame(calcMethod = "sd",Species = rowN ))
  return(output)
}


#[Step 1] Load ???iris??? data in your computer on Rstudio.
data(iris)

#[Step 2] Calculate average, variance, and standard deviation of four continuous variables
#features == Sepal.Length , Sepal.Width ,Petal.Length ,Petal.Width ,Species
Alliris <- iris[1:4]
#average
Allave <- dfmean(Alliris,"All")

#variance
Allvar <- dfvar(Alliris,"All")

#standard deviation
Allsd <- dfSd(Alliris,"All")

#combin
Allresult <- rbind(Allave,Allvar,Allsd)
rownames(Allresult)<- c(rep(1:nrow(Allresult)))
Allresult



#[Step 3] Calculate average, variance, and standard deviation of four continuous variables in each species respectively.
###setosa###
setosa = subset(iris ,Species == "setosa")
setosa = setosa[1:4]

#combin
setosaResult <- rbind(dfmean(setosa,"setosa"),dfvar(setosa,"setosa"),dfSd(setosa,"setosa"))
rownames(setosaResult)<- c(rep(1:nrow(setosaResult)))
setosaResult

####versicolor###
versicolor = subset(iris ,Species == "versicolor")
versicolor = versicolor[1:4]

#combin
versicolorResult <- rbind(dfmean(versicolor,"versicolor"),dfvar(versicolor,"versicolor"),dfSd(versicolor,"versicolor"))
rownames(versicolorResult)<- c(rep(1:nrow(versicolorResult)))
versicolorResult

###virginica###nnnnnnnnnnnnnn
virginica= subset(iris ,Species == "virginica")
virginica = virginica[1:4]

#combin
virginicaResult <- rbind(dfmean(virginica,"virginica"),dfvar(virginica,"virginica"),dfSd(virginica,"virginica"))
rownames(virginicaResult)<- c(rep(1:nrow(virginicaResult)))
virginicaResult

#answer <- rbind(Allresult,setosaResult,versicolorResult,virginicaResult)
answer <- rbind(setosaResult,versicolorResult,virginicaResult)
answer <- rbind(setosaResult,versicolorResult,virginicaResult,Allresult)
answer<-answer[order(answer$calcMethod),]
answer<-answer[order(answer$Species),]
rownames(versicolorResult)<- c(rep(1:nrow(versicolorResult)))
rownames(answer)<- c(rep(1:nrow(answer)))
answer
fix(answer)
View(answer) 
#[Step 4] Let's visualize four continuous variable respectively to
#histogram (you should consider species information as different colors in each histogram)
setosa_sample = subset(iris ,Species == "setosa")
versicolor_sample = subset(iris ,Species == "versicolor")
virginica_sample = subset(iris ,Species == "virginica")



SepalL_Dens_All<-ggdensity(iris, x = "Sepal.Length" , rug =T,fill = "yellow")
SepalL_Dens_All
SepalL_Dens <- ggdensity(iris, x = "Sepal.Length", rug =T,color = "Species",fill = "Species")
Sepalw_Dens <- ggdensity(iris, x = "Sepal.Width", rug =T,color = "Species",fill = "Species")
PetalL_Dens <- ggdensity(iris, x = "Petal.Length", rug =T,color = "Species",fill = "Species")
Petalw_Dens <- ggdensity(iris, x = "Petal.Width", rug =T,color = "Species",fill = "Species")

densPlot <- ggarrange(SepalL_Dens,Sepalw_Dens,PetalL_Dens,Petalw_Dens, labels = c("SepalL_Dens","Sepalw_Dens","PetalL_Dens","Petalw_Dens"),ncol = 2,nrow = 2)
densPlot

#[Step 5] Draw the same information as in Step 4, but with a box-plot.
SepalL_box <- ggboxplot(iris, y = "Sepal.Length",x = "Species", fill = "Species", add = "jitter",shape = "Species",col = "black")
SepalW_box <- ggboxplot(iris, y = "Sepal.Width",x = "Species", fill = "Species", add = "jitter",shape = "Species",col = "black")
PetalL_box <- ggboxplot(iris, y = "Petal.Length",x = "Species", fill = "Species", add = "jitter",shape = "Species",col = "black")
PetalW_box <- ggboxplot(iris, y = "Petal.Width",x = "Species", fill = "Species", add = "jitter",shape = "Species",col = "black")

boxPlot<-ggarrange(SepalL_box,SepalW_box,PetalL_box,PetalW_box, labels = c("SepalL_Dens","Sepalw_Dens","PetalL_Dens","Petalw_Dens"),ncol = 2,nrow = 2)
boxPlot
Plots <- ggarrange(densPlot,boxPlot,nrow = 1,ncol = 2)

Plots
answer

ggarrange(SepalL_Dens,Sepalw_Dens,PetalL_Dens,Petalw_Dens,SepalL_box,SepalW_box,PetalL_box,PetalW_box, labels = c("SepalL_Dens","Sepalw_Dens","PetalL_Dens","Petalw_Dens","SepalL_Dens","Sepalw_Dens","PetalL_Dens","Petalw_Dens"),ncol = 4,nrow = 2)
