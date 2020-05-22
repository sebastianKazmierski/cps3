import matplotlib.pyplot as plt

from converters.adc.rounding_quantizator import RoundingQuantizator
from converters.adc.sampler import Sampler
from converters.adc.sampling_rate import SamplingRate
from converters.dac.first_order_holder import FirstOrderHoldConverter
from converters.dac.sinc_reconstructor import SincReconstructor
from converters.dac.zero_order_hold import ZeroOrderHoldConverter
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


def rysuj_sinus():
    gen = SinGenerator()
    signal = gen.generate(1, 0, 1, 0.05, 10000.0)

    plot_type = PlotType.DISCRETE

    sampler = Sampler()
    sampled_signal = sampler.convert(signal, 1200)

    quantizator = RoundingQuantizator(3)
    quantized_signal = quantizator.convert(signal, 1000)

    zoh = ZeroOrderHoldConverter()
    signal_after_zoh = zoh.convert(sampled_signal, 1000)

    foh = FirstOrderHoldConverter()
    signal_after_foh = foh.convert(sampled_signal, 1000)

    sinc = SincReconstructor(SamplingRate(10000))
    signal_after_sinc = sinc.convert(sampled_signal, 5)

    bar = plt.figure(1)
    # draw_bar(signal, plot_type, bar)
    draw_bar(signal_after_sinc, plot_type, bar)
    bar.show()

    reconstructed_signal = signal_after_sinc
    errors_classes = ReconstructionError.__subclasses__()

    errors = list(map(lambda clazz: clazz(signal, reconstructed_signal), errors_classes))
    for error in errors:
        print(f"{error.get_name()}: {error.value}")


if __name__ == "__main__":
    rysuj_sinus()
