from signals.signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from enums.signal_parameters import SignalParameters
from enums.signal_type import SignalType
from enums.type_of_periodical import SignalPeriodic


class UnitJump(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, jump_time: float,
                 sampling_frequency: float) -> Signal:
        number_of_low_values = (jump_time - start_time) * sampling_frequency
        number_of_high_values = (duration - (jump_time - start_time)) * sampling_frequency

        y_low = [0.0] * round(number_of_low_values)
        y_high = [amplitude] * round(number_of_high_values)

        y = y_low + [(amplitude / 2)] + y_high

        return Signal(start_time, 0.0, sampling_frequency, list(y), SignalType.REAL, SignalPeriodic.NO)

    def get_name(self) -> str:
        return "Skok jednostkowy"

    def get_list_required_parameters(self):
        return [SignalParameters.AMPLITUDE, SignalParameters.START_TIME, SignalParameters.DURATION,
                SignalParameters.JUMP_TIME, SignalParameters.SAMPLING_FREQUENCY]
