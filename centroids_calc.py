from math import sqrt
import gzip
import json
import time


def PrintSimilarities(diction):

	for k in diction.keys():
		print(k, "\n", diction[k])
		print("##################################################")


#Computes percentage of adopters in the promoters between two lists

def JaccSim(lis1, lis2):

	A = set(lis1)
	B = set(lis2)

	Intersection = A.intersection(B)

	Numerator = len(Intersection)
	#Denominator = len(A) + len(B) - Numerator
	Denominator = len(B)

	Jaccardi_Similarity = Numerator/Denominator

	return round(Numerator/len(A)*100, 3)
	#return round(Jaccardi_Similarity, 3)



def bitWiseSubt(lis1, lis2):

	sum = 0
	for i in range(len(lis1)):
		sum = sum + (lis1[i]-lis2[i]) ** 2

	return round(sqrt(sum), 3)

def euclDist(dic1, dic2):

	distances = {}
	for c in dic1.keys():
		distances[c] = bitWiseSubt(dic1[c], dic2[c])

	return distances


start_time = time.time()

Gender_centroids1 = { 1: [65.454, 34.546],
					  2: [7.302, 92.698],
					  3: [93.219, 6.781],
					  4: [40.681, 59.319]}

Gender_centroids2 = { 1: [66.659, 33.341],
					  2: [8.562, 91.438],
					  3: [91.658, 8.342],
					  4: [44.014, 55.986]}

print("\nEuclidean Distances: Gender Centroids")
print(euclDist(Gender_centroids1, Gender_centroids2))


Race_centroids1 = { 1: [47.859, 39.546, 12.594],
					2: [94.027, 2.995, 2.978],
					3: [71.914, 11.818, 16.269],
					4: [13.254, 3.472, 83.274],
					5: [6.397, 90.761, 2.842]}

Race_centroids2 = { 1: [49.726, 35.263, 15.011],
				    2: [92.668, 3.398, 3.934],
				    3: [73.003, 12.753, 14.245],
				    4: [11.016, 2.656, 86.328],
				    5: [7.942, 88.435, 3.623]}


print("\nEuclidean Distances: Race Centroids")
print(euclDist(Race_centroids1, Race_centroids2))

Age_centroids1 = { 1: [9.701, 54.251, 34.995],
				   2: [82.751, 13.614, 3.528],
				   3: [21.521, 66.299, 11.921],
				   4: [2.238, 9.423, 88.202],
				   5: [3.217, 92.44, 4.243]}

Age_centroids2 = { 1: [11.113, 54.013, 33.891],
				   2: [81.354, 15.467, 3.127],
				   3: [19.167, 67.322, 13.279],
				   4: [2.113, 8.605, 89.101],
				   5: [3.493, 92.636, 3.807]}


print("\nEuclidean Distances: Age Centroids")
print(euclDist(Age_centroids1, Age_centroids2))





gend_link = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/with Elbow/Clusters_Demographics/Gender_Clusters.gz'
race_link = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/with Elbow/Clusters_Demographics/Race_Clusters.gz'
age_link = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/with Elbow/Clusters_Demographics/Age_Clusters.gz'

gen_demo = {}
rac_demo = {}
age_demo = {}


with gzip.open(gend_link, 'rt') as g:
	gend_temp = g.read()
g.close()

gen_demo = json.loads(gend_temp)

with gzip.open(race_link, 'rt') as r:
	race_temp = r.read()
r.close()

rac_demo = json.loads(race_temp)

with gzip.open(age_link, 'rt') as a:
	age_temp = a.read()
a.close()

age_demo = json.loads(age_temp)




gend_link1 = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/with Elbow/Clusters_TrendUsage_Demographics/Gender_Trend_Clusters.gz'
race_link1 = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/with Elbow/Clusters_TrendUsage_Demographics/Race_Trend_Clusters.gz'
age_link1 = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/with Elbow/Clusters_TrendUsage_Demographics/Age_Trend_Clusters.gz'

gen_tren = {}
rac_tren = {}
age_tren = {}

with gzip.open(gend_link1, 'rt') as g1:
	gend_temp1 = g1.read()
