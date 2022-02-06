import warnings
from abc import ABC, abstractmethod
from typing import Optional

import numpy as np
import plotly.graph_objects as go


class Process(ABC):
    """The abstract base class for stochastic processes.

    :param
    """

    def __init__(self,
                 starttime: float = 0,
                 endtime: float = 1,
                 num_steps: int = 1000,
                 dim: int = 1,
                 start_value: Optional[np.ndarray] = None):

        if starttime >= endtime:

            raise ValueError("starttime must be bigger than endtime.")

        self.starttime = starttime
        self.endtime = endtime

        if not isinstance(num_steps, int):

            raise ValueError("num_steps must be a positive integer.")

        self.num_steps = num_steps
        self.timeaxis = np.linspace(0, endtime, num_steps)
        self.dt = self.timeaxis[1] - self.timeaxis[0]

        if not isinstance(dim, int):

            raise NotImplementedError(
                "Non-integer dimensions are currently not supported.")

        self.dim = dim

        if start_value is None:
            self.start_value = np.zeros(shape=(self.dim, 1))
        else:
            self.start_value = start_value

    def __repr__(self):

        repr_str = f"""Process(start = {self.starttime}, end = {self.endtime}, dt = {self.dt}, dim = {self.dim})"""

        return repr_str

    @abstractmethod
    def get_increments(self):

        return

    @abstractmethod
    def get_trajectory(self):

        return

    def get_radial_part(self, trajectory: Optional[np.ndarray] = None):

        if trajectory is None:
            trajectory = self.get_trajectory()

        return np.linalg.norm(trajectory, axis=0)

    def plot_trajectory(self):
        """Plot."""

        trajectory = self.get_trajectory()
        

        if self.dim == 1:

            fig = go.Figure()

            path = go.Scatter(
                x=self.timeaxis,
                y=trajectory.squeeze(),
                opacity=.8,
                visible=True,
                line=dict(width=1),
            )
            fig.add_trace(path)

            fig.update_layout(autosize=False, width=900, height=900)

            fig.show()

        if self.dim == 2:

            fig = go.Figure()

            path = go.Scatter(
                x=trajectory[0],
                y=trajectory[1],
                opacity=.8,
                line=dict(width=1),
            )

            fig.add_trace(path)

            fig.update_layout(autosize=False, width=900, height=900)

            fig.show()

        if self.dim >= 3:

            radial_part = self.get_radial_part(trajectory)

            if self.dim > 3:
                warnings.warn(
                    "The dimension of the process is > 3! Plotting first 3 components."
                )

            fig = go.Figure()

            path = go.Scatter3d(
                x=trajectory[0],
                y=trajectory[1],
                z=trajectory[2],
                opacity=.3,
                visible=True,
                line=dict(width=3),
                marker=dict(size=1,
                            color=radial_part,
                            colorscale="sunset",
                            opacity=0.5),
            )
            fig.add_trace(path)

            fig.update_layout(autosize=False, width=900, height=900)

            fig.show()
