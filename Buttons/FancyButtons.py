from static_variables import *
class FancyButton:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

        # Load and prepare button images
        self.original_image = pygame.image.load("images/button.png").convert_alpha()

        # Create base and hover versions
        self.base_image = self.create_tinted_image(color, width, height)
        self.hover_image = self.create_tinted_image(hover_color, width, height)

        self.current_image = self.base_image
        self.alpha = 255

    def create_tinted_image(self, color, width, height):
        """Create a tinted and scaled button image"""
        img = pygame.transform.scale(self.original_image, (width, height))
        colored_img = img.copy()
        colored_img.fill(color, special_flags=pygame.BLEND_RGB_MULT)
        return colored_img

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        self.current_image = self.hover_image if self.rect.collidepoint(mouse_pos) else self.base_image

        # Draw the button image
        screen.blit(self.current_image, self.rect.topleft)

        # Draw text
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())