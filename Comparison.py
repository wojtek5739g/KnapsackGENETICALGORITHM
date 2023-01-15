from GDAlgorithm import GDAlgorithmComp
from GeneticAlgorithm import GeneticAlgorithmComp
from Visualizer import comparison_fitness_function_plot, comparison_distance_plot
from Generate_map import map_generation
from Model import Model
import argparse
import sys

def main(argv):
    parser = argparse.ArgumentParser(description='Launch Genetic and DQ Algorithm comparison')
    parser.add_argument('num_of_launches', type=int, help='Number of launching the comparison')
    parser.add_argument('num_of_cities', type=int, help='Number of cities')
    parser.add_argument('max_X_coord_value', type=int, help='Maximum value of X coordinate')
    parser.add_argument('max_Y_coord_value', type=int, help='Maximum value of Y coordinate')
    parser.add_argument('num_of_individuals', type=int, help='Number of individuals (series of different orders of cities in population')
    parser.add_argument('num_of_iterations', type=int, help='Number of iterations of the algorithm')
    parser.add_argument('mutation_coef', type=float, help='Mutation coefficient')
    parser.add_argument('crossover_coef', type=float, help='Crossover coefficient')
    parser.add_argument('selection', choices=['elitism', 'roulette', 'tournament'], type=str, help='Selection type')
    parser.add_argument('--tournament_size', nargs='?', type=int, help='Tournament size')
    args = parser.parse_args()

    best_specimensGEN = [] #fitness_function_values
    best_specimensDistanceGEN = [] #distance_values
    best_specimensGA = [] #fitness_function_values
    best_specimensDistanceGA = [] #distance_values
    cities_coordinates = map_generation(args.num_of_cities, args.max_X_coord_value, args.max_Y_coord_value)
    GAmodel = Model(cities_coordinates, [], args.mutation_coef, args.crossover_coef, args.tournament_size)
    GDmodel = Model(cities_coordinates, [])
    for i in range(args.num_of_launches):
        print(f"{i+1} Launch: ")
        GAbestSpecimen = GeneticAlgorithmComp(GAmodel, cities_coordinates, args.num_of_individuals, args.num_of_iterations, args.mutation_coef, args.crossover_coef, args.tournament_size, args.selection)
        GDbestSpecimen = GDAlgorithmComp(GDmodel, cities_coordinates, args.num_of_individuals, args.num_of_iterations)
        best_specimensGEN.append(GAbestSpecimen)
        best_specimensDistanceGEN.append(1/GAbestSpecimen)
        best_specimensGA.append(GDbestSpecimen)
        best_specimensDistanceGA.append(1/GDbestSpecimen)
    comparison_fitness_function_plot(args.num_of_launches, best_specimensGEN, best_specimensGA,
                                    args.num_of_cities, args.num_of_individuals, args.num_of_iterations,
                                    args.mutation_coef, args.crossover_coef, args.selection, args.tournament_size)
    comparison_distance_plot(args.num_of_launches, best_specimensDistanceGEN, best_specimensDistanceGA,
                            args.num_of_cities, args.num_of_individuals, args.num_of_iterations,
                            args.mutation_coef, args.crossover_coef, args.selection, args.tournament_size)

if __name__ == "__main__":
    main(sys.argv)