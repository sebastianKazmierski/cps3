from errors.reconstruction_error import ReconstructionError
from signals.signal import Signal


class MD(ReconstructionError):
    def calculate_error_value(self, original: Signal, reconstructed: Signal) -> float:
        super().calculate_error_value(original, reconstructed)
        return max(list(map(lambda t: abs(t[0] - t[1]), list(zip(original.samples, reconstructed.samples)))))
