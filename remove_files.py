import os
from collections import Counter
import time


class Select_file:

    def __init__(self, dir, file_name):
        self.dir = dir
        self.file_name = file_name
        self.count = 0

    def list_all_files(self, dirs):
        _files = []
        list = os.listdir(dirs)  # 列出文件夹下所有的目录与文件
        for file in list:
            path = os.path.join(dirs, file)
            if os.path.isdir(path):
                _files.extend(self.list_all_files(path))
            else:
                _files.append(path)
                self.count = self.count + 1
        # print(Counter(_files))

        return _files

    def remove_files(self):
        for root, dirs, files in os.walk(self.dir):
            if not os.listdir(root):
                os.rmdir(root)

    def rm_file(self):
        files = self.list_all_files(self.dir)
        print(self.count)
        for file in files:
            if file.endswith(self.file_name):
                pass
            else:
                if os.path.exists(file):
                    print(file)
                    os.remove(file)
                else:
                    pass
        for i in range(0, 10):
            self.remove_files()
        print("清洗完成")


if __name__ == '__main__':
    a = Select_file("path", ".rb").remove_files()

