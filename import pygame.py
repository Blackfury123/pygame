import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("LEGENDARY LEGENDER")
background_image = pygame.transform.scale(pygame.image.load('background.webp').convert(), (500, 500))
legender = pygame.transform.scale(pygame.image.load('fortuner.png').convert_alpha(), (200, 200))
legender_rect = legender.get_rect(center=(350, 220))
text = pygame.font.Font(None, 36).render('The Toyota Fortuner Legender.', True, pygame.Color('black'))
text_rect = text.get_rect(center=(250, 360))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))
        screen.blit(legender, legender_rect)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
    game_loop()
