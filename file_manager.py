import pickle

from signal import Signal

directory_with_files = "signals/"


def write(signal: Signal, file_name: str):
    pickle_out = open(directory_with_files + file_name, "wb")
    pickle.dump(signal, pickle_out)
    pickle_out.close()


def read(file_name: str) -> Signal:
    pickle_in = open(directory_with_files + file_name, "rb")
    return pickle.load(pickle_in)
