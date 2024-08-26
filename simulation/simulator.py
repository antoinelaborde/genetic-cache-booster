"""
A class handling the genetic algorithm simulation.
"""
import logging
import random
import time
from dataclasses import dataclass
from enum import Enum
from typing import Tuple



logger = logging.getLogger(__name__)

class MetricComputationMode(Enum):  # noqa
    DETERMINISTIC = "deterministic"
    STOCHASTIC = "stochastic"

@dataclass
class RunStepLog:
    is_collision: bool
    metric_computation_time_seconds: float


class Simulator:
    def __init__(
            self,
            metric_computation_time_seconds: float | Tuple[float, float],
            collision_probability: float
    ):
        """
        :param metric_computation_time_seconds: the time in seconds to compute the metrics for the simulator
            if float: the computation time is deterministic
            if (float, float): the computation time is chosen randomly in the range of provided float
        :param collision_probability: the probability that the metric has already been calculated before
        """
        self.metric_computation_time_seconds = metric_computation_time_seconds
        self.metric_computation_method: MetricComputationMode = MetricComputationMode.DETERMINISTIC \
            if isinstance(self.metric_computation_time_seconds, float) else MetricComputationMode.STOCHASTIC
        self.collision_probability = collision_probability

    def run(self, n: int):
        """
        Run the simulation
        :param n: the number of individuals to simulate
        """
        current_individual = 0
        step_logs = []
        while current_individual < n:
            is_collision = self.is_collision()
            if is_collision:
                logger.info("Collision detected -> use cache")
                computation_time = 0
            else:
                computation_time = self.compute_metric()
            step_log = RunStepLog(
                is_collision=is_collision,
                metric_computation_time_seconds=computation_time,
            )
            step_logs.append(step_log)
        return step_logs

    def compute_metric(self) -> float:
        """
        Compute the metric
        :return: the computation time
        """
        if self.metric_computation_method == MetricComputationMode.DETERMINISTIC:
            computation_time = self.metric_computation_time_seconds
        elif self.metric_computation_method == MetricComputationMode.STOCHASTIC:
            computation_time = random.uniform(
                a=min(self.metric_computation_time_seconds),
                b=max(self.metric_computation_time_seconds),
            )
        else:
            raise NotImplementedError
        time.sleep(computation_time)
        return computation_time

    def is_collision(self) -> bool:
        """
        Return True if a collision happened
        """
        return random.random() <= self.collision_probability
