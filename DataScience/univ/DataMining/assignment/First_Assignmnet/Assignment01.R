setRepositories()

setwd("E:\\GoogleDrive\\SeungHyuen\\Korea_uni\\Class\\4-1\\DataMining\\Assignment\\Homework_1")

data <- read.table("Homework1_SampleData.txt" , head = T, sep = "\t")

dim(data)


label <- colnames(data)

label[which(substring(label,1,4) == "DrHs")] <- "DRHS"
label[which(substring(label,1,3) == "Oto")] <- "OTO"

label <- factor(label)

DRHS <- OTO <- c()

for( i in 1 : nrow(data)){
  DRHS[i]  = mean(as.numeric(data[i,])[which(label == "DRHS")])
  OTO[i]  = mean(as.numeric(data[i,])[which(label == "OTO")])
}

## Difference between ALL and AML based on the central Location
diff <- DRHS - OTO
diffABS <- abs(diff)
hist(diffABS)

##Generating Ranking
rank <- rank(-diffABS)
names(data)
colnames(data)
label
##Generating output table
output <- data.frame(DRHS,OTO,diff,diffABS, rank)
output_order <- output[order(rank),]
write.table(output_order, "Result_Assignment01.txt", sep = "\t", quote = F, row.names = F)





