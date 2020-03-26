import time
import curses

from draw_plot import display
from signal_generators2.impulse_noise import ImpulseNoise
from signal_generators2.noise_gaus_distribution import GausDistribution
from signal_generators2.noise_uniform_distribution import UniformDistribution
from signal_generators2.rectagular_simetric_signal import RectangularSymetricSignal
from signal_generators2.rectangular_signal import RectangularSignal
from signal_generators2.sin import SinGenerator
from signal_generators2.sin_straightened_in_one_half import SinStraightenedInOneHalf
from signal_generators2.sin_straightened_in_two_half import SinStraightenedInTwoHalf
from signal_generators2.traiangul_signal import TriangularSignal
from signal_generators2.unit_impuls import UnitImpuls
from signal_generators2.unit_jump import UnitJump
from signal_parameters import SignalParameters


def get_parameter(parameter: SignalParameters):
    print(parameter.name + ": ")
    return float(input())


list = [ImpulseNoise(), GausDistribution(), UniformDistribution(), RectangularSymetricSignal(),
        RectangularSignal(), SinGenerator(), SinStraightenedInOneHalf(), SinStraightenedInTwoHalf(),
        TriangularSignal(), UnitImpuls(), UnitJump()]
print("Wybierz funkcje: ")
for i in range(len(list)):
    print(str(i) + " " + list[i].get_name())

index = int(input())

signal_generator = list[index]
print(list[index].get_name())

required_parameters = []

for parameter in signal_generator.get_list_required_parameters():
    required_parameters.append(get_parameter(parameter))

signal = signal_generator.generate(*required_parameters)

display(signal)



