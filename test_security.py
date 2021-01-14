import Security_key

password = 'pl79898%&$#&'

#encrypt password
encripted_password = Security_key.encrypt(password)
print ('ENCRYPTED')
print (encripted_password)


#decrypte password
decripted_password = Security_key.decrypt(encripted_password)
print ('ORIGINAL PASSWPRD :' + decripted_password)