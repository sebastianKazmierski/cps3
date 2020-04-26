from numpy import linspace
from numpy.ma import arange

from signals.signal import Signal


class DAConverter:
    def convert(self, signal: Signal, step: int) -> Signal:
        pass

    def get_arguments(self, signal: Signal):
        step = 1 / signal.sampling_frequency
        duration = len(signal.samples) / signal.sampling_frequency
        return arange(signal.start_time, signal.start_time + duration, step)

    def get_new_x_values(self, signal: Signal, step: int):
        end_time = self._get_end_time(signal)
        return linspace(signal.start_time, end_time,
                        int(step * signal.get_number_of_samples_in_one_period()))

    def _get_end_time(self, signal: Signal) -> float:
        return signal.start_time + (len(signal.samples) - 1) / signal.sampling_frequency
