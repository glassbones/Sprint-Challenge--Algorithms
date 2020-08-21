class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)
        self.maxDiff = None

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        def merge(arrA, arrB):
            arrC = []
            while(arrA and arrB):
                if(arrA[0] >= arrB[0]): arrC.append(arrB.pop(0)) 
                else: arrC.append(arrA.pop(0))
            if(arrA): arrC += arrA
            else: arrC += arrB
            return arrC

        def merge_sort(arr):
            if (arr == [] or arr[-1] == arr[0]): return arr # if arr has no elements or 1 element return arr
            return merge(merge_sort(arr[::2]), merge_sort(arr[1::2])) # else take the ordered halves and compare them in merge
        """

        def merge_sort(arr):
            # The last array split
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            # Perform merge_sort recursively on both halves
            left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

            # Merge each side together
            return merge(left, right, arr.copy())


        def merge(left, right, merged):

            left_cursor, right_cursor = 0, 0
            while left_cursor < len(left) and right_cursor < len(right):
            
                # Sort each one and place into the result
                if left[left_cursor] <= right[right_cursor]:
                    merged[left_cursor+right_cursor]=left[left_cursor]
                    left_cursor += 1
                else:
                    merged[left_cursor + right_cursor] = right[right_cursor]
                    right_cursor += 1
                    
            for left_cursor in range(left_cursor, len(left)):
                merged[left_cursor + right_cursor] = left[left_cursor]
                
            for right_cursor in range(right_cursor, len(right)):
                merged[left_cursor + right_cursor] = right[right_cursor]

            return merged

        self._list = merge_sort(self._list)



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)