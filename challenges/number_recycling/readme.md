# Number recycling
* Category: **crypto**

* Flag Format: **uhctf{...}**

* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{sharing-is-not-always-caring-cc324c}</code></li>
</ul></ul></details>

* Connection Info:

* Requirements:

* Credits:
    * mihály

* Hints: <ul><ul>
<li><details>
    <summary><strong>15%</strong>: Get the juicy information from the given files.</summary>
    We are given 2 RSA public keys encoded with the PEM format. This encoding is useful to share and store keys. Unfortunately, it is not human readable. Maybe we can extract the key's parameters using some tool?
</details></li>
<li><details>
    <summary><strong>20%</strong>: Which direction to research.</summary>
    The keys have been changed, but how much exactly? Try comparing the keys. What stayed the same? What changed? Can either help in cracking RSA?
</details></li>
</ul></ul>

## Description
They say recycling is good for the environment. That's why I used recycled public keys to encrypt duplicates of the flag. Don't worry though, I changed the keys a bit so no one would notice!
