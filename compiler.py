import os
import sys
import subprocess
import urllib.request
import zipfile
import tarfile
import shutil
import platform

#compile all .c .cs .py, etc., files to webassembly AFTER code parsing & refactoring

#c, c++

def download_and_extract(url, extract_to): #download and extract zip files

    file_name = url.split('/')[-1]
    download_path = os.path.join(extract_to, file_name) #change

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

def setup_emsdk(file_dir): #setup emscripten if not on user's system

    download_and_extract("https://github.com/emscripten-core/emsdk", extract_to=file_dir)
    #os.rename("emsdk-main", emsdk_path);
    print("Emsdk successfully downloaded.")
    
    os.chdir(file_dir)

    #give proper commands based on user's OS
    user_OS = platform.system
    if(user_OS == "Windows"): 
        subprocess.run(['git', 'pull']) #get latest version / changes
        subprocess.run(['emsdk.bat', 'install', 'latest']) #install latest emsdk version
        subprocess.run(['emsdk.bat', 'activate', 'latest']) #activate version
        subprocess.run(['emsdk_end.bat']) #activate PATH & other variables
        print("Emsdk successfully set up.")
    if(user_OS == "macOS" or user_OS == "Linux"):
        subprocess.run(['git', 'pull'])
        subprocess.run(['./emsdk', 'install', 'latest']) #install latest emsdk version
        subprocess.run(['./emsdk', 'activate', 'latest']) #activate 
        subprocess.run(['source ./emsdk_env.sh']) #activate PATH & other variables
    
        

def c_cpp_to_wasm(game_file_path, output_path): #uses emscripten to compile
    file_dir = ""
    if not shutil.which('emsdk'): #emscripten not on user's system (or path not properly set)
        print("Emsdk not found on System. Initializing download...")
        file_dir = input("Enter directory for emsdk download (Downloads folder suggested): ")
        print("Downloading emsdk to ", file_dir)
        setup_emsdk(file_dir)
    emscripten_path = os.path('emsdk') #placeholder, replace w user file path later
    emcc_path = os.path.join(emscripten_path, 'emcc.py')
    command = [emcc_path, game_file_path, '-o', output_path, 's', 'WASM=1']


#python

#java

#godot, GDscript

# c# -hardest?-

#main():
#check engine, language
#direct to correct compiler