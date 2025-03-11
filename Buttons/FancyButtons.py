from static_variables import *
class FancyButton:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = color
        self.hover_color = hover_color
        self.color = color
        self.alpha = 255  # Transparency for animation

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = self.base_color

        # Button shape
        pygame.draw.rect(screen, self.color, self.rect, border_radius=15)

        # Render text
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())