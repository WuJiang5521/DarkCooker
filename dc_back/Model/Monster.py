from termcolor import colored


class Monster:
    def __init__(self):
        self.min_x = -1
        self.max_x = -2
        self.min_y = -1
        self.max_y = -2
        self.list = []
        self.color = 'white'

    def __len__(self):
        return len(self.list)

    def __getitem__(self, item):
        return self.list[item][0] - self.min_x, self.list[item][1] - self.min_y

    def __str__(self):
        ans = '┌'
        for i in range(self.get_width()):
            ans += '－'
        ans += '┐\n'
        for y in range(self.get_height()):
            ans += '｜'
            for x in range(self.get_width()):
                ans += colored('＊', self.color) if self.in_map(x, y) else '．'
            ans += '｜\n'
        ans += '└'
        for i in range(self.get_width()):
            ans += '－'
        ans += '┘'
        return ans

    def print_self(self, color):
        self.color = color
        print(self)

    def in_map(self, x, y):
        return (x + self.min_x, y + self.min_y) in self.list

    def get_width(self):
        return self.max_x - self.min_x + 1

    def get_height(self):
        return self.max_y - self.min_y + 1

    def reverse(self, x, y):
        if (x, y) in self.list:
            self.list.remove((x, y))
        else:
            self.list.append((x, y))
        self.min_x = -1 if len(self.list) is 0 else min(self.list, key=lambda pos: pos[0])[0]
        self.max_x = -2 if len(self.list) is 0 else max(self.list, key=lambda pos: pos[0])[0]
        self.min_y = -1 if len(self.list) is 0 else min(self.list, key=lambda pos: pos[1])[1]
        self.max_y = -2 if len(self.list) is 0 else max(self.list, key=lambda pos: pos[1])[1]
