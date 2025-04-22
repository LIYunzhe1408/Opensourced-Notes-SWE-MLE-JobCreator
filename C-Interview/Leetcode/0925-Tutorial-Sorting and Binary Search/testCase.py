from mergeSort import mergeSort
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertSort import insertSort
from quickSort import quickSort


test_list = [7, 2, 6, 3, 8, 4, 5]

print("================Single Test==================")
print("Initial", test_list)
print("--------------------------------------")

sortAlgo = quickSort
result = sortAlgo(test_list, 0, len(test_list))

print("Result", result)


print("=================Joint Test==================")
print("Initial", test_list)
print("--------------------------------------")

sortAlgoList = {"bubbleSort": bubbleSort, "selectionSort": selectionSort, "insertSort": insertSort,
                "mergeSort": mergeSort, "quickSort": quickSort}

for algoKey in sortAlgoList.keys():
    if algoKey == "quickSort":
        result = sortAlgoList[algoKey](test_list, 0, len(test_list))
    else:
        result = sortAlgoList[algoKey](test_list)
    print(algoKey, ": ", result)
