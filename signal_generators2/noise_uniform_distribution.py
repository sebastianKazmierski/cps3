import numpy as np

from signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from signal_type import SignalType
from type_of_periodical import SignalPeriodic


class UniformDistribution(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float, fill_factor: float,
                 sampling_frequency: float) -> Signal:
        x = self.get_arguments(start_time, duration, sampling_frequency)

        y = np.random.rand(len(x)) * (2*amplitude) - amplitude
        z = list(y)

        return Signal(start_time, 1 / period, sampling_frequency, z, SignalType.REAL, SignalPeriodic.NO)
