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
    radius = np.random.uniform(min_radius, max_radius)
    print(f'Straight-line distance: {radius:.2f} km')
    radius /= 111.3 # 111.3 km in a degree (equatorial)
    angle = 2 * np.pi * np.random.rand()
    lat_delta = radius * np.sin(angle)
    lon_delta = radius * np.cos(angle) 
    lon_delta /= np.cos(np.deg2rad(lat_center)) # account for decreasing longitudinal distances
    random_location = (lat_center + lat_delta, lon_center + lon_delta)
    return random_location


if __name__ == "__main__":
    print(generate_random_location(48.0, 11.0, 100, 200))
