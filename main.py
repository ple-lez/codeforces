from collections import deque

def main():
    n = int(input())

    # -1 to convert from 1-indexed to 0-indexed
    shortcuts = [int(s) - 1 for s in input().split()]

    distances = [-1] * n
    to_visit = deque()

    # (intersection, distance)
    to_visit.append((0, 0))

    while len(to_visit) > 0:
        intersection, distance = to_visit.popleft()

        # node has already been visited
        if distances[intersection] != -1:
            continue
        distances[intersection] = distance

        shortcut = shortcuts[intersection]
        if distances[shortcut] == -1:
            to_visit.append((shortcuts[intersection], distance + 1))

        if intersection + 1 < n and distances[intersection + 1] == -1:
            to_visit.append((intersection + 1, distance + 1))

        if intersection - 1 > 0 and distances[intersection - 1] == -1:
            to_visit.append((intersection - 1, distance + 1))

    for d in distances:
        print(d, end=' ')
    print('')

if __name__ == "__main__":
    main()