#!/usr/bin/python3
""" package file to organize code and modules in package """

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()