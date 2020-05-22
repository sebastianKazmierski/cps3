from math import log10

from errors.mse import MSE
from errors.reconstruction_error import ReconstructionError
from signals.signal import Signal


class SNR(ReconstructionError):
    def calculate_error_value(self, original: Signal, reconstructed: Signal) -> float:
        original_samples = original.samples

        nominator = 0
        for i in range(len(original_samples)):
            nominator += original_samples[i] * original_samples[i]

        denominator = MSE(original, reconstructed).value * len(original_samples)

        return 10 * log10(nominator / denominator)
