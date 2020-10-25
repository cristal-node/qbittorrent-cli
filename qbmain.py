#!/usr/bin/python

"""
 This program is a client for qbittorrent to operate headlessly. This is
 is a non-official program and comes with absolute no warranty. Feel free
 to use or modify. Keep in mind that the imported library is only supported
 for versions above 4.1 (as the library documentation says)

 Copyright (C) 2020  pri-pro

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""



import time
from qbittorrent import Client
from IPython.display import clear_output

qb = Client('http://127.0.0.1:6784/')
qb.login('admin', 'adminadmin')
torrents = qb.torrents()

def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"
def percent(*args):
    a = float(str(args[0]))
    b = a*100
    result = str(b)[:5] + "%"
    return result
def hash_list():
    info_hash_list = []
    print('enter \'q\' to exit loop')
    num = 1
    while True:
        print(str(num) + '. infohash:', end="")
        k = input()
        if k == "q":
            break
        elif k == "all":
            info_hash_list = "all"
            break
        elif len(k) == 40:
            info_hash_list.append(k)
            num +=1
        else:
            continue
    return info_hash_list
def content_break():
    print("--------------------")
def loop_break():
    print("=========================================================")
    print("=========================================================")


class torrent():
    def __init__(self):
        # print("please give any args")
        print(
            """
            1.  Download by torrent file
            2.  Download by magnet
            3.  Status all active
            4.  Progress(filter)
            5.  Recheck (all or multiple)
            6.  Pause  (all or multiple)
            7.  Resume (all or multiple)
            8.  Remove (all or multiple)
            9.  Focus (only one)
            10. Focus all downloading
            11. Files view
            12. Max priority
            """
        )
        opts = int(input(">>"))
        if opts == 1:
            print("Downloading from file:")
            location = []
            path = input("Folder path:")
            location.append(path)
            self.down_file(location=location)
        elif opts == 2:
            print("Downloading from magnet:")
            location = []
            path = input("Folder path:")
            location.append(path)
            qb.download_from_link(self.link_list(), savepath=location[0])
            # self.down_link(self.link_list(), location=location)
        elif opts == 3:
            print("Status of all actives:")
            self.status()
        elif opts == 4:
            print(
                """progress of-
                1."downloading"
                2."paused"
                3."active"
                4."stalled"
                5."seeding"
                6."completed"
                7."resumed"
                8."errored"
                9."all"
                """
            )
            opts = int(input(">>"))
            if opts == 1:
                self.progress("downloading")
            elif opts == 2:
                self.progress("paused")
            elif opts == 3:
                self.progress("active")
            elif opts == 4:
                self.progress("stalled")
            elif opts == 5:
                self.progress("seeding")
            elif opts == 6:
                self.progress("completed")
            elif opts == 7:
                self.progress("resumed")
            elif opts == 8:
                self.progress("errored")
            elif opts == 9:
                self.progress("all")
            else:
                print("please give a valid input")
                exit()
        elif opts == 5:
            print("Recheck:(if all type \"all\")")
            q = []
            q.append(hash_list())
            if q[0] == "all":
                print("rechecking all!")
                qb.recheck_all()
            else:
                qb.recheck(q[0])
        elif opts == 6:
            print("Pause:(if all type \"all\")")
            q = []
            q.append(hash_list())
            if q[0] == "all":
                print("pause all!")
                qb.pause_all()
            else:
                qb.pause_multiple(q[0])
        elif opts == 7:
            print("Resume:(if all type \"all\")")
            q = []
            q.append(hash_list())
            if q[0] == "all":
                print("resuming all!")
                qb.resume_all()
            else:
                qb.resume_multiple(q[0])
        elif opts == 8:
            print("Remove:(if all type \"all\")")
            q = []
            q.append(hash_list())
            if q[0] == "all":
                print("please don't attemp to remove all")
                qb.delete_all()
            else:
                qb.delete(q[0])
        elif opts == 9:
            print("Focusing:")
            thash = input("infohash:")
            if len(int(thash)) == 40:
                self.focus(thash)
            else:
                print("please try again")
                exit()
        elif opts == 10:
            self.focus_all()
        elif opts == 11:
            print("Viewing file")
            thash = input("infohash:")
            self.file_view(thash)
        elif opts == 12:
            self.max_priority(hash_list())
    def status(self):
        for torrent in torrents:
            print("Torrent name:", torrent["name"])
            print("hash:", torrent["hash"])
            print("Seeds:", torrent["num_seeds"])
            print("File size:", get_size_format(torrent["size"]))
            print("Total size:", get_size_format(torrent["total_size"]))
            print("Download speed:", get_size_format(torrent["dlspeed"]) + "/s")
            # print(torrent)
            print("Progress", percent(torrent["progress"]))
            content_break()
        pass
    def progress(self, *args):
        """
        the filters are:
            1."downloading"
            2."paused"
            3."active"
            4."stalled"
            5."seeding"
            6."completed"
            7."resumed"
            8."errored"
            9."all"
        """
        torrents_filtered = qb.torrents(filter=args[0])
        for torrent in torrents_filtered:
            print("Torrent name:", torrent["name"])
            print("Progress", percent(torrent["progress"]))
            content_break()
        pass
    def recheck(self, *args):
        """takes infohash"""
        if args[0] == "all":
            print("rechecking all!")
            qb.recheck_all()
        else:
            for thash in args[0]:
                print("rechecking:", thash)
                qb.recheck(thash)
        pass
    def down_file(self, **kwargs):
        """takes location"""
        # print(kwargs['location'])
        qb.download_from_file(self.file_list(), savepath=kwargs['location'])
        pass
    def file_list(self):
        torrent_file_list = []
        num = 1
        print('enter \'q\' to exit loop')
        while True:
            print(str(num) + '. Address:', end="")
            k = input()
            if k == "q":
                break
            else:
                torrent_file_list.append(open(k, 'rb'))
                num +=1
        return torrent_file_list
    def link_list(self):
        link_list = []
        print('enter \'q\' to exit loop')
        num = 1
        while True:
            print(str(num) + '. link:', end="")
            k = input()
            if k == "q":
                break
            else:
                link_list.append(k)
                num +=1
                continue
        return link_list
    def remove(self, *args):
        """takes infohash"""
        for thash in args[0]:
            print("deleting:", thash)
            qb.delete(thash)
    def pause(self, *args):
        """takes infohash"""
        if args[0] == "all":
            print("pause all!")
            qb.pause_all()
        else:
            for thash in args[0]:
                print("pausing:", thash)
                qb.pause_multiple(thash)
    def resume(self, *args):
        if args[0] == "all":
            print("resuming all!")
            qb.resume_all()
        else:
            for thash in args[0]:
                print("resuming:", thash)
                qb.resume_multiple(thash)
        pass
    def focus(self, thash):
        """takes infohash"""
        for torrent in torrents:
            if torrent["hash"] == thash:
                while True:
                    clear_output()
                    print("(terminate to close)")
                    print("Torrent name:", torrent["name"])
                    print("Seeds:", torrent["num_seeds"])
                    print("File size:", get_size_format(torrent["size"]))
                    # print("Download speed:", str(torrent["dlspeed"]) + "/s")
                    print("Download speed:", get_size_format(torrent["dlspeed"]) + "/s")
                    # print(torrent)
                    print("Progress", percent(torrent["progress"]))
                    time.sleep(1)
    def focus_all(self):
        while True:
            torrents = qb.torrents(filter="downloading", sort="dlspeed", limit=9) # limit=5
            clear_output()
            for torrent in torrents:
                print("(terminate to close)")
                print("Torrent name:", torrent["name"])
                print("Seeds:", torrent["num_seeds"])
                print("File size:", get_size_format(torrent["size"]))
                # print("Download speed:", str(torrent["dlspeed"]) + "/s")
                print("Download speed:", get_size_format(torrent["dlspeed"]) + "/s")
                # print(torrent)
                print("Progress", percent(torrent["progress"]))
                content_break()
            # loop_break()
            time.sleep(1)
    def file_view(self, thash):
        """takes infohash"""
        file_list = qb.get_torrent_files(thash)
        num = 1
        for file in file_list:
            print(str(num) + ".File name:", file["name"])
            if int(file["priority"]) == 0:
                print("Not downloading")
            print("Size:", get_size_format(file["size"]))
            print("Progress:", percent(file["progress"]))
            num +=1
            content_break()
    def max_priority(self, *args):
        for t in args[0]:
            print("Setting max priority to:", t)
            qb.set_max_priority(t)





if __name__ == "__main__":
    try:
        torrent()
    except:
        pass