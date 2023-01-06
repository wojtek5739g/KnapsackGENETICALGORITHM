from Model import Model
from Visualizer import visualise_specimen, plot_progress
def main():
    city_coordinates = [(0, 2), (5, 4), (120, 4), (56, 42),(10, 2), (20, 4), (30, 4), (40, 42)]
    model = Model(city_coordinates,[],0.01,0.5)
    model.generate_population(100)
    print(model._population)
    best_fits = [model.get_best_specimen()]
    for i in range(1000):
        model.create_offspring()
        model.mutate()
        best_fits.append(model.get_best_specimen())
        print(f"iteration {i}")
    visualise_specimen(city_coordinates, best_fits[-1])
    plot_progress(city_coordinates,best_fits)
    print(best_fits)


if __name__ == "__main__":
    main()