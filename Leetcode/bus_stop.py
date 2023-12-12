from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        adjList = defaultdict(list)
        
        for route_index, route_stops in enumerate(routes):
            for stop in route_stops:
                adjList[stop].append(route_index)

        q = deque()
        vis = set()
        
        for route in adjList[source]:
            q.append(route)
            vis.add(route)

        busCount = 1

        while q:
            size = len(q)

            for _ in range(size):
                route = q.popleft()

                for stop in routes[route]:
                    if stop == target:
                        return busCount

                    for nextRoute in adjList[stop]:
                        if nextRoute not in vis:
                            vis.add(nextRoute)
                            q.append(nextRoute)

            busCount += 1
        
        return -1
    
test = Solution()

test_list = [[8], [2, 8]]
source = 1
target = 2


res = test.numBusesToDestination(test_list, source, target)

print(res)    