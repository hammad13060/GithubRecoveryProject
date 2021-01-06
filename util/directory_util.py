import os
import shutil

class DirectoryUtil:
    @classmethod
    def make_dir(cls, absolute_path):
        cls.delete_dir_if_exist(absolute_path)
        os.makedirs(absolute_path)

    @classmethod
    def delete_dir_if_exist(cls, absolute_path):
        if os.path.exists(absolute_path):
            shutil.rmtree(absolute_path)

    @classmethod
    def get_child_directory_list(cls, absolute_path):
        return (next(os.walk(absolute_path)))[1]
