#SIMULATION FOR GERMAN TANKS DILEMMA
#LIBRARIES
import random
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

#SUBROUTINES AND VARIABLES
N = 1000                               #Number of population
k = 20                                 #sample size
sample = []
estimates20 = []
maxList20 = []
estimates50 = []
maxList50 = []

def sampleCollection(sampleSize, popSize):       #Making the sample
    return random.sample(range(1, popSize + 1), sampleSize)  

def simulation(sampleSize, popSize):
    pList = []
    qList = []
    maximum = 0
    maxOnlyEstimate = 0
    N_hat = 0

    for i in range(10000):
        sample = sampleCollection(sampleSize, popSize)
        maximum = max(sample)

        #Method 1: The Estimator Function Method
        N_hat = (maximum * (sampleSize+1)/sampleSize) - 1
        pList.append(N_hat)

        #Method 2: The Maximum Only Method
        maxOnlyEstimate = maximum 
        qList.append(maxOnlyEstimate)

    return pList, qList

#MAIN PROGRAM

#Figure 1: Estimator vs Baseline (k=20)

#Running the simulation and collecting the results
estimatorList, maxList = simulation(20, N)
estimatorAverage = sum(estimatorList) / len(estimatorList)
maxAverage = sum(maxList) / len(maxList)

#Plotting the graph
plt.figure()

plt.hist(estimatorList, bins=50, alpha=0.6, label="Estimator method")

plt.hist(maxList, bins=50, alpha=0.6, label="Maximum-only method")

plt.axvline(N, color="black", linestyle="--", linewidth=3, zorder=10, label="True N")
plt.axvline(estimatorAverage, color="navy", linestyle="dashdot", linewidth=2.5, label="Estimator mean")
plt.axvline(maxAverage, color="saddlebrown", linestyle="dashdot", linewidth=2.5, label="Maximum-only mean")

plt.xlabel("Estimate of N")
plt.ylabel("Frequency")
plt.title("German tank problem: estimator vs maximum-only")
plt.legend()

plt.savefig("german_tank_estimator_vs_baseline.png", dpi=300, bbox_inches="tight")

# Figure 2: Scatter shrinks with sample size

#Running the simulation and collecting the results
estimates20, _ = simulation(20, N)
estimates50, _ = simulation(50, N)

#Plotting the graphs
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharex=True)

ax1.hist(estimates20, bins=50, alpha=0.7, color="red")

ax1.axvline(N, color="black", linestyle="--", linewidth=2)

ax1.set_title("k = 20")
ax1.set_xlabel("Estimate of N")
ax1.set_ylabel("Frequency")

ax2.hist(estimates50, bins=50, alpha=0.7, color="red")

ax2.axvline(N, color="black", linestyle="--", linewidth=2)

ax2.set_title("k = 50")
ax2.set_xlabel("Estimate of N")

plt.suptitle("Estimator scatter shrinks as sample size grows")

fig.savefig("german_tank_sample_size.png", dpi=300, bbox_inches="tight")
plt.show()


