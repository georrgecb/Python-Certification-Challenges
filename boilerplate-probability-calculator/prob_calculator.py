import random
import copy

class Hat(object):

    def __init__(self, **balls):
        self.balls = balls # {"red": 2, "blue": 1}

        # The dictionary is converted to a list of strings,
        # containing one item for each ball:

        self.contents = [] # ["red", "red", "blue"]
        loop_nr = 0

        for color, number in self.balls.items():

            while loop_nr < number:
                self.contents.append(color)
                loop_nr += 1

            loop_nr = 0

    def draw(self, input_number): #3

        # Remove balls at random from self.contents and return
        # those balls as a list of strings:

        random_list = []
        if input_number <= len(self.contents) : #5

            number = 0

            while number < input_number: # n < 3

                random_index = random.randint(0, (len(self.contents) - 1))

                random_list.append(self.contents[random_index])

                # The balls picked should not go back to the
                # main list - self.contents.
                del self.contents[random_index]

                number += 1
        else:
            random_list = self.contents

        return random_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    N = 0
    M = 0
    Z = 0

    expected_list = []
    count = 0

    for color, number in expected_balls.items():

        while count < number:
            expected_list.append(color)
            count += 1

        count = 0

    while N < num_experiments :
        main_list = copy.deepcopy(hat)
        draw_list = main_list.draw(num_balls_drawn)

        match = True
        for ball in expected_list:

            if ball in draw_list:
                draw_list.remove(ball)

            else:
                match = False

        if match == True:
            M += 1

        N += 1
        
    probability = M / N
    return probability