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
        """
        Sort the robot's list.

        Properties:

        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)
        """
        # Set the light to "on"
        self.set_light_on()

        # While light is on 
        while self.light_is_on():

            # Set light off to indicate a swap has not been made
            self.set_light_off()

            # For item in list
            for _ in range(-1, len(self._list)-1):

                # Check if robot can move to the right
                if self.can_move_right():

                    # Swap None with item at index 0
                    self.swap_item()
                    # Move to the right
                    self.move_right()
                
                    # Compare held item with item at index 1

                    # If either the item at hand, or the item at this
                    # index are None
                    # _item == None or _list[_position] == None
                    if self.compare_item() == None:
                        self.move_left()
                        self.swap_item()

                        self.move_right()
                        # Set light to on
                        self.set_light_on()

                    # If the item at hand is less than the item at that index
                    # _item < _list[_position]
                    elif self.compare_item() == -1:
                        # Move left and swap held item with item at index 0
                        self.move_left()
                        self.swap_item()
                        self.move_right()

                    # If the item at hand is equal than the item at that index
                    # _item == _list[_position]
                    elif self.compare_item() == 0:
                        self.move_left()
                        self.swap_item()
                        self.move_right()

                    # Else: If the item at hand is greater than the item at that index
                    # _item > _list[_position]                    
                    else:
                        # swap held item with item at index 1
                        self.swap_item()
                        # Move left and swap held item with item at index 0
                        self.move_left()
                        self.swap_item()
                        # Set light to on
                        self.set_light_on()
                        # Move back to index 1 and repeat
                        self.move_right()

                # Else move all the way to the start of the list
                else:
                    # While can_move_left is True AND the light is on
                    while self.can_move_left() and self.light_is_on():
                        # move to the left
                        self.move_left()

"""
        # Set the light to "on"
        self.set_light_on()

        # While the light is "on"
        while self.light_is_on():

            # Turn the light "off"
            self.set_light_off()

            # While the robot can move right
            while self.can_move_right():

                
                Compare the held item with the item in front of the robot:
                If the held item's value is greater, return 1.
                If the held item's value is less, return -1.
                If the held item's value is equal, return 0.
                If either item is None, return None.
                

                # Compare the element at this index with the _item (item at hand)
                result = self.compare_item()

                if result == 1:
                    # This means the item at hand is greater than the item at that index
                    # _item > _list[_position]
                    pass


                if result == 0:
                    # This means the item at hand is equal than the item at that index
                    # _item == _list[_position]
                    pass

                if result == None:
                    # This means that either the item at hand, or the item at this
                    # index are None
                    # _item == None or _list[_position] == None

                    # If the item at that index is None
                    #if self._list[self._position] == None:
                        # Swap
                    self.swap_item()
                        # Turn the light "on"
                        #self.set_light_on()

                    #else:

                        

                    # Swap
                    #self.swap_item()
                    # Turn the light "on"
                    #self.set_light_on()


                elif result == -1:
                    # This means the item at hand is less than the item at that index
                    # _item < _list[_position]
                    
                    # Swap
                    self.swap_item()
                    # Turn the light "on"
                    self.set_light_on()

                # If the element at this index is greater than _item (the item at hand)
                #if self._list[self._position] > self._item:
                    # Swap
                    #self.swap_item()
                    # Turn the light "on"
                    #self.set_light_on()

                # Move right  
                self.move_right()

            # Move left till position is 0
            while self.can_move_left():
                self.move_left()
                """
        



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)