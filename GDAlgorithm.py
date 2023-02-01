from Model import Model
import numpy as np
from Generate_map import map_generation
from Visualizer import visualise_specimen, plot_progress
import sys
import argparse

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
        # print(specimen)
        if model.fitness_function(specimen) > model.fitness_function(best_specimen):
            best_specimen = specimen
    #print(1/model.fitness_function(best_specimen))
    return model.fitness_function(best_specimen)

def GDAlgorithm(cities_coordinates):
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
        return specimen

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