import numpy as np
import math
from signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from signal_type import SignalType
from type_of_periodical import SignalPeriodic


class SinStraightenedInOneHalf(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float, fill_factor: float,
                 sampling_frequency: float) -> Signal:
        x = self.get_arguments(start_time, duration, sampling_frequency)

        y = 0.5 * amplitude * (np.sin(((2 * math.pi) / period) * (x - start_time)) + abs(np.sin(((2 * math.pi) / period)
                                                                                                * (x - start_time))))

        return Signal(start_time, 1 / period, sampling_frequency, y, SignalType.REAL, SignalPeriodic.YES)
