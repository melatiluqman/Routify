# graph = {
#     'Rumah': [('Taman', {'distance': 5, 'time': {'car': 10, 'bike': 15, 'walking': 30}}),
#               ('Kantor', {'distance': 7, 'time': {'car': 8, 'bike': 12, 'walking': 25}})],
#     'Taman': [('Kantor', {'distance': 3, 'time': {'car': 5, 'bike': 8, 'walking': 15}})],
#     'Kantor': [('D', {'distance': 4, 'time': {'car': 6, 'bike': 10, 'walking': 20}})],
#     'D': []
# }

# def a_star_algorithm(start_point, destinations, end_point, departure_time, return_time):
#     import heapq  # Library untuk priority queue
#     from datetime import datetime
    
#     # Konversi waktu
#     departure = datetime.strptime(departure_time, "%H:%M")
#     return_ = datetime.strptime(return_time, "%H:%M")
    
#     # Inisialisasi
#     open_set = [(0, start_point, [start_point])]  # (cost, current_node, path)
#     visited = set()
    
#     while open_set:
#         cost, current, path = heapq.heappop(open_set)
        
#         if current == end_point:  # Jika sampai pada titik akhir
#             estimated_time = (return_ - departure).total_seconds() / 3600
#             return path, f"Estimated travel time: {estimated_time:.2f} hours"
        
#         if current in visited:
#             continue
#         visited.add(current)
        
#         for neighbor, attributes in graph.get(current, []):
#             if neighbor not in visited:
#                 new_cost = cost + attributes['distance']  # Tambahkan cost
#                 heapq.heappush(open_set, (new_cost, neighbor, path + [neighbor]))
    
#     return [], "No route found."
