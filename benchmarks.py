import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import timeit as timeit


def GetMaxRewardFirstTry(array):
    result = np.zeros(0)
    sumi = 0
    for i in range(array.size):
        # wert von startindex als Startsumme definieren
        sumi = array[i]
        for j in range(array.size):
            # start index bigger than end index -> ignore (combination already calculated)
            if i < j:
                # add new endindex value to sum
                sumi += array[j]
                result = np.append(result, [sumi])

    if(result.size != 0):
        print(f"Grösste Differenz ist: {max(result)}")


def GetMaxRewardSecondTry(array):
    result = np.zeros(0)
    sumi = 0
    for i in range(array.size):
        # Verlauf berechnen (Kurs)
        sumi += array[i]
        result = np.append(result, sumi)
        # maximum subtrahiert vom minimum der verlauf kurve ergibt die grösste differenz

    if(result.size != 0):
        print(f"Grösste Differenz ist: {max(result) - min(result)}")


def BenchmarkGetMaxReward(func, arraysize):
    performanceResults = pd.DataFrame({'average': [0]})

    for i in range(0, arraysize):
        # generieren von differenzen
        rng = np.random.default_rng()
        rints = rng.integers(low=-10, high=10, size=i)
        arrayGenerated = np.array(rints)

        # Benchmarking mit Timeit Funktionen
        execution_time = timeit.repeat(
            lambda: func(arrayGenerated), repeat=1, number=1,)
        print(execution_time)
        performanceResults = performanceResults.append(
            {'average': np.mean(execution_time)}, ignore_index=True)

    print(performanceResults)

    # Plotten von Verlauf der Zeiten
    plt.scatter(performanceResults.index, performanceResults['average'])
    plt.title(f"{func.__name__} mit Arraylänge {arraysize}")
    plt.xlabel("Arraylänge")
    plt.ylabel("Zeit in Sekunden")
    plt.show()


# Array
array = np.array([31, -41, 59, 26, -53, 58, 97, -93, -23])

GetMaxRewardFirstTry(array)
GetMaxRewardSecondTry(array)


# # Benchmarks

# Verdoppelung 9 -> 18
BenchmarkGetMaxReward(GetMaxRewardFirstTry, 18)
# Vergrösserung des Arrays
BenchmarkGetMaxReward(GetMaxRewardFirstTry, 100)


BenchmarkGetMaxReward(GetMaxRewardSecondTry, 18)
# Vergrösserung des Arrays
BenchmarkGetMaxReward(GetMaxRewardSecondTry, 100)
# Vergrösserung des Arrays
BenchmarkGetMaxReward(GetMaxRewardSecondTry, 1000)
