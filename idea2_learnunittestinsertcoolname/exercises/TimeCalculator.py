import math
from typing import Union


def TimeCalculator_dict(duration):
    tmp = duration

    ms = tmp % 1000
    tmp: int = math.floor(tmp/1000)
    s = tmp % 60
    tmp = math.floor(tmp/60)
    m = tmp % 60
    tmp = math.floor(tmp/60)
    h = tmp % 24
    tmp = math.floor(tmp/24)
    d = tmp

    return {
        'ms': ms, 'seconds': s, 'minutes': m, 'hours': h, 'days': d, 'duration_total': duration
    }

def TimeCalculator_tupel(duration):
    result_dict = TimeCalculator_dict(duration)
    result_tupel = (result_dict['duration_total'],
                    result_dict['days'],
                    result_dict['hours'],
                    result_dict['minutes'],
                    result_dict['seconds'],
                    result_dict['ms'],
                    )
    return result_tupel

if __name__ == "__main__":
    #print(TimeCalculator_dict(3452347890))
    #print(TimeCalculator_tupel(3452347890))
    print("Welcome to the TimeCalculator!")
    duration = int(input('please enter a duration in milliseconds:'))
    print("%d ms are exactly:" % duration)
    tmresult_dict = TimeCalculator_dict(duration)
    for i in ("days","hours","minutes","seconds","ms"):
        print("%8s %d" % (i,tmresult_dict[i]))