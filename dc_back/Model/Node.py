from Model.Result import ResultNode


class Node:
    def __init__(self):
        self.pos = (0, 0)  # 当前位置
        self.meet = 0  # 当前位置结果
        self.params = {}  # 其他参数，由Engine决定
        self.situations = []  # 到目前仍符合的情形
        self.children = {
            -4: [],
            -3: [],
            -2: [],
            -1: [],
            1: [],
            2: [],
            3: [],
            4: [],
        }  # 所有可能的子节点
        self.father = None  # 父节点，根结点的父节点为None

    def transform(self):
        root = ResultNode()
        root.pos = self.pos
        root.meet = self.meet
        root.params = self.params
        root.situations = self.situations
        direct = 4  # TODO: replace 4 with the real direct
        root.target = (root.pos[0] + (direct + 1) // 3, root.pos[1] + (direct + 1) % 3 - 1)
        root.children = [child.transform() for child in self.children[direct]]
        return root
