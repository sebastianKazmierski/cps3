from signal_type import SignalType
import matplotlib.pyplot as plt
import numpy as np


class Signal:
    def __init__(self, start_time: float, signal_frequency: float, sampling_frequency: float, signal_type: SignalType,
                 samples: list):
        self.start_time = start_time
        self.sampling_frequency = sampling_frequency
        self.signal_type = signal_type
        self.samples = samples
        self.signal_frequency = signal_frequency

    def display(self):
        fig1 = plt.figure(figsize=(10, 4))
        axes1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
        period = 1 / self.sampling_frequency
        stop_time = self.start_time + (period * (len(self.samples)))
        axes1.plot(np.arange(self.start_time, stop_time, period), self.samples, color='red', linewidth=3,
                   linestyle='-')
        plt.show()

    def get_number_of_samples_in_one_period(self):
        signal_period = 1 / self.signal_frequency
        sampling_period = 1 / self.sampling_frequency
        return round((signal_period / sampling_period) * self.sampling_frequency)

    def sum_of_samples(self, start_index: int, stop_index: int):
        i = start_index
        sum = 0.0
        while i < stop_index:
            sum += self.samples[i]
        return sum

    def average_signal_value(self):
        number_of_samples = self.get_number_of_samples_in_one_period()
        return self.sum_of_samples(0, number_of_samples) / number_of_samples
