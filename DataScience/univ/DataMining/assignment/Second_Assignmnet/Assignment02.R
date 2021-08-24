setRepositories()
library(ggpubr)
library(dplyr)

setwd("E:\\GoogleDrive\\SeungHyuen\\Korea_uni\\Class\\4-1\\DataMining\\Assignment\\Homework_2")
getwd()

data <- read.table("Homework2_SampleData.txt" , head = T, sep = "\t")

dim(data)
View(data)
colnames(data)
##label_1 <- data
label_1 <- colnames(data)

label_1[which(substring(label_1,1,4) == "DrHs")] <- "DRHS"
label_1[which(substring(label_1,1,3) == "Oto")] <- "OTO"


label_1 <- factor(label_1)
View(label_1)
DRHS <- OTO <- c()

for( i in 1 : nrow(data)){
  DRHS[i]  = mean(as.numeric(data[i,])[which(label_1 == "DRHS")])
  OTO[i]  = mean(as.numeric(data[i,])[which(label_1 == "OTO")])
}
DRHS

## Difference between ALL and AML based on the central Location
diff <- DRHS - OTO
diffABS <- abs(diff)
hist(diffABS)

##Generating Ranking
rank <- rank(-diffABS)

##Generating output table
##output <- data.frame(colnames(data),DRHS,OTO,diff,diffABS, rank)
output <- data.frame(DRHS,OTO,diff,diffABS, rank)
output_order <- output[order(rank),]
View(output_order)

##############T - TEST##################################
View(data)


pval <- c()
for( i in 1 : nrow(data)){
  pval[i] <- t.test(data[i,2:10]  , data[i,11:19] , paired = FALSE, var.equal = TRUE,conf.level = 0.95)$p.value
}

t.test(data[,2:10]  , data[,11:19] , paired = FALSE, var.equal = TRUE,conf.level = 0.95)


print(cnt)
View(pval)
pval_rank <- rank(pval)
pval_out <- data.frame(data[,1],pval,pval_rank)

pval_out <- rename(pval_out,Features =data...1.)
View(pval_out)

pval_out <- pval_out[order(pval_rank),]
pval_out_de <- pval_out[order(pval_rank , decreasing = TRUE),]
head(pval_out)
tail(pval_out)
colnames(pval_out)
top <- c()
top <- head(pval_out,1)
bottom <- tail(pval_out, 1)

top

View(data)

labelName <- label_1[2:19]

top_val <- c(t(data[which(rank(pval_out$pval_rank) <= 1),2:19]))
top <- data.frame(top_val,labelName)
ggdensity(top ,  x= "top_val" , add = "mean" , rug = T , color = "labelName", fill = "labelName")


bottom_val <- c(t(data[which(order(pval_out$pval_rank,decreasing =TRUE ) <= 1),2:19]))
bottom <- data.frame(bottom_val,labelName)
ggdensity(bottom ,  x= "bottom_val" , add = "mean" , rug = T , color = "labelName", fill = "labelName")


View(top_val)
View(top)

View(bottom_val)
View(bottom)

top_df <- data.frame(top,)



## 
cnt <- pval_out[pval_out$pval <= 0.05 ,]
nrow(cnt)
nrow(pval_out)
View(cnt)


################Plot####################################
ggdensity(pval_out ,  x= "pval" , add = "mean" , rug = T )
ggdensity(pval_out_de ,  x= "pval" , add = "mean" , rug = T )





colnames(pval_out)
?ggdensity



