import pandas
import numpy
import configparser
config = configparser.ConfigParser()

print(config.read('example.ini'))

print(config.sections())

print([numpy.random.randint(10) for i in range(10)])

print('Hi my friend')

[print(i) for i in range(10)]

pandas.show_versions()
