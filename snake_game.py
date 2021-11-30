# Alan Blandon
# CPSC 386-01
# 2021-11-26
# alanblandon@csu.fullerton.edu
# @AlanBlandon
#
# Lab 02-00
#
# This file contains the snake-game class.
#

""" System Modules """
import sys
import os
import json
from datetime import date
from random import randrange
import pygame
from player import Player
from food import Food
from button import Button


pygame.init()  # Initialize all imported pygame modules.
# Constant global variables:
WIDTH = 1200
HEIGHT = 800
WHITE_RGB = (255, 255, 255)
BLACK_RGB = (0, 0, 0)
GREEN_RGB = (0, 125, 0)
RED_RGB = (200, 64, 24)
GRAY_RGB = (47, 79, 79)
LIGHT_GREEN_RGB = (0, 255, 0)
LIGHT_RED_RGB = (255, 0, 0)
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 100
SUB_TITLE_FONT = pygame.font.SysFont("ubuntu", 90, bold=True, italic=True)
BUTTON_FONT = pygame.font.SysFont("ubuntu", 45, bold=True)
TEXT_FONT = pygame.font.SysFont("ubuntu", 35, bold=True)
pygame.display.set_caption('Snake Game!')  # Set the caption of the window.


class SnakeGame:
    """SnakeGame Class Functions"""

    def __init__(self):
        """SnakeGame Init Function"""
        self.start_screen()  # Call the start screen function.

    # This function changes the format of the text so that it fits within the
    # window for both the controls and the rules screen.
    @classmethod
    def blit_lines(cls, screen, text, x_value, y_value):
        """Blit Lines Function"""
        height = TEXT_FONT.get_height()
        lines = text.split('\n')
        for i, line in enumerate(lines):
            screen_text = TEXT_FONT.render(line, True, BLACK_RGB)
            screen.blit(screen_text, [x_value, y_value + (i * height)])

    def start_screen(self):
        """Start Screen Function"""
        # Set the size for the start menu screen.
        start_screen = pygame.display.set_mode([WIDTH - 75, HEIGHT - 75])
        # Set the text for the title and buttons on the start menu screen.
        title_font = pygame.font.SysFont("ubuntu", 100, bold=True, italic=True)
        title_text = title_font.render('SNAKE GAME', True, BLACK_RGB)
        play_text = BUTTON_FONT.render('Play Game', True, BLACK_RGB)
        rules_text = BUTTON_FONT.render('Game Rules', True, BLACK_RGB)
        controls_text = BUTTON_FONT.render('Controls', True, WHITE_RGB)
        # Set the coordinates for the buttons on the start menu screen.
        play_x = (WIDTH / 2) - 160
        play_y = (HEIGHT / 2) - 100
        rules_x = (WIDTH / 2) - 10
        rules_y = (HEIGHT / 2) + 80
        controls_x = (WIDTH / 2) - 330
        controls_y = (HEIGHT / 2) + 80
        # While the start menu screen is shown, continue the loop.
        show_start_screen = True
        while show_start_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    show_start_screen = False
                    self.end(0, 0)  # Call the end game function.
            start_screen.fill(WHITE_RGB)  # Change the background color.
            # Display the title text at the specified coordinates.
            start_screen.blit(
                title_text, [(WIDTH / 2) - 345, (HEIGHT / 2) - 270]
            )
            mouse = pygame.mouse.get_pos()  # Get the mouse position.
            click = pygame.mouse.get_pressed()  # Get the mouse click position.
            # Create rectangle objects for each button.
            play_rect = pygame.Rect(play_x, play_y, BUTTON_WIDTH, BUTTON_HEIGHT)
            rules_rect = pygame.Rect(
                rules_x, rules_y, BUTTON_WIDTH + 15, BUTTON_HEIGHT
            )
            controls_rect = pygame.Rect(
                controls_x, controls_y, BUTTON_WIDTH - 15, BUTTON_HEIGHT
            )
            # Initialize each button for the start menu screen.
            play_button = Button(start_screen, GREEN_RGB, play_x, play_y)
            rules_button = Button(start_screen, RED_RGB, rules_x, rules_y)
            controls_button = Button(
                start_screen, BLACK_RGB, controls_x, controls_y
            )
            # Call the make button function.
            play_button.make_button(BUTTON_WIDTH, BUTTON_HEIGHT)
            rules_button.make_button(BUTTON_WIDTH + 15, BUTTON_HEIGHT)
            controls_button.make_button(BUTTON_WIDTH - 15, BUTTON_HEIGHT)
            # Call the is over function to check if the mouse is over a button.
            play_button.is_over(
                LIGHT_GREEN_RGB, BUTTON_WIDTH, BUTTON_HEIGHT, mouse
            )
            rules_button.is_over(
                LIGHT_RED_RGB, BUTTON_WIDTH + 15, BUTTON_HEIGHT, mouse
            )
            controls_button.is_over(
                GRAY_RGB, BUTTON_WIDTH - 15, BUTTON_HEIGHT, mouse
            )
            # Display each button at the specified coordinates.
            start_screen.blit(play_text, [(WIDTH / 2) - 145, (HEIGHT / 2) - 80])
            start_screen.blit(rules_text, [(WIDTH / 2), (HEIGHT / 2) + 100])
            start_screen.blit(
                controls_text, [(WIDTH / 2) - 305, (HEIGHT / 2) + 100]
            )
            # If a button is clicked then call the corresponding function.
            if play_rect.collidepoint(mouse) and click[0]:
                self.run()
            if rules_rect.collidepoint(mouse) and click[0]:
                self.rules_screen()
            if controls_rect.collidepoint(mouse) and click[0]:
                self.controls_screen()
            pygame.display.update()

    def controls_screen(self):
        """Controls Screen Function"""
        # Set the size for the controls screen.
        controls_screen = pygame.display.set_mode((WIDTH - 75, HEIGHT - 75))
        # Set the text for the title and the button on the controls screen.
        text = SUB_TITLE_FONT.render('Controls', True, BLACK_RGB)
        return_text = BUTTON_FONT.render('Return', True, BLACK_RGB)
        control_1 = "- Press the up arrow key to move upwards.\n\n"
        control_2 = "- Press the down arrow key to move downwards.\n\n"
        control_3 = "- Press the left arrow key to move towards the left.\n\n"
        control_4 = "- Press the right arrow key to move towards the right.\n"
        controls_text = control_1 + control_2 + control_3 + control_4
        # Set the coordinates for the return button on the controls screen.
        return_x = (WIDTH / 2) - 140
        return_y = (HEIGHT / 2) + 155
        # While the controls screen is shown, continue the loop.
        show_controls_screen = True
        while show_controls_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    show_controls_screen = False
                    self.end(0, 0)  # Call the end game function.
            controls_screen.fill(WHITE_RGB)  # Change the background color.
            # Display the title text at the specified coordinates.
            controls_screen.blit(text, [(WIDTH / 2) - 210, (HEIGHT / 2) - 360])
            mouse = pygame.mouse.get_pos()  # Get the mouse position.
            click = pygame.mouse.get_pressed()  # Get the mouse click position.
            # Call the blit lines function.
            self.blit_lines(
                controls_screen,
                controls_text,
                (WIDTH / 2) - 500,
                (HEIGHT / 2) - 200,
            )
            # Create a rectangle object for the return button.
            return_rect = pygame.Rect(
                return_x, return_y, BUTTON_WIDTH - 75, BUTTON_HEIGHT
            )
            # Initialize the return button for the controls screen.
            return_button = Button(controls_screen, RED_RGB, return_x, return_y)
            # Call the make button function.
            return_button.make_button(BUTTON_WIDTH - 75, BUTTON_HEIGHT)
            # Call the is over function to check if the mouse is over a button.
            return_button.is_over(
                LIGHT_RED_RGB, BUTTON_WIDTH - 75, BUTTON_HEIGHT, mouse
            )
            # Display the return button at the specified coordinates.
            controls_screen.blit(
                return_text, [(WIDTH / 2) - 125, (HEIGHT / 2) + 175]
            )
            # If the button is clicked then call the corresponding function.
            if return_rect.collidepoint(mouse) and click[0]:
                self.start_screen()
            pygame.display.update()

    def rules_screen(self):
        """Rules Screen Function"""
        # Set the size for the rules screen.
        rules_screen = pygame.display.set_mode((WIDTH - 75, HEIGHT - 75))
        # Set the text for the title and the button on the rules screen.
        text = SUB_TITLE_FONT.render('Rules', True, BLACK_RGB)
        return_text = BUTTON_FONT.render('Return', True, BLACK_RGB)
        rule_1 = "- The snake starts at the center of the board.\n"
        rule_2 = "- The snake moves at a constant speed.\n"
        rule_3 = "- The snake moves only up, down, left or right.\n"
        rule_4 = "- Apples appear at random locations on the board.\n"
        rule_5 = "- When the snake eats an apple, it gets longer.\n"
        rule_6 = "- The game continues until the snake dies, by either\n"
        rule_6_pt2 = "  running into any edge of the board or by running\n"
        rule_6_pt3 = "  into its own tail.\n"
        rule_7 = "- The score is based on the number of apples eaten by the\n"
        rule_7_pt2 = "  snake and by the amount of time the snake survives."
        rules_text = (
            rule_1
            + rule_2
            + rule_3
            + rule_4
            + rule_5
            + rule_6
            + rule_6_pt2
            + rule_6_pt3
            + rule_7
            + rule_7_pt2
        )
        # Set the coordinates for the return button on the rules screen.
        return_x = (WIDTH / 2) - 140
        return_y = (HEIGHT / 2) + 175
        # While the rules screen is shown, continue the loop.
        show_rules_screen = True
        while show_rules_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    show_rules_screen = False
                    self.end(0, 0)  # Call the end game function.
            rules_screen.fill(WHITE_RGB)  # Change the background color.
            # Display the title text at the specified coordinates.
            rules_screen.blit(text, [(WIDTH / 2) - 150, (HEIGHT / 2) - 380])
            mouse = pygame.mouse.get_pos()  # Get the mouse position.
            click = pygame.mouse.get_pressed()  # Get the mouse click position.
            # Call the blit lines function.
            self.blit_lines(
                rules_screen, rules_text, (WIDTH / 2) - 500, (HEIGHT / 2) - 260
            )
            # Create a rectangle object for the return button.
            return_rect = pygame.Rect(
                return_x, return_y, BUTTON_WIDTH - 75, BUTTON_HEIGHT
            )
            # Initialize the return button for the rules screen.
            return_button = Button(rules_screen, RED_RGB, return_x, return_y)
            # Call the make button function.
            return_button.make_button(BUTTON_WIDTH - 75, BUTTON_HEIGHT)
            # Call the is over function to check if the mouse is over a button.
            return_button.is_over(
                LIGHT_RED_RGB, BUTTON_WIDTH - 75, BUTTON_HEIGHT, mouse
            )
            # Display the return button at the specified coordinates.
            rules_screen.blit(
                return_text, [(WIDTH / 2) - 125, (HEIGHT / 2) + 195]
            )
            # If the button is clicked then call the corresponding function.
            if return_rect.collidepoint(mouse) and click[0]:
                self.start_screen()
            pygame.display.update()

    def run(self):
        """Run Game Function"""
        # Declare and initialize each variable that will be utilized while the
        # game is running.
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        score = delta_x = delta_y = counter = 0
        score_font = pygame.font.SysFont("ubuntu", 60, bold=True, italic=False)
        score_x = score_y = snake_size = 25
        snake_length = 6
        snake_list = []
        snake_move_distance = snake_speed = food_size = 20
        move_up_or_down = move_left_or_right = True
        # Set the coordinates for the snake and food objects.
        snake_x = WIDTH / 2
        snake_y = HEIGHT / 2
        food_x = randrange(food_size, WIDTH - food_size)
        food_y = randrange(food_size, HEIGHT - food_size)
        update_score = pygame.USEREVENT + 1
        # Repeatedly create an event on the event queue.
        pygame.time.set_timer(update_score, 3000)
        start_ticks = pygame.time.get_ticks()  # Get the time in milliseconds.
        clock = pygame.time.Clock()  # Create an object to help track time
        # While the game is running, continue the loop.
        game_is_running = True
        while game_is_running:
            # Calculate the number of seconds.
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_is_running = False
                    self.end(seconds, 0)  # Call the end game function.
                if event.type == update_score and counter >= 1:
                    score += 1  # Increment the score.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and move_left_or_right:
                        delta_x = -snake_move_distance
                        delta_y = 0
                        move_left_or_right = False
                        move_up_or_down = True
                        counter += 1  # Increment the move counter.
                    elif event.key == pygame.K_RIGHT and move_left_or_right:
                        delta_x = snake_move_distance
                        delta_y = 0
                        move_left_or_right = False
                        move_up_or_down = True
                        counter += 1  # Increment the move counter.
                    elif event.key == pygame.K_UP and move_up_or_down:
                        delta_y = -snake_move_distance
                        delta_x = 0
                        move_up_or_down = False
                        move_left_or_right = True
                        counter += 1  # Increment the move counter.
                    elif event.key == pygame.K_DOWN and move_up_or_down:
                        delta_y = snake_move_distance
                        delta_x = 0
                        move_up_or_down = False
                        move_left_or_right = True
                        counter += 1  # Increment the move counter.
            # If the snake touches any edge of the boarder, call the end
            # screen function.
            if (
                snake_x <= 0
                or (snake_x >= WIDTH - snake_size)
                or (snake_y >= HEIGHT - snake_size)
                or snake_y <= 0
            ):
                game_is_running = False
                self.end_screen(seconds, score)
            else:
                screen.fill(BLACK_RGB)  # Change the background color.
                snake_x += delta_x  # Update the snake's position horizontally.
                snake_y += delta_y  # Update the snake's position vertically.
                # Create rectangle objects for the snake and the food objects.
                player_rect = pygame.Rect(
                    snake_x, snake_y, snake_size, snake_size
                )
                food_rect = pygame.Rect(food_x, food_y, food_size, food_size)
                # Initialize the player/snake and food objects.
                player = Player(screen, GREEN_RGB, player_rect, score)
                food = Food(screen, RED_RGB, food_rect)
                # Call the draw snake and draw food functions.
                player.draw_snake()
                food.draw_food()
                # Append the snake head to the snake list.
                snake_head = (snake_x, snake_y)
                snake_list.append(snake_head)
                # Constantly delete the tail of the snake so that there's no
                # trail left behind.
                if len(snake_list) > snake_length:
                    del snake_list[0]
                # If the snake/player has already moved and if the snake head
                # touches the snake body, call the end screen function.
                if counter >= 1:
                    for snake_rect in snake_list[:-1]:
                        if snake_rect == snake_head:
                            game_is_running = False
                            self.end_screen(seconds, score)
                # Call the snake body and score functions.
                player.snake_body(snake_list, snake_size)
                player.score(WHITE_RGB, score_font, score_x, score_y)
                # Update portions of the screen for software displays.
                pygame.display.update()
                # If the snake touches/eats the food, increment the score and
                # the snake length, then spawn a new food object.
                if food.is_eaten(player_rect):
                    food_x = randrange(food_size, WIDTH - food_size)
                    food_y = randrange(food_size, HEIGHT - food_size)
                    snake_length += 1
                    score += 1
                clock.tick(snake_speed)

    def end_screen(self, total_seconds, current_score):
        """End Screen Function"""
        # Set the size for the end screen.
        end_screen = pygame.display.set_mode((WIDTH - 200, HEIGHT - 200))
        # Set the text for the title and buttons on the end screen.
        text = SUB_TITLE_FONT.render('GAME OVER', True, BLACK_RGB)
        play_again_text = BUTTON_FONT.render('Play Again', True, BLACK_RGB)
        quit_game_text = BUTTON_FONT.render('Quit Game', True, BLACK_RGB)
        # Set the coordinates for the buttons on the end screen.
        play_again_x = (WIDTH / 2) - 390
        play_again_y = (HEIGHT / 2) - 100
        quit_game_x = (WIDTH / 2) - 70
        quit_game_y = (HEIGHT / 2) - 100
        # While the end screen is shown, continue the loop.
        show_end_screen = True
        while show_end_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    show_end_screen = False
                    # Call the end game function.
                    self.end(total_seconds, current_score)
            end_screen.fill(WHITE_RGB)  # Change the background color.
            # Display the title text at the specified coordinates.
            end_screen.blit(text, [(WIDTH / 2) - 360, (HEIGHT / 2) - 260])
            mouse = pygame.mouse.get_pos()  # Get the mouse position.
            click = pygame.mouse.get_pressed()  # Get the mouse click position.
            # Create rectangle objects for each button.
            play_again_rect = pygame.Rect(
                play_again_x, play_again_y, BUTTON_WIDTH, BUTTON_HEIGHT
            )
            quit_game_rect = pygame.Rect(
                quit_game_x, quit_game_y, BUTTON_WIDTH, BUTTON_HEIGHT
            )
            # Initialize each button for the end screen.
            play_again_button = Button(
                end_screen, GREEN_RGB, play_again_x, play_again_y
            )
            quit_game_button = Button(
                end_screen, RED_RGB, quit_game_x, quit_game_y
            )
            # Call the make button function.
            play_again_button.make_button(BUTTON_WIDTH, BUTTON_HEIGHT)
            quit_game_button.make_button(BUTTON_WIDTH, BUTTON_HEIGHT)
            # Call the is over function to check if the mouse is over a button.
            play_again_button.is_over(
                LIGHT_GREEN_RGB, BUTTON_WIDTH, BUTTON_HEIGHT, mouse
            )
            quit_game_button.is_over(
                LIGHT_RED_RGB, BUTTON_WIDTH, BUTTON_HEIGHT, mouse
            )
            # Display each button at the specified coordinates.
            end_screen.blit(
                play_again_text, [(WIDTH / 2) - 375, (HEIGHT / 2) - 80]
            )
            end_screen.blit(
                quit_game_text, [(WIDTH / 2) - 55, (HEIGHT / 2) - 80]
            )
            # If a button is clicked then call the corresponding function.
            if play_again_rect.collidepoint(mouse) and click[0]:
                self.run()
            if quit_game_rect.collidepoint(mouse) and click[0]:
                self.end(total_seconds, current_score)
            pygame.display.update()

    @classmethod
    def end(cls, total_time, player_score):
        """End Game Function"""
        data = []  # Create a list to hold the game data in the data.json file.
        today = date.today()  # Get today's date.
        current_date = str(today)  # Convert the date to a string.
        total = str(total_time)  # Convert the total time played to a string.
        with open('data.json', 'r') as file:  # Open the data.json file.
            # If the file is empty, then append to the data list. Otherwise,
            # load the existing data into the data list and then append.
            if (
                os.stat("data.json").st_size == 0
                or os.stat("data.json").st_size == 1
            ):
                data.append(
                    {
                        "game_data": [
                            {
                                "date": current_date,
                                "total_time_(seconds)": total,
                                "score": player_score,
                            }
                        ]
                    }
                )
            else:
                data = json.load(file)
                data.append(
                    {
                        "game_data": [
                            {
                                "date": current_date,
                                "time_played_(seconds)": total,
                                "score": player_score,
                            }
                        ]
                    }
                )
        with open('data.json', 'w') as json_file:  # Open the data.json file.
            json.dump(data, json_file, indent=2)  # Dump the data to the file.
            json_file.close()  # Close the data.json file.
        pygame.display.quit()  # Uninitialize all pygame modules.
        sys.exit('Thanks for playing!')
