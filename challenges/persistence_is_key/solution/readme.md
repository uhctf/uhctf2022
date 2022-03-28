# Solution

In `/etc/systemd/system/secure.service` is a systemd service that decrypts, runs, and deletes a payload. The encrypted payload prints a decoy flag, but contains the real flag as a comment.

```
openssl enc -aes-256-cbc -d -in initr -out exploit.py -pass pass:qwertyuiop1234567890
```

<!-- optionally include any relevant solution files in this folder -->