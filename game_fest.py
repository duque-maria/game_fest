import pygame, sys, random

def draw_floor():
    screen.blit(flor_surface,(floor_x_pos,900))
    screen.blit(floor_surface,(floor_x_pos + 576,900))

def create_pipe():
    random_pipe_pos = random.choice(pipe_heigth)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
def remove_pipes(pipes): 
    for pipe in pipes:
        if pipe.centerx == -600:
            pipes.remove(pipe)
    return pipes
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
             death_sound.play()
             return False
    
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False
    
    return True

def rotate_bird(bird):
    new_bird = pygame.transforms.rotozoom(bird,-bird_movement * 3,1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))