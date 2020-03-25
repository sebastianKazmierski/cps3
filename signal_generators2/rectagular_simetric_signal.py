from signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from signal_type import SignalType
from type_of_periodical import SignalPeriodic
from scipy import signal


class RectangularSymetricSignal(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float, fill_factor: float,
                 sampling_frequency: float) -> Signal:
        x = self.get_arguments(start_time, duration, sampling_frequency)

        y = amplitude * signal.square(x, duty=fill_factor)

        return Signal(start_time, 1 / period, sampling_frequency, y, SignalType.REAL, SignalPeriodic.YES)
