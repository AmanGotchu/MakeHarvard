print('kairos handler on')

import requests
import base64
import json
import kairos_face


headers = {
    "app_id": "c44dc5a7",
    "app_key": "90b8cedb0392c1fb1e42d318603708ed",
    "content-type": "application/json"
}

kairos_face.settings.app_id = "c44dc5a7"
kairos_face.settings.app_key = "90b8cedb0392c1fb1e42d318603708ed"


filepath = "/Users/engrbundle/Desktop/MakeHarvard/davidpics/david3.jpg"
filepath2 = "/Users/engrbundle/Desktop/jose6.jpg"

r = kairos_face.enroll_face(file = filepath2, gallery_name = "Deployed", subject_id = "Jose")

