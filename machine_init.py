#! /usr/bin/python3.4

RED = "\033[1;31m"
BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
REVERSE = "\033[;7m"

import os
import sys
import subprocess

def cd_into(to_path):
    os.chdir(to_path[0])

def run_commands(command_groups):
    for group in command_groups:
        print_message(group[0], BLUE)
        for command in group[2]:
            print_message(command[0], BLUE)
            if type(command[2][0]) is not str:
                my_func = command[2][0]
                my_parameters = command[2][1:]
                my_func(my_parameters)
            else:
                result = subprocess.check_call(command[2])
            print_message(command[1], GREEN)
        print_message(group[1], GREEN)

# result = subprocess.run(commands[number]) waiting for python 3.5

def print_message(message, color):
#    sys.stdout.write(color)
    print(message)
#    sys.stdout.write(RESET)
    

##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################

if __name__ == '__main__':
    groups=[]

groups.append(
['***\npreparations...\n',
 'done preparations.\n***\n',
 [['creating directory for deb files...', 'done.\n', ['sh','-c','sudo -u amir mkdir /home/amir/installed_deb_files']]]
])

groups.append(
['***\nvim...',
 'done vim.\n***\n',
 [['installing prerequisites...', 'done.\n', ['apt-get','install','--yes','--force-yes','libncurses5-dev','libgnome2-dev','libgnomeui-dev','libgtk2.0-dev','libatk1.0-dev','libbonoboui2-dev','libcairo2-dev','libx11-dev','libxpm-dev','libxt-dev','python3-dev','git']],
  ['downloading vim...', 'done.\n', ['sh','-c','sudo -u amir git clone https://github.com/vim/vim.git']],
  ['cd into vim...', 'done.\n', [cd_into,'vim']],
  ['configuring vim...', 'done.\n', ['sh','-c','sudo -u amir ./configure --with-features=huge --enable-multibyte --enable-python3interp=yes --with-python3-config-dir=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu --enable-gui=gtk2 --enable-cscope --prefix=/usr']],
  ['making vim...', 'done.\n', ['sh','-c','sudo -u amir make VIMRUNTIMEDIR=/usr/share/vim/vim80']],
  ['installing vim...', 'done.\n', ['make','install']],
  ['installing editor alternative link...', 'done.\n', ['update-alternatives','--install','/usr/bin/editor','editor','/usr/bin/vim','1']],
  ['setting vim as the alternative for editor...', 'done.\n', ['update-alternatives','--set','editor','/usr/bin/vim']]]
])

groups.append(
['***\nyoucompleteme...\n',
 'done youcompleteme.\n***\n',
 [['cd into home...', 'done.\n', [cd_into,'/home/amir']],
  ['downloading vundle...', 'done.\n', ['sh','-c','sudo -u amir git clone https://github.com/VundleVim/Vundle.vim.git /home/amir/.vim/bundle/Vundle.vim']],
  ['downloading .vimrc...', 'done.\n', ['sh','-c','./google_drive_file_downloader.py 0B_AXnUbSJ-r_c3VDVGVoQ0l6cXM .vimrc']],
  ['changing ownership...', 'done.\n', ['sh','-c','chown amir:amir .vimrc']],
  ['installing plugins...', 'done.\n', ['sh','-c','sudo -u amir vim +PluginInstall +qall']],
  ['creating temp directory...', 'done.\n', ['mkdir','ycm_temp']],
  ['cd into temp directory...', 'done.\n', [cd_into,'ycm_temp']],
  ['downloading clang_llvm...', 'done.\n', ['sh','-c','../google_drive_file_downloader.py 0B_AXnUbSJ-r_Uk5DSWt3SWtxRk0 clang_llvm.tar.xz']],
  ['changing ownership...', 'done.\n', ['sh','-c','chown amir:amir clang_llvm.tar.xz']],
  ['extracting clang_llvm...', 'done.\n', ['tar', 'xvf', 'clang_llvm.tar.xz']],
  ['renaming to llvm_root_dir...', 'done.\n', ['sh','-c','mv clang+llvm* llvm_root_dir']],
  ['cd into home...', 'done.\n', [cd_into,'/home/amir']],
  ['installing cmake...', 'done.\n', ['apt-get','install','--yes','--force-yes','cmake']],
  ['installing python dev...', 'done.\n', ['apt-get','install','--yes','--force-yes','python-dev','python3-dev']],
  ['creating build directory...', 'done.\n', ['mkdir','ycm_build']],
  ['cd into build directory...', 'done.\n', [cd_into,'ycm_build']],
  ['generating makefiles...', 'done.\n', ['cmake','-G','Unix Makefiles','-DPATH_TO_LLVM_ROOT='+'/home/amir/ycm_temp/llvm_root_dir','.','/home/amir/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp']],
  ['compiling the libraries...', 'done.\n', ['cmake','--build','.','--target','ycm_core']],
  ['cd into home...', 'done.\n', [cd_into,'/home/amir']],
  ['removing build directory...', 'done.\n', ['rm','-r','ycm_build']],
  ['removing temp directory...', 'done.\n', ['rm','-r','ycm_temp']]]
])

######################################################
# v500
# iscan-data* - first file
# iscan_2.30* - second file
# iscan-plugin* - third file
######################################################

