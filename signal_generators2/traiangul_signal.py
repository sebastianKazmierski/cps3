from signals.signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from enums.signal_parameters import SignalParameters
from enums.signal_type import SignalType
from enums.type_of_periodical import SignalPeriodic
from scipy import signal
import math


class TriangularSignal(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float, fill_factor: float,
                 sampling_frequency: float) -> Signal:
        x = self.get_arguments(start_time, 2*math.pi, sampling_frequency/(2*math.pi*10))
        frequency = 1/period
        y = ((amplitude * signal.sawtooth(x, fill_factor) + amplitude) * 0.5) - 0.5*amplitude
        y2 = list(y)
        for i in range(round(duration/period)-1):
            y2 = y2 + list(y)
        return Signal(start_time, frequency, sampling_frequency, y2, SignalType.REAL, SignalPeriodic.YES)

    def get_name(self) -> str:
        return "Sygnał trójkątny"


    def get_list_required_parameters(self):
        return [SignalParameters.AMPLITUDE, SignalParameters.START_TIME, SignalParameters.DURATION,
                SignalParameters.PERIOD, SignalParameters.FILL_FACTOR, SignalParameters.SAMPLING_FREQUENCY]