def distance_3d(point1, point2):
    """Calculate Euclidean distance between two 3D points"""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5

def parse_points(lines):
    """Parse lines in format 'x,y,z' into list of tuples"""
    return [tuple(map(int, line.split(','))) for line in lines if line.strip()]

def find_closest_pair(points):
    """Find the pair of points with minimum distance"""
    min_distance = float('inf')
    closest_pair = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance_3d(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])
    
    return closest_pair, min_distance

def find_n_shortest_connections(points, n):
    """Find the n shortest connections between points"""
    distances = []
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance_3d(points[i], points[j])
            distances.append((dist, points[i], points[j]))
    
    distances.sort()
    return [(p1, p2) for _, p1, p2 in distances[:n]]

def build_clusters(connections, all_points):
    """Build clusters from point connections, including isolated points"""
    # Map each point to its cluster
    point_to_cluster = {}
    clusters = []
    
    for p1, p2 in connections:
        cluster1 = point_to_cluster.get(p1)
        cluster2 = point_to_cluster.get(p2)
        
        if cluster1 is None and cluster2 is None:
            # Both points are new, create new cluster
            new_cluster = {p1, p2}
            clusters.append(new_cluster)
            point_to_cluster[p1] = new_cluster
            point_to_cluster[p2] = new_cluster
        elif cluster1 is None:
            # Only p1 is new, add to p2's cluster
            cluster2.add(p1)
            point_to_cluster[p1] = cluster2
        elif cluster2 is None:
            # Only p2 is new, add to p1's cluster
            cluster1.add(p2)
            point_to_cluster[p2] = cluster1
        elif cluster1 is not cluster2:
            # Merge two different clusters
            cluster1.update(cluster2)
            for point in cluster2:
                point_to_cluster[point] = cluster1
            clusters.remove(cluster2)
    
    # Add isolated points as individual clusters
    for point in all_points:
        if point not in point_to_cluster:
            clusters.append({point})
    
    return clusters

def calculate_result(clusters):
    """Calculate product of three largest cluster sizes"""
    sizes = sorted([len(cluster) for cluster in clusters], reverse=True)
    return sizes[0] * sizes[1] * sizes[2] if len(sizes) >= 3 else 0

def read_input(filename):
    return [line.strip() for line in open(filename, 'r', encoding='utf-8')]

def find_single_circuit_connection(points):
    """Find the connection that completes a single circuit using Union-Find"""
    # Get all connections sorted by distance
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance_3d(points[i], points[j])
            distances.append((dist, points[i], points[j]))
    
    distances.sort()
    
    # Union-Find: each point starts in its own cluster
    parent = {p: p for p in points}
    
    def find(p):
        if parent[p] != p:
            parent[p] = find(parent[p])
        return parent[p]
    
    def union(p1, p2):
        root1 = find(p1)
        root2 = find(p2)
        if root1 != root2:
            parent[root2] = root1
            return True
        return False
    
    num_clusters = len(points)
    
    for _, p1, p2 in distances:
        # Skip if already in same cluster
        if find(p1) == find(p2):
            continue
        
        union(p1, p2)
        num_clusters -= 1
        
        # When we reach 1 cluster, this connection completed the circuit
        if num_clusters == 1:
            return p1, p2
    
    return None, None

def part_1(data):
    """Find 1000 shortest connections and calculate product of three largest clusters"""
    points = parse_points(data)
    connections = find_n_shortest_connections(points, 1000)
    clusters = build_clusters(connections, points)
    return calculate_result(clusters)

def part_2(data):
    """Find first connection that creates single circuit, return product of X coordinates"""
    points = parse_points(data)
    result = find_single_circuit_connection(points)
    if result and len(result) == 2:
        p1, p2 = result
        return p1[0] * p2[0]
    return 0

def main():
    """Main function to run the solution"""
    input_data = read_input('input.txt')
    print(f"Part 1 = {part_1(input_data)}")
    print(f"Part 2 = {part_2(input_data)}")

if __name__ == "__main__":
    main()
