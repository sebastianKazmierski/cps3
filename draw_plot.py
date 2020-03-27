import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from df import get_arguments
from signal import Signal
from type_of_periodical import SignalPeriodic


def display(signal: Signal):
    fig1 = plt.figure(figsize=(10, 4))
    axes1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    period = 1 / signal.sampling_frequency
    arguments = create_arguments(signal.start_time, period, len(signal.samples))
    axes1.plot(arguments, signal.samples, color='red', linestyle=' ',
               marker='o')
    plt.show()


def create_arguments(start: float, step: float, length: int):
    arguments = []
    value = start
    for i in range(length):
        arguments.append(value)
        value += step
    return arguments


def display_bar(signal: Signal, number_of_compartment: int):
    if signal.signal_periodic == SignalPeriodic.YES:
        number_of_samples_in_one_period = signal.get_number_of_samples_in_one_period()
        number_of_samples_in_period = len(
            signal.samples) // number_of_samples_in_one_period * number_of_samples_in_one_period
    else:
        number_of_samples_in_period = len(signal.samples)

    bins = count_intervals2(signal, number_of_compartment)
    plt.hist(signal.samples[:number_of_samples_in_period], bins=bins, edgecolor="k")
    plt.xticks(bins)
    plt.show()


def count_min_max(signal: Signal, number_of_compartment: int):
    min_value = signal.samples[0]
    max_value = signal.samples[0]

    for sample in signal.samples:
        if sample < min_value:
            min_value = sample
        elif sample > max_value:
            max_value = sample
    return min_value, max_value


# def count_intervals(signal: Signal, number_of_intervals: int):
#     min_value, max_value = count_min_max(signal, number_of_intervals)
#     step = (max_value - min_value) / number_of_intervals
#     intervals = []
#     low_value = min_value
#
#     for i in range(number_of_intervals):
#         intervals.append(interval[low_value, low_value + step])
#         low_value += step
#
#     return intervals


def count_intervals2(signal: Signal, number_of_intervals: int):
    min_value, max_value = count_min_max(signal, number_of_intervals)
    step = (max_value - min_value) / number_of_intervals
    intervals = [min_value]
    low_value = min_value

    for i in range(number_of_intervals):
        low_value += step
        intervals.append(low_value)
    return intervals
