import numpy as np

from signals.signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from enums.signal_parameters import SignalParameters
from enums.signal_type import SignalType
from enums.type_of_periodical import SignalPeriodic


class GausDistribution(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float,
                 sampling_frequency: float) -> Signal:
        x = self.get_arguments(start_time, duration, sampling_frequency)

        y = np.random.randn(len(x)) * (2 * amplitude) - amplitude
        z = list(y)

        return Signal(start_time, 1 / period, sampling_frequency, z, SignalType.REAL, SignalPeriodic.NO)

    def get_name(self) -> str:
        return "Szum gaussowski"

    def get_list_required_parameters(self):
        return [SignalParameters.AMPLITUDE, SignalParameters.START_TIME, SignalParameters.DURATION,
                SignalParameters.PERIOD, SignalParameters.SAMPLING_FREQUENCY]
