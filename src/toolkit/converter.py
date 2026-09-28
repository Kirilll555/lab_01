from errors import ConverterError

units = {
    'mm': ('length', 0.001, 0),
    'cm': ('length', 0.01, 0),
    'm':  ('length', 1, 0),
    'km': ('length', 1000, 0),
    'g':  ('weight', 0.001, 0),
    'kg': ('weight', 1, 0),
    'c':  ('temp', 1, 0),
    'f':  ('temp', 5/9, -32),
    'k':  ('temp', 1, -273.15),
}

def validate(unit_1, unit_2):
    unit_1 = unit_1.lower()
    unit_2 = unit_2.lower()
    if unit_1 not in units or unit_2 not in units:
        raise ConverterError('Неизвестная единица измерения')
    s1, x1, b1 = units[unit_1]
    s2, x2, b2 = units[unit_2]

    if s1 != s2:
        raise ConverterError('Единицы измерения не совпадают')
    return s1, x1, b1, s2, x2, b2

def convert(value, unit_1, unit_2):
    s1, x1, b1, s2, x2, b2 = validate(unit_1, unit_2)
    result = (value + b1) * x1
    if s1 == 'temp' and result < -273.15:
        raise ConverterError('Результат ниже абсолютного нуля')
    return  float(result / x2 - b2)
