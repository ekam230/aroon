import numpy
import pyti
from pyti.exponential_moving_average import exponential_moving_average as ema
#from pyti.relative_strength_index import relative_strength_index as rsi
from pyti.aroon import aroon_up
from pyti.aroon import aroon_down


def aroon(data):
    """
    Function return result
    """
    quotes = {}
    # xdate = quotes['timestamp']=numpy.asarray([item[0] for item in data])
    quotes['open'] = numpy.asarray([item[1] for item in data])
    quotes['high'] = numpy.asarray([item[2] for item in data])
    quotes['low'] = numpy.asarray([item[3] for item in data])
    quotes['close'] = numpy.asarray([item[4] for item in data])
    open = quotes['open']
    open = open[0]
    close = quotes['close']
    close = close[0]
    high = quotes['high']
    high = high[::-1]
    #print(high)
    low = quotes['low']
    low = low[::-1]
    #print(low)

    #    * Logic

    # print(aroon_up(high,7))
    # print(aroon_down(low,7))

    aroon = aroon_up(high,7) - aroon_down(low,7)
    # print(aroon[-1])

    # bar = close > open ? 1 : close < open ? -1 : 0
    bar = None

    # // Свеча зеленая
    if (close > open):
        bar = "green"
        print(f'Close: {close} > Open: {open}')
        print("Bar: ", bar)

    #   // Свеча красная
    elif(close < open):
        bar = "red"
        print(f"Close: {close} < Open: {open}")
        print("Bar: ", bar)

    #   // Ничего не произошло
    else:
        bar = "still"
        print(f'Close: {close} = Open: {open}')
        print("Bar: ", bar)



    #    * Signals
    aroon_int = aroon[-1]
    print(f"Aroon: {aroon_int}")
    up = None
    if aroon_int > 80 and bar == "red":
        up = True
        print(f"Aroon: {aroon_int}, Up = true")

    down = None
    if aroon_int < -80 and bar == "green":
        down = True
        print(f"Aroon: {aroon_int}, Down = true")

    if up:
        return 'up'
    elif down:
        return 'down'
    else:
        return 'hold'
