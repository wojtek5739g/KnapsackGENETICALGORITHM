from Model import Model
from Visualizer import visualise_specimen, plot_progress
def test_model():
    model = Model([(0, 2), (5, 4), (120, 4), (56, 42)], [[1, 2], [2, 3]])
    assert model.fitnessFunction(model.get_population()[0]) == 115.0

def test_specimen():
    visualise_specimen([(0, 2), (5, 4), (120, 4), (56, 42)], [3,1,2,0])
def test_progress_visualization():
    plot_progress([(0, 2), (5, 4), (120, 4), (56, 42)], [[0,1,2,3],[3,1,2,0]])