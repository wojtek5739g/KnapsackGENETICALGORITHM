from Model import Model
import numpy as np
from Generate_map import map_generation
from Visualizer import visualise_specimen, plot_progress
import sys
import argparse

#def GDAlgorithmComp(model, cities_coordinates, num_of_individuals, num_of_iterations):
#    model.generate_population(num_of_individuals)
#    best_fits = np.array([model.get_best_specimen()])
#    for i in range(num_of_iterations):
#        model.generate_population(num_of_individuals)
#        best_specimen = model.get_best_specimen()
#        best_fits = np.append(best_fits, [best_specimen], axis = 0)
#        print(f"iteration {i}: Distance: {1/model.fitness_function(best_specimen)}")
#    return model.fitness_function(best_fits[-1])

def GDAlgorithmComp(cities_coordinates):
    model = Model(cities_coordinates, [])
    best_specimen = np.array([i for i in range(len(cities_coordinates))])
    for i_start,start in enumerate(cities_coordinates):
        specimen = np.array([],dtype=int)
        specimen = np.append(specimen, i_start)
        location = start
        visited = set()
        visited.add(i_start)
        for i in range(len(cities_coordinates)):
            distances = [model.distance_function(location,j) for j in cities_coordinates]
            distances_sorted = sorted(distances)
            for j, j_dist in enumerate(distances_sorted):
                k = np.where(distances == j_dist)[0][0]
                if k not in visited:
                    specimen = np.append(specimen, k)
                    visited.add(k)
                    location = cities_coordinates[k]
                    break
        print(specimen)
        if model.fitness_function(specimen) > model.fitness_function(best_specimen):
            best_specimen = specimen
    #print(1/model.fitness_function(best_specimen))
    return model.fitness_function(best_specimen)
        
            


def GDAlgorithm(num_of_cities, max_X_coord_value, max_Y_coord_value, num_of_individuals, num_of_iterations):
    cities_coordinates = map_generation(num_of_cities, max_X_coord_value, max_Y_coord_value)
    model = Model(cities_coordinates, [])
    model.generate_population(num_of_individuals)
    best_fits = np.array([model.get_best_specimen()])
    for i in range(num_of_iterations):
        model.generate_population(num_of_individuals)
        best_specimen = model.get_best_specimen()
        best_fits = np.append(best_fits, [best_specimen], axis = 0)
        print(f"iteration {i}: Distance: {1/model.fitness_function(best_specimen)}")
    visualise_specimen(cities_coordinates, best_fits[0])
    print(model.fitness_function(best_fits[0]))
    print(model.fitness_function(best_fits[-1]))
    visualise_specimen(cities_coordinates, best_fits[-1])
    plot_progress(cities_coordinates, best_fits)

def main(argv):
    parser = argparse.ArgumentParser(description='Launch DQAlgorithm')
    parser.add_argument('num_of_cities', type=int, help='Number of cities')
    parser.add_argument('max_X_coord_value', type=int, help='Maximum value of X coordinate')
    parser.add_argument('max_Y_coord_value', type=int, help='Maximum value of Y coordinate')
    parser.add_argument('num_of_individuals', type=int, help='Number of individuals (series of different orders of cities in population')
    parser.add_argument('num_of_iterations', type=int, help='Number of iterations of the algorithm')
    args = parser.parse_args()
    GDAlgorithm(args.num_of_cities, args.max_X_coord_value, args.max_Y_coord_value, args.num_of_individuals, args.num_of_iterations)

if __name__ == "__main__":
    main(sys.argv)