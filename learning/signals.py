import copy
import math
import random
import matplotlib.pyplot as plt
from src.signal_filters import outliers_filter, median_filter, moving_average_filter, get_outliers, interpolate_missing_values


time = [i for i in range(250)]

# Create clean signal
clean_signal = []
for t in time:
    x = math.sin(t * 0.05)
    clean_signal.append(x)

# Create noisy signal
noisy_signal = []
for i, sig in enumerate(clean_signal):
    x = sig
    if i % 20 == 0:
        x += random.uniform(-3, 3)
    else:
        x += random.gauss(0, 0.15)

    noisy_signal.append(x)

# Get outliers
outliers = get_outliers(noisy_signal)
# print("Outliers:", outliers)


# Show data
plt.plot(time, clean_signal, label="Clean signal")
plt.plot(time, noisy_signal, label="Noisy signal")

# Very good without removing outliers
median_filter_signal = median_filter(noisy_signal, 10)
plt.plot(time, median_filter_signal, label="Median filter")

outliers_filter_signal = outliers_filter(noisy_signal)
# plt.plot(time, outliers_filter_signal, label="Outliers filter")

# Moveing average without outliers removed is not as good, but with them removed its practically same as median filter
moving_average_signal = moving_average_filter(outliers_filter_signal, 10)
plt.plot(time, moving_average_signal, label="Moving average - no outliers")

plt.legend()
plt.show()

# Testing lerp
signal_2 = []
x = [i for i in range(50)]
for y in x:
    val = math.sin(y * 0.2)
    if random.uniform(0, 1) < 0.5 and y != 0 and y < 49:
        signal_2.append(None)
    else:
        signal_2.append(val)

interpolated = interpolate_missing_values(copy.copy(signal_2))

plt.plot(x, interpolated, label="Interpolated signal")
plt.plot(x, signal_2, label="Clean signal", linewidth=5)
plt.legend()
plt.show()

print(interpolate_missing_values([1,2,None,None,None,6,None,8]))
