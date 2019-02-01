import sys


def intercept(ytdl):
    while 1:
        try:
            url = sys.stdin.readline()
        except KeyboardInterrupt:
            break

        if not url:
            break

        ytdl.download([url])
        sys.stderr.write("done")
        sys.stderr.flush()
