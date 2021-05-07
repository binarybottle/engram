## Linux

Install:

    cat usr-share-X11-xkb-symbols-us >> /usr/share/X11/xkb/symbols/us
    echo Now restart your X session.

Activate:

    setxkbmap -layout us    -variant engram         # one layout; no switch
    setxkbmap -layout us,us -variant engram,basic   # dual layout switching

