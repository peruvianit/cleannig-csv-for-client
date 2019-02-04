

import os
import os.path

class FileUtils:

    def countFiles(self, directory):
        files = []

        if os.path.isdir(directory):
            for path, dirs, filenames in os.walk(directory):
                files.extend(filenames)

        return len(files)

    def getFiles(self, directory, filter):
        files = []
        if os.path.isdir(directory):
            for path, dirs, filenames in os.walk(directory):
                for sfile in filenames:
                    if (str(sfile).upper().endswith(str(filter).upper())):
                        files.append(sfile)

        return files


    def existFile(self, path):
        return os.path.isfile(path)