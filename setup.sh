#!/bin/bash
# CSFE Python Scripts (Web Scraping)
# Author: Marcus Hancock-Gaillard

echo "Setting up CSFE Python Scripts.."
mkdir -p ~/temp/cookies/
mkdir -p ~/py_modules/
mkdir -p ~/passwd/

chmod +x ./bin/*
cp ./bin/* /usr/local/bin/

if [[ -e /usr/bin/python3 ]]; then
	echo "Installing BeautifulSoup for Python3"
	pip3 install bs4
  pip3 install lxml
	read -p "CSFE Username: " user
	sed -i "s,mhancock-gaillard,$user," common.py
	cp common.py ~/py_modules/
  python3 /usr/local/bin/csfepass
  echo "Finished installing CSFE scripts."
else
	echo "You will need to install python3 and python3-pip to run these scripts. After installing run setup again."
fi
