# FontLocker

<!-- crypto, forensics, osint, reversing, stegano, websec, misc -->
* Category: **{{websec}}**

<!-- * "uhctf{...}": must match regex "uhctf{([a-z0-9]+-)*[0-9a-f]{6}}" -->
<!-- * "free-form": anything goes, mention in description what to look for -->
* Flag Format: **{{uhctf{...}}**

<!-- {{FLAG_TYPE}} can be "static" or "regex" -->
* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>{{static}}: <code>uhctf{should-ve-used-firefox-c709b3</code></li>
</ul></ul></details>

<!-- If you can give a single link, hostname, or one-line connection
instructions, use this built-in feature. If things are more complicated, leave
this empty and explain everything in the description instead. -->
* Connection Info:
<!-- Not given -->

<!-- Use the challenge's display names, not the folder names -->
* Requirements:

<!-- Only enter people's first name in lowercase, it will be changed later -->
* Credits:
    * ward

<!-- {{HINT_COST}} is a percentage of the challenge's total value -->
<!-- {{HINT_DESCRIPTION}} explains what exactly the hint will help with -->
* Hints: <ul><ul>
<li><details>
    <summary><strong>10%</strong>: Tells you how to get started with the attachment</summary>
    Open the attachment in Wireshark, apply the filter (type 'http' in the bar above) and read the first packet (Frame No. 4)
</details></li>
</ul></ul>


## Description
<!-- HTML can be used here if needed -->
{{DESCRIPTION_PARAGRAPH}}
A new sort of safe was created to hold a flag. Luckily, we were able to intercept an authorized user accessing it.
{{DESCRIPTION_PARAGRAPH}}
