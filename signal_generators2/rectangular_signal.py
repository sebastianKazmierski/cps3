from signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from signal_parameters import SignalParameters
from signal_type import SignalType
from type_of_periodical import SignalPeriodic
from scipy import signal


class RectangularSignal(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float, fill_factor: float,
                 sampling_frequency: float) -> Signal:
        x = self.get_arguments(start_time, duration, sampling_frequency)
        frequency = 1 / period

        y = amplitude * signal.square(x * frequency, duty=fill_factor)

        return Signal(start_time, frequency, sampling_frequency, y, SignalType.REAL, SignalPeriodic.YES)

    def get_name(self) -> str:
        return "Sygnał prostokątny"


    def get_list_required_parameters(self):
        return [SignalParameters.AMPLITUDE, SignalParameters.START_TIME, SignalParameters.DURATION,
                SignalParameters.PERIOD, SignalParameters.FILL_FACTOR, SignalParameters.SAMPLING_FREQUENCY]