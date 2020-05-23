from draw.draw_plot import display
from files.file_manager import write, read
from signals.signal import Signal
from signal_generators2.impulse_noise import ImpulseNoise
from signal_generators2.noise_gaus_distribution import GausDistribution
from signal_generators2.noise_uniform_distribution import UniformDistribution
from signal_generators2.rectagular_simetric_signal import RectangularSymetricSignal
from signal_generators2.rectangular_signal import RectangularSignal
from signal_generators2.sin import SinGenerator
from signal_generators2.sin_straightened_in_one_half import SinStraightenedInOneHalf
from signal_generators2.sin_straightened_in_two_half import SinStraightenedInTwoHalf
from signal_generators2.traiangul_signal import TriangularSignal
from signal_generators2.unit_impuls import UnitImpuls
from signal_generators2.unit_jump import UnitJump
from signals.signal_operation import SignalOperation
from enums.signal_parameters import SignalParameters
from enums.type_of_plot import PlotType


def start():
    answer = 1
    while answer != 4:
        print("Wybierz co chcesz zrobic")
        print("1. Wykonaj operacjie na sygnałach")
        print("2. Wygeneruj nowy sygnał")
        print("3. Wczytaj sygnał z pliku")
        print("4. Zakończ program")
        answer = int(input())
        if answer == 1:
            perform_operation()
        elif answer == 2:
            present_signal(generate_signal())
        elif answer == 3:
            present_signal(load_signal_from_file())


def get_parameter(parameter: SignalParameters):
    print(parameter.name + ": ")
    return float(input())


def show_statistics(read_signal: Signal):
    print("Wartość średnia:                                        " + str(read_signal.average_signal_value()))
    print("Wartość średnia bezwzględna:                            " + str(read_signal.absolute_average_signal_value()))
    print("Moc średnia:                                            " + str(read_signal.average_power_of_signal()))
    print("Wariancja sygnału w przedziale wokół wartości średniej: " + str(read_signal.signal_variance()))
    print("Wartość skuteczna:                                      " + str(read_signal.effective_value()))


def load_signal_from_file():
    print("Podaj nazwę pliku:")
    file_name = input()
    return read(file_name)


def generate_signal():
    list = [ImpulseNoise(), GausDistribution(), UniformDistribution(), RectangularSymetricSignal(),
            RectangularSignal(), SinGenerator(), SinStraightenedInOneHalf(), SinStraightenedInTwoHalf(),
            TriangularSignal(), UnitImpuls(), UnitJump()]
    print("Wybierz funkcje: ")
    for i in range(len(list)):
        print(str(i) + " " + list[i].get_name())
    index = int(input())
    signal_generator = list[index]
    print(list[index].get_name())
    required_parameters = []
    for parameter in signal_generator.get_list_required_parameters():
        required_parameters.append(get_parameter(parameter))
    return signal_generator.generate(*required_parameters)


def present_signal(signal: Signal):
    show_statistics(signal)
    print("Wybierz rodzaj wykresu")
    print("1. Dyskretny")
    print("2. Ciągły")
    answer = int(input())
    if answer == 1:
        plot_type = PlotType.DISCRETE
    elif answer == 2:
        plot_type = PlotType.CONTINUOUS
    print("Podaj liczbę przedziałów dla której chcesz wyświetlić histogram:")
    answer = int(input())
    display(signal, plot_type, answer)
    save_to_file(signal)


def save_to_file(signal):
    print("Czy chcesz zapisac sygnał do pliku? (t/N)")
    answer = input()
    if answer == "t" or answer == "T":
        print("Podaj nazwę pliku:")
        file_name = input()
        write(signal, file_name)


def get_one_element_of_operation():
    print("1. Wczytaj sygnał z pliku")
    print("2. Wygeneruj nowy sygnał")
    answer = int(input())
    if answer == 1:
        return load_signal_from_file()
    else:
        return generate_signal()


def get_elements_of_operation():
    print("Wybierz pierwszy składnik operacji")
    element1 = get_one_element_of_operation()
    print("Wybierz drugi składnik operacji")
    element2 = get_one_element_of_operation()
    return element1, element2


def perform_operation():
    print("Wybierz rodzaj operacji")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    answer = int(input())
    signal1, signal2 = get_elements_of_operation()
    signal_operation = SignalOperation()
    if answer == 1:
        result = signal_operation.add(signal1, signal2)
    elif answer == 2:
        result = signal_operation.subtract(signal1, signal2)
    elif answer == 3:
        result = signal_operation.multiply(signal1, signal2)
    elif answer == 4:
        result = signal_operation.division(signal1, signal2)
    present_signal(result)
