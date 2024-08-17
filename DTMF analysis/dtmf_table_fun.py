
'''
DTMF table

       1209 Hz     1336 Hz     1447 Hz
697 Hz   1           2           3
770 Hz   4           5           6
852 Hz   7           8           9
941 Hz   *           0           #

'''

def isFreqInTable(freq1, freq2):
    offset = 3
    digit = 0
    if((697-offset <= freq1 <= 697+offset) and (1209-offset <= freq2 <= 1209+offset)): 
        digit = '1'
    elif ((697-offset <= freq1 <= 697+offset) and (1336-offset <= freq2 <= 1336+offset)):
        digit = '2'
    elif ((697-offset <= freq1 <= 697+offset) and (1477-offset <= freq2 <= 1477+offset)):
        digit = '3'
#####################################################################################################
    elif ((770-offset <= freq1 <= 770+offset) and (1209-offset <= freq2 <= 1209+offset)):
        digit = '4'
    elif ((770-offset <= freq1 <= 770+offset) and (1336-offset <= freq2 <= 1336+offset)):
        digit = '5'
    elif ((770-offset <= freq1 <= 770+offset) and (1477-offset <= freq2 <= 1477+offset)):
        digit = '6'
#####################################################################################################
    elif ((852-offset <= freq1 <= 852+offset) and (1209-offset <= freq2 <= 1209+offset)):
        digit = '7'
    elif ((852-offset <= freq1 <= 852+offset) and (1336-offset <= freq2 <= 1336+offset)):
        digit = '8'
    elif ((852-offset <= freq1 <= 852+offset) and (1477-offset <= freq2 <= 1477+offset)):
        digit = '9'
#####################################################################################################
    elif ((941-offset <= freq1 <= 941+offset) and (1209-offset <= freq2 <= 1209+offset)):
        digit = '*'
    elif ((941-offset <= freq1 <= 941+offset) and (1336-offset <= freq2 <= 1336+offset)):
        digit = '0'
    elif ((941-offset <= freq1 <= 941+offset) and (1477-offset <= freq2 <= 1477+offset)):
        digit = '#'
#####################################################################################################
    else:
        digit = 'No DTMF.'
    return digit
