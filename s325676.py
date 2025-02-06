import numpy as np

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])


def f2(x: np.ndarray) -> np.ndarray:
    pass

def f3(x: np.ndarray) -> np.ndarray:
    return np.add(np.multiply(np.arctan(np.add(np.arctan(1.9423158330970622), 8.311556888397728)), np.cosh(np.cosh(np.arctan(1.9423158330970622)))), np.negative(np.add(np.add(np.multiply(np.square(x[0]), np.rint(-2.065621497047198)), np.divide(3.503326125821749, np.reciprocal(x[2]))), np.multiply(x[1], np.square(x[1])))))

def f4(x: np.ndarray) -> np.ndarray:
    return 3.3325688447227532 + (np.cos(x[1]) / 0.1428298184783164) - ((-0.5653322717250981 - x[0]) / -10.9872282724623779)

def f5(x: np.ndarray) -> np.ndarray:
    return ((2.467100421154991e-12 * (np.power(4.18958630424536, (3.017249747918303 - x[1])) - 4.084409304778444)) * np.power(x[0], x[1]))

def f6(x: np.ndarray) -> np.ndarray: 
    return (x[1] - (((-3.7176133491516232 * x[0]) + (3.7181064589095936 * x[1])) / (np.minimum(4.381559519733427, -3.803901432200341) - np.cbrt(3.7181064589095936))))

def f7(x: np.ndarray) -> np.ndarray: ...


def f8(x: np.ndarray) -> np.ndarray: ...