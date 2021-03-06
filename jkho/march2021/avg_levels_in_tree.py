# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# for each time you recruse, incrmenet it by 1, and have a dictionary that is accessible to all
class Solution:
    dictionarySumCount = {}
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.recurse(root,0)
        print(self.dictionarySumCount)
        ls = []
        for key in sorted(self.dictionarySumCount):
            layerCount,layerSum = self.dictionarySumCount[key]
            avg = layerSum/layerCount
            ls.append(avg)
        return ls
        
    def recurse(self, node: TreeNode, currentLayer):
        if node.left:
            self.recurse(node.left,currentLayer+1)
        if node.right:
            self.recurse(node.right,currentLayer+1)
        if currentLayer in self.dictionarySumCount:
            count, total = self.dictionarySumCount[currentLayer]
            self.dictionarySumCount[currentLayer] = [count+1,total+node.val]
        else:
            self.dictionarySumCount[currentLayer] = [1,node.val]
        