#!/bin/bash

FMT_LIM_YELLOW="\033[38;5;226m"
FMT_LIM_GREEN="\033[38;5;082m"
FMT_LIM_BLUE="\033[38;5;021m"
FMT_LIM_PURPLE="\033[38;5;093m"
FMT_LIM_PINK="\033[38;5;163m"
FMT_LIM_RED="\033[38;5;196m"
FMT_BOLD="\033[1m"
NC="\033[0m"

# Define the path to the project
TARGET_DIR="/home/$USER/ziFlw"
CONFIG_DIR="$TARGET_DIR/accounts"
CONFIG_FILE="$CONFIG_DIR/config.json"
EXE="$TARGET_DIR/bin/ziflw"
BIN_DIR="/home/$USER/.local/bin"
X_COOKIEPATH="$CONFIG_DIR/twitter"
IG_COOKIEPATH="$CONFIG_DIR/instagram"
FB_COOKIEPATH="$CONFIG_DIR/facebook"

# Check if the directory exists and remove it
if [ -d "$TARGET_DIR" ]; then
    rm -rf "$TARGET_DIR"
fi

# Clone the repository
echo -e "${FMT_LIM_YELLOW}Building the ziFlw...${NC}\n\n"
if ! git clone https://github.com/mirr-x/ziFlw "$TARGET_DIR"; then
    echo -e "${FMT_LIM_RED}Failed to clone the repository.${NC}"
    exit 1
fi

sleep 1

# Install the requirements
pip3 install -r "$TARGET_DIR/bin/requirements.txt"

sleep 1

# Create the config directory if it doesn't exist
mkdir -p "$CONFIG_DIR"

# Fill the environment variables
echo -e "$(echo -e ${FMT_BOLD}Do you want to build the project? [Y/n]: ${NC})"
read -r BUILD
if [[ "$BUILD" == "Y" || "$BUILD" == "y" ]]; then
    echo -e "\n${FMT_LIM_YELLOW}  Create an account on https://www.like4like.org${NC}    ⚠️ "
    echo -e "   ${FMT_LIM_PURPLE}│${NC}"
    echo -e "$(echo -e "${FMT_LIM_PURPLE}   └────────Enter the Username: ${NC}")"
    read -r USERNAME
    echo "export LIKE4LIKE_USERNAME=\"$USERNAME\"" >> ~/.zshrc
    echo -e "   ${FMT_LIM_PURPLE}│${NC}"
    echo -e "$(echo -e "${FMT_LIM_PURPLE}   └────────Enter the Password: ${NC}")"
    read -r PASSWORD
    echo "export LIKE4LIKE_PASSWORD=\"$PASSWORD\"" >> ~/.zshrc
    echo -e "\n${FMT_LIM_YELLOW}  create fake accounts${NC}    ⚠️ \n"

    # Read multi-line input for Twitter cookies
    echo -e "${FMT_LIM_PINK}   └────────Enter the Twitter Cookies (JSON): ${NC}"
    echo -e "${FMT_LIM_PINK}   └────────Press Ctrl+D for EOF${NC}"
    TWITTER_COOKIES=$(cat)
    mkdir -p "$X_COOKIEPATH" && touch "$X_COOKIEPATH/X_cookie.json"
    echo "$TWITTER_COOKIES" > "$X_COOKIEPATH/X_cookie.json"

    # Read multi-line input for Instagram cookies
    echo -e "${FMT_LIM_PINK}   └────────Enter the Instagram Cookies (JSON): ${NC}"
    echo -e "${FMT_LIM_PINK}   └────────Press Ctrl+D for EOF${NC}"
    INSTAGRAM_COOKIES=$(cat)
    mkdir -p "$IG_COOKIEPATH" && touch "$IG_COOKIEPATH/IG_cookie.json"
    echo "$INSTAGRAM_COOKIES" > "$IG_COOKIEPATH/IG_cookie.json"

    # Read multi-line input for Facebook cookies
    echo -e "${FMT_LIM_PINK}   └────────Enter the Facebook Cookies (JSON): ${NC}"
    echo -e "${FMT_LIM_PINK}   └────────Press Ctrl+D for EOF${NC}"
    FACEBOOK_COOKIES=$(cat)
    mkdir -p "$FB_COOKIEPATH" && touch "$FB_COOKIEPATH/FB_cookie.json"
    echo "$FACEBOOK_COOKIES" > "$FB_COOKIEPATH/FB_cookie.json"

    echo -e "\n${FMT_LIM_YELLOW}  Prepare the discord Webhook${NC}    ⚠️ "
    echo -e "   ${FMT_LIM_PURPLE}│${NC}"
    echo -e "$(echo -e "${FMT_LIM_PURPLE}   └────────Enter the discord Webhook: ${NC}")"
    read -r WEBHOOK
    echo "export DISCORD_WEBHOOK_URL=\"$WEBHOOK\"" >> ~/.zshrc
fi
source ~/.zshrc

sleep 1

# Move the binary to the bin directory
chmod +x "$EXE"
sudo ln -s "$EXE" /usr/bin/ziflw

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
        ${FMT_LIM_YELLOW}• USAGE:${NC}                                                          ${FMT_LIM_PURPLE}X
            ${FMT_LIM_RED}$ ${NC} ziflw                                                      ${FMT_LIM_PURPLE}X
                                                                          X
                                                                          X
${FMT_LIM_PURPLE}--------------------------------------------------------------------------%
${FMT_LIM_YELLOW}[${NC}                                                                         ${FMT_LIM_PURPLE}|
    ${FMT_LIM_PURPLE}{${NC}                                                                     ${FMT_LIM_PURPLE}|
        ${FMT_LIM_BLUE}\"Made By\"${NC}: ${FMT_LIM_GREEN}\"mirr-x\"${NC},                                              ${FMT_LIM_PURPLE}|
        ${FMT_LIM_BLUE}\"Link\"${NC}: ${FMT_LIM_GREEN}\"https://github.com/mirr-x\"${NC}                               ${FMT_LIM_PURPLE}|
    ${FMT_LIM_PURPLE}}${NC}                                                                     ${FMT_LIM_PURPLE}|
${FMT_LIM_YELLOW}[${NC}                                                                         ${FMT_LIM_PURPLE}|
--------------------------------------------------------------------------%
${NC}
${NC}"

else
    echo -e "\n\n${FMT_LIM_RED}Failed to clone the repository.${NC}"
    exit 1
fi
