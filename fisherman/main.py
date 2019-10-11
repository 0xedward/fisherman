import argparse
import sys
import validators

from fisherman.services import apility, emailrep
from fisherman.utils import colors

def main():
    parser = argparse.ArgumentParser(description="""
    A tool to catch phishes
    
    Lookup email reputation:
    ------------------------------
    fisherman santiago@example.com
    """, formatter_class=argparse.RawDescriptionHelpFormatter, prog="fisherman")

    parser.add_argument("email", type=str,
                        help="Email you want to check the reputation of")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="View detailed results from each service queried")
    args = parser.parse_args()

    if not validators.email(args.email):
        colors.print_pink("Error: {} is not in a valid email address format".format(args.email))
        sys.exit()

    banner()

    if args.verbose:
        colors.print_gray("Verbose mode activated")

    emailrep.check_email_rep(args.email, args.verbose)
    apility.check_email_rep(args.email, args.verbose)


def banner():
    print(r"""
                                 _____ 
                               .' `.  \
                         _____/     \  \
                      .-'    J      _\--\_
                     (       |   .-'      \
                     |  _  .'`..'         |
____     .----""----->-`-.'   |    .-'E"\ /                                             _ ___
    `-._/          .'   `oo.__J  .<  _| .'------.        _____.------------------------' `   `-
                  /          `-`<  `=/-'         `._.---'
                 J       `.    `-) -'`.
_________________E  `     |      `'|  |
                / L  -.    L       F  |.--------------._____________
               /  J     -. |      J   |\                            `--------------------._____
              /    L    _  F      |AAA|J_
             J     J      <-._____|  .'  \
             F      L .' `--.  _  |.___   `-.
            J ---   J   '      |  |    `.  .-\
            F `---   \____.._     |_  .\ \'.`-|
           J   .'.'.-'       `--._|`._\\)\\)///
           |.'   .'_.---.       \ '    /  \\`-._
           J    /        L      |-  -  \  //|   `-._
            L  /         |     J     /  `"' |       `-._
            J.'        / |     F  _.-|' '   F           `-._
           __F-._______| |    J--'  J      J                `-._
         .'.'  \\  |\  F |    |'    |      |                    `-.
        /_/    |\\ | \/F |    F     |__.---<                       `-.
       /       | \\| //| |__.J      |     J|         __              |
      J        |  \\// F-'  )|      |     |       .-'  \             |
      |        |   () /F    ||      (     J      /      \            |
      |        |  //\\/F    ||      (    =`.     |_.--.  `.          |
      |        | //|/\\( '== )\    /      ==`---. /  _(    \         |
      J        |// |/ \|`  ==`.)   \__.________.'(  / | |\  `.      _|_.---'
       \       //-'    /     ==\   `--' `------'  `.( `-'\`.  \   -' |
        `.____(/'      \_       )                   \\_  _)`\_|-'    |
                       `-`-----'                     `-.__.'     .- `| ' -.
                                  .|>             .-._/-  \_.___._ ______.'
 VK         ()   ---._____      .' /         ____             __   .-.   `--'`.___
          .'/                 _|. /______  .'.   `-.__.  __.-'  `-.   `-._.        `._
         (__ \               /.`-'  _.---< `._____.-.< .'                   `._        \
     -------------           `-----'             _.- 
    ------------'
    """)

if __name__ == "__main__":
    main()
