def find_optimal_building_two_pointers(buildings):
    """
    Find optimal building using two-pointer expansion from each potential home.
    
    Parameters:
    buildings (list): List of dictionaries with boolean values for each shop type
                     Each building has format: {'barber': bool, 'school': bool, 'lawyer': bool}
    
    Returns:
    list: List of tuples (building_index, total_distance, distances) sorted by total distance
    """
    building_scores = []
    shop_types = ['barber', 'school', 'lawyer']
    
    def find_distances_from_building(center_idx):
        distances = {shop: float('inf') for shop in shop_types}
        found_shops = set()
        
        # Start with the building itself
        for shop in shop_types:
            if buildings[center_idx][shop]:
                distances[shop] = 0
                found_shops.add(shop)
        
        # If we found all shops in the center building, we're done
        if len(found_shops) == len(shop_types):
            return distances
        
        # Expand outward using two pointers
        left = center_idx - 1
        right = center_idx + 1
        
        while (left >= 0 or right < len(buildings)) and len(found_shops) < len(shop_types):
            # Check left building if within bounds
            if left >= 0:
                distance = center_idx - left
                for shop in shop_types:
                    if shop not in found_shops and buildings[left][shop]:
                        distances[shop] = distance
                        found_shops.add(shop)
            
            # Check right building if within bounds
            if right < len(buildings):
                distance = right - center_idx
                for shop in shop_types:
                    if shop not in found_shops and buildings[right][shop]:
                        distances[shop] = distance
                        found_shops.add(shop)
            
            left -= 1
            right += 1
        
        return distances
    
    # Calculate scores for each building
    for i in range(len(buildings)):
        distances = find_distances_from_building(i)
        total_distance = sum(distances.values())
        building_scores.append((i, total_distance, distances))
    
    # Sort buildings by total distance
    building_scores.sort(key=lambda x: x[1])
    
    return building_scores

# Example usage
buildings = [
    {'barber': True,  'school': False, 'lawyer': False},  # Building 0
    {'barber': False, 'school': True,  'lawyer': False},  # Building 1
    {'barber': False, 'school': False, 'lawyer': False},  # Building 2
    {'barber': False, 'school': False, 'lawyer': True },  # Building 3
    {'barber': True,  'school': False, 'lawyer': False},  # Building 4
    {'barber': False, 'school': True,  'lawyer': True }   # Building 5
]

# Get ranked buildings
ranked_buildings = find_optimal_building_two_pointers(buildings)

# Print results
print("Buildings ranked by total distance to all services:")
for idx, (building, total_distance, distances) in enumerate(ranked_buildings):
    print(f"\nRank {idx + 1}: Building {building}")
    print(f"Total distance: {total_distance} blocks")
    print("Distance to each service:")
    for service, distance in distances.items():
        print(f"- {service}: {distance} blocks")