from math import sqrt
import time




def eval_Print(origDictProm, origDictAdop, prom_bias_dict, adop_bias_dict):

	for c in prom_bias_dict.keys():

		print("Promoter Cluster Demographics::: ",origDictProm[c], " --------BIAS= ", prom_bias_dict[c])
		print("Adopter Cluster Demographics:::: ",origDictAdop[c], " --------BIAS= ", adop_bias_dict[c])
		print("\n")




def bitWiseSubt(lis1, lis2):

	sum = 0
	for i in range(len(lis1)):
		sum = sum + (lis1[i]-lis2[i]) ** 2

	return round((sqrt(sum)/100), 3)

def euclDist(dic1, baseline):

	distances = {}
	for c in dic1.keys():
		distances[c] = bitWiseSubt(dic1[c], baseline)

	return distances



start_time = time.time()

############BASELINE DEMOGRAPHICS########US POPULATION###########
#[Male, Female]
base_demographics_gen = [49.2, 50.8]

#[White, Black, Asian] 
base_demographics_rac = [72.4, 12.6, 4.8]

#[Adolescent(<20), Young(20-40), Mid-Aged(40-65)] 
base_demographics_age = [18.1, 31.2, 37.7]

# ############BASELINE DEMOGRAPHICS######## RANDOM 1% OF TWITTER POPULATION ACCORDING TO DR. ABHIJNAN'S PAPER###########
# #[Male, Female]
# base_demographics_gen = [46.9, 53.1]

# #[White, Black, Asian] 
# base_demographics_rac = [67.9, 13.7, 18.3]

# #[Adolescent(<20), Young(20-40), Mid-Aged(40-65)] 
# base_demographics_age = [29.3, 61.2, 9.5]



###############Promoters Demographics, coalitions clusters#############

Gender_promoters = {1: [65.454, 34.546],
					 2: [7.302, 92.698],
					 3: [93.219, 6.781],
					 4: [40.681, 59.319]}

prom_gen_bias = euclDist(Gender_promoters, base_demographics_gen)

Race_promoters = { 1: [47.859, 39.546, 12.594],
					2: [94.027, 2.995, 2.978],
					3: [71.914, 11.818, 16.269],
					4: [13.254, 3.472, 83.274],
					5: [6.397, 90.761, 2.842]}


prom_rac_bias = euclDist(Race_promoters, base_demographics_rac)

Age_promoters = {1: [9.701, 54.251, 34.995],
				2: [82.751, 13.614, 3.528],
				3: [21.521, 66.299, 11.921],
				4: [2.238, 9.423, 88.202],
				5: [3.217, 92.44, 4.243]}


prom_age_bias = euclDist(Age_promoters, base_demographics_age)

###############Adopters Demographics, coalitions clusters#############					 

Gender_adopters = {1: [66.659, 33.341],
					 2: [8.562, 91.438],
					 3: [91.658, 8.342],
					 4: [44.014, 55.986]}


adop_gen_bias = euclDist(Gender_adopters, base_demographics_gen)

Race_adopters = { 1: [49.726, 35.263, 15.011],
				  2: [92.668, 3.398, 3.934],
				  3: [73.003, 12.753, 14.245],
				  4: [11.016, 2.656, 86.328],
				  5: [7.942, 88.435, 3.623]}


adop_rac_bias = euclDist(Race_adopters, base_demographics_rac)

Age_adopters = { 1: [11.113, 54.013, 33.891],
				2: [81.354, 15.467, 3.127],
				3: [19.167, 67.322, 13.279],
				4: [2.113, 8.605, 89.101],
				5: [3.493, 92.636, 3.807]}


adop_age_bias = euclDist(Age_adopters, base_demographics_age)


print("\n\n <GENDER> BASE_DEMOGRAPHIC: ", base_demographics_gen)
eval_Print(Gender_promoters, Gender_adopters, prom_gen_bias, adop_gen_bias)

print("\n\n <RACE> BASE_DEMOGRAPHIC: ", base_demographics_rac)
eval_Print(Race_promoters, Race_adopters, prom_rac_bias, adop_rac_bias)

print("\n\n <AGE> BASE_DEMOGRAPHIC: ", base_demographics_age)
eval_Print(Age_promoters, Age_adopters, prom_age_bias, adop_age_bias)






print("\n\nElapsed Time")
print("--- %s seconds ---" % (time.time() - start_time))