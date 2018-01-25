import os
import subprocess
import time

try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts))
        return result

    return timed

@timeit
def getDirSizeRecursively(dirPath):
    """
    This method will walk through a directory and return the cumulative filesize in bytes of all
    the files in the directory and its subdirectories.

    :param dirPath: Path to a directory.
    :return: cumulative size in bytes of all files in the directory.
    :rtype: int
    """
    totalSize = 0
    # The value from running stat on each linked file is equal. To prevent the same file
    # from being counted multiple times, we save the inodes of files that have more than one
    # nlink associated with them.

    unixBlockSize = 512

    seenInodes = set()
    for dirPath, dirNames, fileNames in os.walk(dirPath):
        folderSize = 0
        for f in fileNames:
            fp = os.path.join(dirPath, f)
            fileStats = os.stat(fp)
            if fileStats.st_nlink > 1:
                if fileStats.st_ino not in seenInodes:
                    folderSize += fileStats.st_blocks * unixBlockSize
                    seenInodes.add(fileStats.st_ino)
                else:
                    continue
            else:
                folderSize += fileStats.st_blocks * unixBlockSize
        totalSize += folderSize
    return totalSize

@timeit
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

@timeit
def du(path):
    return subprocess.check_output(['du','-sb', path]).split()[0].decode('utf-8')

if __name__ == '__main__':
    dirPath = '/home/lifeisaboutfishtacos/Desktop/build_toil'
    print(get_size(dirPath))
    print(getDirSizeRecursively(dirPath))
    print(du(dirPath))