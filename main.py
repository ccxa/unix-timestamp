import sys
import datetime
from datetime import datetime as dt


def help_function():    
    help_msg = "Shows help.        $ --help \n" \
            "To get normal date $ --unix <UnixDate>\n" \
            "To get unix date.  $ --normal <Y M D H M S>"
    print(help_msg)


def get_unix_date(normal_date):
    try:
        arg_index = args.index('--normal')
        normal_date = args[arg_index+1:]
        int_normal_date = []
        for i in normal_date:
            int_normal_date.append(int(i))
        y, m, d, h, _m, s = int_normal_date
        date = datetime.datetime(y, m, d, h, _m, s)
        unix_ts = int(date.timestamp())
        print(unix_ts)
    except (IndexError, ValueError):
        print('Error! no valid input for normal arg! use [--help]')


def get_normal_date(unix_date):
    try:
        unix_date = args[args.index('--unix') + 1]
        print(dt.fromtimestamp(int(unix_date)))
    except (IndexError, ValueError):
        print('Error! no valid input for unix arg! use [--help]')


args = sys.argv
unix_arg, normal_arg = False, False


if '--help' in args:
    help_function()

elif '--unix' in args:
    get_normal_date(args)

elif '--normal' in args:
    get_unix_date(args)

else:
    print("No valid input, use [--help]")
