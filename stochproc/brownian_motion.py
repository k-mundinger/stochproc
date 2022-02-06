import numpy as np

from stochproc.process import Process


class BrownianMotion(Process):

    """N-dimensional Brownian motion."""

    def get_increments(self):

        return np.random.normal(0,
                                np.sqrt(self.dt),
                                size=(self.dim, self.num_steps - 1))
                                

    def get_trajectory(self):

        increments = self.get_increments()
        increments_and_start = np.concatenate((self.start_value, increments),
                                              axis=1)

        return np.cumsum(increments_and_start, axis=1)
