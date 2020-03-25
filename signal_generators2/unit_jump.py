from signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from signal_type import SignalType
from type_of_periodical import PeriodicalSignal
from scipy import signal


class UnitJump(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float, jump_time: float,
                 sampling_frequency: float) -> Signal:
        number_of_low_values = (jump_time - start_time) * sampling_frequency
        number_of_high_values = (duration - (jump_time - start_time)) * sampling_frequency

        y_low = [0.0] * round(number_of_low_values)
        y_high = [amplitude] * round(number_of_high_values)

        y = y_low + [(amplitude / 2)] + y_high

        frequency = 1 / period
        return Signal(start_time, frequency, sampling_frequency, list(y), SignalType.REAL, PeriodicalSignal.NO)
