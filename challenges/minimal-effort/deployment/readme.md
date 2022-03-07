# Deployment
The QR code was generated in Bash using the command:

    qrencode -l H -s 32 "uhctf{never-do-things-by-halves-ad0165}" -o qrcode.png

The `-l H` argument means high redundancy, allowing the QR code to be recovered
even if a large part of it is lost. The `-s 32` argument sets the resulution to
32 pixels per dot.

The damaged QR code was created using the GIMP paintbrush.