import numpy as np
import math
import statistics


# statistics.mean()
def mean(numbers):
    return np.sum(numbers) / len(numbers)


# statistics.media()
def median(numbers):
    m = int(len(numbers) / 2)

    if (len(numbers) % 2) == 0:
        return (numbers[int(m) - 1] + numbers[int(m)]) / 2
    else:
        return numbers[int(m)]


# statistics.variance()
def variance(numbers):
    m = mean(numbers)
    sum = 0

    for value in numbers:
        sum += (value-m)**2

    return sum/(len(numbers)-1)


# statistics.stdev()
def standard_deviation(numbers):
    v = variance(numbers)
    return math.sqrt(v)


# statistics.mode()
def mode(numbers):
    max_mode = 0
    mode_v = numbers[0]
    idx = 0
    count = 0

    for value in numbers:
        if idx == len(numbers) - 1 or value != numbers[idx + 1]:
            if count > max_mode or (count == max_mode and value < mode_v):
                max_mode = count
                mode_v = value
            count = 0
        else:
            count += 1
        idx += 1

    return mode_v


# statistics.quartiles()
def quartiles(numbers):

    q = []
    l = int(len(numbers) / 2)
    q.append(median(numbers[0:l]))
    q.append(median(numbers))
    q.append(median(numbers[l + 1:len(numbers)]))

    return q


def main():
    n = int(input())

    values = input()
    r = values.split(" ")

    r = np.array(r)
    r = r.astype("float")
    r = np.sort(r)

    print("%.1f" % mean(r))
    print("%.1f" % median(r))
    print("%.1f" % mode(r))
    print("%.1f" % standard_deviation(r))


if __name__ == "__main__":
    main()