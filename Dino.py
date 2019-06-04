import pygame as pg
import Dino_objects
from pygame.math import Vector2
import random

#Sprites
#self.thanos_car = Dino_objects.Obstacle(Vector2(1200,424),'thanos car.png',90,50)
#self.ugandanknuckle = Dino_objects.Obstacle(Vector2(1000,386),'UgandanKnuckle.png',110,88)
OBSTACLE_TIMER = pg.USEREVENT+0
# Screen
size = [1200, 700]

pg.mixer.pre_init(22050, -16, 2, 1024)
pg.init()
pg.mixer.quit()
pg.mixer.init(22050, -16, 2, 1024)

class DinoGame():
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.fps = 90
        self.player = Dino_objects.Player(Vector2(40,300))
        self.ground1 = Dino_objects.Ground(Vector2(0,474))
        self.ground2 = Dino_objects.Ground(Vector2(1200,474))
        self.screen = pg.display.set_mode(size)
        self.done = False
        self.all_players = pg.sprite.Group()
        self.all_players.add(self.player)
        self.all_grounds = pg.sprite.Group()
        self.all_grounds.add(self.ground1)
        self.all_grounds.add(self.ground2)
        self.all_obstacles = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.ground1)
        self.all_sprites.add(self.ground2)
        self.game_start = True
        pg.time.set_timer(OBSTACLE_TIMER, 900 * random.randint(1,3))
        self.score = 0
        self.game_over_font = pg.font.SysFont('Arial', 150)
        self.score_font = pg.font.SysFont('Arial', 35)
        self.game_over_text = self.game_over_font.render('Game Over!', False, (255,255,255))
        self.try_again_text = self.score_font.render('Press "R" to try again', False, (255,255,255))
        self.background_color = (77,127,150)
        self.game_over = False
        self.score_update = True
        self.speed_value = 10
        self.jump_soundeffect_1 = pg.mixer.Sound('jump_soundeffect_1.wav')
        self.jump_soundeffect_2 = pg.mixer.Sound('jump_soundeffect_2.wav')
        self.jump_soundeffect_3 = pg.mixer.Sound('jump_soundeffect_3.wav')

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if self.game_start:
                    if event.key == pg.K_SPACE and not self.player.jumping:
                        self.player.jumping = True
                        self.player.velocity += Vector2(0,-16)
                        self.random_jump_sound = random.randint(1,3)
                        if self.random_jump_sound == 1:
                            self.jump_soundeffect_1.play(0)
                        if self.random_jump_sound == 2:
                            self.jump_soundeffect_2.play(0)
                        if self.random_jump_sound == 3:
                            self.jump_soundeffect_3.play(0)

                if event.key == pg.K_SPACE and not self.game_start:
                    self.game_start = True

                if event.key == pg.K_r and self.game_over:
                    self.score = 0
                    self.game_over = False
                    self.player = Dino_objects.Player(Vector2(40,300))
                    self.ground1 = Dino_objects.Ground(Vector2(0,474))
                    self.ground2 = Dino_objects.Ground(Vector2(1200,474))
                    self.all_players.add(self.player)
                    self.all_grounds.add(self.ground1)
                    self.all_grounds.add(self.ground2)
                    self.all_sprites.add(self.player)
                    self.all_sprites.add(self.ground1)
                    self.all_sprites.add(self.ground2)
                    pg.time.set_timer(OBSTACLE_TIMER, 900 * random.randint(1,3))
                    self.speed_value = 10
                    self.score_update = True
                    self.background_color = (77,127,150)


            elif event.type == OBSTACLE_TIMER and self.game_start:
                pg.time.set_timer(OBSTACLE_TIMER, 0)
                random_obstacle = random.randint(1,4)
                if random_obstacle == 1:
                    self.thanos_car = Dino_objects.Obstacle(Vector2(1200,424),'thanos car.png',90,50)
                    self.thanos_car.speed = Vector2(self.speed_value,0)
                    self.all_obstacles.add(self.thanos_car)
                    self.all_sprites.add(self.thanos_car)
                if random_obstacle == 2:
                    self.ugandanknuckle = Dino_objects.Obstacle(Vector2(1200,386),'UgandanKnuckle.png',110,88)
                    self.ugandanknuckle.speed = Vector2(self.speed_value,0)
                    self.all_obstacles.add(self.ugandanknuckle)
                    self.all_sprites.add(self.ugandanknuckle)
                if random_obstacle == 3:
                    self.crab_rave = Dino_objects.Obstacle(Vector2(1200,405), 'crabrave.png', 140,69)
                    self.crab_rave.speed = Vector2(self.speed_value,0)
                    self.all_obstacles.add(self.crab_rave)
                    self.all_sprites.add(self.crab_rave)
                if random_obstacle == 4:
                    self.shaggyultrainstinct = Dino_objects.Obstacle(Vector2(1200,346), 'shaggyultrainstinct.png', 97,128)
                    self.shaggyultrainstinct.speed = Vector2(self.speed_value,0)
                    self.all_obstacles.add(self.shaggyultrainstinct)
                    self.all_sprites.add(self.shaggyultrainstinct)
                pg.time.set_timer(OBSTACLE_TIMER, 900 * random.randint(1,3))

    def game_over_event(self):
        for obstacle in self.all_obstacles:
            obstacle.kill()
        self.ground1.kill()
        self.ground2.kill()
        pg.time.set_timer(OBSTACLE_TIMER,0)
        self.player.kill()
        self.background_color = (0,0,0)
        self.score_update = False


    def update(self):
        for sprite in self.all_sprites:
            sprite.update()
        for obstacle in self.all_obstacles:
            if obstacle.rect.x <= -50:
                obstacle.kill()
            if pg.sprite.collide_rect(self.player, obstacle):
                self.game_over = True
        if pg.sprite.collide_rect(self.player, self.ground1):
            self.player.rect.y = 300
            self.player.jumping = False
        elif pg.sprite.collide_rect(self.player, self.ground2):
            self.player.rect.y = 300
            self.player.jumping = False
        if self.score_update:
            self.score += 10 / 90
            self.score_text = self.score_font.render('Score: ' + str(int(self.score)), False, (255,255,255))
        self.speed_value += 1 / 360
        self.ground1.speed = Vector2(self.speed_value,0)
        self.ground2.speed = Vector2(self.speed_value,0)
        if self.ground1.rect.right < 0:
            self.ground1.setposition(Vector2(self.ground2.rect.right,474))
        if self.ground2.rect.right < 0:
            self.ground2.setposition(Vector2(self.ground1.rect.right,474))
        if self.game_over:
            self.game_over_event()

    def draw(self):
        self.screen.fill(self.background_color)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.score_text,(10,10))
        if self.game_over:
            self.screen.blit(self.game_over_text, (190,200))
            self.screen.blit(self.try_again_text, (450,400))

    def run(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)


game = DinoGame()
game.run()


# Close the window and quit.
pygame.quit()
