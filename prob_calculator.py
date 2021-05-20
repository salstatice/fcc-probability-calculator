import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for num_balls in range(value):
                self.contents.append(key)

    def draw(self, num_balls_drawn):
        if len(self.contents) < num_balls_drawn:
            return self.contents
        else:
            result = [ self.contents.pop(random.randint(0, len(self.contents)-1)) for i in range(num_balls_drawn) ]
            return result  


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_match = 0
    
    # turn expected_balls dict to list
    expected = []
    for key, value in expected_balls.items():
        for num_balls in range(value):
            expected.append(key)

    for num in range(num_experiments):
        # draw balls
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        
        # compare balls drawn with expected
        expected_copy = expected.copy()
        for ball in balls_drawn:
            if ball in expected_copy:
                expected_copy.remove(ball)
        if expected_copy == []:
            num_match += 1 

    probability = num_match / num_experiments
    return probability
