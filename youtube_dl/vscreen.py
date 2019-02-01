import sys


def intercept(ytdl):
    download = ytdl.download
    readline = sys.stdin.readline
    while 1:
        try:
            url = readline()
        except KeyboardInterrupt:
            break

        if not url:
            break

        download([url])
