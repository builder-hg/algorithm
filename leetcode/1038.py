"""
DFS 방식으로 순회한다.
방향은 우측으로 타고 들어간 후, 좌측으로 간다.

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0
        def updateFn(cur):
            if not cur:         # 종료조건
                return

            updateFn(cur.right) # 우측 선 탐색

            self.val += cur.val # 노드에서 해야할 작업 1, 값 누적
            cur.val = self.val  # 노드에서 해야할 작업 2, 값 갱신

            updateFn(cur.left)  # 우측 탐색 후 좌측 탐색

        updateFn(root)
        return root
        
"""