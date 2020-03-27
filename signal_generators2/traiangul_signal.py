from signals.signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from enums.signal_parameters import SignalParameters
from enums.signal_type import SignalType
from enums.type_of_periodical import SignalPeriodic
from scipy import signal


class TriangularSignal(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float, fill_factor: float,
                 sampling_frequency: float) -> Signal:
        x = self.get_arguments(start_time, duration, sampling_frequency)
        frequency = 1/period
        y = (amplitude * signal.sawtooth(x, fill_factor) + amplitude) * 0.5
        return Signal(start_time, frequency, sampling_frequency, list(y), SignalType.REAL, SignalPeriodic.YES)

    def get_name(self) -> str:
        return "Sygnał trójkątny"


    def get_list_required_parameters(self):
        return [SignalParameters.AMPLITUDE, SignalParameters.START_TIME, SignalParameters.DURATION,
                SignalParameters.PERIOD, SignalParameters.FILL_FACTOR, SignalParameters.SAMPLING_FREQUENCY]