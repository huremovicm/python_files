import scipy.io.wavfile as wavfile

def multiSigImport():
    sig_list = []

    sig_list.append(wavfile.read("tones/6.wav"))
    sig_list.append(wavfile.read("tones/9.wav"))
    sig_list.append(wavfile.read("tones/1.wav"))
########################################################
    sig_list.append(wavfile.read("tones/7.wav"))
    sig_list.append(wavfile.read("tones/7.wav"))
########################################################
    sig_list.append(wavfile.read("tones/5.wav"))
    sig_list.append(wavfile.read("tones/9.wav"))
########################################################
    sig_list.append(wavfile.read("tones/2.wav"))
    sig_list.append(wavfile.read("tones/3.wav"))

    return sig_list