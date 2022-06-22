import hashlib

print(hashlib.sha256(b"password").hexdigest())
print(hashlib.sha256(b"hello wold").hexdigest())
print(hashlib.sha256(b"password123").hexdigest())
print(hashlib.sha256(b"cat").hexdigest())

# Use of the salt
salt=b"abc123"
import hashlib
print("Hash with salt")
print(hashlib.sha256(b"abc123" + b"password123").hexdigest())

print(hashlib.sha256(salt + b"password123").hexdigest())

print("Iterated 1000 hash sha256")
hash = hashlib.sha256(b"abc123" + b"password123").hexdigest()
for i in range(1000):
  hash = hashlib.sha256(b"abc123" + hash.encode('ascii')).hexdigest()
  
print(hash)