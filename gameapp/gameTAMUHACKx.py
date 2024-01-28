import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Addition Game")

BACKGROUND_COLOR = (12, 72, 112)
TEXT_COLOR = (247, 89, 218)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

font = pygame.font.Font(None, 64)

apple_img = pygame.image.load("C:\\Users\\midde\\OneDrive\\Desktop\\red-apple-cartoon-png.png")
apple_img = pygame.transform.scale(apple_img, (50, 50))

#FUNCTIONS:

def generate_problem():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return num1, num2

def render_apples(number, x, y):
    for i in range(number):
        screen.blit(apple_img, (x, y + i * 60))

#MAIN LOOP

def main():
    clock = pygame.time.Clock()
    running = True
    apples_mode = False
    problem = generate_problem()
    answer = ""
    consecutive_wrong_attempts = 0

    while running:
        screen.fill(BACKGROUND_COLOR)

        if consecutive_wrong_attempts >= 2:
            apples_mode = not apples_mode
            consecutive_wrong_attempts = 0

        if apples_mode:
            num1, num2 = problem
            render_apples(num1, WIDTH // 4 - 50, HEIGHT // 4 - 100)
            plus_sign = font.render('+', True, TEXT_COLOR)
            plus_sign_rect = plus_sign.get_rect(center=(WIDTH // 2, HEIGHT // 4))
            screen.blit(plus_sign, plus_sign_rect)
            render_apples(num2, WIDTH * 3 // 4 - 50, HEIGHT // 4 - 100)
        else:
            num1, num2 = problem
            text = font.render(f"What is {num1} + {num2}?", True, TEXT_COLOR)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 - 150))
            screen.blit(text, text_rect)

        input_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 50)
        pygame.draw.rect(screen, TEXT_COLOR, input_rect, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        if int(answer) == num1 + num2:
                            result_text = font.render("Correct!", True, GREEN)
                            consecutive_wrong_attempts = 0
                        else:
                            result_text = font.render("Incorrect!", True, RED)
                            consecutive_wrong_attempts += 1
                        result_rect = result_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 150))
                        screen.blit(result_text, result_rect)
                        pygame.display.flip()
                        pygame.time.delay(1000)
                    except ValueError:
                        pass
                    problem = generate_problem()
                    answer = ""
                elif event.key == pygame.K_BACKSPACE:
                    answer = answer[:-1]
                elif event.unicode.isdigit():
                    answer += event.unicode

        input_text = font.render(answer, True, TEXT_COLOR)
        input_text_rect = input_text.get_rect(center=input_rect.center)
        screen.blit(input_text, input_text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
