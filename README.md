# qbittorrent-cli
A qBittorrent client for operating headlessly

This program can download torrent files by using qBittorrent. You can add multiple torrent by file or magnet, recheck, check speed etc.

# You should run the gui or daemon atleast once to agree qbittorrent's terms.
# For use everywhere
You should change the username and the password of qbittorrent web api. (via gui or tweaking config file)

# For use in Google Colab
The program was created keep in mind of google colab.
# For first time running in Google Colab
1. Install and run qbittorrent-nox without daemon.
2. Copy the config folder("/root/.local/share/qBittorrent") to any folder in Drive.
3. Copy the config file("/root/.config/qBittorrent/qBittorrent.conf") to any folder in Drive. (for convenience choose same folder)
4. Edit the qbittorrent.sh file and enter the path of config folder and config file
5. Use the notebook for everyday use.

You should keep alive connection. (maybe disconnect timeout is 30mins) You can use js console to it keep alive for 6hrs. (^▽^)/
