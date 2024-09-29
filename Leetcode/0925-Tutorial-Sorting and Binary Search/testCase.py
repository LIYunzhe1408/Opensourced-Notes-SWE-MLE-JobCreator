from mergeSort import mergeSort
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertSort import insertSort


test_list = [7, 2, 6, 3, 8, 4, 5]

print("================Single Test==================")
print("Initial", test_list)
print("--------------------------------------")

sortAlgo = insertSort
result = sortAlgo(test_list)

print("Result", result)


print("=================Joint Test==================")
print("Initial", test_list)
print("--------------------------------------")

sortAlgoList = {"bubbleSort": bubbleSort, "selectionSort": selectionSort, "insertSort": insertSort,
                "mergeSort": mergeSort}

for algoKey in sortAlgoList.keys():
    result = sortAlgoList[algoKey](test_list)
    print(algoKey, ": ", result)
