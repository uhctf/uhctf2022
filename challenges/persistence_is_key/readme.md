# Persistence is key

<!-- crypto, forensics, osint, reversing, stegano, websec, misc -->
* Category: **forensics**

<!-- * "uhctf{...}": must match regex "uhctf{([a-z0-9]+-)*[0-9a-f]{6}}" -->
<!-- * "free-form": anything goes, mention in description what to look for -->
* Flag Format: **uhctf**

<!-- {{FLAG_TYPE}} can be "static" or "regex" -->
* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{P3rs1st4nc3_1s_h4rd_t0_h1d3}</code></li>
</ul></ul></details>


<!-- Use the challenge's display names, not the folder names -->
* Requirements:
    * attachments/extract.tar.gz

<!-- Only enter people's first name in lowercase, it will be changed later -->
* Credits:
    * jorrit

<!-- {{HINT_COST}} is a percentage of the challenge's total value -->
<!-- {{HINT_DESCRIPTION}} explains what exactly the hint will help with -->
* Hints: <ul><ul>
<li><details>
    <summary><strong>25%</strong>: Where to start</summary>
    It would be a good idea to look at ways to create a persistent service on linux.
</details></li>
<li><details>
    <summary><strong>50%</strong>: Where to look</summary>
    Systemd seems like a good way to create a persistent service.
</details></li>
</ul></ul>

## Description
<!-- HTML can be used here if needed -->
One of our machines has some malware we can't find, but it is there every time, even after a reboot. Please investigate, we managed to extract part of the filesystem.