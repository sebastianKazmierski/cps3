from signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from signal_type import SignalType
from type_of_periodical import SignalPeriodic
from scipy import signal


class UnitImpuls(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float, fill_factor: float,
                 sampling_frequency: float) -> Signal:
        x = self.get_arguments(start_time, duration, sampling_frequency)
        if start_time <= 0 and abs(round(start_time)) <= duration:
            index_of_jump = round(abs(start_time) / duration * (len(x)-1))
            y = signal.unit_impulse(len(x), index_of_jump)
        else:
            y = x*0.0

        frequency = 1 / period
        return Signal(start_time, frequency, sampling_frequency, list(y), SignalType.REAL, SignalPeriodic.NO)