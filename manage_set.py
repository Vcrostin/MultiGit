import os

import git
from manage_cache import cache_struct_load


def set_parser_handler(argv):
    print('Add working!')
    return


def dest_set_handler(argv):
    cls = cache_struct_load()

    print(os.path.join(os.getcwd(), argv.path))
    # cls['Destination'] = os.path.join(os.getcwd(), argv.path)
    return


def set_parser_arg(parser):
    parser.set_defaults(func=set_parser_handler)
    subparsers = parser.add_subparsers(prog='Subcommand', title='set subcommand', help='sub-command help')
    set_dest = subparsers.add_parser('dest', help='configure destination')
    set_dest.add_argument('path', help='set path to destination repository', type=str)
    set_dest.set_defaults(func=dest_set_handler)
    return
