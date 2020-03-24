import file_manager

from signal_generators2.sin import SinGenerator
from signal_type import SignalType

test = SinGenerator(SignalType.REAL)
signal = test.generate(1, 1, 10, 2, 0, 5)

file_manager.write(signal, "signal2.pickle")

read_signal = file_manager.read("signal2.pickle")

print(read_signal.average_signal_value())


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
# fig1=plt.figure(figsize=(10,4))
# axes1=fig1.add_axes([0.1,0.1,0.8,0.8])
#
# axes1.plot(x,yc,color='red', linewidth=3, linestyle='-')
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
