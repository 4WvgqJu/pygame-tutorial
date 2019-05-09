"""Editing graphical shapes.
* placing rectangles"""

import pygame
from random import randint
from pygame.locals import *
from pygamelib import *

words = ['beauty', 'strength', 'love', 'dream', 'silence']
cmd = {
    K_BACKSPACE:'Game.objects.pop()',
    K_p:'Game.capture(self)',
    K_t:'print("test")',}

class GuiDemo(Game):
    """Draw text in different sizes and colors."""
    def __init__(self):
        super(GuiDemo, self).__init__()
        Text('Placing rectangles', size=50)
        Text('Press A to add, BACK to remove', size=24)
        self.editing = False
        self.cmd = cmd


    def on_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.key == K_a:
                Rectangle(pos=event.pos, size=(0, 0))
                self.editing = True
            else:
                sel = self.find_objects(event.pos)
                for obj in sel:
                    obj.selected = True

        elif event.type == MOUSEMOTION:
            if self.editing:
                Game.objects[-1].rect.inflate_ip(event.rel)

        elif event.type == MOUSEBUTTONUP:
            self.editing = False

if __name__ == '__main__':
    GuiDemo().run()