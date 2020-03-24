from signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from signal_type import SignalType
import numpy as np
import math
import matplotlib.pyplot as plt


class SinGenerator(SignalGenerator):
    def __init__(self, signal_type: SignalType):
        self.signal_type = signal_type

    def generate(self, amplitude: float, start_time: float, duration: float, period: float, fill_factor: float,
                 sampling_frequency: float) -> Signal:
        ts = 1 / sampling_frequency
        txs = np.arange(0, (start_time + duration + ts / 2), ts)

        y = amplitude * np.sin(((2 * math.pi) / period) * (txs - start_time))

        return Signal(start_time, 1/period, sampling_frequency, SignalType.REAL, y)


