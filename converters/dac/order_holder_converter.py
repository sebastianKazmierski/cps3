from abc import abstractmethod
from copy import deepcopy

from converters.dac.da_converter import DAConverter
from signals.signal import Signal


class OrderHolderConverter(DAConverter):
    def convert(self, signal: Signal, step: int) -> Signal:
        x_axis_values = self.get_arguments(signal)
        f = self.get_interpolation_function(x_axis_values, signal.samples)
        new_x_values = self.get_new_x_values(signal, step)
        new_samples = f(new_x_values)

        new_signal = deepcopy(signal)
        new_signal.samples = new_samples
        new_signal.sampling_frequency = signal.sampling_frequency * step
        return new_signal

    @abstractmethod
    def get_interpolation_function(self, x_values, y_values):
        pass
