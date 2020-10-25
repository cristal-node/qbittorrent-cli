#!/usr/bin/bash


# This script is made specially for using in google colab. If you want to
# use this for any other perpose, you should make some modification.


sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-unstable
# qbittorrent-gui is also supoorted
sudo apt install qbittorrent-nox
pip install python-qbittorrent

# these you should change ONLY for google colab
mkdir -p '/root/.local/share/'
mkdir -p '/root/.config/qBittorrent'
ln -s -f "your qbittorrent config folder" '/root/.local/share/qBittorrent'
ln -s -f 'your qbittorrent config file' '/root/.config/qBittorrent/qBittorrent.conf'
ln -s -f 'the place of program' './qbmain.py'
# example:
# ln -s -f '/content/drive/My Drive/.config/qb/qbittorrent' '/root/.local/share/qBittorrent'
# ln -s -f '/content/drive/My Drive/.config/qb/qbittorrent/qBittorrent.conf' '/root/.config/qBittorrent/qBittorrent.conf'
# ln -s -f '/content/drive/My Drive/Colab Notebooks/qb/qbmain.py' './qbmain.py'



# change the port if you desire
qbittorrent-nox --webui-port=6784 -d
