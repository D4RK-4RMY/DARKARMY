#!/bin/bash
clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'
echo""
echo -e "${RED}                                                                "                                                                                  
echo "
██████   █████  ██████  ██   ██  █████  ██████  ███    ███ ██    ██ 
██   ██ ██   ██ ██   ██ ██  ██  ██   ██ ██   ██ ████  ████  ██  ██  
██   ██ ███████ ██████  █████   ███████ ██████  ██ ████ ██   ████   
██   ██ ██   ██ ██   ██ ██  ██  ██   ██ ██   ██ ██  ██  ██    ██    
██████  ██   ██ ██   ██ ██   ██ ██   ██ ██   ██ ██      ██    ██    "
echo "                                                               "                                                                    
echo -e "${GREEN}                                          ~@~ Coded By 1ucif3r ~@~ ${NC}"
echo ""
echo -e "${YELLOW} www.darkarmy.live | Instagram.com/1ucif3r | Github.com/D4RK-4RMY ${NC} "
echo ""
echo "---------------------------------------------------------------------------------------"
echo ""
echo -e "${RED}[!] This Tool Must Run As ROOT [!]${NC}"
echo ""
echo -e "${CYAN}[>] Press ENTER to Install DARKARMY, CTRL+C to Abort.${NC}"
read INPUT
echo ""

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/DARKARMY"
    BIN_DIR="$PREFIX/usr/bin/"
    pkg install -y git python2
else
    INSTALL_DIR="/usr/share/doc/DARKARMY"
    BIN_DIR="/usr/bin/"
fi

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[!] A Directory DARKARMY Was Found.. Do You Want To Replace It ? [y/n]:" ;
    read mama
    if [ "$mama" = "y" ]; then
        rm -R "$INSTALL_DIR"
    else
        exit
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone https://github.com/D4RK-4RMY/DARKARMY.git "$INSTALL_DIR";
echo "#!/bin/bash
python $INSTALL_DIR/darkarmy.py" '${1+"$@"}' > DARKARMY;
chmod +x DARKARMY;
sudo cp DARKARMY /usr/bin/;
rm DARKARMY;


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "[✔] Successfuly Installed !!! [✔]";
    echo "";
    echo "[✔]========================================================================[✔]";
    echo "[✔] ✔✔✔ All Is Done!! you can execute tool by typing DARKARMY !! ✔✔✔ [✔]";
    echo "[✔]========================================================================[✔]";
    echo "";
else
    echo "[✘] Installation Failed !!! [✘]";
    exit
fi
