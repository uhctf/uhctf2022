# Magical Shipping Inc
* Category: **reversing**

* Flag Format: **uhctf{...}**

* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{the-best-defense-is-wasting-peoples-time-09bcc8}</code></li>
</ul></ul></details>

* Connection Info: \#TODO

* Requirements:

* Credits:
    * mihály

* Hints: <ul><ul>
<li><details>
    <summary><strong>5%</strong>: The binary is somehow not readable by traditional methods.</summary>
    Magical Shipping Inc. loves packages. They package everything, even their binaries apparently.
</details></li>
<li><details>
    <summary><strong>15%</strong>: You know how to open the binary, but it just won't cooperate.</summary>
    This malware seems to have some anti-unpacking protection. The creator must have packaged the original binary, and then modified it to prevent extraction. Maybe we can reverse the edit?
</details></li>
</ul></ul>

## Description
The shipping company Magical Shipping Inc. sent you an e-mail. Apparently they released a new application which allows you to track packages. They even attached it in the mail. How useful! This is totally not malware you just downloaded, right...?

Figure out what is in the binary!