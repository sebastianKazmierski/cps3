from abc import abstractmethod

from signals.signal import Signal


class ReconstructionError:
    def __init__(self, original_signal: Signal, reconstructed_signal: Signal):
        self._value = self.calculate_error_value(original_signal, reconstructed_signal)
        pass

    @property
    def value(self):
        return self._value

    @abstractmethod
    def calculate_error_value(self, original: Signal, reconstructed: Signal) -> float:
        assert len(original.samples) == len(reconstructed.samples)
        pass

    def get_name(self):
        return type(self).__name__
