# Lazy formatting: Part 2
* Category: **misc**

* Flag Format: **uhctf{...}**

* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{real-hackers-live-off-the-land-a69c22}</code></li>
</ul></ul></details>

* Connection Info: \#TODO

* Requirements:

* Credits:
    * mihály

* Hints: <ul><ul>
<li><details>
    <summary><strong>30%</strong>: Gain advanced access to the server.</summary>
    Direct shell access would be much more useful than executing commands via the website. Maybe we can ask the web server to open a connection to us?
</details></li>
<li><details>
    <summary><strong>20%</strong>: Helps to discover the system misconfiguration.</summary>
    The sysadmin did not even bother remembering the user's password. He just logs in from time to time and updates the system. No questions asked.
</details></li>
<li><details>
    <summary><strong>25%</strong>: Useful website listing ways to get out.</summary>
    https://gtfobins.github.io/
</details></li>
</ul></ul>

## Description
This is unbelievable. Even the sysadmin at F2 Software is lazy! It is not that hard manage some computers... Why is this company still in business?

The flag is in the `root` user's home directory.

TIP: Windows firewall might block your entry. We recommend using Kali Linux.
