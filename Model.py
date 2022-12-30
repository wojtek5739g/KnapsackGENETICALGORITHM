import numpy as np
import random

class Model:
    city_coordinates = [] # [(x,y), ...]
    population = [] #[[1,2,3,...], [3, 7, 6, ...], ...]
    def __init__(self, city_coordinates, population):
        self._city_coordinates = city_coordinates
        self._population = population

    def distanceFunction(self, xy1, xy2):
        x1, y1 = xy1
        x2, y2 = xy2
        return np.sqrt((x2-x1)**2 + (y2-y1)**2)

    def get_city_coordinates(self):
        return self._city_coordinates

    def get_population(self):
        return self._population

    def fitnessFunction(self, specimen):
        ret = 0
        for city1, city2 in zip(specimen[:-1], specimen[1:]):
            ret += self.distanceFunction(self.get_city_coordinates()[city1], self.get_city_coordinates()[city2])
        return ret









