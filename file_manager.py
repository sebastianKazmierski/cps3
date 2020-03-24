import pickle

from signal import Signal


def write(signal: Signal, file_name: str):
    pickle_out = open(file_name, "wb")
    pickle.dump(signal, pickle_out)
    pickle_out.close()


def read(file_name: str) -> Signal:
    pickle_in = open(file_name, "rb")
    return pickle.load(pickle_in)
