import numpy as np

from converters.adc.ad_converter import ADConverter
from enums.type_of_periodical import SignalPeriodic
from converters.adc.sampling_rate import SamplingRate
from signals.signal import Signal
from copy import deepcopy


class RoundingQuantizator(ADConverter):

    def __init__(self, bits: int) -> None:
        super().__init__()
        self.bits = bits

    def convert(self, signal: Signal, sampling_ratio: int) -> Signal:
        new_signal = deepcopy(signal)
        new_signal.sampling_frequency /= sampling_ratio
        new_signal.signal_periodic = SignalPeriodic.NO

        samples = self._get_samples(signal.samples[0::sampling_ratio])
        new_signal.samples = samples
        return new_signal

    def _get_samples(self, samples: list) -> list:
        max_value = max(samples)
        min_value = min(samples)
        diff = max_value - min_value

        sections_count = 2 ** self.bits
        section_diff = diff / (sections_count - 1)

        sections = list(np.arange(min_value, max_value + section_diff, section_diff))
        new_values = _get_new_values(samples, sections)
        return new_values


def _get_new_values(samples: list, sections: list) -> list:
    return list(map(lambda sample: _get_new_value(sample, sections), samples))


def _get_new_value(sample: float, sections: list) -> float:
    values = list(map(lambda section: abs(section - sample), sections))
    return sections[values.index(min(values))]
