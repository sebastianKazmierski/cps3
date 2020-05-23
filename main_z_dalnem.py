import matplotlib.pyplot as plt

from converters.adc.rounding_quantizator import RoundingQuantizator
from converters.adc.sampler import Sampler
from converters.adc.sampling_rate import SamplingRate
from converters.dac.first_order_holder import FirstOrderHoldConverter
from converters.dac.sinc_reconstructor import SincReconstructor
from converters.dac.zero_order_hold import ZeroOrderHoldConverter
from cps3.filter import Filter
from draw.draw_plot import draw_bar
from enums.type_of_plot import PlotType
from errors.reconstruction_error import ReconstructionError
from errors.md import MD
from errors.mse import MSE
from errors.psnr import PSNR
from errors.snr import SNR
from errors.reconstruction_error import ReconstructionError
from signal_generators2.sin import SinGenerator
from signal_operation import SignalOperation
from cps3 import filter
from draw.draw_plot import create_arguments


def rysuj_sinus():
    gen = SinGenerator()
    signal = gen.generate(1, 0, 1, 0.05, 10000.0)

    filter1 = Filter(500, 50)

    filteredSignal = filter1.filter(signal)



    plot_type = PlotType.CONTINUOUS

    # sampler = Sampler()
    # sampled_signal = sampler.convert(signal, 1200)
    #
    # quantizator = RoundingQuantizator(3)
    # quantized_signal = quantizator.convert(signal, 1000)
    #
    # zoh = ZeroOrderHoldConverter()
    # signal_after_zoh = zoh.convert(sampled_signal, 1000)
    #
    # foh = FirstOrderHoldConverter()
    # signal_after_foh = foh.convert(sampled_signal, 1000)
    #
    # sinc = SincReconstructor(SamplingRate(10000))
    # signal_after_sinc = sinc.convert(sampled_signal, 5)

    # bar = plt.figure(1)
    # # draw_bar(signal, plot_type, bar)
    # draw_bar(filteredSignal, plot_type, bar)

    period = 1 / signal.sampling_frequency
    arguments = create_arguments(signal.start_time, period, len(signal.samples))

    period2 = 1 / filteredSignal.sampling_frequency
    arguments2 = create_arguments(filteredSignal.start_time, period, len(filteredSignal.samples))

    # # draw_bar(signal, plot_type, bar)
    # bar.show()

    plt.plot(arguments2, filteredSignal.samples)
    plt.plot(arguments, signal.samples)


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
