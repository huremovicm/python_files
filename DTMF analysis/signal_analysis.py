import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt



def signal_fft(s_rate, signal):  
    FFT = abs(scipy.fft(signal)) 


    freqs = fftpk.fftfreq(len(FFT), (1/s_rate)) 

    plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])

    FFT = FFT.tolist() 
    FFT_int = [int(i) for i in FFT] 

    fft_list = [] 
    
    for i in FFT:
        fft_list.append(int(i))

    fft_list.sort(reverse=True)


    peak1 = fft_list[0] 
    peak2 = 0
   
    for amp in fft_list:
        if (fft_list[0] != amp):
                peak2 = amp
                break


    freqs_l = [] 
   
    for j in freqs:
        freqs_l.append(abs(j))


    

    freq_1 = int(freqs_l[FFT_int.index(peak1)])
    freq_2 = int(freqs_l[FFT_int.index(peak2)])

   
    if freq_1 < freq_2:
        tmp = freq_1
        freq_1 = freq_2
        freq_2 = tmp

    
    title_plot = "Frequency (Hz): " + str(freq_1)+" and "+ str(freq_2)

    plt.title(title_plot )
    plt.ylabel('Power')
    plt.xlabel('Frequency')
    plt.show()

    return freq_2, freq_1

