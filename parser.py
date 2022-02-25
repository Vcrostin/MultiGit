import argparse

VERSION = '0.1'


def parse_shared():
    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument('--force', action='count', help='execute even if it cause error UD')
    shared.add_argument('-r', action='count', help='recurse action UD')
    shared.add_argument("--soft", action='count', help="show diff after operation complete (without any changes) UD")
    shared.add_argument('--version', action='version', version='%(prog)s {}'.format(VERSION))
    return shared


def args_parser(argv):
    parser = argparse.ArgumentParser(prog='GitMultiMerge', usage="merge git from a diff repo")
    parser.set_defaults(func=lambda _: print("U don't entry any subcommand"))
    subparsers = parser.add_subparsers(prog='Subcommand', title='Commands name', help='sub-command help')
    shared = parse_shared()
    from manage_add import add_parser_arg
    add_parser_arg(subparsers.add_parser('add', parents=[shared], help='add files to cache UD'))
    from manage_cache import cache_parser_arg
    cache_parser_arg(subparsers.add_parser('cache', parents=[shared], help='working with cached info UD'))
    clean_parser = subparsers.add_parser('clean', parents=[shared], help='clean cache UD')
    paste_parser = subparsers.add_parser('paste', parents=[shared], help='paste files from cache UD')
    reset_parser = subparsers.add_parser('reset', parents=[shared], help='reject latest change UD')
    from manage_set import set_parser_arg
    set_parser_arg(subparsers.add_parser('set', parents=[shared], help='set both repo UD'))
    commit_parser = subparsers.add_parser('commit', parents=[shared], help='commit any changes UD')
    # parser.add_argument('--quite', action='store_false', help='copy and add files without commit and any references')
    # parser.add_argument('--set-copy-branch', help='set source repo')
    # parser.add_argument('--set-load-branch', help='set destination repo')
    # parser.add_argument('--no-timestamp', action='store_false', help='remove timestamp information from commit')
    # parser.add_argument('--no-reference', action='store_false', help='remove reference to source commit from commit message')
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(VERSION))
    # parser.add_argument('')
    args = parser.parse_args(argv)
    args.func(args)
