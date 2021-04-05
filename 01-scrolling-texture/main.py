#!/usr/bin/env python3
''' Experiment 1 - Scrolling Texture

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import arcade

SCREEN_TITLE = 'Experiment 1 - Scrolling Texture'

SCREEN_WIDTH = 1280  # 720p screen
SCREEN_HEIGHT = 720


class Experiment(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.BLACK)

        self.sprites = None  # List of sprites.
        self.robot1 = None
        self.robot2 = None

        self.robot2_idx = 0
        self.robot2_textures = 0

    def setup(self):
        ''' Load resources and initialize.
        '''
        self.sprites = arcade.SpriteList()

        self.robot1 = arcade.Sprite('resources/character_robot_jump.png')
        self.robot1.top = SCREEN_HEIGHT - 100
        self.robot1.left = 100
        self.sprites.append(self.robot1)

        # self.robot2 = arcade.Sprite('resources/character_robot_jump-2y.png')
        self.robot2 = arcade.Sprite()
        for i in range(self.robot1.height - 1):
            texture = arcade.load_texture('resources/character_robot_jump-2y.png', 0, i, self.robot1.width, self.robot1.height)
            self.robot2.append_texture(texture)
            self.robot2_textures = self.robot2_textures + 1
        self.robot2.set_texture(self.robot2_idx)
        self.robot2.top = SCREEN_HEIGHT - 100
        self.robot2.left = 200
        self.sprites.append(self.robot2)

        arcade.schedule(self.scroll_sprite2, 1/60)

    def scroll_sprite2(self, dt):
        '''
        No idea how to do this in Arcade without defining a new sprite for each
        step of the animation.
        '''
        self.robot2_idx = (self.robot2_idx + 1) % self.robot2_textures
        self.robot2.set_texture(self.robot2_idx)

    def on_draw(self):
        ''' Draw the screen.
        '''
        arcade.start_render()
        self.sprites.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.close()


def main():
    ''' Run our experiment.
    '''
    window = Experiment()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
