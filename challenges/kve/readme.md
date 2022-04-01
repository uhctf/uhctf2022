# KVE (Known Vulnerability Extender)
* Category: **reversing**

* Flag Format: **uhctf{...}**

* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{ez-bo-cve-ftw-c6e2ff}</code></li>
</ul></ul></details>

* Connection Info: \#TODO: <ip>:<team_port>/Public_UPNP_gatedesc.xml

* Requirements:

* Credits:
    * mihály

* Hints: <ul><ul>
<li><details>
    <summary><strong>30%</strong>: Hints at how to find the vulnerability.</summary>
    This device does not seem to be using the latest firmware version.
</details></li>
</ul></ul>

## Description
During a network assessment we uncovered this weird port on the network. It seems to belong to a Wi-Fi range extender. Can you find out whether it is somehow vulnerable and get us the flag?

Note:
- the flag is located in the root (`/`) directory of the device.
- a firewall is placed in front of the device. Ports aside from the ones given will not be accessible.