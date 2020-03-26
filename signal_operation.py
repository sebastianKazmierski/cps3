from signal import Signal
from signal_type import SignalType
from type_of_periodical import SignalPeriodic
import operator


def get_periodical(signal1: Signal, signal2: Signal) -> SignalPeriodic:
    if signal1.signal_periodic == SignalPeriodic.YES and signal2.signal_periodic == SignalPeriodic.YES:
        return SignalPeriodic.YES
    else:
        return SignalPeriodic.NO


def check_compatibility(signal1: Signal, signal2: Signal):
    message = ""
    if signal1.sampling_frequency != signal2.sampling_frequency:
        message += "Sygnały nie mają tej samej częstotliwości prubkowania\n"
    if signal1.start_time != signal2.start_time:
        message += "Sygnały nie mają tego samego czasu początkowego\n"
    if len(signal1.samples) != len(signal2.samples):
        message += "Sygnały nie mają tej samej ilości próbek"
        if signal1.signal_type == SignalType.COMPLEX or signal2.signal_type == SignalType.COMPLEX:
            message += "Minum jeden z wybranych sygnałów jest sugnałem zespolonym"


class SignalOperation:

    def add(self, signal1: Signal, signal2: Signal):
        return self.perform_signal_action(signal1, signal2, operator.add)

    def subtract(self, signal1: Signal, signal2: Signal):
        return self.perform_signal_action(signal1, signal2, operator.sub)

    def multiply(self, signal1: Signal, signal2: Signal):
        return self.perform_signal_action(signal1, signal2, operator.mul)

    def division(self, signal1: Signal, signal2: Signal):
        check_compatibility(signal1, signal2)
        signal1_values = signal1.samples
        signal2_values = signal2.samples

        new_values = list(range(len(signal1_values)))
        for i in range(len(signal1_values)):
            if signal2_values[i] != 0.0:
                new_values[i] = signal1_values[i] / signal2_values[i]
            else:
                new_values[i] = signal1_values[i]

        return Signal(signal1.start_time, signal1.signal_frequency, signal1.sampling_frequency, new_values,
                      SignalType.REAL, get_periodical(signal1, signal2))

    def perform_signal_action(self, signal1: Signal, signal2: Signal, operation: operator) -> Signal:
        check_compatibility(signal1, signal2)
        singal1_values = signal1.samples
        signal2_values = signal2.samples

        new_values = operation(singal1_values, signal2_values)

        return Signal(signal1.start_time, signal1.signal_frequency, signal1.sampling_frequency, new_values,
                      SignalType.REAL, get_periodical(signal1, signal2))
