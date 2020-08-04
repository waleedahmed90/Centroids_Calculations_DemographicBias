##The code in the current repository will work after the code from the following repository

https://github.com/waleedahmed90/Demographic-Bias-Control-Clustering-Part- has been successfully executed

#Running "python centroids_calc.py" will result in the following output

#Input files used in the code:

#LINK TO THE CORRESPONDING FILES [*_Clusters.gz].
IN <Cluster_Demographics> FOLDER CREATED BY THE CODE PRESENT IN THE FOLLOWING REPOSITORY

"https://github.com/waleedahmed90/Demographic-Bias-Control-Clustering-Part-"

Following variables will contain the corresponding paths

1) gend_link
2) race_link
3) age_link

#LINK TO THE CORRESPONDING FILES [*_Trend_Clusters.gz']. IN <Clusters_TrendUsage_Demographics> FOLDER CREATED BY THE CODE PRESENT IN THE FOLLOWING REPOSITORY "https://github.com/waleedahmed90/Demographic-Bias-Control-Clustering-Part-"

Following variables will contain the corresponding paths

1) gend_link1
2) race_link1
3) age_link1


>>>>>>>>>>>>>>>>>>>>>>Running "python centroids_calc.py" results into following output on the console

Euclidean Distances: Gender Centroids
{1: 1.704, 2: 1.782, 3: 2.208, 4: 4.714}

Euclidean Distances: Race Centroids
{1: 5.26, 2: 1.71, 3: 2.481, 4: 3.873, 5: 2.9}

Euclidean Distances: Age Centroids
{1: 1.808, 2: 2.355, 3: 2.904, 4: 1.222, 5: 0.552}
##################################################


Percentage of Adopters present in the promoters::GENDER CLUSTERS
[65.454, 34.546]---[66.659, 33.341] 
 34.748
##################################################
[7.302, 92.698]---[8.562, 91.438] 
 25.064
##################################################
[93.219, 6.781]---[91.658, 8.342] 
 27.274
##################################################
[40.681, 59.319]---[44.014, 55.986] 
 30.057
##################################################
##################################################


Percentage of Adopters present in the promoters::RACE CLUSTERS
[47.859, 39.546, 12.594]---[49.726, 35.263, 15.011] 
 27.489
##################################################
[94.027, 2.995, 2.978]---[92.668, 3.398, 3.934] 
 26.498
##################################################
[71.914, 11.818, 16.269]---[73.003, 12.753, 14.245] 
 37.884
##################################################
[13.254, 3.472, 83.274]---[11.016, 2.656, 86.328] 
 28.008
##################################################
[6.397, 90.761, 2.842]---[7.942, 88.435, 3.623] 
 25.113
##################################################
##################################################


Percentage of Adopters present in the promoters::AGE
[9.701, 54.251, 34.995]---[11.113, 54.013, 33.891] 
 27.309
##################################################
[82.751, 13.614, 3.528]---[81.354, 15.467, 3.127] 
 25.775
##################################################
[21.521, 66.299, 11.921]---[19.167, 67.322, 13.279] 
 40.944
##################################################
[2.238, 9.423, 88.202]---[2.113, 8.605, 89.101] 
 25.438
##################################################
[3.217, 92.44, 4.243]---[3.493, 92.636, 3.807] 
 21.371
##################################################
##################################################


Elapsed Time
--- 0.03870415687561035 seconds ---


>>>>>>>>>>>>>>>>>>>>>>Running "python biasCalculations.py" results into following output on the console


 <GENDER> BASE_DEMOGRAPHIC:  [49.2, 50.8]
Promoter Cluster Demographics:::  [65.454, 34.546]  --------BIAS=  0.23
Adopter Cluster Demographics::::  [66.659, 33.341]  --------BIAS=  0.247


Promoter Cluster Demographics:::  [7.302, 92.698]  --------BIAS=  0.593
Adopter Cluster Demographics::::  [8.562, 91.438]  --------BIAS=  0.575


Promoter Cluster Demographics:::  [93.219, 6.781]  --------BIAS=  0.623
Adopter Cluster Demographics::::  [91.658, 8.342]  --------BIAS=  0.6


Promoter Cluster Demographics:::  [40.681, 59.319]  --------BIAS=  0.12
Adopter Cluster Demographics::::  [44.014, 55.986]  --------BIAS=  0.073




 <RACE> BASE_DEMOGRAPHIC:  [72.4, 12.6, 4.8]
Promoter Cluster Demographics:::  [47.859, 39.546, 12.594]  --------BIAS=  0.373
Adopter Cluster Demographics::::  [49.726, 35.263, 15.011]  --------BIAS=  0.336


Promoter Cluster Demographics:::  [94.027, 2.995, 2.978]  --------BIAS=  0.237
Adopter Cluster Demographics::::  [92.668, 3.398, 3.934]  --------BIAS=  0.223


Promoter Cluster Demographics:::  [71.914, 11.818, 16.269]  --------BIAS=  0.115
Adopter Cluster Demographics::::  [73.003, 12.753, 14.245]  --------BIAS=  0.095


Promoter Cluster Demographics:::  [13.254, 3.472, 83.274]  --------BIAS=  0.987
Adopter Cluster Demographics::::  [11.016, 2.656, 86.328]  --------BIAS=  1.025


Promoter Cluster Demographics:::  [6.397, 90.761, 2.842]  --------BIAS=  1.023
Adopter Cluster Demographics::::  [7.942, 88.435, 3.623]  --------BIAS=  0.995




 <AGE> BASE_DEMOGRAPHIC:  [18.1, 31.2, 37.7]
Promoter Cluster Demographics:::  [9.701, 54.251, 34.995]  --------BIAS=  0.247
Adopter Cluster Demographics::::  [11.113, 54.013, 33.891]  --------BIAS=  0.242


Promoter Cluster Demographics:::  [82.751, 13.614, 3.528]  --------BIAS=  0.752
Adopter Cluster Demographics::::  [81.354, 15.467, 3.127]  --------BIAS=  0.738


Promoter Cluster Demographics:::  [21.521, 66.299, 11.921]  --------BIAS=  0.437
Adopter Cluster Demographics::::  [19.167, 67.322, 13.279]  --------BIAS=  0.436


Promoter Cluster Demographics:::  [2.238, 9.423, 88.202]  --------BIAS=  0.572
Adopter Cluster Demographics::::  [2.113, 8.605, 89.101]  --------BIAS=  0.584


Promoter Cluster Demographics:::  [3.217, 92.44, 4.243]  --------BIAS=  0.714
Adopter Cluster Demographics::::  [3.493, 92.636, 3.807]  --------BIAS=  0.717




Elapsed Time
--- 0.0007090568542480469 seconds ---

<<<<Author: Waleed Ahmed, Date: (Aug 04, 2020), (Saarbrücken, Deutschland)>>>>

