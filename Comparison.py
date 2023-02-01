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

    best_specimensDistanceGEN1 = [] #distance_values
    best_specimensDistanceGEN2 = []
    best_specimensDistanceGEN3 = []
    best_specimensDistanceGD = [] #distance_values

    for i in range(args.num_of_launches):
        cities_coordinates = map_generation(args.num_of_cities, args.max_X_coord_value, args.max_Y_coord_value)
        GAmodel = Model(cities_coordinates, [], args.mutation_coef, args.crossover_coef, args.tournament_size)

        print(f"{i+1} Launch: ")
        GAbestSpecimen = GeneticAlgorithmComp(GAmodel, cities_coordinates, args.num_of_individuals, args.num_of_iterations, args.mutation_coef, args.crossover_coef, 2, args.selection)
        best_specimensDistanceGEN1.append(1/GAbestSpecimen)
        print(f"{i+1} Launch: ")
        GAbestSpecimen = GeneticAlgorithmComp(GAmodel, cities_coordinates, args.num_of_individuals, args.num_of_iterations, args.mutation_coef, args.crossover_coef, 3, args.selection)
        best_specimensDistanceGEN2.append(1/GAbestSpecimen)
        print(f"{i+1} Launch: ")
        GAbestSpecimen = GeneticAlgorithmComp(GAmodel, cities_coordinates, args.num_of_individuals, args.num_of_iterations, args.mutation_coef, args.crossover_coef, 4, args.selection)
        best_specimensDistanceGEN3.append(1/GAbestSpecimen)

        GDbestSpecimen = GDAlgorithmComp(cities_coordinates)
        best_specimensDistanceGD.append(1/GDbestSpecimen)

    comparison_distance_plot(args.num_of_launches, best_specimensDistanceGEN1, best_specimensDistanceGEN2, best_specimensDistanceGEN3, best_specimensDistanceGD,
                            args.num_of_cities, args.num_of_individuals, args.num_of_iterations,
                            args.mutation_coef, args.crossover_coef, args.selection, args.tournament_size)

if __name__ == "__main__":
    main(sys.argv)