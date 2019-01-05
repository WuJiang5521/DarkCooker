from Model import *
from ComputeCore.Engines import *
import copy
from termcolor import cprint
import json


class Core:
    SET_WIDTH = 0
    SET_HEIGHT = 1
    ADD_MONSTER = 2
    DELETE_MONSTER = 3
    MODIFY_MONSTER = 4
    CALCULATE = 5

    def __init__(self):
        self.history = []
        self.model = {
            'width': 4,
            'height': 4,
            'monsters': [],
            'situations': [],
            'result': {},
        }
        self.engine = {
            'default': DefaultEngine(self.model),
        }
        self.use_engines = ['default']
        self.verbose = {
            'size': True,
            'monsters': True,
            'situations': True,
            'result': True,
        }

    def handle(self, cmd, msg):
        self.history.append({'type': cmd, 'msg': msg})
        if cmd == Core.SET_WIDTH:
            self.__set_width(msg)
        elif cmd == Core.SET_HEIGHT:
            self.__set_height(msg)
        elif cmd == Core.ADD_MONSTER:
            self.__add_monster()
        elif cmd == Core.DELETE_MONSTER:
            self.__del_monster(msg)
        elif cmd == Core.MODIFY_MONSTER:
            self.__mdf_monster(msg)
        elif cmd == Core.CALCULATE:
            print(self.__cal())
        else:
            pass

    def __set_width(self, msg):
        if isinstance(msg, int) and msg > 0:
            if len(self.model['monsters']) is 0 or msg >= max(self.model['monsters'],
                                                              key=lambda item: item.get_width()):
                self.model['width'] = msg

    def __set_height(self, msg):
        if isinstance(msg, int) and msg > 0:
            if len(self.model['monsters']) is 0 or msg >= max(self.model['monsters'],
                                                              key=lambda item: item.get_height()):
                self.model['height'] = msg

    def __add_monster(self):
        self.model['monsters'].append(Monster())

    def __del_monster(self, msg):
        if isinstance(msg, int):
            if msg < len(self.model['monsters']):
                self.model['monsters'].pop(msg)

    def __mdf_monster(self, msg):
        keys = msg.keys()
        if 'id' in keys and 'x' in keys and 'y' in keys:
            index = msg['id']
            x = msg['x']
            y = msg['y']
            if isinstance(index, int) and index < len(self.model['monsters']):
                monster = self.model['monsters'][index]
                if isinstance(x, int) and 0 <= x < self.model['width'] and \
                        isinstance(y, int) and 0 <= y < self.model['height']:
                    monster.reverse(x, y)

    def __cal(self):
        if self.verbose['size']:
            print({'width': self.model['width'], 'height': self.model['height']})
        if self.verbose['monsters']:
            self.print_monsters()
        self.__cal_situations()
        if self.verbose['situations']:
            self.print_situations()
        self.__cal_engines()
        if self.verbose['result']:
            self.print_result()
        result = {}
        for i in range(len(self.use_engines)):
            result[self.use_engines[i]] = self.model['result'][self.use_engines[i]].json()
        return json.dumps(result)

    def print_monsters(self):
        print("====== Monsters ======")
        for i in range(len(self.model['monsters'])):
            cprint("Monster {}:".format(i + 1), Colors.get_color(i + 1))
            self.model['monsters'][i].print_self(Colors.get_color(i + 1))
        print("======================")

    def __cal_situations(self):
        width = self.model['width']
        height = self.model['height']
        self.model['situations'] = [Situation(width, height)]
        for i in range(len(self.model['monsters'])):
            monster = self.model['monsters'][i]
            while len(self.model['situations']) > 0 and self.model['situations'][0].get_monster_num() <= i:
                father = self.model['situations'].pop(0)
                for x in range(width - monster.get_width() + 1):
                    for y in range(height - monster.get_height() + 1):
                        if x + y is not 0:
                            if father.can_place_monster(monster, x, y):
                                child = copy.deepcopy(father)
                                child.place_monster(monster, x, y)
                                self.model['situations'].append(child)

    def print_situations(self):
        print("===== Situations =====")
        for i in range(len(self.model['situations'])):
            print("Situation {}:".format(i))
            print(self.model['situations'][i])
        print("======================")

    def __cal_engines(self):
        for choice in self.use_engines:
            self.model['result'][choice] = self.engine[choice].run()

    def print_result(self):
        print("======= Result =======")
        for i in range(len(self.use_engines)):
            print("Result {} from Engine {}:".format(i, self.use_engines[i]))
            self.model['result'][self.use_engines[i]].print_self(0)
        print("======================")


if __name__ == '__main__':
    core = Core()
    core.handle(Core.SET_WIDTH, 4)
    core.handle(Core.SET_HEIGHT, 4)
    core.handle(Core.ADD_MONSTER, None)
    core.handle(Core.ADD_MONSTER, None)
    core.handle(Core.MODIFY_MONSTER, {'id': 0, 'x': 0, 'y': 0})
    core.handle(Core.MODIFY_MONSTER, {'id': 0, 'x': 0, 'y': 1})
    core.handle(Core.MODIFY_MONSTER, {'id': 0, 'x': 0, 'y': 2})
    core.handle(Core.MODIFY_MONSTER, {'id': 0, 'x': 1, 'y': 2})
    core.handle(Core.MODIFY_MONSTER, {'id': 1, 'x': 2, 'y': 2})
    core.handle(Core.MODIFY_MONSTER, {'id': 1, 'x': 2, 'y': 1})
    core.handle(Core.MODIFY_MONSTER, {'id': 1, 'x': 1, 'y': 2})
    core.handle(Core.MODIFY_MONSTER, {'id': 1, 'x': 1, 'y': 1})
    core.handle(Core.CALCULATE, None)
