from Model import Model
from Visualizer import visualise_specimen, plot_progress
def main():
    city_coordinates = []
    model = Model([(0, 2), (5, 4), (120, 4), (56, 42),(10, 2), (20, 4), (30, 4), (40, 42)],[],0.01,0.5)
    model.generate_population()
    best_fits = [model.get_best_specimen]
    for i in range(10000):
        model.create_offspring()
        model.mutate()
        best_fits.append(model.get_best_specimen())
    visualise_specimen(best_fits[-1])
    plot_progress(best_fits)


if __name__ == "__main__":
    main()