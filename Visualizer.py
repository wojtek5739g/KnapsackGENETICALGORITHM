import numpy as np
import matplotlib.pyplot as plt
from Model import Model
import statistics as st

def visualise_specimen(city_coordinates,specimen):
    plt.figure()
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.xlabel("x")
    plt.ylabel("y")
    city_coordinates2 = np.transpose(np.array(city_coordinates))
    i = 0
    for j in specimen:
        plt.text(city_coordinates[j][0]+1,city_coordinates[j][1]+1,f"{i}", size = 22)
        i+=1
    for i, city in enumerate(specimen[:-1]):
        plt.arrow(city_coordinates[city][0],city_coordinates[city][1],
        city_coordinates[specimen[i+1]][0]-city_coordinates[city][0],
        city_coordinates[specimen[i+1]][1]-city_coordinates[city][1],
        width = 0.5, color = "tab:blue", length_includes_head = True
        )
    plt.scatter(city_coordinates2[0], city_coordinates2[1], color = "tab:green", s = 60)
    plt.show()

def plot_progress(city_coordinates, best_specimens):
    fitness_function_values = []
    model = Model(city_coordinates,[],0,0)
    for specimen in best_specimens:
        fitness_function_values.append(1/model.fitness_function(specimen))
    plt.figure()
    plt.xlabel("iteracja")
    plt.ylabel("długość trasy")
    plt.title("Zmiana długości trasy najlepszego osobnika")
    plt.plot(np.arange(0,len(fitness_function_values),1), fitness_function_values, marker = "o")
    plt.show()

def comparison_fitness_function_plot(num_of_launches, best_specimensGEN, best_specimensGA, num_of_cities, num_of_individuals,
        num_of_iterations, mutation_coef, crossover_coef, selection, tournament_size):
    '''
    Plotting comparison of best specimen of each launching of the program from two algorithms
    '''
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_ylabel('Index of launch')
    ax.set_ylabel('fitness Function')
    ax.minorticks_on()
    ax.grid(which='major', color='#DDDDDD', linewidth=1)
    ax.grid(which='minor', color='#DDDDDD', linestyle=':', linewidth=0.8)

    launches = np.arange(1, num_of_launches+1, 1)
    ax.plot(launches, best_specimensGEN, color='green', label='Genetic Algorithm')
    ax.plot(launches, best_specimensGA, color='blue', label='Greedy Algorithm')

    if type(tournament_size) == None:
        text = f'Number of cities = {num_of_cities}\nNumber of specimen: {num_of_individuals}\n'\
                f'Number of iterations: {num_of_iterations}\nMutation coefficient: {mutation_coef}\n'\
                f'Crossover coefficient: {crossover_coef}\nSelection type: {selection}'
    else:
        text = f'Number of cities = {num_of_cities}\nNumber of specimen: {num_of_individuals}\n'\
                f'Number of iterations: {num_of_iterations}\nMutation coefficient: {mutation_coef}\n'\
                f'Crossover coefficient: {crossover_coef}\nSelection type: {selection}\n'\
                f'Tournament size: {tournament_size}'

    #fig.text(x = 0.2,y = 0.75,s = text,bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 10})
    plt.title(text)
    plt.legend()

    plt.show()

def comparison_distance_plot(num_of_launches, best_specimensGEN, best_specimensGA,best_specimensGEN_min, num_of_cities, num_of_individuals,
        num_of_iterations, mutation_coef, crossover_coef, selection, tournament_size):
    '''
    Plotting comparison of best specimen of each launching of the program from two algorithms
    '''
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_ylabel('Index of launch')
    ax.set_ylabel('Distance')
    ax.minorticks_on()
    ax.grid(which='major', color='#DDDDDD', linewidth=1)
    ax.grid(which='minor', color='#DDDDDD', linestyle=':', linewidth=0.8)
    launches = np.arange(1, num_of_launches+1, 1)
    ax.plot(launches, best_specimensGEN, color='green', label='Genetic Algorithm')
    ax.plot(launches, best_specimensGA, color='blue', label='Greedy Algorithm')
    ax.plot(launches, best_specimensGEN_min, color='cyan', label='Best of Genetic Algorithm')

    if type(tournament_size) == None:
        text = f'Liczba miast: {num_of_cities}\nPopulacja: {num_of_individuals}\n'\
                f'Liczba iteracji: {num_of_iterations}\nWspółczynnik mutacji: {mutation_coef}\n'\
                f'Współczynnik krzyżowania: {crossover_coef}\nRodzaj selekcji: {selection}'
    else:
        text = f'Liczba miast: {num_of_cities}\nPopulacja: {num_of_individuals}\n'\
                f'Liczba iteracji: {num_of_iterations}\nWspółczynnik mutacji: {mutation_coef}\n'\
                f'Współczynnik krzyżowania: {crossover_coef}\nRodzaj selekcji: {selection}\n'\
                f'Rozmiar turnieju: {tournament_size}'

    # ax.text(st.mean(launches), -st.mean(best_specimensGEN+best_specimensGA), text, fontsize=10)
    #fig.text(x = 0.2,y = 0.75,s = text,bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 10})
    plt.title(text)
    ax.legend()
    plt.show()






