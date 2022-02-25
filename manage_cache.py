
import os
import json

CACHE_PATH_KEY = 'MULTIGIT_CACHE_PATH'


def get_cache_path():
    return os.environ.get(CACHE_PATH_KEY, '~/.MultiCache/')


def set_cache_path(path):
    cur_path = os.getcwd()
    os.environ[CACHE_PATH_KEY] = os.path.join(cur_path, path)


JSON_PATH = os.path.join(get_cache_path(), '.multigit.json')


def cache_dump(cache):
    cache_json = json.dumps(cache, indent=4)
    with open(JSON_PATH, 'w') as stream:
        stream.write(cache_json)


def cache_struct_load():
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, 'r') as stream:
            return json.loads(stream.read())
    return {}


def cache_parser_handler(args):
    print('U have to choose more direct command (-h for help)')
    return


def show_cache_handler(args):
    cache = cache_struct_load()
    print(cache)
    return


def pop_cache_handler(args):
    cache = cache_struct_load()
    des = cache.get('Destination')
    if des is not None:
        print('Some drop logic')
    else:
        print('You must specify destination project first')
    return


def cache_parser_arg(parser):
    parser.set_defaults(func=cache_parser_handler)
    subparsers = parser.add_subparsers(prog='Subcommand', title='cache subcommand', help='sub-command help')
    cache_show = subparsers.add_parser('show', help='show cache files')
    cache_show.add_argument('--set-copy-branch', help='set source repo')
    cache_show.set_defaults(func=show_cache_handler)
    cache_pop = subparsers.add_parser('pop', help='pop cache files to destination')
    cache_pop.set_defaults(func=pop_cache_handler)
    # cache_update = subparsers.add_parser('save', help='save cache files UD')
    # cache_update.set_defaults(func=save_cache_handler)
    return
