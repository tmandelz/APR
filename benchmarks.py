import statistics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import timeit as timeit


def GetMaxReward(array):
    result = np.zeros(0)
    sumi = 0
    for i in range(array.size):
        # wert von startindex als Startsumme definieren
        sumi = array[i]
        for j in range(array.size):
            # start index bigger than end index -> ignore (combination already calculated)
            if i < j:
                # add new endindex value to sum
                sumi = sumi + array[j]
                result = np.append(result, [sumi])
    print(max(result))


def Benchmark(arraysize):
    performanceResults = pd.DataFrame({'average': [0]})

    for i in range(9, arraysize):
        rng = np.random.default_rng()
        rints = rng.integers(-100, 100, size=i)
        arrayGenerated = np.array(rints)
        execution_time = timeit.repeat(
            lambda: GetMaxReward(arrayGenerated), repeat=1, number=1,)
        print(execution_time)
        performanceResults = performanceResults.append(
            {'average': np.mean(execution_time)}, ignore_index=True)

    print(performanceResults)
    plt.scatter(performanceResults.index, performanceResults['average'])
    plt.show()


# Array
array = np.array([31, -41, 59, 26, -53, 58, 97, -93, -23])
GetMaxReward(array)
# Verdoppelung 9 -> 18
Benchmark(18)
# Vergrösserung des Arrays
Benchmark(100)
# Vergrösserung des Arrays
Benchmark(500)
