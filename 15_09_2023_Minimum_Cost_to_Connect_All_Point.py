"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""
class Solution:
    def par_value(self, par_child_list: List[int], index: int) -> int:
        if index == par_child_list[index]:
            return index
        else:
            return self.par_value(par_child_list, par_child_list[index])

    def assign_val(self, par_child_list: List[int], index: int, value: int):
        if index == par_child_list[index]:
            par_child_list[index] = value
        else:
            self.assign_val(par_child_list, par_child_list[index], value)
            par_child_list[index] = value

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges_with_weight = []
        n = len(points)
        par_child_list = list(range(n))  # Initialize with each point as its own parent
        min_cost = 0

        # Calculate the weight of edges between all pairs of points
        for i in range(n):
            for j in range(i + 1, n):
                temp_value = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                edges_with_weight.append([temp_value, i, j])

        # Sort edges by weight
        edges_with_weight.sort(key=lambda x: x[0])

        # Kruskal's algorithm
        for edge in edges_with_weight:
            weight, i, j = edge
            par_first = self.par_value(par_child_list, i)
            par_second = self.par_value(par_child_list, j)

            if par_first != par_second:
                min_cost += weight
                self.assign_val(par_child_list, j, par_first)

        return min_cost
