setRepositories()

library(tidyverse)  
library(cluster)    
library(factoextra) 
library(FactoMineR) 
library(dendextend) 
library(NbClust) 
library(colorspace)
library(data.table)
library(factoextra)
library(dplyr)
# DeskTop
WORK_DIR <- "E:\\GoogleDrive\\SeungHyuen\\Korea_uni\\Class\\4-2\\ClassMeterials\\Convergence_Infomatics\\Homework\\Homework2"
# LapTop
#WORK_DIR <- "E:\\GoogleDrive\\SeungHyuen\\Korea_uni\\Class\\4-2\\ClassMeterials\\Convergence_Infomatics\\Homework\\Homework2"

setwd(WORK_DIR)
getwd()




#Read Data
dataOriginal <- data.frame(fread("1.Homework2_OriginalData.tsv",sep = "\t" ,head = T, stringsAsFactors = F))
dataFiltered <- data.frame(fread("2.Homework2_FilteredData.tsv",sep = "\t" ,head = T, stringsAsFactors = F))

#remove sampleName
removeNum <- function(df){
  for(i in 1 : nrow(df)){
    df[i,1] <- substr(df[i,1] , 1 , nchar(df[i,1])-1)
  }
  return(df)
}

Original<-removeNum(dataOriginal)
Filtered<-removeNum(dataFiltered)

#################################################################################################
# [Q1] After performing PCA analysis on both data, try plotting using PC1 and PC2, respectively.#
#      When drawing a PCA plot, fill different colors depending on the disease.                 #
#      (Tip) There are 3 samples for each disease.                                              #
#################################################################################################
plotPCA <- function(data , title_){
  data.pca <- PCA(data[,-1], graph =  FALSE)
  fviz_pca_ind(data.pca , geom.ind =  "point", 
               fill.ind = data$sampleName,     
               pointshape = 23, pointsize = 4, 
               legend.title = "Disease",       
               title = title_                  
  )
}
# Disease.
# COVID19, Asthma, COPD, Tuberculosis, LungCancer, AIDS, Alzheimer

plotPCA(Original , "Original Data PCA Plot")
plotPCA(Filtered , "Filtered Data PCA Plot")

##################################################################################
# [Q2] Are there any significant differences in the results between the two data?#
#      What is the reason? If so, what data should be used?                      #
##################################################################################
#
# --차이-- 
# Filtered data more performing than Original data 
# --reason-- 
# Origina PC 47.7% + 21.8% =69.5%
# Filtered PC 62.2% + 34.4% = 96.6% 
# Filtered is more perform 27.4%, so choose Filtered data is the best choice
#
##################################################################################s


#####################################################################################################################
# [Q3] Perform clustering analysis using hierarchical clustering.                                                   #  
# Let's find the parameter in the format most similar to the PCA result (Distance Metric, Linkage Methods, and etc.)#
# On the Dendrogram, cut and mark the optimal number of clusters you think.                                         #
#####################################################################################################################

dataFiltered.scale <- scale(dataFiltered[,-1])
rownames(dataFiltered.scale) <- dataFiltered$sampleName 


fviz_nbclust(dataFiltered.scale, FUN = hcut, method = "silhouette", cex = 2)
#결과??? : 3
fviz_nbclust(dataFiltered.scale, FUN = hcut, method = "gap_stat", cex = 2)
#결과??? : 5
fviz_nbclust(dataFiltered.scale, FUN = hcut, method = "wss", cex = 2)
#결과??? : 4
## This three method's average is four, and I also think four clusters is best choice  

# 
#  dist method using Euclidean and manhattan 
ed <- dist(dataFiltered.scale, method = "euclidean")
md <- dist(dataFiltered.scale, method = "manhattan")

#  Three linkage method for checking all results for visualization 
hc_ED_complet <- hclust(ed, method = "complete")
hc_ED_average <- hclust(ed, method = "average")
hc_ED_single <- hclust(ed, method = "single")

hc_MD_complet <- hclust(md, method = "complete")
hc_MD_average <- hclust(md, method = "average")
hc_MD_single <- hclust(md, method = "single")


# 
plot(hc_MD_complet, cex = 1, hang = -1 , xlab = "Disease")
rect.hclust(hc_MD_complet,k=4, border = 2:5)

#Q3 answer plot
# my last choice, average and manhattan
plot(hc_MD_average, cex = 1, hang = -1, xlab = "Disease")
rect.hclust(hc_MD_average,k=4, border = 2:5)

#########################################################################################################
# [Q4] Perform clustering analysis using kmeans clustering based on Euclidean Distance.                 #
# Please find optimal number of clusters (k) by changing the from 2 to 10 based on the Silhouette Score.#
# Draw a plot for silhouette score.                                                                     #
#########################################################################################################


# Already obtained in Q3
# Filtered.scale <- scale(Filtered[,-1])
# rownames(Filtered.scale) <- dataFiltered$sampleName 
dataFiltered.nb <- NbClust(dataFiltered.scale, min.nc=2, max.nc=10,
                       method="kmeans",distance = "euclidean", index="silhouette" )

dataFiltered.nb

barColor = c("lightblue", "mistyrose", "lightcyan", "lavender", "cornsilk")
#Q4 answer visual
barplot(dataFiltered.nb$All.index,xlab = "Number of Cluster", ylab = "Value_Index" ,
        col = barColor, main = "silhouette")


fviz_cluster(list(data = dataFiltered.scale, cluster = dataFiltered.nb$Best.partition),
             ggtheme = theme_classic() ,
             pointshape = 23, pointsize = 4,
             legend.title = "Disease Cluster",
             main = "kmeans_Cluster"
)+labs(subtitle = "Euclidean")
dataFiltered.nb
#Q4 answer end

?fviz_cluster

# Optimal cluster for personal thought
result_kmeans<- kmeans(dataFiltered.scale, 4, nstart = 100)
fviz_cluster(list(data = dataFiltered.scale, cluster = result_kmeans$cluster),
             geom = c("point" , "arrow"),
             ggtheme = theme_classic() ,
             pointshape = 23, pointsize = 4,
             legend.title = "Disease Cluster",
             main = "kmeans_Cluster"
)




 