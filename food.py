# Alan Blandon
# CPSC 386-01
# 2021-11-26
# alanblandon@csu.fullerton.edu
# @AlanBlandon
#
# Lab 02-00
#
# This file contains the food class.
#

""" System Module """
import pygame


class Food:
    """Food Class Functions"""

    def __init__(self, screen, color, food_rect):
        """Food Init Function"""
        self._screen = screen
        self._color = color
        self._food_rect = food_rect

    def draw_food(self):
        """Draw Food Function"""
        pygame.draw.rect(self._screen, self._color, self._food_rect)

    def is_eaten(self, player_rect):
        """Is Eaten Function"""
        if pygame.Rect.colliderect(player_rect, self._food_rect):
            return True
        return None
