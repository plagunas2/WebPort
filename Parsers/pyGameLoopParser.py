#parses for main game loops to translate to browser-compatible loops
#using JS's requestAnimationFrame, emscipten's func, or pygbag's async


''' python / pygbag parser 
import asyncio and change game loop to async def main()
move global vars to before loop
in main loop, after pygame.display.update(), include await asyncio.sleep(0)
end script with asyncio.run(main())

'''

#import pygbag
import os
import ast

global_vars = []

#change main() to async def main()
class GameLoopTransformer(ast.NodeTransformer):
    def visit_Main(self, node):
        if node.name == 'main': 
            print("Main loop found, modifying...")
            node.name = 'main'
            node.async_ = True
        return node
    
#TODO add import asyncio to beginning!
#TODO move variables!
#TODO add asyncio.run(main()) to end!

def pythonParser(main_loop_path):
    
    with open(main_loop_path) as file:
        file_content = file.read()
    tree = ast.parse(file_content)

    transformer = GameLoopTransformer
    new_main_file = transformer.visit_Main(tree) #put this file somewhere specific

    
    