g1.close()

gen_tren = json.loads(gend_temp1)

with gzip.open(race_link1, 'rt') as r1:
	race_temp1 = r1.read()
r1.close()

rac_tren = json.loads(race_temp1)

with gzip.open(age_link1, 'rt') as a1:
	age_temp1 = a1.read()
a1.close()

age_tren = json.loads(age_temp1)


#dictionaries to contain the similarities between clusters from *_demo dictionaries from their counter-parts

Gen_JS = {}
Rac_JS = {}
Age_JS = {}


demo_clus_gen = list(gen_demo.keys()) 
demo_clus_rac = list(rac_demo.keys()) 
demo_clus_age = list(age_demo.keys()) 


tren_clus_gen = list(gen_tren.keys())
tren_clus_rac = list(rac_tren.keys())
tren_clus_age = list(age_tren.keys())


Gen_JS[demo_clus_gen[0]+"---"+tren_clus_gen[3]] = JaccSim(gen_demo[demo_clus_gen[0]], gen_tren[tren_clus_gen[3]])
Gen_JS[demo_clus_gen[1]+"---"+tren_clus_gen[2]] = JaccSim(gen_demo[demo_clus_gen[1]], gen_tren[tren_clus_gen[2]])
Gen_JS[demo_clus_gen[2]+"---"+tren_clus_gen[1]] = JaccSim(gen_demo[demo_clus_gen[2]], gen_tren[tren_clus_gen[1]])
Gen_JS[demo_clus_gen[3]+"---"+tren_clus_gen[0]] = JaccSim(gen_demo[demo_clus_gen[3]], gen_tren[tren_clus_gen[0]])



Rac_JS[demo_clus_rac[0]+"---"+tren_clus_rac[4]] = JaccSim(rac_demo[demo_clus_rac[0]], rac_tren[tren_clus_rac[4]])
Rac_JS[demo_clus_rac[1]+"---"+tren_clus_rac[3]] = JaccSim(rac_demo[demo_clus_rac[1]], rac_tren[tren_clus_rac[3]])
Rac_JS[demo_clus_rac[2]+"---"+tren_clus_rac[0]] = JaccSim(rac_demo[demo_clus_rac[2]], rac_tren[tren_clus_rac[0]])
Rac_JS[demo_clus_rac[3]+"---"+tren_clus_rac[2]] = JaccSim(rac_demo[demo_clus_rac[3]], rac_tren[tren_clus_rac[2]])
Rac_JS[demo_clus_rac[4]+"---"+tren_clus_rac[1]] = JaccSim(rac_demo[demo_clus_rac[4]], rac_tren[tren_clus_rac[1]])



Age_JS[demo_clus_age[0]+"---"+tren_clus_age[1]] = JaccSim(age_demo[demo_clus_age[0]], age_tren[tren_clus_age[1]])
Age_JS[demo_clus_age[1]+"---"+tren_clus_age[3]] = JaccSim(age_demo[demo_clus_age[1]], age_tren[tren_clus_age[3]])
Age_JS[demo_clus_age[2]+"---"+tren_clus_age[0]] = JaccSim(age_demo[demo_clus_age[2]], age_tren[tren_clus_age[0]])
Age_JS[demo_clus_age[3]+"---"+tren_clus_age[2]] = JaccSim(age_demo[demo_clus_age[3]], age_tren[tren_clus_age[2]])
Age_JS[demo_clus_age[4]+"---"+tren_clus_age[4]] = JaccSim(age_demo[demo_clus_age[4]], age_tren[tren_clus_age[4]])


print("##################################################")
print("\n\nPercentage of Adopters present in the promoters::GENDER CLUSTERS")
PrintSimilarities(Gen_JS)

print("##################################################")
print("\n\nPercentage of Adopters present in the promoters::RACE CLUSTERS")
PrintSimilarities(Rac_JS)

print("##################################################")
print("\n\nPercentage of Adopters present in the promoters::AGE")
PrintSimilarities(Age_JS)



print("##################################################")
print("\n\nElapsed Time")
print("--- %s seconds ---" % (time.time() - start_time))
