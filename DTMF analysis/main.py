
import scipy.io.wavfile as wavfile


from dtmf_table_fun import isFreqInTable
from signal_analysis import signal_fft
from multiple_signal_import import multiSigImport

list_sig = multiSigImport()

i = 0
print("Number: ", end='')

while i < len(list_sig):
    s_rate, signal = list_sig[i]
    analyzed = signal_fft(s_rate, signal)
    print(isFreqInTable(analyzed[0], analyzed[1]), end='')
    if(i != 0 and i % 2 == 0):
        print(' ', end='')
    i = i+1
print('\n')
