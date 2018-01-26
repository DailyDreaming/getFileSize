import os
import subprocess
import time
import shlex

try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%2.2f sec' % (te - ts)),
        return result
    return timed

@timeit
def getDirSizeRecursively(dirPath):
    totalSize = 0
    total_size = 0
    unixBlockSize = 512
    seenInodes = set()
    for dirPath, dirNames, fileNames in os.walk(dirPath):
        folderSize = 0
        for f in fileNames:
            fp = os.path.join(dirPath, f)
            fileStats = os.lstat(fp)
            if fileStats.st_nlink > 1:
                if fileStats.st_ino not in seenInodes:
                    total_size += int(subprocess.check_output(['du', '--block-size=1', fp]).split()[0].decode('utf-8'))
                    folderSize += fileStats.st_blocks * unixBlockSize
                    seenInodes.add(fileStats.st_ino)
                else:
                    continue
            else:
                total_size += int(subprocess.check_output(['du', '--block-size=1', fp]).split()[0].decode('utf-8'))
                folderSize += fileStats.st_blocks * unixBlockSize
        totalSize += folderSize
    return totalSize

@timeit
def getDuRecursively(dirPath):
    total_size = 0
    seenInodes = set()
    for dirPath, dirNames, fileNames in os.walk(dirPath):
        folderSize = 0
        for f in fileNames:
            fp = os.path.join(dirPath, f)
            fileStats = os.lstat(fp)
            if fileStats.st_nlink > 1:
                if fileStats.st_ino not in seenInodes:
                    total_size += int(subprocess.check_output(['du', '--block-size=1', fp]).split()[0].decode('utf-8'))
                    seenInodes.add(fileStats.st_ino)
                else:
                    continue
            else:
                total_size += int(subprocess.check_output(['du', '--block-size=1', fp]).split()[0].decode('utf-8'))
        total_size += folderSize
    return total_size

@timeit
def naive_get_du(path ='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += int(subprocess.check_output(['du', '--block-size=1', fp]).split()[0].decode('utf-8'))
    return total_size

@timeit
def du(path):
    p = subprocess.Popen(shlex.split('du --block-size=1 -s ' + path), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout.split()[0].decode('utf-8')

@timeit
def naive_get_size(path ='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

if __name__ == '__main__':
    dirPath = '/home/lifeisaboutfishtacos/Desktop'
    print('  getDirSizeRecursively:  ' + str(getDirSizeRecursively(dirPath)))
    print('  getDuRecursively:       ' + str(getDuRecursively(dirPath)))
    print('  naive_get_du:           ' + str(int(naive_get_du(dirPath))))
    print('  du:                     ' + str(int(du(dirPath))))
    print('  naive_get_size:         ' + str(naive_get_size(dirPath)))
