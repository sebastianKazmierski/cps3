import matplotlib.pyplot as plt

from cps3.filter import Filter
from enums.type_of_plot import PlotType
from signal_generators2.rectangular_signal import RectangularSignal
from signal_generators2.sin import SinGenerator
from draw.draw_plot import create_arguments
from signal_generators2.traiangul_signal import TriangularSignal
from signals.signal_operation import SignalOperation


def rysuj_sinus():
    gen = SinGenerator()
    signal_operation = SignalOperation()
    triangular_gen = TriangularSignal()
    triangular_signal = triangular_gen.generate(1, 0, 1, 0.10, 0.7,  10001.0)

    sin_signal = gen.generate(1, 0, 0.005, 0.001, 100000.0)
    triangular_signal = gen.generate(0.3, 0, 0.005, 0.00015, 100000.0)

    signal = signal_operation.add(sin_signal, triangular_signal)

    filter1 = Filter(100, 33)

    filteredSignal = filter1.filter(signal)

    plot_type = PlotType.CONTINUOUS

    # draw_bar(filteredSignal, plot_type, bar)

    period = 1 / signal.sampling_frequency
    arguments = create_arguments(signal.start_time, period, len(signal.samples))

    period2 = 1 / filteredSignal.sampling_frequency
    arguments2 = create_arguments(filteredSignal.start_time, period, len(filteredSignal.samples))

    period3 = 1 / triangular_signal.sampling_frequency
    arguments3 = create_arguments(triangular_signal.start_time, period, len(triangular_signal.samples))

    period4 = 1 / sin_signal.sampling_frequency
    arguments4 = create_arguments(sin_signal.start_time, period, len(sin_signal.samples))

    # # draw_bar(signal, plot_type, bar)
    # bar.show()

    # plt.plot(arguments2, filteredSignal.samples)
    plt.plot(arguments, signal.samples)
    # plt.plot(arguments3, triangular_signal.samples)
    # plt.plot(arguments4, sin_signal.samples)

    plt.legend(["Dataset 1", "Dataset 2"])

    plt.show()

    # reconstructed_signal = signal_after_sinc
    # errors_classes = ReconstructionError.__subclasses__()
    #
    # errors = list(map(lambda clazz: clazz(signal, reconstructed_signal), errors_classes))
    # for error in errors:
    #     print(f"{error.get_name()}: {error.value}")


if __name__ == "__main__":
    rysuj_sinus()
