# -*- coding: utf-8 -*-
from contextlib import contextmanager


@contextmanager
def restore(*learners):
    states = [learner.__getstate__() for learner in learners]
    try:
        yield
    finally:
        for state, learner in zip(states, learners):
            learner.__setstate__(state)


def run_learner(learner, n_points=1):
    """Evaluate the learner's function n_points times.

    Run the learner's `choose_points` and `add_point` methods
    while blocking the kernel. For example; this is useful to
    easily extract error messages.

    Parameters
    ----------
    learner : adaptive.BaseLearer object
        A learner that as choose_points, add_point, and function
        methods.
    n_points : int
        Number of points to evaluate.
    """
    for _ in range(n_points):
        xs, _ = learner.choose_points(1)
        for x in xs:
            y = learner.function(x)
            learner.add_point(x, y)
