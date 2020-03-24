import file_manager
from signal import Signal
from signal_generators2.noise_gaus_distribution import GausDistribution
from signal_generators2.noise_uniform_distribution import UniformDistribution
import matplotlib.pyplot as plt

from signal_generators2.rectagular_simetric_signal import RectangularSymetricSignal
from signal_generators2.rectangular_signal import RectangularSignal
from signal_generators2.sin import SinGenerator
import numpy as np

from signal_generators2.sin_straightened_in_one_half import SinStraightenedInOneHalf
from signal_generators2.sin_straightened_in_two_half import SinStraightenedInTwoHalf
from signal_generators2.traiangul_signal import TriangularSignal
from signal_type import SignalType


def show_statistics(read_signal: Signal):
    print(read_signal.average_signal_value())
    print(read_signal.absolute_average_signal_value())
    print(read_signal.average_power_of_signal())
    print(read_signal.signal_variance())
    print(read_signal.effective_value())


def display(signal: Signal):
    fig1 = plt.figure(figsize=(10, 4))
    axes1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    period = 1 / signal.sampling_frequency
    stop_time = signal.start_time + (period * (len(signal.samples)))
    axes1.plot(np.arange(signal.start_time, stop_time, period), signal.samples, color='red', linewidth=3,
               linestyle='-')
    plt.show()


test = SinGenerator()
signal = test.generate(1, 1, 10, 2, 0, 5)

file_manager.write(signal, "signal2.pickle")

read_signal = file_manager.read("signal2.pickle")

uniform = UniformDistribution()
gaus = GausDistribution()
SinOneHalf = SinStraightenedInOneHalf()
sinThoHalf = SinStraightenedInTwoHalf()
rectangularSignal = RectangularSignal()
rectangularSymetricSignal = RectangularSymetricSignal()
triangular_signal = TriangularSignal()

signalUniform = rectangularSymetricSignal.generate(2, 1, 10, 0.1, 0.5, 100)

print("elo")
show_statistics(signalUniform)
display(signalUniform)

# freq = 50
# time_period = 1/freq
# time = time_period*2
# amplitude=2
#
# t=np.linspace(0,time,500,endpoint=True)
# x=2*3.14*freq*t
#
# yc=amplitude*np.sin(x)
#
#
# Fsampling =1000
# ts = 1/Fsampling
# txs = np.arange(0,(time+ts/2),ts)
#
# r = np.round(len(t)/len(txs))
# xts = np.arange(0,len(t),r).astype('int')
# xs = x[xts]
# ys = yc[xts]
#
# fig1 = plt.figure(figsize=(10, 4))
# axes1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
# #
# axes1.plot(x, yc, color='red', linewidth=3, linestyle='-')
# plt.show()


#
# axes1.set_ylim([-3,3])
# axes1.set_xlim([0,np.max(x)])
# # axes1.set_xticks(2*3.24*freq)*(np.arange(0,41,5)*1e-3)
# # axes1.set_xtickslabels(np.arange(0,41,5), fontsize=4)
# # axes1.set_yticks([-2,-1,0,1,2])
# # axes1.set_ytickslabels([-2,-1,0,1,2],fontsize = 14)
# axes1.set_xlabel("time (ms)", fontsize=18)
# axes1.set_ylabel("Amplitude", fontsize =18)
# axes1.set_title("Signal Vs time",fontsize=18)
#
#
# plt.show()
