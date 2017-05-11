#! /usr/bin/python3.4

import subprocess

command = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'python3-pip']
subprocess.call(command)


command = [
    'pip3',
    'install',
    'requests']
subprocess.call(command)


import os
#from os.path import expanduser
import requests
from multiprocessing import Process, Queue

def run_commands(commands):
    for number in sorted(commands.keys()):
        if number in [11, 19, 21, 24, 30]:
            my_func = commands[number][0]
            my_parameters = commands[number][1:]
            my_func(my_parameters)

        else:
# result = subprocess.run(commands[number]) waiting for python 3.5
            result = subprocess.call(commands[number])

        print('Completed command number ' + str(number) + '\n')




def my_change_dir(to_path):
    os.chdir(to_path[0])


def download_file_from_google_drive(args):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(URL, params = { 'id' : args[0] }, stream = True)

    token = get_confirm_token(response)
    if token:
        params = { 'id' : args[0], 'confirm' : token }
        response = session.get(URL, params = params, stream = True)
    
    save_response_content(response, args[1])

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

  

##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################


if __name__ == '__main__':
  commands = {}


######################################################
# preparations
######################################################
  commands[0] = [
    'mkdir',
    '/home/amir/installed_deb_files']



######################################################
# vim
######################################################

  # installing prerequisites
  commands[9] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'libncurses5-dev',
    'libgnome2-dev',
    'libgnomeui-dev',
    'libgtk2.0-dev',
    'libatk1.0-dev',
    'libbonoboui2-dev',
    'libcairo2-dev',
    'libx11-dev',
    'libxpm-dev',
    'libxt-dev',
    'python3-dev',
    'git']

  # downloading vim
  commands[10] = [
    'git',
    'clone',
    'https://github.com/vim/vim.git']

  # cd into vim
  commands[11] = [
    my_change_dir,
    'vim']

  # configuring vim
  commands[12] = [
    './configure',
    '--with-features=huge',
    '--enable-multibyte',
    '--enable-python3interp=yes',
    '--with-python3-config-dir=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu',
    '--enable-gui=gtk2',
    '--enable-cscope',
    '--prefix=/usr']

  # making vim
  commands[13] = [
    'make',
    'VIMRUNTIMEDIR=/usr/share/vim/vim80']

  # installing vim
  commands[14] = [
    'make',
    'install']

  # setting vim as default editor
  commands[15] = [
    'update-alternatives',
    '--install',
    '/usr/bin/editor',
    'editor',
    '/usr/bin/vim',
    '1']

  commands[16] = [
    'update-alternatives',
    '--set editor',
    '/usr/bin/vim']

  commands[17] = [
    'update-alternatives',
    '--install',
    '/usr/bin/vi',
    'editor',
    '/usr/bin/vim',
    '1']

  commands[18] = [
    'update-alternatives',
    '--set vi',
    '/usr/bin/vim']

######################################################
# youcompleteme
######################################################


  # cd into home
  commands[19] = [
    my_change_dir,
    '/home/amir']

  # downloading vundle
  commands[20] = [
    'git',
    'clone',
    'https://github.com/VundleVim/Vundle.vim.git',
    '/home/amir/.vim/bundle/Vundle.vim']

  # downloading .vimrc
  commands[21] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_c3VDVGVoQ0l6cXM',
    '.vimrc']

  commands[22] = [
    'vim',
    '+PluginInstall',
    '+qall']

  commands[23] = [
    'mkdir',
    '/home/amir/ycm_temp']

  # downloading clang_llvm
  commands[24] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_Uk5DSWt3SWtxRk0',
    '/home/amir/ycm_temp/clang_llvm.tar.xz']

  commands[25] = [
    'tar',
    'jxvf',
    '/home/amir/ycm_temp/clang_llvm.tar.xz']

  commands[26] = [
    'mv',
    '/home/amir/ycm_temp/clang_llvm.tar.xz',
    'llvm_root_dir']

  commands[27] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',      
    'cmake']

  commands[28] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',      
    'python-dev',
    'python3-dev']

# creating build directory
  commands[29] = [
    'mkdir',
    '/home/amir/ycm_build']

