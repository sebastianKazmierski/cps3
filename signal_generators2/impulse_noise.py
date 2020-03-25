from signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from signal_type import SignalType
from type_of_periodical import PeriodicalSignal
import numpy as np


class ImpulseNoise(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float, probability: float,
                 sampling_frequency: float) -> Signal:

        y = list(range(round(duration * sampling_frequency)))
        for i in range(round(duration * sampling_frequency)):
            random_number = np.random.rand()
            if random_number < probability:
                y[i] = amplitude
            else:
                y[i] = 0

        frequency = 1 / period
        return Signal(start_time, frequency, sampling_frequency, list(y), SignalType.REAL, PeriodicalSignal.NO)
