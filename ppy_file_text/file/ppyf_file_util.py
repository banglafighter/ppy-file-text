import os
import shutil
from pathlib import Path


class FileUtil:
    @staticmethod
    def is_exist(path):
        return os.path.exists(path)

    @staticmethod
    def is_it_file(path):
        return os.path.isfile(path)

    @staticmethod
    def is_it_dir(path):
        return os.path.isdir(path)

    @staticmethod
    def get_file_extension(filename):
        if '.' in filename:
            return filename.rsplit('.', 1)[1].lower()

    @staticmethod
    def filename_only(name_with_extension):
        return Path(name_with_extension).stem

    @staticmethod
    def delete(path):
        if FileUtil.is_exist(path):
            if FileUtil.is_it_file(path):
                os.remove(path)
            elif FileUtil.is_it_dir(path):
                shutil.rmtree(path, ignore_errors=True)
            else:
                return False
        return True

    @staticmethod
    def create_directories(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def rename(source, destination):
        os.rename(source, destination)

    @staticmethod
    def copy(source, destination, ignore=None):
        if os.path.isdir(source):
            return shutil.copytree(source, destination, ignore)
        else:
            return shutil.copy(source, destination)

    @staticmethod
    def join_path(*args):
        return os.path.join(*args)

    @staticmethod
    def file_size_into_byte(path):
        if FileUtil.is_exist(path):
            return os.stat(path).st_size
        return None

    @staticmethod
    def human_readable_file_size(size):
        B = float(size)
        KB = float(1024)
        MB = float(KB ** 2)
        GB = float(KB ** 3)
        TB = float(KB ** 4)

        if B < KB:
            return '{0} {1}'.format(B, 'B' if 0 == B > 1 else 'B')
        elif KB <= B < MB:
            return '{0:.2f} KB'.format(B / KB)
        elif MB <= B < GB:
            return '{0:.2f} MB'.format(B / MB)
        elif GB <= B < TB:
            return '{0:.2f} GB'.format(B / GB)
        elif TB <= B:
            return '{0:.2f} TB'.format(B / TB)

