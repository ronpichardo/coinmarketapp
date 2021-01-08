# CoinMarketCap App

## Overview
App for checking current prices on the Cryptocurrency market.

CoinMarketCap is a site that gives you free access to current and historic data for Bitcoin and thousands of altcoins.

This program is intended for monitoring your Crytocurrency of choice with the future implementation of being alerted of 5%-10% changes in price.
Alerting will be via a Discord Webhook, information and instructions can be found here: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks

## Requirements
Python Version: Python3.6
Prior to using this program, an API-Key provided by Coinmarketcap is required, you can sign-up and get a key at https://coinmarketcap.com/api/
![coinmarketapi](https://user-images.githubusercontent.com/63974878/104034189-9025a180-519e-11eb-8ea6-1654946f623f.png)


## Installation
Required Libraries - Requests
Mac/Linux
```shell
$ git clone https://github.com/ronpichardo/coinmarketapp.git
$ cd coinmarketapp
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Windows w/ PowerShell
```shell
$ git clone https://github.com/ronpichardo/coinmarketapp.git
$ cd coinmarketapp
$ python3 -m venv venv
$ ./venv/bin/Activate.ps1
$ pip install -r requirements.txt
```

Optional if you would like to change the config.example.json to config.json in your terminal
```shell
$ mv config.example.json config.json
```

## Usage

1. Add API-Key that was received via https://coinmarketcap.com/api/ to the config.example.json and save the file as config.json
![CoinApiKey](https://user-images.githubusercontent.com/63974878/104036463-6d48bc80-51a1-11eb-81c6-9f4d2deb19bd.png)

* WiP - Code to be added for usage 
