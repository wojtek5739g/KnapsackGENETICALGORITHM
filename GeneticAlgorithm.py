from Model import Model
import numpy as np
from Visualizer import visualise_specimen, plot_progress
from Generate_map import map_generation
import sys
import argparse
from GDAlgorithm import GDAlgorithm

def GeneticAlgorithmComp(model, cities_coordinates, num_of_individuals, num_of_iterations, mutation_coef, crossover_coef, tournament_size, selection):
    model.generate_population(num_of_individuals)
    best_fits = np.array([model.get_best_specimen()])
    for i in range(num_of_iterations):
        if selection == 'elitism':
            model.create_offspring_elitism()
        elif selection == 'roulette':
            model.create_offspring_roulette()
        elif selection == 'tournament':
            model.create_offspring_tournament()
        model.mutate()
        best_specimen = model.get_best_specimen()
        best_fits = np.append(best_fits, [best_specimen], axis = 0)
        print(f"iteration {i}: Distance: {1/model.fitness_function(best_specimen)}")
    return model.fitness_function(best_fits[-1])

def GeneticAlgorithm(cities_coordinates, num_of_individuals, num_of_iterations, mutation_coef, crossover_coef, tournament_size, selection):
    model = Model(cities_coordinates, [], mutation_coef, crossover_coef, tournament_size)
    model.generate_population(num_of_individuals)
    best_fits = np.array([model.get_best_specimen()])
    for i in range(num_of_iterations):
        if selection == 'elitism':
            model.create_offspring_elitism()
        elif selection == 'roulette':
            model.create_offspring_roulette()
        elif selection == 'tournament':
            model.create_offspring_tournament()
        model.mutate()
        best_specimen = model.get_best_specimen()
        best_fits = np.append(best_fits, [best_specimen], axis = 0)
        print(f"iteration {i}: Distance: {1/model.fitness_function(best_fits[i])}")
    # visualise_specimen(cities_coordinates, best_fits[0])
    for i in best_fits:
        print(1/model.fitness_function(i))
    print(f'Distance value of best fit of first generation (iteration):  {1/model.fitness_function(best_fits[0])}')
    print(f'Distance value of best fit of last generation (iteration):  {1/model.fitness_function(best_fits[-1])}')
    visualise_specimen(cities_coordinates, best_fits[-1])
    # plot_progress(cities_coordinates, best_fits)
    print('Algorytm zachłanny: ')
    GA_specimen = GDAlgorithm(cities_coordinates)
    print(1/model.fitness_function(GA_specimen))
    visualise_specimen(cities_coordinates,GA_specimen)
    return best_fits

def main(argv):
    parser = argparse.ArgumentParser(description='Launch Genetic Algorithm')
    parser.add_argument('num_of_cities', type=int, help='Number of cities')
    parser.add_argument('max_X_coord_value', type=int, help='Maximum value of X coordinate')
    parser.add_argument('max_Y_coord_value', type=int, help='Maximum value of Y coordinate')
    parser.add_argument('num_of_individuals', type=int, help='Number of individuals (series of different orders of cities in population')
    parser.add_argument('num_of_iterations', type=int, help='Number of iterations of the algorithm')
    parser.add_argument('mutation_coef', type=float, help='Mutation coefficient')
    parser.add_argument('crossover_coef', type=float, help='Crossover coefficient')
    parser.add_argument('selection', choices=['elitism', 'roulette', 'tournament'], type=str, help='Selection type')
    parser.add_argument('--tournament_size', type=int, nargs='?', const=0, help='Tournament size')
    args = parser.parse_args()
    cities_coordinates = map_generation(args.num_of_cities, args.max_X_coord_value, args.max_Y_coord_value)
    bestfits2 = GeneticAlgorithm(cities_coordinates, args.num_of_individuals, args.num_of_iterations, args.mutation_coef, args.crossover_coef, 2, args.selection)
    bestfits3 = GeneticAlgorithm(cities_coordinates, args.num_of_individuals, args.num_of_iterations, args.mutation_coef, args.crossover_coef, 3, args.selection)
    bestfits4 = GeneticAlgorithm(cities_coordinates, args.num_of_individuals, args.num_of_iterations, args.mutation_coef, args.crossover_coef, 4, args.selection)
    plot_progress(cities_coordinates, bestfits2, bestfits3, bestfits4)

if __name__ == "__main__":
    main(sys.argv)