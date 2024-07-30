from collections import defaultdict, deque

class SocialNetwork:
    def __init__(self):
        self.network = defaultdict(set)

    def add_friendship(self, person1, person2):
        self.network[person1].add(person2)
        self.network[person2].add(person1)

    def find_friends(self, person):
        return self.network[person]

    def find_common_friends(self, person1, person2):
        return self.network[person1] & self.network[person2]

    def find_nth_connection(self, start, end):
        if start == end:
            return 0
        visited = set()
        queue = deque([(start, 0)])
        while queue:
            current, depth = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            for friend in self.network[current]:
                if friend == end:
                    return depth + 1
                if friend not in visited:
                    queue.append((friend, depth + 1))
        return -1

if __name__ == "__main__":
    sn = SocialNetwork()
    sn.add_friendship("Alice", "Bob")
    sn.add_friendship("Bob", "Janice")
    sn.add_friendship("Alice", "Charlie")
    sn.add_friendship("Charlie", "Janice")
    sn.add_friendship("Bob", "Eve")

    print("Friends of Alice:", sn.find_friends("Alice"))
    print("Friends of Bob:", sn.find_friends("Bob"))
    print("Common friends of Alice and Bob:", sn.find_common_friends("Alice", "Bob"))
    print("Common friends of Alice and Charlie:", sn.find_common_friends("Alice", "Charlie"))

    print("Nth connection (Alice to Janice):", sn.find_nth_connection("Alice", "Janice"))
    print("Nth connection (Alice to Bob):", sn.find_nth_connection("Alice", "Bob"))
    print("Nth connection (Alice to Eve):", sn.find_nth_connection("Alice", "Eve"))
    print("Nth connection (Alice to non-existent):", sn.find_nth_connection("Alice", "non-existent"))
