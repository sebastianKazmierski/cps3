from signal_type import SignalType
# import matplotlib.pyplot as plt
import numpy as np

from type_of_periodical import SignalPeriodic


class Signal:
    def __init__(self, start_time: float, signal_frequency: float, sampling_frequency: float, samples: list,
                 signal_type: SignalType, signal_periodic: SignalPeriodic):
        self.start_time = start_time
        self.sampling_frequency = sampling_frequency
        self.signal_type = signal_type
        self.samples = samples
        self.signal_frequency = signal_frequency
        self.signal_periodic = signal_periodic

    # def display(self):
    #     fig1 = plt.figure(figsize=(10, 4))
    #     axes1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    #     period = 1 / self.sampling_frequency
    #     stop_time = self.start_time + (period * (len(self.samples)))
    #     axes1.plot(np.arange(self.start_time, stop_time, period), self.samples, color='red', linewidth=3,
    #                linestyle='-')
    #     plt.show()

    def get_number_of_samples_in_one_period(self):
        if self.signal_periodic == SignalPeriodic.YES:
            signal_period = 1 / self.signal_frequency
            sampling_period = 1 / self.sampling_frequency
            return round((signal_period / sampling_period))
        return len(self.samples)

    def sum_of_samples(self, start_index: int, stop_index: int):
        i = start_index
        sum = 0.0
        while i < stop_index:
            sum += self.samples[i]
            i += 1
        return sum

    def average_signal_value(self):
        number_of_samples = self.get_number_of_samples_in_one_period()
        return self.sum_of_samples(0, number_of_samples) / number_of_samples

    def sum_of_absolute_samples(self, start_index: int, stop_index: int):
        i = start_index
        sum = 0.0
        while i < stop_index:
            sum += abs(self.samples[i])
            i += 1
        return sum

    def absolute_average_signal_value(self):
        number_of_samples = self.get_number_of_samples_in_one_period()
        return self.sum_of_absolute_samples(0, number_of_samples) / number_of_samples

    def sum_of_square_samples(self, start_index: int, stop_index: int):
        i = start_index
        sum = 0.0
        while i < stop_index:
            sum += (self.samples[i]) ** 2
            i += 1
        return sum

    def average_power_of_signal(self):
        number_of_samples = self.get_number_of_samples_in_one_period()
        return self.sum_of_square_samples(0, number_of_samples) / number_of_samples

    def sum_of_absolute_samples_variance_average(self, start_index: int, stop_index: int):
        i = start_index
        average = self.average_signal_value()
        sum = 0.0
        while i < stop_index:
            sum += (self.samples[i] - average) ** 2
            i += 1
        return sum

    def signal_variance(self):
        number_of_samples = self.get_number_of_samples_in_one_period()
        return self.sum_of_absolute_samples_variance_average(0, number_of_samples) / number_of_samples

    def effective_value(self):
        return np.sqrt(self.average_power_of_signal())
