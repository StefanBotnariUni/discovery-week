from static_variables import *
class RadioButton:
    def __init__(self, x, y, text, is_checked=False):
        self.x = x
        self.y = y
        self.text = text
        self.is_checked = is_checked
        self.radius = 15  # Radio button size

    def draw(self, screen):
        # Outer circle
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius, 2)

        # Inner filled circle (if checked)
        if self.is_checked:
            pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius // 2)

        # Render text
        text_surf = small_font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(midleft=(self.x + 25, self.y))
        screen.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos):
        return (mouse_pos[0] - self.x) ** 2 + (mouse_pos[1] - self.y) ** 2 <= self.radius ** 2
