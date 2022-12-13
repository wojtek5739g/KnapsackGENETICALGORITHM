from Model import Model

def test_model():
    model = Model([(0, 2), (5, 4), (120, 4), (56, 42)], [[1, 2], [2, 3]])
    assert model.fitnessFunction(model.get_population()[0]) == 115.0


