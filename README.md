# Python-Secure-Chatroom

## About

A chatroom application written in Python using TKinter & based on RabbitMQ broker using open-LDAP for authentication

## Learning objectives

When we've completed this Code Pattern, you will understand how to:

- **Objective 1**: LDAP server configuration, helping us manage user authentication.
- **Objective 2**: How to set up an authority server that accepts certification requests, creates them, then signs them in order to verify their state
- **Objective 3**: How to use RabbitMQ for chatting, which is an enterprise level tool.

## Flow

When thinking of chatroom capabilities, our elegant application you will need the following set of features:

1- **Client side :**
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Register -> Enter credentials (first time)
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Login / block authentication (redirect)
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. View all active users
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Select user-> chat area opened / Select room
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Using RSA technique  to encrypt/decrypt all messages sent between clients.
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. See message date & time
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Disconnect && quit application

2- **Server side :**

- Register user : 
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Add new user to the active directory via LDAP 
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Create PKI -> get a x509 certificaton via authority server
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Start communication with the chat/Rabbitmq server
- Login user :
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Enter credentials -> verify user in the active directory via LDAP
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Verify the signature via authority server
- Chatting :
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. Encrypt /decrypt messages while exchanging them between clients

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![Demo architecture](https://i.ibb.co/zx75pzD/arch.png)

![Demo encryption](https://github.com/khalilMejri/TalkyWalky/blob/master/docs/Annotation%202020-01-23%20214852.png)


## Features:

- Save a log of the chat
- Clear the chat history
- Emoji button with various emojies to choose from and use
- Change your username
  - revert to default username
  - view your username history
  - clear your username history
- Style Customization
  - choose a custom font
  - choose from 6 different color themes
  - revert to default layout
- Select a default window size of program for everytime it opens
  - return to the default window size whenever

## Dependencies

- [RabbitMQ](https://github.com/khalilMejri/TalkyWalky): Messaging Broker based on AMQP protocol
- [pycryptodome](https://github.com/khalilMejri/TalkyWalky): well-documented python library for encryption/decryption..
- [OpenSSL](https://github.com/khalilMejri/TalkyWalky): a python package that provides a high-level interface to the functions in the OpenSSL library such as X509 certs generation.
- [Tkinter](https://github.com/khalilMejri/TalkyWalky): Standard Python interface to the Tk GUI toolkit.
- [cryptography](https://github.com/khalilMejri/TalkyWalky): python library for X509 certs with good API
- [OpenLDAP](https://github.com/khalilMejri/TalkyWalky): is an implementation under ubuntu for LDAP protocol
- [Pika](https://github.com/khalilMejri/TalkyWalky): Rabbitmq python client.

## Watch the Video

[![](https://i.ibb.co/SvDjbvZ/Annotation-2020-01-24-005326.png)](https://drive.google.com/open?id=1h2x8_4kPlm4656Bjh0Pp3KeyIaOd_f4f)

## Setup

You have multiple options to setup your own instance:

- [Run it locally](#run-locally)

### 1. Open LDAP server in your machine

Clone the `TalkyWaly` repository locally. In a terminal, run:

```bash
$ git clone https://github.com/khalilmejri/talkywalky.git
```

Our application would have the following folder structure:

```bash
 TalkyWalky/
   └── CA/
     ├── ...
     ├── ca_server.py
     ├── ...
     └── certificate_ca.pem
   ├── ...
   ├── server.py
   ├── main.py
   ├── chat.py
   ├── requirements.txt
   ├── ...
   └── client_cert.pem

```

**Installation**

```bash
# install node modules for the API
$ pip install -r requirements.txt --no-index --find-links file:///tmp/packages
```

### 2. Run rabbitMQ service

```bash
$ systemctl service rabbitmq start
```

### 3. Create an Instance of Messaging-server

```bash
$ ./server.py
```

### 4. Create an Instance of Authority-server

```bash
$ ./CA/ca_server.py
```

**Get your ldap domain string. Almost all your servers need it; keep it safe!**

### 5. Run

Finally, start the main app enjoy :)

```bash
# start app client
$ ./main.py
```

You can now connect to `ldap:<ur_ldap_host_address>:389` to start chatting.

### Refs

[http://www.grotan.com/ldap/python-ldap-samples.html](http://www.grotan.com/ldap/python-ldap-samples.html) <br/>
[https://turbogears.readthedocs.io/en/latest/cookbook/ldap-auth.html](https://turbogears.readthedocs.io/en/latest/cookbook/ldap-auth.html)
