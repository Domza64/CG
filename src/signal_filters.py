import numpy as np

def moving_average_filter(signal, window_size):
    averages = []

    for i in range(len(signal)):
        window = signal[i : i + window_size]
        avg = sum(window) / len(window)
        averages.append(avg)

    return averages

def median_filter(signal, window_size):
    output = []

    for i in range(len(signal)):
        window = signal[i : i + window_size]
        med = np.median(window)
        output.append(med)

    return output

def outliers_filter(signal, threshold = 1.0):
    # Hope first value is not outlier and hope theres not 2 or more outliers in a row :)
    output = [signal[0]]

    for i in range(1, len(signal)):
        vel = abs(signal[i] - signal[i-1])
        # if velocity too big, it's outlier so use prev value
        if vel > threshold:
            # output.append(signal[i-1])
            output.append(output[-1])
        else:
            output.append(signal[i])
        #output.append(signal[i-1] if vel > threshold else signal[i])

    return output

def get_outliers(signal, threshold=1.0):
    # First is 0, and skipped in loop as obviously it cant be compared to its prev value that does not exist
    velocity = [0]

    for i in range(1, len(signal)):
        vel = abs(signal[i] - signal[i-1])
        velocity.append(vel)

    return [x for x in velocity if x > threshold]

def lerp(a, b, t): # t val should be 0->1 where 0.5 is 50%
    # print("A:", a, "B:", b, "t:", t)
    return a * (1 - t) + b * t

def get_next_not_none_index(signal, index):
    for i in range(index, len(signal)):
        if signal[i] != None:
            return i

def interpolate_missing_values(signal):
    # Hope first and last are not None, because that explodes everything
    for i in range(len(signal) - 1):
        a = signal[i]
        # print("Current:", a)
        if signal[i+1] == None:
            b_index = get_next_not_none_index(signal, i + 1)
            b = signal[b_index]
            # print("Next is none, current a:", a, "and b:", b)
            missing_pieces = b_index - i # i is a_index
            j = 1
            for _ in range(missing_pieces - 1):
                t = j / (missing_pieces)
                lerp_val = lerp(a, b, t)
                # print("Setting position:", i+j, "to:", lerp_val)
                signal[i + j] = lerp_val
                j += 1

    return signal