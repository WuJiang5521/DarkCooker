from Model.Monster import Monster


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
        }

    def handle(self, cmd, msg):
        self.history.append({'type': cmd, 'msg': msg})
        if cmd == Core.SET_WIDTH:
            if isinstance(msg, int):
                if msg >= max(self.model['monsters'], key=lambda x: x.width()):
                    self.model['width'] = msg
        elif cmd == Core.SET_HEIGHT:
            if isinstance(msg, int):
                if msg >= max(self.model['monsters'], key=lambda x: x.height()):
                    self.model['height'] = msg
        elif cmd == Core.ADD_MONSTER:
            self.model['monsters'].append(Monster())
        elif cmd == Core.DELETE_MONSTER:
            if isinstance(msg, int):
                if msg < len(self.model['monsters']):
                    self.model['monsters'].pop(msg)
        elif cmd == Core.MODIFY_MONSTER:
            keys = msg.keys()
            if 'id' in keys and 'x' in keys and 'y'
        elif cmd == Core.CALCULATE:
            pass
        else:
            pass


if __name__ == '__main__':
    core = Core()
    core.handle(Core.SET_WIDTH, 5)
    core.handle(Core.SET_HEIGHT, 5)
    core.handle(Core.ADD_MONSTER, None)
    core.handle(Core.ADD_MONSTER, None)
    core.handle(Core.MODIFY_MONSTER, {'id': 0, 'x': 0, 'y': 0})
    core.handle(Core.MODIFY_MONSTER, {'id': 0, 'x': 0, 'y': 1})
    core.handle(Core.MODIFY_MONSTER, {'id': 0, 'x': 0, 'y': 2})
    core.handle(Core.MODIFY_MONSTER, {'id': 0, 'x': 1, 'y': 2})
    core.handle(Core.MODIFY_MONSTER, {'id': 1, 'x': 0, 'y': 0})
    core.handle(Core.MODIFY_MONSTER, {'id': 1, 'x': 0, 'y': 1})
    core.handle(Core.MODIFY_MONSTER, {'id': 1, 'x': 1, 'y': 0})
    core.handle(Core.MODIFY_MONSTER, {'id': 1, 'x': 1, 'y': 1})
    core.handle(Core.CALCULATE, None)
