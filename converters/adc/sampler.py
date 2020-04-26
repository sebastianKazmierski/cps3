from copy import deepcopy

from converters.adc.ad_converter import ADConverter
from enums.type_of_periodical import SignalPeriodic
from signals.signal import Signal


class Sampler(ADConverter):
    def convert(self, signal: Signal, sampling_ratio: int) -> Signal:
        new_signal = deepcopy(signal)
        new_signal.sampling_frequency /= sampling_ratio
        new_signal.samples = signal.samples[0::sampling_ratio]
        new_signal.signal_periodic = SignalPeriodic.NO
        return new_signal
