# Syn-Clock-Rest-Api
REST-based web service to perform the clock synchronization between client and server

## Table of Contents
* [Overview](#overview)
* [Technologies Used](#technologies-used)
* [Getting Started](#getting-started)


## Overview
This is a simple example of server with web service using REST architrcture style which sends out date string on its endpoint. The client side is calling the api endpoint and then changing the client system time on Unix machine.

## Technologies Used
### Server
* Flask
* Flask RESTful

### Client
* Python (requests, subprocess)

## Getting Started
This setup requires python environment so please install python 3. The following instructions guide you to run server on localhost and client side will display output on terminal window
* Open terminal window 
```
$ git clone https://github.com/asindhar/syn-clock-rest-api.git
$ cd rest-api
$ pip install requirement.txt
$ python server.py

Open 2nd terminal window to run client side
$ python client.py
```

You may deploy your server on your public IP address on one machine and try running client code on some other machine. In this case, Please do following changes:

### server.py
From
app.run()

To
app.run('YOUR_IP_ADDRESS') 
ex: app.run('0.0.0.0')

### client.py
From
api_url = 'http://localhost:5000/' 

To
api_url = 'http://YOUR_IP_ADDRESS:5000/' 

