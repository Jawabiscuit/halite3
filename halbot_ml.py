# Python 3.6
import hlt                                        # main halite stuff
from hlt import constants                         # halite constants
from hlt.positionals import Position, Direction   # helper for moving
import random                                     # randomly picking a choice for now.
import logging                                    # logging stuff to console


# game object
game = hlt.Game()

# Initializes the game
game.ready("halbot-ml")

# This loop handles each turn of the game.
while True:
    # The game object changes every turn, and you refresh that state by
    game.update_frame()

    # You extract player metadata and the updated map metadata here for convenience.
    me = game.me

    '''
    comes from game, game comes from before the loop, hlt.Game points to networking, which is where you will
    find the actual Game class (hlt/networking.py). From here, GameMap is imported from hlt/game_map.py.

    open that file to seee all the things we do with game map.'''
    game_map = game.game_map  # game map data. Recall game is

    # A command queue holds all the commands you will run this turn. You build this list up and submit it at the
    #   end of the turn.
    command_queue = []

    # specify the order we know this all to be
    direction_order = [Direction.North, Direction.South, Direction.East, Direction.West, Direction.Still]

    for ship in me.get_ships():
        logging.info(f"{ ship.position}, {ship.position + Position(-3, 3) }")
        logging.info(f"{ game_map[ship.position + Position(-3, 3)] }")

        size = 3
        contents = []
        
        for y in range(-1 * size, size + 1):
            row = []
            for x in range(-1 * size, size + 1):
                row.append([x, y])
            contents.append(row)
        
        command_queue.append(ship.move(Direction.North))

    # ship costs 1000, dont make a ship on a ship or they both sink
    if len(me.get_ships()) < 1:
        if me.halite_amount >= constants.SHIP_COST and not game_map[me.shipyard].is_occupied:
            command_queue.append(me.shipyard.spawn())

    # Send your moves back to the game environment, ending this turn.
    game.end_turn(command_queue)
