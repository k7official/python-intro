import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      while v:
        self.contents.append(k)
        v -= 1

  def draw(self, number_of_balls):
    if number_of_balls > len(self.contents):
      return self.contents
    else:
      removed_balls = []
      for i in range(0, number_of_balls):
        ball = random.choice(self.contents)
        removed_balls.append(ball)
        self.contents.remove(ball)
      return removed_balls
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(0, num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    prob = True
    for key, val in expected_balls.items():
      if balls_drawn.count(key) >= val:
        prob = True
      else:
        prob = False
        break
    if prob:
      M += 1

  estimate = M / num_experiments
  return estimate
