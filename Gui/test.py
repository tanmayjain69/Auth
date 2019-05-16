import subprocess

from firebase import firebase
import pyrebase

config = {
  "apiKey": "AIzaSyCzWwwT2EVNV-PR4QFk3UVMXHT_P94C3FY",
  "authDomain": "login-ce190.firebaseapp.com",
  "databaseURL": "https://login-ce190.firebaseio.com/",
     "storageBucket": "login-ce190.appspot.com"
}
fb = firebase.FirebaseApplication('https://login-ce190.firebaseio.com', None)
print( fb.get('/hash', None))
db = pyrebase.initialize_app(config)
fbdb = db.database()
auth=db.auth()
try:
    user = auth.sign_in_with_email_and_password("arnavsingh40@gmail.com", "subject17")
    user['displayName'] = 'arnav'
except :
    print("oh shit")
z='ac@gmail.com'
removeSpecialChars = z.translate ({ord(c): "098" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
print(removeSpecialChars)
print(user)
# res = fb.put('/users/', sent.get('user', ''), sent)
# print(res)
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
sent=dict()
sent[current_machine_id]="None"
fb.put("/current/",current_machine_id,"none")
# authentication = firebase.FirebaseAuthentication('subject17', 'arnavsingh40@gmail.com' ,True, True)
# print(fb.authentication)
# fb.authentication=authentication
#print (authentication.extra)
# user = authentication.get_user()
# print (user.email)
url='a23sasddassdaassdaasd'

hasg='2sdasdsadfw'
data = dict()
data[url] = hasg
# fbdb.child("hash").child("tanmay").set(data)

res = fb.put('/hash/{}'.format("tanmay"),url,hasg)


print(res)
# for key in res:
#     print(key)
#     print(res[key])