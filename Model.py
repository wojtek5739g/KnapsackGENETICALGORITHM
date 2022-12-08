import numpy as np
class Model:
    city_coordinates = [] # [(x,y), ...]
    population = [] #[1,2,3,...]
    def __init__(self) -> None:
        pass
    def distanceFunction(self,xy1, xy2):
        x1,y1 = xy1
        x2,y2 = xy2
        return np.sqrt((x2-x1)**2 + (y2-y1)**2)
    def fitnessFunction(self, specimen):
        ret = 0
        for city1, city2 in zip(specimen[:-1], specimen[1:]):
            ret += self.distanceFunction(self.city_coordinates[city1], self.city_coordinates[city2])
        return ret



        
        


