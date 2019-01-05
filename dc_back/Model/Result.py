def print_indent(tab):
    for i in range(tab):
        print('  ', end='')


class ResultNode:
    pos = (0, 0)  # 当前位置
    meet = 0  # 当前位置结果
    params = {}  # 其他参数，由Engine决定
    target = (1, 1)  # 下一步目标
    situations = []  # 到目前仍符合的情形
    children = []  # 所有位置在target的子节点

    def print_self(self, tab):
        print_indent(tab)
        print('{')
        print_indent(tab + 1)
        print('pos: {}, meet: {}, situations: {},'.format(str(self.pos), str(self.meet), str(self.situations)))
        print_indent(tab + 1)
        print('params: {},'.format(str(self.params)))
        if len(self.children) > 0:
            print_indent(tab + 1)
            print('children: [')
            for child in self.children:
                child.print_self(tab + 2)
            print_indent(tab + 1)
            print(']')
        print_indent(tab)
        print('}' + ('' if tab is 0 else ','))
