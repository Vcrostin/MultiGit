#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from git import Repo
from parser import args_parser
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    args_parser(argv)
