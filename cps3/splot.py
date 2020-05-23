from signals.signal import Signal


def get_value(samples: list, index: int)->float:
    if index < 0 or index > len(samples) - 1:
        return 0.0
    return samples[index]


def get_splot(h: Signal, x: Signal) -> list:
    m = len(h.samples)
    n = len(x.samples)

    splot = list(range(m + n - 2))
    for i in range(m + n - 2):
        point = 0
        for j in range(m - 1):
            point += h.samples[j] * get_value(x.samples, i - j)
        splot[i] = point
    return splot

def get_splot(h: list, x: list) -> list:
    m = len(h)
    n = len(x)

    splot = list(range(m + n - 2))
    for i in range(m + n - 2):
        point = 0
        for j in range(m - 1):
            point += h[j] * get_value(x, i - j)
        splot[i] = point
    return splot