def read_input(filename):
    graph = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            node, neighbors = line.split(': ')
            graph[node] = neighbors.split(' ')
    return graph

def count_paths(graph, current, target, memo):
    if current == target:
        return 1
    
    if current in memo:
        return memo[current]
    
    if current not in graph:
        return 0
        
    total_paths = 0
    for neighbor in graph[current]:
        total_paths += count_paths(graph, neighbor, target, memo)
    
    memo[current] = total_paths
    return total_paths

def part_1(graph):
    return count_paths(graph, 'you', 'out', {})

def part_2(graph):
    # Calculate paths for: svr -> dac -> fft -> out
    svr_dac = count_paths(graph, 'svr', 'dac', {})
    dac_fft = count_paths(graph, 'dac', 'fft', {})
    fft_out = count_paths(graph, 'fft', 'out', {})
    count1 = svr_dac * dac_fft * fft_out
    
    # Calculate paths for: svr -> fft -> dac -> out
    svr_fft = count_paths(graph, 'svr', 'fft', {})
    fft_dac = count_paths(graph, 'fft', 'dac', {})
    dac_out = count_paths(graph, 'dac', 'out', {})
    count2 = svr_fft * fft_dac * dac_out
    
    return count1 + count2

def main():
    """Main function to run the solution"""
    # Assuming running from root directory
    input_data = read_input('11/input.txt')
    print(f"Part 1 = {part_1(input_data)}")
    print(f"Part 2 = {part_2(input_data)}")

if __name__ == "__main__":
    main()
