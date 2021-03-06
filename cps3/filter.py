import math
from signals.signal import Signal
from cps3.splot import get_splot


def high_pass(n: int):
    return (-1) ^ n


def get_value(samples: list, index: int) -> float:
    if index < 0 or index > len(samples) - 1:
        return 0.0
    return samples[index]


class Filter:
    def __init__(self, m: int, k: int) -> None:
        super().__init__()
        self.m = m
        self.k = k

    def filter(self, signal: Signal) -> Signal:
        x = signal.samples
        n = len(x)

        splot = list(range(n))
        for i in range(n):
            point = 0
            for j in range(self.m - 1):
                point += (self.filter_impulsive_answer(j) * get_value(x, i - j))
                # point += high_pass(j) * self.hanning(j) * self.filter_impulsive_answer(j) * get_value(x, i - j)
            splot[i] = point

        signal2 = Signal(signal.start_time, signal.signal_frequency, signal.sampling_frequency, splot,
                         signal.signal_type, signal.signal_periodic)
        return signal2

    def filter_impulsive_answer(self, n: int):
        if n == (self.m - 1) / 2:
            return 2 / self.k
        return math.sin(2 * math.pi * (n - ((self.m - 1) / 2)) / self.k) / (math.pi * ((n - (self.m - 1)) / 2))

    def hanning(self, n: int):
        return 0.5 - 0.5 * math.cos(2 * math.pi * n / self.m)
