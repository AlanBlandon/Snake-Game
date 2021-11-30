#!/usr/bin/env python3
# Alan Blandon
# CPSC 386-01
# 2021-11-26
# alanblandon@csu.fullerton.edu
# @AlanBlandon
#
# Lab 02-00
#
# This file contains the main function that runs the game.
#

""" System Module """
from snake_game import SnakeGame


def main():
    """Main Function"""
    game = SnakeGame()
    game.run()


if __name__ == '__main__':
    main()
