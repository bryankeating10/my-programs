import pygame

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colored Square")

# Get user input for color
hex_color = input("Enter a color in hexadecimal format (e.g., #FF5733): ").strip()

# Validate and convert the hex color to RGB
try:
    if hex_color.startswith("#") and len(hex_color) == 7:
        color = pygame.Color(hex_color)  # Convert hex to RGB
    else:
        raise ValueError("Invalid format")
except ValueError:
    print("Invalid hex color! Defaulting to white.")
    color = (255, 255, 255)  # Default to white

# Square properties
SQUARE_SIZE = 200
square_x = (WIDTH - SQUARE_SIZE) // 2
square_y = (HEIGHT - SQUARE_SIZE) // 2

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black

    # Draw the square
    pygame.draw.rect(screen, color, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Update the display

# Quit pygame
pygame.quit()