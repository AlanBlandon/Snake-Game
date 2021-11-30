# Alan Blandon
# CPSC 386-01
# 2021-11-26
# alanblandon@csu.fullerton.edu
# @AlanBlandon
#
# Lab 02-00
#
# This file contains the button class.
#

""" System Module """
import pygame


class Button:
    """Button Class Functions"""

    def __init__(self, screen, color, x_value, y_value):
        """Button Init Function"""
        self._screen = screen
        self._color = color
        self._x_val = x_value
        self._y_val = y_value

    def make_button(self, width, height):
        """Make Button Function"""
        pygame.draw.rect(
            self._screen, self._color, [self._x_val, self._y_val, width, height]
        )

    def is_over(self, color, width, height, position):
        """Is Over Function"""
        if (
            self._x_val + width > position[0] > self._x_val
            and self._y_val + height > position[1] > self._y_val
        ):
            pygame.draw.rect(
                self._screen, color, [self._x_val, self._y_val, width, height]
            )
