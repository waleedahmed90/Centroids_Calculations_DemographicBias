from math import sqrt
import gzip
import json
import time


def PrintSimilarities(diction):

	for k in diction.keys():
		print(k, "\n", diction[k])
		print("##################################################")


#Computes Jaccardi Similarity between two lists

def JaccSim(lis1, lis2):

	A = set(lis1)
	B = set(lis2)

	Intersection = A.intersection(B)

	Numerator = len(Intersection)
	#Denominator = len(A) + len(B) - Numerator
	Denominator = len(B)

	Jaccardi_Similarity = Numerator/Denominator

	return round(Jaccardi_Similarity, 3)



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

Gender_centroids1 = {1: [34.763, 65.237],
					 2: [73.487, 26.513],
					 3: [5.936, 94.064],
					 4: [95.939, 4.061],
					 5: [54.576, 45.424]}

Gender_centroids2 = {1: [35.425, 64.575],
					 2: [72.925, 27.075],
					 3: [5.282, 94.718],
					 4: [94.817, 5.183],
					 5: [54.583, 45.417]}

print("\nEuclidean Distances: Gender Centroids")
print(euclDist(Gender_centroids1, Gender_centroids2))


Race_centroids1 = { 1: [97.374, 1.26, 1.366],
					2: [3.496, 95.131, 1.373],
					3: [56.868, 7.455, 35.677],
					4: [7.748, 2.292, 89.96],
					5: [34.443, 52.785, 12.772],
					6: [63.773, 25.304, 10.924],
					7: [80.335, 8.674, 10.991]}

Race_centroids2 = { 1: [95.827, 1.95, 2.223],
					2: [4.218, 94.163, 1.619],
					3: [50.413, 7.456, 42.131],
					4: [5.358, 1.445, 93.197],
					5: [37.786, 49.375, 12.84],
					6: [65.025, 21.784, 13.191],
					7: [79.193, 9.506, 11.301]}


print("\nEuclidean Distances: Race Centroids")
print(euclDist(Race_centroids1, Race_centroids2))

Age_centroids1 = {1: [10.101, 65.432, 23.991],
				  2: [91.655, 6.352, 1.953], 
				  3: [1.612, 95.207, 3.097],
				  4: [1.697, 6.449, 91.776], 
				  5: [40.963, 49.258, 9.428], 
				  6: [10.444, 43.142, 44.856],
				  7: [18.161, 73.198, 8.48]}

Age_centroids2 = {1: [12.725, 64.458, 22.399],
				  2: [91.107, 7.369, 1.516], 
				  3: [1.981, 95.569, 2.421],
				  4: [1.659, 6.471, 91.838], 
				  5: [38.56, 52.366, 8.855], 
				  6: [9.825, 46.397, 42.283],
				  7: [16.138, 73.256, 10.44]}


print("\nEuclidean Distances: Age Centroids")
print(euclDist(Age_centroids1, Age_centroids2))





gend_link = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/Clusters_Demographics/Gender_Clusters.gz'
race_link = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/Clusters_Demographics/Race_Clusters.gz'
age_link = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/Clusters_Demographics/Age_Clusters.gz'

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




gend_link1 = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/Clusters_TrendUsage_Demographics/Gender_Trend_Clusters.gz'
race_link1 = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/Clusters_TrendUsage_Demographics/Race_Trend_Clusters.gz'
age_link1 = '/Users/WaleedAhmed/Documents/THESIS_DS_CODE/code_cleaning/dataReadCode_2/Code_HashtagsDemographics/Clusters_TrendUsage_Demographics/Age_Trend_Clusters.gz'

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


