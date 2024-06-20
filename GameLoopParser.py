#parses for main game loops to translate to browser-compatible loops
#using JS's requestAnimationFrame, emscipten's func, or pygbag's async


''' python / pygbag parser 
import asyncio and change game loop to async def main()
move global vars to before loop
in main loop, after pygame.display.update(), include await asyncio.sleep(0)
end script with asyncio.run(main())

'''

import pygbag
import os
import ast

global_vars = []

def parsePython(main_loop_path):
    with open(main_loop_path, 'a') as ml:
        ml.write("PLACEHOLDER")

