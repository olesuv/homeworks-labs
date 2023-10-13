import math
import random as rnd
import tkinter as tki
import matplotlib.pyplot as plt


def frange(start, stop=None, step=None):
    start = float(start)
    if stop is None:
        stop = start + 0.0
        start = 0.0
    if step is None:
        step = 1.0

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1


TestingSignal = [10, 11, 17]


class Signal():
    SignalReal = [[], []]

    def SignalGenerator(self, Xboundary0, Xboundary1, Yboundary0, Yboundary1, variant):
        if variant == 0:
            for i in frange(Xboundary0, Xboundary1, abs(Xboundary0 - Xboundary1) / 1000):
                self.SignalReal[0].append(i)
                self.SignalReal[1].append(rnd.uniform(Yboundary0, Yboundary1))
        elif variant == 1:
            for i in frange(Xboundary0, Xboundary1, abs(Xboundary0 - Xboundary1) / 1000):
                self.SignalReal[0].append(i)
                self.SignalReal[1].append(
                    math.sin(i + Yboundary0) * Yboundary1)
        elif variant == 2:
            for i in frange(Xboundary0, Xboundary1, abs(Xboundary0 - Xboundary1) / 1000):
                self.SignalReal[0].append(i)
                self.SignalReal[1].append(
                    math.cos(i + Yboundary0) * Yboundary1)

    # Масштабування
    def Scaling(self, InSignal, Scale):
        Scaled = InSignal.copy()
        Scaled[1] = [i * Scale for i in Scaled[1]]
        return Scaled

    # Реверс по часу
    def TimeReversal(self, InSignal):
        Reversed = InSignal.copy()
        Reversed[0] = Reversed[0][::-1]
        return Reversed

    # Зсув по часу
    def TimeShift(self, InSignal, Shift):
        Shifted = InSignal.copy()
        Shifted[0] = [i + Shift for i in Shifted[0]]
        return Shifted

    # Розширення
    def Widen(self, InSignal, WidthFactor):
        Widened = InSignal.copy()
        Widened[0] = [i * WidthFactor for i in Widened[0]]
        return Widened

    # Додавання
    def Combination(self, InSignal1, InSignal2):
        Combined = []
        for i in range(max(len(InSignal1[0]), len(InSignal2[0]))):
            if InSignal1[0][i] == InSignal2[0][i]:
                Combined.append(InSignal1[1][i] + InSignal2[1][i])
        return Combined

    # Множення
    def Multiplication(self, InSignal1, InSignal2):
        Multiplied = []
        for i in range(max(len(InSignal1[0]), len(InSignal2[0]))):
            if InSignal1[0][i] == InSignal2[0][i]:
                Multiplied.append(InSignal1[1][i] + InSignal2[1][i])
        return Multiplied


Generated = Signal()
Generated.SignalGenerator(0, 10, 0, 1, 2)

# Plot Generated Signal
plt.plot(Generated.SignalReal[0],
         Generated.SignalReal[1], label='Original Signal')

# Time Shifted Signal
GG = Generated.TimeShift(Generated.SignalReal, 3)
plt.plot(GG[0], GG[1], 'g', label='Time Shifted Signal (Зсув по часу)')

# Time Reversed Signal
YY = Generated.TimeReversal(Generated.SignalReal)
plt.plot(YY[0], YY[1], 'y', label='Time Reversed Signal (Реверс по часу)')

# Scaled Signal
# SS = Generated.Scaling(Generated.SignalReal, 1.5)
# plt.plot(SS[0], SS[1], 'b', label='Scaled Signal (Масштабування)')

# Widened Signal
# WW = Generated.Widen(Generated.SignalReal, 2)
# plt.plot(WW[0], WW[1], 'purple', label='Widened Signal (Розширення)')

# Combined Signal
# CC = Generated.Combination(Generated.SignalReal, GG)
# plt.plot(CC[0], CC[1], 'red', label='Combined Signal (Додавання)')

# Multiplied Signal
# MM = Generated.Multiplication(SS, WW)
# plt.plot(MM[0], MM[1], 'green', label='Multiplied Signal (Множення)')

# Labels
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Signal Operations')

# Add legend
plt.legend()


# Display plot
plt.show()
