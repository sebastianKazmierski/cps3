from math import log10

from errors.mse import MSE
from errors.reconstruction_error import ReconstructionError
from signals.signal import Signal


class PSNR(ReconstructionError):
    def calculate_error_value(self, original: Signal, reconstructed: Signal) -> float:
        super().calculate_error_value(original, reconstructed)

        original_samples = original.samples
        nominator = max(original_samples)
        denominator = MSE(original, reconstructed).value

        return 10 * log10(nominator / denominator)
