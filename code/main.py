import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_speed = 250
helicopter_speed = 200

truck_image = pygame.image.load("truck.png")
gas_station_image = pygame.image.load("gas_station.png")
home_image = pygame.image.load("home.png")
storage_image = pygame.image.load("storage.png")
helicopter_image = pygame.image.load("helicopter.png")
truck_pos = truck_image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
gas_station_pos = (screen.get_width()/2 ,screen.get_height()-150)
home_pos = (0,screen.get_height()/2)
storage_pos = (screen.get_width()-100,screen.get_height()-100)
helicopter_pos = helicopter_image.get_rect(center=(screen.get_width()-100, 0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # Draw the truck image
    screen.blit(truck_image, truck_pos.topleft)
    screen.blit(gas_station_image, gas_station_pos)
    screen.blit(home_image,home_pos)
    screen.blit(storage_image,storage_pos)
    screen.blit(helicopter_image,helicopter_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        truck_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        truck_pos.y += player_speed * dt
    if keys[pygame.K_a]:
        truck_pos.x -= player_speed * dt
    if keys[pygame.K_d]:
        truck_pos.x += player_speed * dt

    if helicopter_pos.x < truck_pos.x:
        helicopter_pos.x += helicopter_speed * dt
    if helicopter_pos.x > truck_pos.x:
        helicopter_pos.x -= helicopter_speed * dt
    if helicopter_pos.y < truck_pos.y:
        helicopter_pos.y += helicopter_speed * dt
    if helicopter_pos.y > truck_pos.y:
        helicopter_pos.y -= helicopter_speed * dt

    if(helicopter_pos.x == truck_pos.x and helicopter_pos.y == truck_pos.y):
        print("You have been caught by the helicopter")
        running = False


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()