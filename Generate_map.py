import random

def map_generation(N, Mx, My):
    '''
    N - number of cities
    Mx - maximum coordinate value along x axis
    My - maximum coordinate value along y axis
    '''
    existing_coords = []
    while len(existing_coords) < N:
      Xcoordinates = [random.randrange(0, Mx+1) for i in range(N)]
      Ycoordinates = [random.randrange(0, My+1) for i in range(N)]
      city_coords = (random.choice(Xcoordinates), random.choice(Ycoordinates))
      if city_coords not in existing_coords:
          existing_coords.append(city_coords)
    return existing_coords