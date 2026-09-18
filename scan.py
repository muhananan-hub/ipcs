```python
#Jangan ganti author , hargai creator cape loh buat nya

import LIST
from LIST.id import *
from LIST.it import *
from LIST.jp import *
from LIST.us import *
from LIST.fr import *
from LIST.kr import *
from LIST.de import *
from LIST.tr import *
import requests
import re
import os

b = "\033[0;34m"
g = "\033[1;32m"
w = "\033[1;37m"
r = "\033[1;31m"
y = "\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"


def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")


def main():
    clear_screen()

    print("{}        ____ ".format(r))
    print("   _[]_/____\__n_ ")
    print("  |_____.--.__()_|")
    print("  |I   //# \\\    |")
    print("{}  |P   \\\__//    | ".format(w))
    print("  |CS   '--'     | ")
    print("{}  '--------------'----------{}------------------.  ".format(r, w))
    print("{}  | {}Author  : {}HVmbl3 {}     | {}INDO{}N{}{}ESIA         | ".format(
        r, w, r, w, r, ir, reset, w
    ))
    print("{}  | {}Youtube : {}Shodiq 2701 {}| {}+62-813-6487-3762 {}|".format(
        r, w, w, w, lgray, w
    ))
    print("{}  '------------------------------------{}-------'  ".format(r, w))

    print("")
    print("  {}[ 1 ] {}Desa Kidang".format(r, w))
    print("  {}[ 2 ] {}Desa Sengkol".format(r, w))
    print("  {}[ 3 ] {}Desa Kuta".format(r, w))
    print("  {}[ 4 ] {}Desa Rembitan".format(r, w))
    print("  {}[ 5 ] {}Desa Sukarara".format(r, w))
    print("  {}[ 6 ] {}Desa Sembalun".format(r, w))
    print("  {}[ 7 ] {}Desa Tetebatu".format(r, w))
    print("  {}[ 8 ] {}Desa Gerung".format(r, w))
    print("  {}[ 9 ] {}Exit".format(r, w))
    print("")

    select = input(
        "\033[1;31m[ \033[1;37mSelect@Number \033[1;31m]\033[1;37m> "
    ).strip()

    filtering(select)


def filtering(pilih):

    if pilih == "1":
        desa_kidang()

    elif pilih == "2":
        desa_sengkol()

    elif pilih == "3":
        desa_kuta()

    elif pilih == "4":
        desa_rembitan()

    elif pilih == "5":
        desa_sukarara()

    elif pilih == "6":
        desa_sembalun()

    elif pilih == "7":
        desa_tetebatu()

    elif pilih == "8":
        desa_gerung()

    elif pilih == "9":
        print(r + "Exiting ..." + w)
        os.sys.exit()

    else:
        print(r + "Pilihan tidak tersedia!" + w)
        input("\nPress Enter to continue...")
        main()


if __name__ == "__main__":
    main()
```