Gen_JS[demo_clus_gen[0]+"---"+tren_clus_gen[1]] = JaccSim(gen_demo[demo_clus_gen[0]], gen_tren[tren_clus_gen[1]])
Gen_JS[demo_clus_gen[1]+"---"+tren_clus_gen[3]] = JaccSim(gen_demo[demo_clus_gen[1]], gen_tren[tren_clus_gen[3]])
Gen_JS[demo_clus_gen[2]+"---"+tren_clus_gen[2]] = JaccSim(gen_demo[demo_clus_gen[2]], gen_tren[tren_clus_gen[2]])
Gen_JS[demo_clus_gen[3]+"---"+tren_clus_gen[0]] = JaccSim(gen_demo[demo_clus_gen[3]], gen_tren[tren_clus_gen[0]])
Gen_JS[demo_clus_gen[4]+"---"+tren_clus_gen[4]] = JaccSim(gen_demo[demo_clus_gen[4]], gen_tren[tren_clus_gen[4]])



Rac_JS[demo_clus_rac[0]+"---"+tren_clus_rac[0]] = JaccSim(rac_demo[demo_clus_rac[0]], rac_tren[tren_clus_rac[0]])
Rac_JS[demo_clus_rac[1]+"---"+tren_clus_rac[4]] = JaccSim(rac_demo[demo_clus_rac[1]], rac_tren[tren_clus_rac[4]])
Rac_JS[demo_clus_rac[2]+"---"+tren_clus_rac[2]] = JaccSim(rac_demo[demo_clus_rac[2]], rac_tren[tren_clus_rac[2]])
Rac_JS[demo_clus_rac[3]+"---"+tren_clus_rac[3]] = JaccSim(rac_demo[demo_clus_rac[3]], rac_tren[tren_clus_rac[3]])
Rac_JS[demo_clus_rac[4]+"---"+tren_clus_rac[1]] = JaccSim(rac_demo[demo_clus_rac[4]], rac_tren[tren_clus_rac[1]])
Rac_JS[demo_clus_rac[5]+"---"+tren_clus_rac[5]] = JaccSim(rac_demo[demo_clus_rac[5]], rac_tren[tren_clus_rac[5]])
Rac_JS[demo_clus_rac[6]+"---"+tren_clus_rac[6]] = JaccSim(rac_demo[demo_clus_rac[6]], rac_tren[tren_clus_rac[6]])






Age_JS[demo_clus_age[0]+"---"+tren_clus_age[3]] = JaccSim(age_demo[demo_clus_age[0]], age_tren[tren_clus_age[3]])
Age_JS[demo_clus_age[1]+"---"+tren_clus_age[6]] = JaccSim(age_demo[demo_clus_age[1]], age_tren[tren_clus_age[6]])
Age_JS[demo_clus_age[2]+"---"+tren_clus_age[5]] = JaccSim(age_demo[demo_clus_age[2]], age_tren[tren_clus_age[5]])
Age_JS[demo_clus_age[3]+"---"+tren_clus_age[4]] = JaccSim(age_demo[demo_clus_age[3]], age_tren[tren_clus_age[4]])
Age_JS[demo_clus_age[4]+"---"+tren_clus_age[1]] = JaccSim(age_demo[demo_clus_age[4]], age_tren[tren_clus_age[1]])
Age_JS[demo_clus_age[5]+"---"+tren_clus_age[2]] = JaccSim(age_demo[demo_clus_age[5]], age_tren[tren_clus_age[2]])
Age_JS[demo_clus_age[6]+"---"+tren_clus_age[0]] = JaccSim(age_demo[demo_clus_age[6]], age_tren[tren_clus_age[0]])




print("##################################################")
print("\n\nJaccardi Similarity between GENDER Clusters")
PrintSimilarities(Gen_JS)

print("##################################################")
print("\n\nJaccardi Similarity between RACE Clusters")
PrintSimilarities(Rac_JS)

print("##################################################")
print("\n\nJaccardi Similarity between AGE Clusters")
PrintSimilarities(Age_JS)



print("##################################################")
print("\n\nElapsed Time")
print("--- %s seconds ---" % (time.time() - start_time))