groups.append(
['***\nv500...\n',
 'done v500.\n***\n',
 [['downloading first package...', 'done.\n', ['sh','-c','./google_drive_file_downloader.py 0B_AXnUbSJ-r_MkhSU1pWZUROYXc installed_deb_files/v500_first_package.deb']],
  ['downloading second package...', 'done.\n', ['sh','-c','./google_drive_file_downloader.py 0B_AXnUbSJ-r_TWc1Sm1YS1dsVVk installed_deb_files/v500_second_package.deb']],
  ['downloading third package...', 'done.\n', ['sh','-c','./google_drive_file_downloader.py 0B_AXnUbSJ-r_ZHV6aE1FLUtEUDg installed_deb_files/v500_third_package.deb']],
  ['changing ownership...', 'done.\n', ['sh','-c','chown amir:amir installed_deb_files/v500_first_package.deb']],
  ['changing ownership...', 'done.\n', ['sh','-c','chown amir:amir installed_deb_files/v500_second_package.deb']],
  ['changing ownership...', 'done.\n', ['sh','-c','chown amir:amir installed_deb_files/v500_third_package.deb']],
  ['installing xstlproc...', 'done.\n', ['apt-get','install','--yes','--force-yes','xsltproc']],
  ['installing first package...', 'done.\n', ['dpkg','--install','installed_deb_files/v500_first_package.deb']],
  ['installing second package...', 'done.\n', ['dpkg','--install','installed_deb_files/v500_second_package.deb']],
  ['installing third package...', 'done.\n', ['dpkg','--install','installed_deb_files/v500_third_package.deb']]]
])

groups.append(
['***\nlatex...\n',
 'done latex.\n***\n',
 [['installing texlive-full...', 'done.\n', ['apt-get','install','--yes','--force-yes','texlive-full']],
  ['downloading culmus package...', 'done.\n', ['sh','-c','./google_drive_file_downloader.py 0B_AXnUbSJ-r_UkxPc1JFa0JLdU0 installed_deb_files/culmus_package.deb']],
  ['changing ownership...', 'done.\n', ['sh','-c','chown amir:amir installed_deb_files/culmus_package.deb']],
  ['installing culmus package...', 'done.\n', ['dpkg','--install','installed_deb_files/culmus_package.deb']]]
])

groups.append(
['***\nflash...\n',
 'done flash.\n***\n',
 [['downloading flash player...', 'done.\n', ['sh','-c','./google_drive_file_downloader.py 0B_AXnUbSJ-r_dHc0NU95SHp3c3c Downloads/flash_player.tar.gz']],
  ['changing ownership...', 'done.\n', ['sh','-c','chown amir:amir Downloads/flash_player.tar.gz']],
  ['cd into downloads...', 'done.\n', [cd_into,'/home/amir/Downloads']],
  ['extracting flash player...', 'done.\n', ['tar','xvf','flash_player.tar.gz']],
  ['copying flash player .so file into plugins...', 'done.\n', ['cp','libflashplayer.so','/usr/lib/mozilla/plugins/']],
  ['copying flash player properties into plugins...', 'done.\n', ['cp','usr/bin/flash-player-properties','/usr/lib/mozilla/plugins/']],
  ['cleaning downloads directory...', 'done.\n', ['sh','-c','rm -r *']]]
])

groups.append(
['***\ncgdb...\n',
 'done cgdb.\n***\n',
 [['cd into /usr/local...', 'done.\n', [cd_into,'/usr/local']],
  ['downloading cgdb...', 'done.\n', ['git', 'clone', 'git://github.com/cgdb/cgdb.git']],
  ['cd into cgdb...', 'done.\n', [cd_into,'cgdb']],
  ['installing automake...', 'done.\n', ['apt-get','install','--yes','--force-yes','automake']],
  ['installing libncurses5-dev...', 'done.\n', ['apt-get','install','--yes','--force-yes','libncurses5-dev']],
  ['installing flex...', 'done.\n', ['apt-get','install','--yes','--force-yes','flex']],
  ['installing bison...', 'done.\n', ['apt-get','install','--yes','--force-yes','bison']],
  ['installing texinfo...', 'done.\n', ['apt-get','install','--yes','--force-yes','texinfo']],
  ['installing help2man...', 'done.\n', ['apt-get','install','--yes','--force-yes','help2man']],
  ['installing libreadline-gplv2-dev...', 'done.\n', ['apt-get','install','--yes','--force-yes','libreadline-gplv2-dev']],
  ['running autogen...', 'done.\n', ['sh','-c','./autogen.sh']],
  ['running configure...', 'done.\n', ['sh','-c','./configure --prefix=/usr/local']],
  ['installing make...', 'done.\n', ['apt-get','install','--yes','--force-yes','make']],
  ['making...', 'done.\n', ['make']],
  ['installing cgdb...', 'done.\n', ['make','install']]]
])

groups.append(
['***\nvmplayer...\n',
 'done vmplayer.\n***\n',
 [['installing gcc...', 'done.\n', ['apt-get','install','--yes','--force-yes','gcc']],
  ['installing linux headers...', 'done.\n', ['apt-get','install','--yes','--force-yes','linux-headers-amd64']],
  ['installing make...', 'done.\n', ['apt-get','install','--yes','--force-yes','make']]]
])


run_commands(groups)
