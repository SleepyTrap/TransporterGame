import pygame

class Button:
    """
    Class representing a button.
    """
    def __init__(self, x, y, w, h, text, font, color=(0, 0, 0), bg_color=(255, 255, 255)):
        """
        Initialize the button with position, size, text, font, and colors.
        """
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.bg_color = bg_color
        self.text = text
        self.font = font
        self.txt_surface = self.font.render(text, True, self.color)

    def draw(self, screen):
        """
        Draw the button on the screen.
        """
        pygame.draw.rect(screen, self.bg_color, self.rect)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def is_clicked(self, event):
        """
        Check if the button is clicked.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class InputBox:
    """
    Class representing an input box.
    """
    def __init__(self, x, y, w, h, font, text=''):
        """
        Initialize the input box with position, size, font, and initial text.
        """
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.font = font
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """
        Handle events for the input box.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        """
        Update the input box size if the text is too long.
        """
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        """
        Draw the input box on the screen.
        """
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)