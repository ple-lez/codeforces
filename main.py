from collections import deque

def main():
    n = int(input())
    shortcuts = [int(s) - 1 for s in input().split()]

    distances = [-1] * n
    to_visit = deque()
    visited = set()

    # (intersection, distance)
    to_visit.append((0, 0))
    while len(to_visit) > 0:
        intersection, distance = to_visit.popleft()

        if intersection in visited:
            continue
        
        visited.add(intersection)
        distances[intersection] = distance

        if shortcuts[intersection] not in visited:
            to_visit.append((shortcuts[intersection], distance + 1))

        if intersection + 1 < n and intersection + 1 not in visited:
            to_visit.append((intersection + 1, distance + 1))

        if intersection - 1 > 0 and intersection  - 1 not in visited:
            to_visit.append((intersection - 1, distance + 1))

    print(' '.join([str(d) for d in distances]))


if __name__ == "__main__":
    main()