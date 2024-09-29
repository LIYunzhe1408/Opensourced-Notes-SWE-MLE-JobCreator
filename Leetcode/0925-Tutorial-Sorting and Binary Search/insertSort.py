def insertSort(array):
    N = len(array)  # how many cards I have

    for i in range(1, N):
        picked_card = array[i]

        j = i - 1
        # This replaces the for loop, because the loop should be break when the order is sorted.
        # Using for loop will be too tedious using if statement.
        while picked_card < array[j] and j >= 0:
            array[j + 1] = array[j]
            j -= 1

        # for j in range(i-1, -1, -1):
        #     if picked_card < array[j]:
        #         array[j+1] = array[j]
        #     else:
        #         break
        array[j+1] = picked_card
    return array
