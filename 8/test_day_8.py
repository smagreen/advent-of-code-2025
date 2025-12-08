import pytest
import os

# Import the functions from the same directory
from day_8 import (parse_points, find_closest_pair, distance_3d, 
                    find_n_shortest_connections, build_clusters, calculate_result, part_2)

class TestDay8:
    
    def test_find_closest_pair(self):
        """Test finding closest pair with test.txt data"""
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        with open(test_file, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f]
        
        points = parse_points(lines)
        closest_pair, _ = find_closest_pair(points)
        
        # The two boxes with minimum distance should be:
        expected_pair = {(162, 817, 812), (425, 690, 689)}
        actual_pair = {closest_pair[0], closest_pair[1]}
        
        assert actual_pair == expected_pair
        
    def test_distance_3d(self):
        """Test 3D distance calculation"""
        point1 = (0, 0, 0)
        point2 = (3, 4, 0)
        assert distance_3d(point1, point2) == 5.0
        
        point1 = (1, 2, 3)
        point2 = (1, 2, 3)
        assert distance_3d(point1, point2) == 0.0
    
    def test_clusters(self):
        """Test cluster building with 10 shortest connections"""
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        with open(test_file, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f]
        
        points = parse_points(lines)
        connections = find_n_shortest_connections(points, 10)
        clusters = build_clusters(connections, points)
        
        # Should have 11 clusters total
        assert len(clusters) == 11
        
        # Check cluster sizes
        sizes = sorted([len(cluster) for cluster in clusters], reverse=True)
        assert sizes[0] == 5  # One cluster with 5 points
        assert sizes[1] == 4  # One cluster with 4 points
        assert sizes[2] == 2  # One cluster with 2 points
        assert sizes[3] == 2  # Another cluster with 2 points
        # Seven clusters with 1 point each
        assert sizes[4:] == [1, 1, 1, 1, 1, 1, 1]
        
        # Result should be 5 * 4 * 2 = 40
        result = calculate_result(clusters)
        assert result == 40
    
    def test_single_circuit(self):
        """Test finding connection that creates single circuit"""
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        with open(test_file, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f]
        
        # Result should be product of X coordinates: 216 * 117 = 25272
        result = part_2(lines)
        assert result == 25272

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])
