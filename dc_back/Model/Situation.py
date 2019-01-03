class Situation:
    def __init__(self, x, y):
        self.width = x
        self.height = y
        self.map = [[0 for j in range(y)] for i in range(x)]
        self.monster_num = 0

    def __str__(self):
        ans = '┌'
        for i in range(self.width):
            ans += '－'
        ans += '┐\n'
        for y in range(self.height):
            ans += '｜'
            for x in range(self.width):
                ans += chr(self.map[x][y] + 65296)
            ans += '｜\n'
        ans += '└'
        for i in range(self.width):
            ans += '－'
        ans += '┘'
        return ans

    def get_monster_num(self):
        return self.monster_num

    def can_place_monster(self, monster, x, y):
        for i in range(len(monster)):
            dx, dy = monster[i]
            if self.map[x + dx][y + dy] is not 0:
                return False
        return True

    def place_monster(self, monster, x, y):
        self.monster_num += 1
        for i in range(len(monster)):
            dx, dy = monster[i]
            self.map[x + dx][y + dy] = self.monster_num
