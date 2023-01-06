import numpy as np
import random
from itertools import permutations
class Model:
    _city_coordinates = [] # [(x,y), ...]
    _population = [] #[[1,2,3,...], [3, 7, 6, ...], ...]
    _mutation_coefficient = 0
    _crossover_coefficient = 0
    def __init__(self, city_coordinates, population, mutation_coefficient, crossover_coefficient):
        self._city_coordinates = city_coordinates
        self._population = population
        self._mutation_coefficient = mutation_coefficient
        self._crossover_coefficient = crossover_coefficient

    def distance_function(self, xy1, xy2):
        x1, y1 = xy1
        x2, y2 = xy2
        return np.sqrt((x2-x1)**2 + (y2-y1)**2)

    def generate_population(self,N):
        sample = [i for i in range(len(self._city_coordinates))]
        self._population = [random.sample(sample, len(sample)) for _ in range(N)]

    def mutate(self):
        for i,specimen in enumerate(self._population):
            if random.uniform(0,1) < self._mutation_coefficient:
                a = random.randrange(0,len(specimen))
                b = random.randrange(0,len(specimen))
                self._population[i][a],  self._population[i][b] = self._population[i][b],  self._population[i][a]

    def get_city_coordinates(self):
        return self._city_coordinates

    def get_population(self):
        return self._population

    def fitness_function(self, specimen):
        ret = 0
        for city1, city2 in zip(specimen[:-1], specimen[1:]):
            ret += self.distance_function(self.get_city_coordinates()[city1], self.get_city_coordinates()[city2])
        return ret

    def crossover(self, specimen_a, specimen_b):
        a = random.randint(0,len(specimen_a))
        b = random.randint(a,len(specimen_a))
        specimen_a[a:b], specimen_b[a:b] = specimen_b[a:b], specimen_a[a:b]
        set_a = set()
        set_b = set()
        doubles_a = []
        doubles_b = []
        for i,j in zip(specimen_a, specimen_b):
            if i not in set_a:
                set_a.add(i)
            else:
                doubles_a.append(i)
            if j not in set_b:
                set_b.add(j)
            else:
                doubles_b.append(j)
        n_changed = 0
        for i, val_i in enumerate(specimen_a):
            if i < a or i >= b:
                if val_i in doubles_a:
                    specimen_a[i] = doubles_b[n_changed]
                    n_changed += 1
        n_changed = 0
        for i, val_i in enumerate(specimen_b):
            if i < a or i >= b:
                if val_i in doubles_b:
                    specimen_b[i] = doubles_a[n_changed]
                    n_changed += 1
        return (specimen_a, specimen_b)
        
    def create_offspring(self):
        fitness_index = [self.fitness_function(specimen) for specimen in self._population]
        max_value = sum(fitness_index)
        selected = []
        for i in range(len(self._population)):
            val = random.uniform(0,max_value)
            for j, weight in enumerate(reversed(fitness_index)):
                val-=weight
                if val <= 0:
                    selected.append(len(fitness_index) - j - 1)
                    break
        self._population = [self._population[i] for i in selected]
        for i in range(0,len(self._population), 2):
            if random.uniform(0,1) < self._crossover_coefficient:
                self._population[i], self._population[i+1] = self.crossover(self._population[i], self._population[i+1])
        

    def get_best_specimen(self):
        best = 0
        best_fitness = -1
        for i in self._population:
            fitness = self.fitness_function(i) 
            if fitness > best_fitness:
                best_fitness = fitness
                best = i
        return best












