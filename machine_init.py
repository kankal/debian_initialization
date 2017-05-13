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
import requests
from multiprocessing import Process, Queue

def run_commands(commands):
    for number in sorted(commands.keys()):
        if number in [11, 19, 21, 24, 30]:
            my_func = commands[number][0]
            my_parameters = commands[number][1:]
            my_func(my_parameters)
        else:
            result = subprocess.check_call(commands[number])
        print('Completed command number ' + str(number) + '\n')

# result = subprocess.run(commands[number]) waiting for python 3.5


def cd_into(to_path):
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
    cd_into,
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
    '--set',
    'editor',
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
    '--set',
    'vi',
    '/usr/bin/vim']

######################################################
# youcompleteme
######################################################


  # cd into home
  commands[19] = [
    cd_into,
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
    'ycm_temp']

  commands[24] = [
    cd_into,
    'ycm_temp']

  # downloading clang_llvm
  commands[25] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_Uk5DSWt3SWtxRk0',
    'clang_llvm.tar.xz']

  commands[26] = [
    'tar',
    'jxvf',
    'clang_llvm.tar.xz']

  commands[27] = [
    'mv',
    'clang_llvm',
    'llvm_root_dir']

  commands[28] = [
    cd_into,
    '/home/amir']

  commands[29] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',      
    'cmake']

  commands[30] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',      
    'python-dev',
    'python3-dev']

# creating build directory
  commands[31] = [
    'mkdir',
    'ycm_build']

# cd into build directory
  commands[32] = [
    cd_into,
    'ycm_build']

  commands[33] = [
    'cmake',
    '-G',
    '"Unix Makefiles"',
    '-DPATH_TO_LLVM_ROOT='+'/home/amir/ycm_temp/llvm_root_dir',
    '.',
    '/home/amir/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp']

  commands[34] = [
    'cmake',
    '-build',
    '.',
    '--target',
    'ycm_core',
    '--config',
    'Release']

  commands[35] = [
    cd_into,
    '/home/amir']

  commands[36] = [
    'rm',
    '-r',
    'ycm_build']

  commands[37] = [
    'rm',
    '-r',
    'ycm_temp']

######################################################
# v500
# iscan-data* - first file
# iscan_2.30* - second file
# iscan-plugin* - third file
######################################################

   
  commands[38] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_MkhSU1pWZUROYXc',
    'installed_deb_files/v500_first_package.deb']

  commands[39] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_TWc1Sm1YS1dsVVk',
    'installed_deb_files/v500_second_package.deb']

  commands[40] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_ZHV6aE1FLUtEUDg',
    'installed_deb_files/v500_third_package.deb']

  commands[41] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'xstlproc']

  commands[42] = [
    'dpkg',
    '--install',
    'installed_deb_files/v500_first_package.deb']

  commands[43] = [
    'dpkg',
    '--install',
    'installed_deb_files/v500_second_package.deb']

  commands[44] = [
    'dpkg',
    '--install',
    'installed_deb_files/v500_third_package.deb']

######################################################
# latex
######################################################

  commands[45] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'texlive-full']
    
  commands[46] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_UkxPc1JFa0JLdU0',
    'installed_deb_files/culmus_package.deb']

  commands[47] = [
    'dpkg',
    '--install',
    'installed_deb_files/culmus_package.deb']


######################################################
# flash
######################################################

  commands[48] = [
    cd_into,
    'Downloads']
    
  commands[49] = [
    download_file_from_google_drive,
    '0B_AXnUbSJ-r_dHc0NU95SHp3c3c',
    'flash_player.tar.gz']

  commands[50] = [
    'tar',
    'xvf',
    'flash_player.tar.gz']

  commands[51] = [
    'cp',
    'libflashplayer.so',
    '/usr/lib/mozilla/plugins/']

  commands[52] = [
    'cp',
    'usr/bin/flash-player-properties',
    '/usr/lib/mozilla/plugins/']

  commands[53] = [
    'rm',
    '-r',
    '*']


######################################################
# cgdb
######################################################

  commands[54] = [
    cd_into,
    '/usr/local']

  commands[55] = [
    'git',
    'clone',
    'git://github.com/cgdb/cgdb.git']

  commands[56] = [
    cd_into,
    'cgdb']

  commands[57] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'automake']

  commands[58] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'libncurses5-dev']

  commands[59] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'flex']

  commands[60] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'bison']

  commands[61] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'texinfo']

  commands[62] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'help2man']

  commands[63] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'libreadline-gplv2-dev']

  commands[64] = [
    './autogen.sh']

  commands[65] = [
    './configure',
    '--prefix=/usr/local']

  commands[66] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'make']

  commands[67] = [
    'make']

  commands[68] = [
    'make',
    'install']
    
    
######################################################
# vmplayer
######################################################

  commands[69] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'gcc']

  commands[70] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'linux-headers-amd64']

  commands[71] = [
    'apt-get',
    'install',
    '--yes',
    '--force-yes',
    'make']
    
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
