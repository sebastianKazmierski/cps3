import matplotlib.pyplot as plt
import numpy as np

from converters.adc.rounding_quantizator import RoundingQuantizator
from converters.adc.sampler import Sampler
from converters.dac.first_order_holder import FirstOrderHoldConverter
from converters.dac.sinc_reconstructor import SincReconstructor
from converters.dac.zero_order_hold import ZeroOrderHoldConverter
from draw.draw_plot import draw_bar
from enums.type_of_plot import PlotType
from signal_generators2.sin import SinGenerator
from converters.adc.sampling_rate import SamplingRate


def rysuj_sinus():
    gen = SinGenerator()
    signal = gen.generate(1, 0, 1, 1, 10000.0)
    plot_type = PlotType.DISCRETE

    sampler = Sampler()
    sampled_signal = sampler.convert(signal, 1000)

    quantizator = RoundingQuantizator(2)
    quantized_signal = quantizator.convert(signal, 1000)

    zoh = ZeroOrderHoldConverter()
    signal_after_zoh = zoh.convert(sampled_signal, 5)

    foh = FirstOrderHoldConverter()
    signal_after_fox = foh.convert(sampled_signal, 5)

    sinc = SincReconstructor(SamplingRate(100))
    signal_after_sinc = sinc.convert(sampled_signal, 5)

    bar = plt.figure(1)
    # draw_bar(signal, plot_type, bar)
    # draw_bar(sampled_signal, plot_type, bar)
    # draw_bar(quantized_signal, plot_type, bar)
    draw_bar(signal_after_sinc, plot_type, bar)
    bar.show()

    print("Probki oryginał: " + str(len(signal.samples)))
    print("Probki sampled: " + str(len(sampled_signal.samples)))
    print("Probki sinced: " + str(len(signal_after_sinc.samples)))



if __name__ == "__main__":
    rysuj_sinus()
