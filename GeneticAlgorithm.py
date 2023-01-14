from Model import Model
from Visualizer import visualise_specimen, plot_progress
from Generate_map import map_generation
import sys
import argparse

def GeneticAlgorithmComp(model, cities_coordinates, num_of_individuals, num_of_iterations, mutation_coef, crossover_coef, tournament_size, selection):
    model.generate_population(num_of_individuals)
    best_fits = [model.get_best_specimen()]
    for i in range(num_of_iterations):
        if selection == 'elitism':
            model.create_offspring_elitism()
        elif selection == 'roulette':
            model.create_offspring_roulette()
        elif selection == 'tournament':
            model.create_offspring_tournament()
        model.mutate()
        best_specimen = model.get_best_specimen()
        best_fits.append(best_specimen)
        print(f"iteration {i}: Distance: {1/model.fitness_function(best_specimen)**(1/3)}")
    return model.fitness_function(best_fits[-1])

def GeneticAlgorithm(num_of_cities, max_X_coord_value, max_Y_coord_value, num_of_individuals, num_of_iterations, mutation_coef, crossover_coef, tournament_size, selection):
    cities_coordinates = map_generation(num_of_cities, max_X_coord_value, max_Y_coord_value)
    model = Model(cities_coordinates, [], mutation_coef, crossover_coef, tournament_size)
    model.generate_population(num_of_individuals)
    best_fits = [model.get_best_specimen()]
    for i in range(num_of_iterations):
        if selection == 'elitism':
            model.create_offspring_elitism()
        elif selection == 'roulette':
            model.create_offspring_roulette()
        elif selection == 'tournament':
            model.create_offspring_tournament()
        model.mutate()
        best_specimen = model.get_best_specimen()
        best_fits.append(best_specimen)
        print(f"iteration {i}: Distance: {1/model.fitness_function(best_specimen)**(1/3)}")
    visualise_specimen(cities_coordinates, best_fits[0])
    print(f'Fitness value of best fit of first generation (iteration):  {model.fitness_function(best_fits[0])}')
    print(f'Fitness value of best fit of last generation (iteration):  {model.fitness_function(best_fits[-1])}')
    visualise_specimen(cities_coordinates, best_fits[-1])
    plot_progress(cities_coordinates, best_fits)

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
    GeneticAlgorithm(args.num_of_cities, args.max_X_coord_value, args.max_Y_coord_value, args.num_of_individuals, args.num_of_iterations, args.mutation_coef, args.crossover_coef, args.tournament_size, args.selection)

if __name__ == "__main__":
    main(sys.argv)