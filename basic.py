import numpy as np
# import statistics


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


def main():
    n = int(input())

    values = input()
    r = values.split(" ")

    r = np.array(r)
    r = r.astype("float")
    r = np.sort(r)
    print("%.1f" % mean(r))
    print("%.1f" % median(r))
    print(mode(r))


if __name__ == "__main__":
    main()