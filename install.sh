#!bin/bash

name=komdat
install_path=$HOME/$name

mkdir -p $install_path

bold=$(tput bold)
normal=$(tput sgr0)

#getting the latest package list
echo "\n${bold}==========Updating package list==========${normal}"
sudo apt update -y
sudo apt upgrade -y

#installing git
echo "\n${bold}==========Installing git==========${normal}"
sudo apt install git -y

git clone -b nanang-dev https://github.com/mikoaf/komdat.git $install_path

process=$?

if [ $process -eq 0 ]; then
    #installing dependencies
    echo "\n${bold}==========Installing dependencies==========${normal}"
    sudo apt install python3-pip -y
    sudo apt install python3-venv -y
    sudo apt install python3-dev -y
    sleep 0.5

    sudo apt install nodejs -y
    sudo apt install npm -y
    sudo npm install -g n -y
    sudo n latest -y
    sleep 0.5

    sudo npm install -g pm2 -y

    #setting up virtual environment
    echo "\n${bold}==========Setting up virtual environment==========${normal}"
    python3 -m venv $install_path/env

    if [ $? -eq 0 ]; then
        #installing python dependencies
        echo "\n${bold}==========Installing python dependencies==========${normal}"
        pip install -r $install_path/requirements.txt
        sleep 0.5

        #running the app
        echo "\n${bold}==========Running the app with pm2==========${normal}"
        pm2 start $install_path/app.py --name $name --interpreter $install_path/env/bin/python
        pm2 startup
        pm2 save
        sleep 0.5

        echo "\n${bold}==========Installation completed==========${normal}"
        echo "The app is running in the background"
    else
        echo "\n${bold}==========Installation failed==========${normal}"
        echo "Please check the error message above"
        # rm -rf $install_path
        exit 1
    fi
else
    echo "\n${bold}==========Installation failed==========${normal}"
    echo "Please check the error message above"
    # rm -rf $install_path
    exit 1
fi