# cd into build directory
  commands[30] = [
    my_change_dir,
    '/home/amir/ycm_build']

  commands[31] = [
    'cmake',
    '-G',
    '"Unix Makefiles"',
    '-DPATH_TO_LLVM_ROOT='+'/home/amir/ycm_temp/llvm_root_dir',
    '.',
    '/home/amir/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp']

  commands[32] = [
    'cmake',
    '-build',
    '.',
    '--target',
    'ycm_core',
    '--config',
    'Release']

  commands[33] = [
    'rm',
    '-r',
    '/home/amir/ycm_build']

  commands[34] = [
    'rm',
    '-r',
    '/home/amir/ycm_temp']

######################################################
# v500
# iscan-data* - first file
# iscan_2.30* - second file
# iscan-plugin* - third file
######################################################

  commands[35] = [
    my_change_dir,
    /home/amir]
    
  commands[36] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_MkhSU1pWZUROYXc',
    '/home/amir/installed_deb_files/v500_first_package.deb']

  commands[37] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_TWc1Sm1YS1dsVVk',
    '/home/amir/installed_deb_files/v500_second_package.deb']

  commands[38] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_ZHV6aE1FLUtEUDg',
    '/home/amir/installed_deb_files/v500_third_package.deb']

  commands[39] = [
    'sudo',
    'apt-get',
    'install',
    'xstlproc']

  commands[40] = [
    'sudo',
    'dpkg',
    '--install',
    '/home/amir/installed_deb_files/v500_first_package.deb']

  commands[41] = [
    'sudo',
    'dpkg',
    '--install',
    '/home/amir/installed_deb_files/v500_second_package.deb']

  commands[42] = [
    'sudo',
    'dpkg',
    '--install',
    '/home/amir/installed_deb_files/v500_third_package.deb']

######################################################
# latex
######################################################

  commands[43] = [
    'sudo',
    'apt-get',
    'install',
    'texlive-full']
    
  commands[44] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_UkxPc1JFa0JLdU0',
    '/home/amir/installed_deb_files/culmus_package.deb']

  commands[45] = [
    'sudo',
    'dpkg',
    '--install',
    '/home/amir/installed_deb_files/culmus_package.deb']


######################################################
# flash
######################################################

  commands[46] = [
    my_change_dir,
    'Downloads']
    
  commands[47] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_dHc0NU95SHp3c3c',
    'flash_player.tar.gz']

  commands[48] = [
    'sudo',
    'tar',
    'xvf',
    'flash_player.tar.gz']

  commands[49] = [
    'sudo',
    'cp',
    'libflashplayer.so',
    '/usr/lib/mozilla/plugins/']

  commands[50] = [
    'sudo',
    'cp',
    'usr/bin/flash-player-properties',
    '/usr/lib/mozilla/plugins/']

  commands[51] = [
    'sudo',
    'rm',
    '-r',
    '*']

  run_commands(commands)






'''
  # screen is never dimmed
  commands[1] = [
    'gsettings',
    'set',
    'org.gnome.settings-daemon.plugins.power',
    'idle-dim',
    'false']
  # screen is never being idle
  commands[2] = [
    'gsettings',
    'set',
    'org.gnome.desktop.session',
    'idle-delay',
    '0']
  # screen is never locked
  commands[3] = [
    'gsettings',
    'set',
    'org.gnome.desktop.screensaver',
    'lock-delay',
    '0']
  # a new wallpaper
  commands[4] = [
    'gsettings',
    'set',
    'org.gnome.desktop.background',
    'picture-uri',
    'file:///usr/share/backgrounds/DSC3907_by_Todor_Velichkov.jpg']
  # auto hide launcher
  commands[5] = [
    'gsettings',
    'set',
    'org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/',
    'launcher-hide-mode',
    '1']
  # resizing launcher icon
  commands[6] = [
    'gsettings',
    'set',
    'org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/',
    'icon-size',
    '30']
  # number of horizontal workspaces
  commands[7] = [
    'gsettings',
    'set',
    'org.compiz.core:/org/compiz/profiles/unity/plugins/core/',
    'hsize',
    '2']
  # number of vertical workspaces
  commands[8] = [
    'gsettings',
    'set',
    'org.compiz.core:/org/compiz/profiles/unity/plugins/core/',
    'vsize',
    '2']
'''
