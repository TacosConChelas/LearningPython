import sys

def main():
    coordinates_tuple = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]
    # print(f"Latitude: {coordinates[0]}")
    # print(f"Longitude: {coordinates[1]}")
    #latitude, longitude = coordinates
    
    # print(f"Latitude: {latitude}")
    # print(f"Latitude: {longitude}")
    print(f"tuple: {sys.getsizeof(coordinates_tuple)} bytes")

    print(f"list: {sys.getsizeof(coordinates_list)} bytes")


main()