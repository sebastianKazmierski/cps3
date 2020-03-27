from signals.signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from enums.signal_parameters import SignalParameters
from enums.signal_type import SignalType
from enums.type_of_periodical import SignalPeriodic
from scipy import signal


class UnitImpuls(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float,
                 sampling_frequency: float) -> Signal:
        x = self.get_arguments(start_time, duration, sampling_frequency)
        if start_time <= 0 and abs(round(start_time)) <= duration:
            index_of_jump = round(abs(start_time) / duration * (len(x) - 1))
            y = amplitude * signal.unit_impulse(len(x), index_of_jump)
        else:
            y = x * 0.0

        return Signal(start_time, 0.0, sampling_frequency, list(y), SignalType.REAL, SignalPeriodic.NO)

    def get_name(self) -> str:
        return "Impuls jednostkowy"

    def get_list_required_parameters(self):
        return [SignalParameters.AMPLITUDE, SignalParameters.START_TIME, SignalParameters.DURATION,
                SignalParameters.SAMPLING_FREQUENCY]
