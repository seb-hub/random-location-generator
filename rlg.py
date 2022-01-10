import numpy as np


def generate_random_location(lat_center, lon_center, min_radius, max_radius):
    '''
    Generate random coordinates of a location nearby.

    Parameters
    ----------
    lat_center: float
        Latitude of your position.
    lon_ceter: float
        Longitude of your position.
    min_radius: int
        Minimum distance of random location.
    max_radius: int
        Maximum distance of random location.

    Returns
    -------
    random_location: tuple of (float, float)
        Latitude and longitude of random location.

    https://gis.stackexchange.com/questions/25877/generating-random-locations-nearby
    '''
    # 111.3 km in a degree (equatorial)
    radius = np.random.randint(min_radius, max_radius) / 111.3
    (u, v) = (np.random.rand(), np.random.rand())
    w = radius * np.sqrt(u)
    t = 2 * np.pi * v
    x = w * np.cos(t) 
    y = w * np.sin(t)
    x /= np.cos(lon_center)
    random_location = (lat_center + x, lon_center + y)
    return random_location


if __name__ == "__main__":
    print(generate_random_location(48.0, 11.0, 100, 200))
