import clang.cindex
import re

def find_main_loop(source_code): #get main loop
    main_loop_pattern = re.compile(r'while\s*\(.*running.*\)\s*{')
    match = main_loop_pattern.search(source_code)
    if match:
        print("Main loop found, modifying...")
        return match.start(), match.end()
    return None, None

def find_int_main(source_code):
    int_main_pattern = re.compile(r'int main\(\) \{')
    match = int_main_pattern.search(source_code)
    if match:
        return match.start(), match.end()

def add_emscripten_loop(source_code):
    return 1

def replace_main_loop(source_code, start, end):
    before_loop = source_code[:start]
    after_loop = source_code[end:]

    main_loop_code = "TODO"