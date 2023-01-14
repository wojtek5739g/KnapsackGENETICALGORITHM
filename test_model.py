from Model import Model
from Visualizer import visualise_specimen, plot_progress

def test_model():
    model = Model([(0, 2), (5, 4), (120, 4), (56, 42)], [[1, 2], [2, 3]],0,0)
    assert model.fitnessFunction(model.get_population()[0]) == 115.0

def test_specimen():
    visualise_specimen([(0, 2), (5, 4), (120, 4), (56, 42)], [3,1,2,0])
def test_progress_visualization():
    plot_progress([(0, 2), (5, 4), (120, 4), (56, 42)], [[0,1,2,3],[3,1,2,0]])

def test_crossover():
    model = Model([(0, 2), (5, 4), (120, 4), (56, 42),(10, 2), (20, 4), (30, 4), (40, 42)], [[0, 1,2,3], [1, 2,0,3]],0,0)
    print(model.crossover(model._population[0], model._population[1]))

def test_distance():
    model = Model([(-1,-1),(1,1),(-1,1),(1,-1)], [[0,1,2,3]], 0,0)
    print(1/model.fitness_function(model._population[0]))
