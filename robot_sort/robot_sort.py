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
        '''
        Sort the robot's list.
        Must sort numbers from smallest to largest.
        Doesn't return anything. Just performs the sort. The list gets returned when robot._list is printed.

        **Robot starts at list[0]. So if robot can move right, perform some operations.

        Robot needs to be able to grab the first element since the class is instantiated with None. How do I do this?

        if robot's item is none, swap item?
        I think at the end, the last thing we'll have to do is swap the last item to be sorted with None, so that None goes back to the current item being held. Until then, there will alway be one item in the list that is None

        Notes, attempt 2:
        Use light to signify if a sort happened?

        I can't make it do multiple loops that push it all the way back to position 0, because it has no way of knowing when to stop. With the restraints I can't tell it how many times to loop or when it should break out of the loop. So I either need to do one iteration through the whole list, or manually move left and right...

        Use "None" as signifier of end of list? Move None through? Placeholder for sorted item?

        If None is placeholder for item, that means it needs to find the smallest item on the first go. Then second, then third, etc.

        While light is on:
            While robot can move right:
                move right
                compare items...if -1,  don't do anything but if 1, swap item

                Once item is swapped, keep going until the current item gets to the end of the list
                move the current item to the place where None is -- gotta go left
                Move None right and swap again so that None is in the next index
                

        '''

        '''
        Steps, attempt 1
        
        Set light on. On == true self.set_light_on
        While light is on, (while self.light_is_on) loop through the list. The light will be turned off at the end, once it is done sorting, and that is how we'll break out of the while loop.

        If self.compare_item == None, swap item (so that None enters the list, and list[0] becomes currently held item)

        Check if robot can move right, and if so, move right. This will put us at position 1.

        Compare item. If compare item returns -1, check if can move right, if true, move right. Puts us at l[1].

        Compare item. If compare item returns 1, swap item.

        Keep going through list making comparisons. If can_move_right returns False, check if robot can move left, if it can move left. Loop and do so until it reaches position 0?
        
        '''
        # if light not on, turn it on
        if not self.light_is_on():
            self.set_light_on()
        
        # while the light is on, perform:
        while self.light_is_on():

            self.swap_item()

            # while the robot can move right, compare items
            while self.can_move_right():
                # if held item is greater than item in the last position in the list and robot can no longer move right, swap the items.
                # if self.compare_item() == -1 and not self.can_move_right():
                #     self.swap_item()
                #     self.move_left()
                self.move_right()
                # if held item is less than item at current list position, move right
                if self.compare_item() == -1:
                    self.move_right()
                # if held item is greater than item at current list position, swap items
                elif self.compare_item() == 1:
                    self.swap_item()
                    self.move_right()
            else:
                while self.can_move_left() and self.compare_item() != None:
                    self.move_left()

            # if self.compare_item() == None:
            #     self.swap_item()

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)