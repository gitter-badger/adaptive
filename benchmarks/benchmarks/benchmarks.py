import adaptive

import numpy as np
import random


offset = random.uniform(-0.5, 0.5)

def f_1d(x, offset=offset):
    a = 0.01
    return x + a**2 / (a**2 + (x - offset)**2)


def f_2d(xy):
    x, y = xy
    a = 0.2
    return x + np.exp(-(x**2 + y**2 - 0.75**2)**2/a**4)


class TimeLearner1D:
    def setup(self):
        self.learner = adaptive.Learner1D(f_1d, bounds=(-1, 1))

    def time_run(self):
        for _ in range(1000):
            points, _ = self.learner.choose_points(1)
            self.learner.add_data(points, map(f_1d, points))


class TimeLearner2D:
    def setup(self):
        self.learner = adaptive.Learner2D(f_2d, bounds=[(-1, 1), (-1, 1)])
        self.xs = np.random.rand(50**2, 2)
        self.ys = np.random.rand(50**2)

    def time_run(self):
        for _ in range(50**2):
            points, _ = self.learner.choose_points(1)
            self.learner.add_data(points, map(f_2d, points))

    def time_choose_points(self):
        for _ in range(50**2):
            self.learner.choose_points(1)

    def time_add_point(self):
        for x, y in zip(self.xs, self.ys):
            self.learner.add_point(x, y)
