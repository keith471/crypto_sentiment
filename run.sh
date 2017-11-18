#!/bin/sh

#################################################################
#																#
#	Project setup 												#
#																#
#################################################################

# create environment if non existing
if [ ! -d "env" ]; then
	virtualenv env
fi

source env/bin/activate
pip install -r requirements.txt
echo "started virtual environment and installed requirements"

## Run setup script
echo "setting up project..."
python setup.py test
echo "setup project"

#################################################################
#																#
#	Running project 											#
#																#
#################################################################

if [ ! -d "logs" ]; then
	mkdir logs
fi

# Tweet collector and analyzer
echo "starting tweet collector/analyzer"
python stocktwits_collect_analyze.py test > 'logs/out.stocktwits_collect_analyze.log' 2>&1 &

# Coin collector
echo "starting bitcoin price collector"
python price_collect.py test BTC > 'logs/out.price_collect.btc.log' 2>&1 &

echo "starting ethereum price collector"
python price_collect.py test ETH > 'logs/out.price_collect.eth.log' 2>&1 &

# Web visualizer
echo "installing bower components"
cd static && bower install && cd ..

echo "starting web server"
python server.py test >'logs/out.server.log' 2>&1 &
