import matplotlib.pyplot as plt
import numpy as np

from signal import Signal


def display(signal: Signal):
    fig1 = plt.figure(figsize=(10, 4))
    axes1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    period = 1 / signal.sampling_frequency
    stop_time = signal.start_time + (period * (len(signal.samples)))
    axes1.plot(np.arange(signal.start_time, stop_time, period), signal.samples, color='red', linestyle=' ',
               marker='o')
    plt.show()
