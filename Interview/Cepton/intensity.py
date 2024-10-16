class Intensity:
    def __init__(self):
        self.difference_array = []

    def add(self, start, end, amount):
        if start >= end:
            print("Input range error.")
            raise

        if amount != 0:
            self.update_difference_array_at_position(start, amount)
            self.update_difference_array_at_position(end, -amount)
        else:
            print("Plz input another amount rather than 0.")
            raise

    def set(self, start, end, amount):
        """
        Assume the purpose of the set() funtion is to overwrite the value in the range.
        1. Get the initial intensity of the boundary position
        2. Remove configurations within the range
        3. Update difference array
        :param start[int]
        :param end[int]
        :param amount[int]
        """
        if start >= end:
            print("Input range error.")
            raise
        if amount == 0:
            print("Plz input another amount rather than 0.")
            raise

        idx_start, idx_end = self.find_position_index(start), self.find_position_index(end)
        intensity_start, intensity_end = 0, 0
        for i in range(idx_start):
            intensity_start += self.difference_array[i][1]
        for i in range(idx_end):
            intensity_end += self.difference_array[i][1]

        # TODO The time complexity of Pop operation in a list is O(N). Implementing within a loop results in O(N^2)
        # while idx_start < len(self.difference_array) and self.difference_array[idx_start][0] < end:
        #     self.difference_array.pop(idx_start)

        # Fixed The Del Slice operation costs O(N)
        del self.difference_array[idx_start:idx_end]

        self.update_difference_array_at_position(start, amount - intensity_start)
        self.update_difference_array_at_position(end, intensity_end - amount)

    def update_difference_array_at_position(self, position, amount):
        idx = self.find_position_index(position)
        if idx < len(self.difference_array) and self.difference_array[idx][0] == position:
            self.difference_array[idx][1] += amount
        else:
            self.difference_array.insert(idx, [position, amount])

    def find_position_index(self, position):
        """
        Binary Search to find the position with O(logN)
        :param position[int] value of the start/end point
        :return: left[int]
        """
        left = 0
        right = len(self.difference_array)
        while left < right:
            mid = (left + right) // 2
            if self.difference_array[mid][0] < position:
                left = mid + 1
            else:
                right = mid
        return left

    def get_segments(self):
        """
        Return list with expected format
        :return: result[list]
        """
        result = []
        increment = 0
        for element in self.difference_array:
            temp = increment
            increment += element[1]
            if temp != increment:
                result.append([element[0], increment])
        return result


intensity = Intensity()
try:
    # Case 1
    # intensity.add(10, 30, 1)
    # intensity.add(20, 40, 1)
    # intensity.add(10, 40, -2)

    # Case 2
    # intensity.add(10, 30, 1)
    # intensity.add(20, 40, 1)
    # intensity.add(10, 40, -1)
    # intensity.add(10, 40, -1)

    # Case 3
    # intensity.set(0, 20, 7)
    # intensity.set(5, 10, 3)

    # Case 4
    # intensity.add(0, 10, 5)
    # intensity.set(0, 10, 7)

    # Case 5
    intensity.add(10, 30, 1)
    intensity.add(20, 40, 1)
    intensity.add(10, 40, -1)
    intensity.add(10, 40, -1)

except:
    print("-----------------------------------------")
    print("Check the instruction above and try again")
    print("The Intensity below may not be correct")
finally:
    print("Intensity: ", 0 if len(intensity.get_segments()) == 0 else intensity.get_segments())

