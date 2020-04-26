import matplotlib.pyplot as plt
from signals.signal import Signal
from enums.type_of_periodical import SignalPeriodic
from enums.type_of_plot import PlotType


def display(signal: Signal, plot_type: PlotType, number_of_compartment: int):
    bar = plt.figure(1)
    draw_bar(signal, plot_type, bar)
    histogram = plt.figure(2)
    draw_histogram(signal, number_of_compartment)
    bar.show()
    histogram.show()


def draw_bar(signal: Signal, plot_type: PlotType, fig):
    axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    period = 1 / signal.sampling_frequency
    arguments = create_arguments(signal.start_time, period, len(signal.samples))
    if plot_type == PlotType.DISCRETE:
        draw_discrete_signal(arguments, axes1, signal)
    elif plot_type == PlotType.CONTINUOUS:
        draw_continuous_signal(arguments, axes1, signal)


# FIXME TU SIE WLACZA RYSOWANIE LINII NA WYKRESIE - > linestyle='-' dla ciaglej linestyle='--' dla przerywanej
def draw_discrete_signal(arguments, axes1, signal):
    axes1.plot(arguments, signal.samples, color='red', linestyle='--',
               marker='o')


def draw_continuous_signal(arguments, axes1, signal):
    axes1.plot(arguments, signal.samples, color='red', linewidth=3,
               linestyle='-')


def draw_histogram(signal: Signal, number_of_compartment: int):
    if signal.signal_periodic == SignalPeriodic.YES:
        number_of_samples_in_one_period = signal.get_number_of_samples_in_one_period()
        number_of_samples_in_period = len(
            signal.samples) // number_of_samples_in_one_period * number_of_samples_in_one_period
    else:
        number_of_samples_in_period = len(signal.samples)

    bins = count_intervals2(signal, number_of_compartment)
    plt.hist(signal.samples[:number_of_samples_in_period], bins=bins, edgecolor="k")
    plt.xticks(bins)


def create_arguments(start: float, step: float, length: int):
    arguments = []
    value = start
    for i in range(length):
        arguments.append(value)
        value += step
    return arguments


def count_min_max(signal: Signal, number_of_compartment: int):
    min_value = signal.samples[0]
    max_value = signal.samples[0]

    for sample in signal.samples:
        if sample < min_value:
            min_value = sample
        elif sample > max_value:
            max_value = sample
    return min_value, max_value


def count_intervals2(signal: Signal, number_of_intervals: int):
    min_value, max_value = count_min_max(signal, number_of_intervals)
    step = (max_value - min_value) / number_of_intervals
    intervals = [min_value]
    low_value = min_value

    for i in range(number_of_intervals):
        low_value += step
        intervals.append(low_value)
    return intervals
