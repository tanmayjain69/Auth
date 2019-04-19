from firebase import firebase
user = 'rahul'
pwd = 'hello'
stat = '0'
sent = {'user': user, 'pwd': pwd, 'stat': stat}

fb = firebase.FirebaseApplication('https://login-ce190.firebaseio.com', None)
res = fb.put('/users/', sent.get('user', ''), sent)
print(res)
res = fb.put('/users/', sent.get('user', ''), 'stat', '0')
print(res)
res = fb.get('/users', None)
print(res)
