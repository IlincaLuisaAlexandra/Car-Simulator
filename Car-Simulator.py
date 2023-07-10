from microbit import *
i = 0
nivel = 0
text_list_dif: List[str] = []
car0: game.LedSprite = None
car1: game.LedSprite = None
car2: game.LedSprite = None
car3: game.LedSprite = None
car4: game.LedSprite = None
gameOn = False
player: game.LedSprite = None
basic.show_string("Welcome!")
text_list_dif = ["E", "H"]


def on_button_pressed_a():
    global i
    if nivel == 0:
        i = i - 1
        if i < 0:
            i = 1
        basic.show_string("" + text_list_dif[i])
    elif player.get(LedSpriteProperty.X) > 0:
        player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global nivel
    if nivel == 0:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.happy),SoundExpressionPlayMode.UNTIL_DONE)
        nivel = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global i
    if nivel == 0:
        i = i + 1
        if i > 1:
            i = 0
        basic.show_string("" + text_list_dif[i])
    elif player.get(LedSpriteProperty.X) < 4:
        player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def controlCar(car: game.LedSprite):
    global gameOn
    basic.pause(randint(0, 5000))
    while gameOn == True:
        if car.get(LedSpriteProperty.Y) == 4:
            if player.is_touching(car):
                gameOn = False
            else:
                game.set_score(game.score() + 1)
                car.set(LedSpriteProperty.Y, 0)
                basic.pause(randint(0, 5000))
        else:
            car.change(LedSpriteProperty.Y, 1)
            basic.pause(500)


def on_forever():
    if nivel == 0:
        basic.show_string("" + text_list_dif[i])
    if nivel==1:
        global player, gameOn
        game.set_score(0)
        player = game.create_sprite(2, 4)
        gameOn = True
        while gameOn == True:
            basic.pause(100)
        basic.show_string("Restart?")
        
        
        """     
        if input.logo_was_pressed():
                    nivel = 0
        if input.sound_level() > 100:
            nivel=0
            nivel=1
        """
basic.forever(on_forever)

def on_forever0():
    if nivel==1:
        global car0
        if(i==0):
            basic.pause(250)
        else: basic.pause(100)
        if gameOn == True:
            car0 = game.create_sprite(0, 0)
            controlCar(car0)
basic.forever(on_forever0)

def on_forever1():
    if nivel==1:
        global car1
        if(i==0):
            basic.pause(250)
        else: basic.pause(100)
        if gameOn == True:
            car1 = game.create_sprite(1, 0)
            controlCar(car1)
basic.forever(on_forever1)

def on_forever2():
    if nivel==1:
        global car2
        if(i==0):
            basic.pause(250)
        else: basic.pause(100)
        if gameOn == True:
            car2 = game.create_sprite(2, 0)
            controlCar(car2)
basic.forever(on_forever2)
        
def on_forever3():
    if nivel==1:
        global car3
        if(i==0):
            basic.pause(250)
        else: basic.pause(100)
        if gameOn == True:
            car3 = game.create_sprite(3, 0)
            controlCar(car3)
basic.forever(on_forever3)

def on_forever4():
    if nivel==1:
        global car4
        if(i==0):
            basic.pause(250)
        else: basic.pause(100)
        if gameOn == True:
            car4 = game.create_sprite(4, 0)
            controlCar(car4)
basic.forever(on_forever4)