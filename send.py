from urllib import *
import urllib
import json
import sys
import json
import os
import base64

#MY_API_KEY="AIzaSyAUV7UBjoqWFXTt2awvMhe4kUYqW4eh0Ew"
#messageTitle = sys.argv[1]
#messageBody = sys.argv[2]

#os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

#with open('tunnels.json') as data_file:
#    datajson = json.load(data_file)
#msg = ""
#for i in datajson['tunnels']:
#  msg = msg + i['public_url'] +'\n'
#  break

#msg variable contains ngrok web url
image = open('/Users/engrbundle/Desktop/obama4.jpg', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
#image_64_encode.replace("\\\n", "")
image_64_encode.replace(",", "")

data={ "to" : "/topics/my_little_topic",
       "notification" : { "body" : messageBody,
                          "title" : messageTitle,
                          "icon" : '/Users/engrbundle/Desktop/babyimage.jpeg',
                            #"url" : msg,
                            "image" : "image_64_encode"

                              } }



#dataAsJSON = json.dumps(data)

#print(dataAsJSON)

#request = Request( "https://gcm-http.googleapis.com/gcm/send", dataAsJSON, { "Authorization" : "key="+MY_API_KEY, "Content-type" : "application/json" } )

#print (urlopen(request).read())
