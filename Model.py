import numpy as np
import random
from itertools import permutations

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
        for i,specimen in enumerate(self._population[:-5]):
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
        #specimen_a[a:b], specimen_b[a:b] = specimen_b[a:b], specimen_a[a:b]
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
        print(specimen_a, specimen_b, doubles_a, doubles_b)
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
        indexes_of_chosen_individuals = random.sample(range(len(self._population)), self._tournament_size)
        # print(f"indexes_of_chosen_individuals = {indexes_of_chosen_individuals}")
        chosen_individuals = [self._population[i] for i in random.sample(range(len(self._population)), self._tournament_size)]
        # print(f"chosen_individuals = {chosen_individuals}")
        values_of_chosen_individuals = [self.fitness_function(specimen) for specimen in chosen_individuals]
        # print(f"values_of_chosen_individuals = {values_of_chosen_individuals}")
        max_value_of_chosen_individuals = max(values_of_chosen_individuals)
        # print(f"max_value_of_chosen_individuals = {max_value_of_chosen_individuals}")
        individual_with_max_value_of_chosen_individuals = chosen_individuals[np.where(values_of_chosen_individuals == max_value_of_chosen_individuals)[0][0]]
        individual_with_max_value_of_chosen_individuals = list(dict.fromkeys(individual_with_max_value_of_chosen_individuals))
        # print(f'np.where: {np.where(values_of_chosen_individuals == max_value_of_chosen_individuals)}')
        # print(f'invdividual with max_value_of_chosen_individuals = {individual_with_max_value_of_chosen_individuals}')

        for i in indexes_of_chosen_individuals:
            self._population[i] = individual_with_max_value_of_chosen_individuals

        for i in range(0,len(self._population), 2):
            if random.uniform(0,1) < self._crossover_coefficient:
                self._population[i], self._population[i+1] = self.crossover(self._population[i], self._population[i+1])

    def get_best_specimen(self):
        specimen_fitnessses = [self.fitness_function(i) for i in self._population]
        best = self._population[specimen_fitnessses.index(max(specimen_fitnessses))]
        return best












