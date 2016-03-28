#!/usr/bin/python 
 

import paho.mqtt.client as mqtt 
import ssl 
import json,time 
import button 
import datetime
import os
import socket
import paho.mqtt.publish as publish 

def on_connect(client, userdata, flags, rc): 
    print ("Subscriber Connection status code: "+connack_string(rc)) 

def on_publish(client, userdata, mid):
    print(client, userdata, mid)
 
 
#Connect to AWS IoT
print("starting aws client")
awsclient = mqtt.Client(client_id="rasp1",protocol=mqtt.MQTTv311) 
awsclient.on_connect = on_connect 
awsclient.on_publish = on_publish 
awsclient.tls_set("/root/root-CA.pem",certfile="/root/b3e793921d-certificate.pem.crt",keyfile="/root/b3e793921d-private.pem.key",tls_version=ssl.PROTOCOL_SSLv23,ciphers=None) 
awsclient.tls_insecure_set(True) 
awsclient.connect(<using my address>.iot.eu-west-2.amazonaws.com",8883,60) 
awsclient.loop_start() 
 
rc=0 
while rc == 0: 
   data={} 
   data['time']=datetime.now().strftime('%Y/%m/%d %H:%M:%S') 
   data['temp']='64'
   data['humid']='65'
   payload = json.dumps(data) 
   print("Payload: " + payload) 
   awsclient.publish("Rasp/data", payload, qos=1) 
   time.sleep(10)  
 
print('rc: ' +str(rc)) 
