import math
import matplotlib.pyplot as matplotlib
import random

from numpy import mat

bucket = {}

class NormalDistribution:

    def __init__(self, mean, sigma):
        self.mean = mean
        self.sigma = sigma
    
    def sample_number(self):
        min = 0
        max = mean * 1.5
        numbers = [random.randrange(min, max) for x in range(10)]
        z_scores = []
        for num in numbers:
            z_scores.append(self.z_score(num))
        
        final_number = z_scores[0]
        chosen_number = numbers[0]

        iterations = len(numbers)
        current = 1

        for score in z_scores[1:]:
            #print(str(score) + "/" + str(final_number))
            if(abs(score) < abs(final_number)):
                #print("Chose better number: "+str(numbers[current])+" vs "+str(chosen_number))
                final_number = score
                chosen_number = numbers[current]

            else:
                roll = False
                check = abs(score)
                if(check < 1):
                    roll = random.randrange(0, 100) <= 65
                elif(check < 2):
                    roll = random.randrange(0, 100) <= 95
                elif(check < 3):
                    roll = random.randrange(0, 1000) <= 997
                else:
                    roll = random.randrange(0, 1000000)

                if(roll == True):
                    #print("Jackpot!: "+str(numbers[current])+" vs "+str(chosen_number))
                    final_number = score
                    chosen_number = numbers[current]
            current += 1
        return chosen_number 


    def z_score(self, num):
        return (num - self.mean) / self.sigma


mean = 2500



nd = NormalDistribution(mean, 1)

for i in range(100000):
    sample = nd.sample_number()
    #sample = random.randrange(0, 100)
    if(sample in bucket.keys()):
        bucket[sample] += 1
    else:
        bucket[sample] = 1

print(bucket)
x = bucket.keys()
y = bucket.values()

matplotlib.plot(x, y, 'o')
matplotlib.show()