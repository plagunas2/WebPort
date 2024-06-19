import os
import sys
import subprocess
import urllib.request
import zipfile
import tarfile

#compile all .c .cs .py, etc., files to webassembly AFTER code parsing & refactoring

#c, c++

def download_and_extract(url, extract_to='.'): #download and extract zip files

    file_name = url.split('/')[-1]
    download_path = os.path.join(extract_to, file_name)

    print(f"Downloading {url}...")
    urllib.request.urlretrieve(url, download_path)
    print(f"Downloaded {file_name}")

    if file_name.endswith('.zip'):
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    elif file_name.endswith('.tar.gz') or file_name.endswith('.tgz'):
        with tarfile.open(download_path, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_to)
    
    print(f"Extracted {file_name}")

def setup_emsdk(emsdk_path='emsdk'): #setup emscripten if not on user's system
    if not os.path.exists(emsdk_path):
        print("Emsdk not found on system. Downloading Emscripten SDK...")
        download_and_extract("https://github.com/emscripten-core/emsdk", extract_to='.')
        os.rename("emsdk-main", emsdk_path);
        print("Emsdk successfully installed.")
    
    os.chdir(emsdk_path)
    subprocess.run(['git', 'pull']) #get latest version / changes
    subprocess.run(['./emsdk', 'install', 'latest']) #install latest emsdk version
    subprocess.run(['./emsdk', 'activate', 'latest']) #activate (should set up path automatically)
    os.chdir('..')
    print("Emsdk successfully set up.")

def c_cpp_to_wasm(game_file_path, output_path): #uses emscripten to compile
    #TODO automatically download emscripten if user doesn't have it
    setup_emsdk()
    emscripten_path = "C:\Users\prisc\emsdk\upstream\emscripten" #placeholder, replace w user file path later
    emcc_path = os.path.join(emscripten_path, 'emcc.py')
    command = [emcc_path, game_file_path, '-o', output_path, 's', 'WASM=1']


#python

#java

#godot, GDscript

# c# -hardest?-

#main():
#check engine, language
#direct to correct compiler