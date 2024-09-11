#!/bin/bash

# Colors
GREEN='\033[32m'
RED='\033[31m'
YELLOW='\033[33m'
NC='\033[0m'
PURPLE='\033[35m'
Orange='\033[33m'
BLUE='\033[34m'
FMT_BOLD="\033[1m"

# Limited palette colors for terminals that don't support truecolor
FMT_LIM_RED="\033[38;5;196m"
FMT_LIM_ORANGE="\033[38;5;202m"
FMT_LIM_YELLOW="\033[38;5;226m"
FMT_LIM_GREEN="\033[38;5;082m"
FMT_LIM_BLUE="\033[38;5;021m"
FMT_LIM_PURPLE="\033[38;5;093m"
FMT_LIM_PINK="\033[38;5;163m"PURPLE
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Define the path to the project
TARGET_DIR="/home/$USER/ziFlw"
BIN_DIR="/home/$USER/.local/bin"
PY="/home/$USER/ziflw/app.py"

# Check if the directory exists and remove it
if [ -d "$TARGET_DIR" ]; then
    rm -rf "$TARGET_DIR"
fi

# Clone the repository
echo -e "${FMT_LIM_YELLOW}Building the ziFlw...${NC}\n\n"
if ! git clone https://github.com/mirr-x/ziFlw "$TARGET_DIR"; then
    echo "${FMT_LIM_RED}Failed to clone the repository.${NC}"
    exit 1
fi

sleep 1

# install the requirements
pip3 install -r "$TARGET_DIR/bin/requirements.txt"

sleep 1

# Fill the environment variables
read -p "$(echo -e ${FMT_BOLD}Do you want to build the project? [Y/n]: ${NC})" BUILD
if [ "$BUILD" = "Y" ] || [ "$BUILD" = "y" ]; then
    echo -e "\n${FMT_LIM_YELLOW}   ⚠️    Create an account on https://www.like4like.org${NC}    ⚠️ \n"
    read -p "$(echo -e "${FMT_LIM_PURPLE} - Enter the Username: ${NC}")" USERNAME
    echo "export LIKE4LIKE_USERNAME=\"$USERNAME\"" >> ~/.bashrc
    read -p "$(echo -e ${FMT_LIM_PURPLE} - Enter the Password: ${NC})" PASSWORD
    echo "export LIKE4LIKE_PASSWORD=\"$PASSWORD\"" >> ~/.bashrc
    echo -e "\n${FMT_LIM_YELLOW}   ⚠️    create fake accounts${NC}    ⚠️ \n"
    read -p "$(echo -e "${FMT_LIM_PURPLE} - Enter the twitter Cookies (JSON): ${NC}")" COOKIES_X
    echo "export TWITTER_COOKIES=\"$COOKIES_X\"" >> ~/.bashrc
    read -p "$(echo -e "${FMT_LIM_PURPLE} - Enter the instagram Cookies (JSON): ${NC}")" COOKIES_IG
    echo "export INSTA_COOKIES=\"$COOKIES_IG\"" >> ~/.bashrc
    read -p "$(echo -e "${FMT_LIM_PURPLE} - Enter the facebook Cookies (JSON): ${NC}")" COOKIES_FB
    echo "export FACE_COOKIES=\"$COOKIES_FB\"" >> ~/.bashrc
    echo -e "\n${FMT_LIM_YELLOW}   ⚠️    Prepare the discord WEbHOOK${NC}    ⚠️ \n"
    read -p "$(echo -e "${FMT_LIM_PURPLE} - Enter the discord Webhook: ${NC}")" WEBHOOK
    echo "export DISCORD_WEBHOOK_URL=\"$WEBHOOK\"" >> ~/.bashrc
fi

# move the binary to the bin directory
chmod +x $PY
sudo ln -s $PY /usr/bin/ziflw

sleep 1

# Confirm completion
if [ -d "$TARGET_DIR" ]; then
    echo -e "${FMT_LIM_PURPLE}
·▄▄▄▄•▪  ·▄▄▄      ▄▄▌  ▄▄▌        ▄▄▌ ▐ ▄▌
▪▀·.█▌██ ▐▄▄·▪     ██•  ██•  ▪     ██· █▌▐█
▄█▀▀▀•▐█·██▪  ▄█▀▄ ██▪  ██▪   ▄█▀▄ ██▪▐█▐▐▌
█▌▪▄█▀▐█▌██▌.▐█▌.▐▌▐█▌▐▌▐█▌▐▌▐█▌.▐▌▐█▌██▐█▌
·▀▀▀ •▀▀▀▀▀▀  ▀█▄▀▪.▀▀▀ .▀▀▀  ▀█▄▀▪ ▀▀▀▀ ▀▪   
                                   
                                ${FMT_LIM_GREEN}....is now installed!${NC}"
    sleep 1
    echo -e "
${FMT_LIM_PURPLE}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                                          ${FMT_LIM_PURPLE}X
                                                                          ${FMT_LIM_PURPLE}X
        ${FMT_LIM_ORANGE}• USAGE:${NC}                                                          ${FMT_LIM_PURPLE}X
            ${FMT_LIM_RED}$ ${NC} ziflw                                                      ${FMT_LIM_PURPLE}X
                                                                          X
                                                                          X
${FMT_LIM_PURPLE}--------------------------------------------------------------------------%
${YELLOW}[${NC}                                                                         ${FMT_LIM_PURPLE}|
    ${PURPLE}{${NC}                                                                     ${FMT_LIM_PURPLE}|
        ${BLUE}\"Made By\"${NC}: ${GREEN}\"mirr-x\"${NC},                                              ${FMT_LIM_PURPLE}|
        ${BLUE}\"Link\"${NC}: ${GREEN}\"https://github.com/mirr-x\"${NC}                               ${FMT_LIM_PURPLE}|
    ${PURPLE}}${NC}                                                                     ${FMT_LIM_PURPLE}|
${YELLOW}[${NC}                                                                         ${FMT_LIM_PURPLE}|
--------------------------------------------------------------------------%
${NC}
${NC}"

else
    echo -e "\n\n${FMT_LIM_RED}Failed to clone the repository.${NC}"
    exit 1
fi