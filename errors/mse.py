from errors.reconstruction_error import ReconstructionError
from signals.signal import Signal


class MSE(ReconstructionError):
    def calculate_error_value(self, original: Signal, reconstructed: Signal) -> float:
        super().calculate_error_value(original, reconstructed)
        original_samples = original.samples
        reconstructed_samples = reconstructed.samples

        error_value = 0
        for i in range(len(original_samples)):
            error_value += (original_samples[i] - reconstructed_samples[i]) ** 2

        error_value /= len(original_samples)
        return error_value
