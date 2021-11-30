# Alan Blandon
# CPSC 386-01
# 2021-11-26
# alanblandon@csu.fullerton.edu
# @AlanBlandon
#
# Lab 02-00
#
# This file contains the player class.
#

""" System Module """
import pygame


class Player:
    """Player Class Functions"""

    def __init__(self, screen, color, rect, score):
        """Player Init Function"""
        self._screen = screen
        self._color = color
        self._rect = rect
        self._score = score

    def draw_snake(self):
        """Draw Snake Function"""
        pygame.draw.rect(self._screen, self._color, self._rect)

    def snake_body(self, body, size):
        """Snake Body Function"""
        for rect in body:
            pygame.draw.rect(
                self._screen, self._color, [rect[0], rect[1], size, size]
            )
            pygame.draw.rect(
                self._screen, self._color, [rect[0], rect[1], size, size]
            )

    def score(self, color, font, x_value, y_value):
        """Score Function"""
        score_text = font.render("Score: " + str(self._score), True, color)
        self._screen.blit(score_text, [x_value, y_value])
