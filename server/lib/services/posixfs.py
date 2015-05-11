import os
import sys
import stat
import pwd
import shutil
import logging

import settings as global_settings



class PosixFS():
    @staticmethod
    def file_exists(filepath):
        filepath = os.path.abspath(filepath)
        exists = os.path.exists(filepath)
        return exists

    @staticmethod
    def create_file(filepath):
        filepath = os.path.abspath(filepath)
        if os.path.exists(filepath):
            logging.info('File {} already exists, not creating'.format(filepath))
            return filepath
        fd = open(filepath,'w')
        fd.close()
        logging.info('Created file at {}'.format(filepath))
        return filepath

    @staticmethod
    def read_file(filepath):
        filepath = os.path.abspath(filepath)
        with open(filepath, 'r') as f:
            content = f.read()
        return content

    @staticmethod
    def update_file(filepath, content):
        filepath = os.path.abspath(filepath)
        with open(filepath, 'w') as local_file:
            for line in content:
                local_file.write(line)
        logging.info('Updated file at {}, with content:\n{}'.format(filepath,content[:80]))
        return filepath

    @staticmethod
    def delete_file(filepath):
        filepath = os.path.abspath(filepath)
        if os.path.isdir(filepath):
            shutil.rmtree(filepath)
        else:
            os.remove(filepath)
        return filepath

    @staticmethod
    def create_directory(filepath):
        filepath = os.path.abspath(filepath)
        os.mkdir(filepath)
        return filepath

    @staticmethod
    def move_file(origpath, newpath):
        origpath = os.path.abspath(origpath)
        newpath = os.path.abspath(newpath)
        shutil.move(origpath,newpath)
        return newpath

    @staticmethod
    def copy_file(origpath, newpath):
        origpath = os.path.abspath(origpath)
        newpath = os.path.abspath(newpath)
        if os.path.isdir(origpath):
            shutil.copytree(origpath,newpath)
        else:
            shutil.copy2(origpath,newpath)
        return newpath

    @staticmethod
    def rename_file(origpath, newpath):
        origpath = os.path.abspath(origpath)
        newpath = os.path.abspath(newpath)
        os.rename(origpath,newpath)
        return newpath

    @staticmethod
    def list_root_paths(username, **kwargs):
        root_patterns = global_settings.FILESYSTEM_ROOT_DIRECTORIES
        formatted_patterns = []
        for patt in root_patterns:
            patt = patt.replace('{{USERNAME}}',username)
            formatted_patterns.append(patt)
        return formatted_patterns

    @staticmethod
    def list_root_dirs_for_user(username):
        root_dirs = []
        for patt in list_root_paths(username):
            root_dirs.append({ patt: [ f for f in list_dir_for_user(username,patt) ] })
        return root_dirs

    @staticmethod
    def get_dir_contents(dirpath):
        contents = []
        for i in os.listdir(dirpath):
            filepath = os.path.join(dirpath,i)
            is_dir = os.path.isdir(filepath)
            if is_dir:
                filepath = filepath + '/'
            contents.append( ( i,filepath,is_dir ) )
        return contents