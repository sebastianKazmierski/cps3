import numpy as np

class SignalGenerator:
    # def generate(self, amplitude: float, start_time: float, duration: float, period: float, fill_factor: float,
    #              sampling_frequency: float) -> Signal:
    #     pass

    def get_arguments(self, start_time, duration, sampling_frequency):
        ts = 1 / sampling_frequency
        return np.arange(start_time, (start_time + duration + ts / 2), ts)

    def get_name(self) -> str:
        pass

    def get_list_required_parameters(self):
        pass
