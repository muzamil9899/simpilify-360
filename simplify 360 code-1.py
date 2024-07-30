from collections import defaultdict, deque

def calculate_times(tasks, dependencies):
    # Initialize data structures
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    duration = {}
    earliest_start = {}
    earliest_finish = {}
    latest_start = {}
    latest_finish = {}
    
    # Initialize the tasks and dependencies
    for task, dur in tasks.items():
        duration[task] = dur
        earliest_start[task] = 0
        earliest_finish[task] = 0
        latest_start[task] = float('inf')
        latest_finish[task] = float('inf')
        in_degree[task] = 0
    
    for dep in dependencies:
        u, v = dep
        graph[u].append(v)
        in_degree[v] += 1
    
    # Find the start task
    start_task = None
    for task in tasks:
        if in_degree[task] == 0:
            start_task = task
            break
    
    if start_task is None:
        raise ValueError("No start task found. Check the input dependencies.")
    
    # Calculate Earliest Start and Finish Times using Topological Sort
    topo_sort = []
    queue = deque([start_task])
    while queue:
        current = queue.popleft()
        topo_sort.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            earliest_start[neighbor] = max(earliest_start[neighbor], earliest_finish[current])
        earliest_finish[current] = earliest_start[current] + duration[current]
    
    # The earliest time all tasks will be completed
    earliest_completion_time = max(earliest_finish.values())
    
    # Set the latest finish time of the last task to the earliest completion time
    for task in tasks:
        if len(graph[task]) == 0:
            latest_finish[task] = earliest_completion_time
    
    # Calculate Latest Start and Finish Times in reverse topological order
    for task in reversed(topo_sort):
        latest_finish[task] = min(latest_finish[task], earliest_finish[task])
        latest_start[task] = latest_finish[task] - duration[task]
        for predecessor in [key for key, values in graph.items() if task in values]:
            latest_finish[predecessor] = min(latest_finish[predecessor], latest_start[task])
    
    # The latest time all tasks will be completed
    latest_completion_time = max(latest_finish.values())
    
    return earliest_completion_time, latest_completion_time

# Example usage
tasks = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 1,
    'E': 6
}

dependencies = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('D', 'E')
]

earliest_completion, latest_completion = calculate_times(tasks, dependencies)
print(f"Earliest time all tasks will be completed: {earliest_completion}")
print(f"Latest time all tasks will be completed: {latest_completion}")
