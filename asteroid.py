import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        
        rand_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(rand_angle)
        vector_2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_1.velocity = vector_1 * 1.2
        new_ast_2.velocity = vector_2 * 1.2

       
        return new_ast_1, new_ast_2







        

    

