from copy import deepcopy
from scipy.special import sinc

from numpy import arange, array

from converters.adc.sampling_rate import SamplingRate
from converters.dac.da_converter import DAConverter
from signals.signal import Signal


class SincReconstructor(DAConverter):
    def __init__(self, sampling_rate: SamplingRate):
        self._sampling_rate = sampling_rate

    def convert(self, signal: Signal, step: int) -> Signal:
        old_sampling_period = (signal.samples[-1] - signal.samples[0]) / len(signal.samples)
        new_sampling_period = (signal.samples[-1] - signal.samples[0]) / self._sampling_rate.rate

        new_samples = []
        new_x_values = self.get_signal_x_values(signal, new_sampling_period)
        for new_x in new_x_values:
            new_value = 0
            old_x_values = self.get_arguments(signal)
            for old_index in range(len(old_x_values)):
                new_value += signal.samples[old_index] * sinc(new_x / old_sampling_period - old_index)
            new_samples.append(new_value)

        new_signal = deepcopy(signal)
        new_signal.samples = new_samples
        new_signal.sampling_frequency = self._sampling_rate.rate
        return new_signal

    def get_signal_x_values(self, signal: Signal, new_sampling_period: float):
        end_time = signal.samples[-1]
        duration = end_time - signal.start_time
        timestamp = signal.start_time
        number_of_samples = int(duration / new_sampling_period)

        x_values = []
        for i in range(number_of_samples):
            x_values.append(timestamp)
            timestamp += new_sampling_period

        return x_values
