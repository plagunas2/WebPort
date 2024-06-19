import argparse
import subprocess
import os
import sys

supported_eng = ['Unity', 'Godot', 'none']
supported_lang = ['C', 'C++', 'Python', 'Java']
#TODO support multiple languages in a game

def main():
    parser = argparse.ArgumentParser(description='Port your game to the web!')
    #take in args for: language, engine, game file path, main loop path, and output location
    parser.add_argument('--Engine', type=str, default='none', help='Specify Engine used to create game')
    parser.add_argument('--Language', type=str, default='none', help='Specify Language used to create game') #required
    parser.add_argument('--GamePath', type=str, default=None, help='Specify where the game project file path is') #required
    parser.add_argument('--MainLoopPath', type=str, default='none', help='Specify where the main game loop is (if present)')
    parser.add_argument('--output', type=str, default=None, help='Output path for final WASM project')
    args = parser.parse_args()

    if (args.Engine):
        if (args.Engine not in supported_eng):
            raise Exception("This engine is not supported yet")
        else:
            #engine = args.Engine
            print("Selected Engine: ", args.Engine)

    if (args.Language):
        if (args.Language not in supported_lang):
            raise Exception("This language is not supported yet")
        else:
            #lang = args.Language
            print("Selected Language: ", args.Language)

    if (args.GamePath == None):
        raise Exception("Game File Path is required!")
    #TODO check that path exists

    if (args.MainLoopPath):
        #TODO check that file ends in supported language: cs, cpp, c, py, etc.
        print("Selected Main Loop File Path: ", args.MainLoopPath)

    if (args.output == None):
        raise Exception("Output File Path is required!")

    #get absolute file path from user's system
    jsfile_rel = "./main.js"
    jsfile_abs = os.path.abspath(jsfile_rel)
    print(jsfile_abs)

    try: #check if node.js is on user's system (just in case)
        subprocess.run(['node', '-v'], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError:
        print("Error: Node.js is not installed or not found in the system's PATH.")
        sys.exit(1)

    command = ['node', jsfile_abs, args.Language, args.Engine, args.MainLoopPath] 
    subprocess.run(command) #run js file with args

if __name__ == '__main__':
    main()
    