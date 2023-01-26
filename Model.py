import numpy as np
import random
from itertools import permutations
from operator import itemgetter

class Model:
    # _city_coordinates = [] # [(x,y), ...]
    # _population = [] #[[1,2,3,...], [3, 7, 6, ...], ...]
    def __init__(self, city_coordinates, population, mutation_coefficient=0, crossover_coefficient=0, tournament_size=0):
        self._city_coordinates = city_coordinates
        self._population = np.array(population)
        self._mutation_coefficient = mutation_coefficient
        self._crossover_coefficient = crossover_coefficient
        self._tournament_size = tournament_size

    def distance_function(self, xy1, xy2):
        x1, y1 = xy1
        x2, y2 = xy2
        return np.sqrt((x2-x1)**2 + (y2-y1)**2)

    def generate_population(self, N):
        sample = [i for i in range(len(self._city_coordinates))]
        self._population = np.array([random.sample(sample, len(sample)) for _ in range(N)])

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
        return (1/ret)

    def crossover(self, specimen_a, specimen_b):
        a = random.randint(0,len(specimen_a))
        b = random.randint(a,len(specimen_a))
        temp = np.copy(specimen_a[a:b])
        specimen_a[a:b] = specimen_b[a:b]
        specimen_b[a:b] = temp
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

    def create_offspring_roulette(self):
        fitness_index = [self.fitness_function(specimen) for specimen in self._population]
        max_value = sum(fitness_index)
        selected = []
        for i in range(len(self._population)):
            val = random.uniform(0,max_value)
            for j, weight in enumerate(fitness_index):
                val-=weight
                if val <= 0:
                    selected.append(j)
                    break
        self._population = np.array([self._population[i] for i in selected])
        for i in range(0,len(self._population), 2):
            if random.uniform(0,1) < self._crossover_coefficient:
                self._population[i], self._population[i+1] = self.crossover(self._population[i], self._population[i+1])

    def create_offspring_elitism(self):
        fitness_index = [self.fitness_function(specimen) for specimen in self._population]
        sorted_fitness_index = sorted(fitness_index)[::-1]
        #best = [self._population[np.where(fitness_index == sorted_fitness_index[i])[0][0]] for i in range(10)]
        best = [self._population[np.where(fitness_index == sorted_fitness_index[0])[0][0]] for i in range(10)]
        max_value = sum(fitness_index)
        selected = []
        for i in range(len(self._population)-10):
            val = random.uniform(0,max_value)
            for j, weight in enumerate(fitness_index):
                val-=weight
                if val <= 0:
                    selected.append(j)
                    break
        self._population = np.array([self._population[i] for i in selected])
        self._population = np.concatenate((self._population, best), axis = 0)
        for i in range(0,len(self._population), 2):
            if random.uniform(0,1) < self._crossover_coefficient:
                self._population[i], self._population[i+1] = self.crossover(self._population[i], self._population[i+1])

    def create_offspring_tournament(self):
        new_population = []
        for k in range(len(self._population)):
            idxs_of_chosen_ind = random.sample(range(len(self._population)), self._tournament_size)
            list_tournament = []
            for i in idxs_of_chosen_ind:
                list_index_value = []
                list_index_value.append(i)
                list_index_value.append(self.fitness_function(self._population[i]))
                list_tournament.append(list_index_value)

            max_value = 0
            max_index = 0
            p = 0.5

            list_tournament = sorted(list_tournament, key=itemgetter(1), reverse=True)
            # for idx, elem in enumerate(list_tournament):
            #     if (random.uniform(0, 1) < p*(1-p)**idx):
            #         max_value = elem[1]
            #         max_index = elem[0]
            #     if (idx == len(list_tournament) and max_value==0):
            #         max_value = elem[1]
            #         max_index = elem[0]

            new_population.append(self._population[list_tournament[0][0]])
            # self._population[np.argmin([self.fitness_function(x) for x in self._population])] = self._population[max_index]

        self._population = new_population

        for i in range(0,len(self._population), 2):
            if random.uniform(0,1) < self._crossover_coefficient:
                self._population[i], self._population[i+1] = self.crossover(self._population[i], self._population[i+1])

    def get_best_specimen(self):
        specimen_fitnessses = [self.fitness_function(i) for i in self._population]
        best = self._population[specimen_fitnessses.index(max(specimen_fitnessses))]
        return best












