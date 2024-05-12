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

    #make .env file
    echo "\nCreating .env file ..."
    MQTT_BROKER="mqtt.eclipseprojects.io"
    MQTT_PORT=1883
    PUBLISH_TOPIC="komdat/dht/data"
    SUBSCRIBE_TOPIC="komdat/dht/start"
    echo "MQTT_BROKER=$MQTT_BROKER" > $install_path/.env
    echo "MQTT_PORT=$MQTT_PORT" >> $install_path/.env
    echo "PUBLISH_TOPIC=$PUBLISH_TOPIC" >> $install_path/.env
    echo "SUBSCRIBE_TOPIC=$SUBSCRIBE_TOPIC" >> $install_path/.env

    #setting up virtual environment
    echo "\nSetting up virtual environment ..."
    python3 -m venv $install_path/env
    cd $install_path
    source env/bin/activate

    if [ $? -eq 0 ]; then
        #installing python dependencies
        echo "\n${bold}==========Installing python dependencies==========${normal}"
        python3 -m pip install -r $install_path/requirements.txt
        sleep 0.5

        #running the app
        echo "\n${bold}==========Running with pm2==========${normal}"
        sudo pm2 start $install_path/main.py --name $name --interpreter $install_path/env/bin/python
        sudo pm2 startup
        sudo pm2 save
        sleep 0.5

        deactivate
        cd $HOME

        echo "\n${bold}==========Installation completed==========${normal}"
        echo "The app is running in the background"
        echo "System will reboot in 5 seconds"
        sleep 5
        sudo reboot
    else
        echo "\n${bold}==========Installation failed==========${normal}"
        echo "Please check the error message above"
        rm -rf $install_path
        exit 1
    fi
else
    echo "\n${bold}==========Installation failed==========${normal}"
    echo "Please check the error message above"
    rm -rf $install_path
    exit 1
fi