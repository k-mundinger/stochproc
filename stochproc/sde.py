import numpy as np

from typing import Callable, Optional

from stochproc.process import Process


class OneDimSDE(Process):

    """ A process X_t given as the solution of
    $$ dX_t = b(X_t, t)dt + /sigma(X_t, t)dB_t $$,
    where b is the drift, /sigma the volatility
    and B_t a standard brownian motion.

    :param b: Function of variables x and t
    :param sigma: function of variables x and t
    """

    def __init__(self,
                 b: Callable,
                 sigma: Callable,
                 starttime: float = 0,
                 endtime: float = 1,
                 num_steps: int = 1000,
                 dim: int = 1,
                 start_value: Optional[np.ndarray] = None):

        super().__init__(starttime = starttime,
                         endtime = endtime,
                         num_steps = num_steps,
                         dim = dim,
                         start_value = start_value)

        self.b = b
        self.sigma = sigma

    def get_trajectory(self):

        """ Implements the Euler-Maruyama-Scheme.
        https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method
        """

        dW_t = np.random.normal(0,
                            np.sqrt(self.dt),
                            size=self.num_steps)

        trajectory = np.zeros_like(self.timeaxis)
        trajectory[0] = self.start_value

        for i in range(1, self.num_steps):

            trajectory[i] = (trajectory[i-1] +
                             self.b(trajectory[i-1], self.timeaxis[i-1]) * self.dt +
                             self.sigma(trajectory[i-1], self.timeaxis[i-1]) * dW_t[i-1])
        
        return trajectory

        # increments = self.get_increments()
        # return np.cumsum(increments)

    def get_increments(self):

        """ Implements the Euler-Maruyama-Scheme.
        https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method
        """

        dW_t = np.random.normal(0,
                            np.sqrt(self.dt),
                            size=self.num_steps)

        increments = np.zeros_like(self.timeaxis)
        increments[0] = self.start_value

        for i in range(1, self.num_steps):

            increments[i] = (self.b(increments[i-1], self.timeaxis[i-1]) * self.dt +
                             self.sigma(increments[i-1], self.timeaxis[i-1]) * dW_t[i-1])
        
        return increments
