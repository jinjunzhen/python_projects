class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        actual = self.traveral(root, target)
        # will get either greater minimum or smaller maximum
        if actual == target:
            return actual

        if actual > target:
            another_search = target - (actual - target)
        else:
            another_search = target + (target - actual)

        actual_two = self.traveral(root, another_search)

        if  abs(actual - target) < abs(actual_two - target):
            return actual
        else:
            return actual_two