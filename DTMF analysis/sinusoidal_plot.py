import numpy as np
from matplotlib import pyplot as plt
import wave
from multiple_signal_import import multiSigImport

sin_list = multiSigImport()

i = 0

while(i < len(sin_list)):
    s_r, sig = sin_list[i]
    t = np.linspace(0, len(sig) / s_r, num=len(sig))
    plt.figure(i+1)
    plt.plot(t, sig)
    plt.show()
    i = i+1
