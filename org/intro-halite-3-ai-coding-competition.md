

# [Introduction - Halite III (2018) AI Coding Competition p.1](https://pythonprogramming.net/introduction-halite-iii-ai-coding-competition/)

Welcome everyone to a tutorial on Halite III, a game where you compete against
other programmers to create artificial intelligences to collect resources.

The overall theme of Halite III is that you have ships (or turtles), that move
about to collect "halite" in the ocean. The ships can move in the cardinal
directions (north, south, east, or west). You task is to move each ship in a
direction per turn. If you move over halite, you will automatically collect it.
As your ship fills with halite, you need to drop it off at a shipyard or depot.

You can create more ships with the shipyard, and ships themselves are what you
can turn into depots for a cost. As ships move, they also expend halite. If your
ship is in close proximity to an enemy, then that ship is "inspired" and will
collect halite quicker. If ships collide, they both sink.

Alright, so, when I hear this, I can immediately recognize the crux of this
competition boils down to one major thing: pathing, how to best navigate our
ships. Our main focus will be on the micro level, on a per-ship basis.

We will of course need to consider other objectives like building more ships,
converting ships to depots and trying to surround a smaller number of enemy
ships in order to get our ships inspired.

Before we go too far, you will need to get the files required to run locally, or
you can run in the browser. The browser is nice, but can make debugging tedious.
Once you have a lot of the more basic stuff working, I think browser is more
convenient.

Also, there is an embedded tutorial that is worth going through. Beyond this, it
can also be helpful to download the files locally, if only just to read the
source code. It's all heavily commented and it's a good idea to know what's
already available to you to use (methods, functions&#x2026;etc).

For example, if you download the local code, and go into the hlt directory,
check out `entity.py`, you can see various methods for each of the entities in the
game. If you check out `game_map.py`, you can see all of the methods you can call,
such as finding out if a certain position is occupied by a ship or structure,
and even a simple navigation function that you'll probably eventually want to
modify.

Since this is primarily a pathing issue, our first major task is actually to
just figure out where the heck we want to go. Okay, so let's get started! Here's
some basic starting code, taken from the tutorial on the Halite website. You can
follow along either in the embedded editor, or locally.


# IPython and Org Notes

I've created an [ipython notebook]((:url-or-port%20"http://127.0.0.1:8888"%20:name%20"testing_grounds.ipynb")) (link won't work until notebook server is
started) to take notes and execute test code.

Executing code is setup for org as well. To execute a single src block, put
point inside block and press <kbd>C-c C-c</kbd> to run the code.

More about org babel execution can be found [here](https://orgmode.org/worg/org-contrib/babel/intro.html) and in ein's [documentation](http://millejoh.github.io/emacs-ipython-notebook/#org-mode-integration).

    import sys
    
    a = 14500
    b = a + 1000
    
    print(f"A: {a} B: {b}")
    
    sys.version

'3.6.4 |Anaconda custom (64-bit)| (default, Jan 16 2018, 10:22:32) [MSC v.1900 64 bit (AMD64)]'

