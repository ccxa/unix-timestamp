import sys
import datetime
from datetime import datetime as dt

args = sys.argv
unix_arg, normal_arg = False, False


def help_function():    
    help_msg = "Shows help.        $ --help \n" \
            "To get normal date $ --unix <UnixDate>\n" \
            "To get unix date.  $ --normal <Y M D H M S>"
    print(help_msg)


def get_unix_date(normal_date):
    try:
        normal_date = args[args.index('--normal') + 1:]
        int_normal_date = []
        for i in normal_date:
            int_normal_date.append(int(i))
        y, m, d, h, _m, s = int_normal_date
        date = datetime.datetime(y, m, d, h, _m, s)
        unix_ts = date.timestamp()
        print(unix_ts)
    except (IndexError, ValueError):
        print('Error! no valid input for unix arg!')


def get_normal_date(unix_date):
    try:
        unix_date = args[args.index('--unix') + 1]
        print(dt.fromtimestamp(int(unix_date)))
    except (IndexError, ValueError):
        print('Error! no valid input for normal arg!')



if '--help' in args:
    help_function()

else:

    if '--unix' in args:
        get_normal_date(args)
     
    if '--normal' in args:
        get_unix_date(args)

    else:
        print("No valud input, use [--help]")
