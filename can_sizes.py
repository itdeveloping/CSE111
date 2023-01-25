import math

# storage information for each can into al list
# Name, Radius, Height, Cost per Can
steel_can_sizes = [
    ["#1 Picnic", 6.83, 10.16, 0.28],
    ["#1 Tall", 7.78, 11.91, 0.43],
    ["#2", 8.73, 11.59, 0.45],
    ["#2.5", 10.32, 11.91, 0.61],
    ["#3 Cylinder", 10.79, 17.78, 0.86],
    ["#5", 13.02, 14.29, 0.83],
    ["#6Z", 5.4, 8.89, 0.22],
    ["#8Z short", 6.83, 7.62, 0.26],
    ["#10", 15.72, 17.78, 1.53],
    ["#211", 6.83, 12.38, 0.34],
    ["#300", 7.62, 11.27, 0.38],
    ["#303", 8.1, 11.11, 0.42],
]


def main():

    print(f" \t\t \t\t\t  Cost \t\t     Surface  \t  Storage")
    print(f"Name\t\t Radius\t    Height     per can\t   Volume \tArea   Efficiency")
    for can_info in steel_can_sizes:
        can_name = can_info[0]
        can_radius = can_info[1]
        can_height = can_info[2]
        can_cost = can_info[3]
        volume = compute_volume(can_radius, can_height)
        surface_area = compute_surface_area(can_radius, can_height)
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        print(
            f"{can_name:<15}  {can_radius:>6} {can_height:>10}     ${can_cost:>6} {volume:>10.2f} {surface_area:>10.2f} {storage_efficiency:>12.2f}"
        )


def compute_volume(radius, height):
    # volume = π radius2 height
    volume = math.pi * radius * radius * height
    return volume


def compute_surface_area(radius, height):
    # surface_area = 2π radius (radius + height)
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency


main()
