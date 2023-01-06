import numpy as np
import matplotlib.pyplot as plt
from Model import Model
def visualise_specimen(city_coordinates,specimen):
    plt.figure()
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.xlabel("x")
    plt.ylabel("y")
    city_coordinates2 = np.transpose(np.array(city_coordinates))
    i = 0
    for j in specimen:
        plt.text(city_coordinates[j][0],city_coordinates[j][1],f"{i}", size = 22)
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
    finess_function_values = []
    model = Model(city_coordinates,[],0,0)
    for specimen in best_specimens:
        finess_function_values.append(model.fitness_function(specimen))
    plt.figure()
    plt.xlabel("iteracja")
    plt.ylabel("funkcja dopasowania")
    plt.title("Zmiana dopasowania najlepszego osobnika")
    plt.plot(np.arange(0,len(finess_function_values),1), finess_function_values)
    plt.show()

    




