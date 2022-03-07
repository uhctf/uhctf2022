# Minimal Effort

<!-- crypto, forensics, osint, reversing, stegano, websec, misc -->
* Category: **stegano**

<!-- * "uhctf{...}": must match regex "uhctf{([a-z0-9]+-)*[0-9a-f]{6}}" -->
<!-- * "free-form": anything goes, mention in description what to look for -->
* Flag Format: **uhctf{...}**

<!-- {{FLAG_TYPE}} can be "static" or "regex" -->
* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{never-do-things-by-halves-ad0165}</code></li>
</ul></ul></details>

<!-- If you can give a single link, hostname, or one-line connection
instructions, use this built-in feature. If things are more complicated, leave
this empty and explain everything in the description instead. -->
* Connection Info:

<!-- Use the challenge's display names, not the folder names -->
* Requirements:

<!-- Only enter people's first name in lowercase, it will be changed later -->
* Credits:
    * reinaert

<!-- {{HINT_COST}} is a percentage of the challenge's total value -->
<!-- {{HINT_DESCRIPTION}} explains what exactly the hint will help with -->
* Hints: <ul><ul>
<li><details>
    <summary><strong>50%</strong>: How to solve the challenge</summary>
    QR codes can have a lot of redundancy built-in, so no data might be lost.
    The top two positioning markings are completely gone, but the abottom-left
    one is still intact. Using a basic image editor, you could copy the
    bottom-left one to the other two corners, and that might be enough for
    a good QR code reader to recognize the QR code again.
</details></li>
</ul></ul>

## Description
<!-- HTML can be used here if needed -->
Have you ever seen how people fail to anonymize pictures on the internet?
Sometimes they will cross out names with transparant colors, sometimes they
cross out too little of a name, and sometimes they forget that the name also
appears somewhere else in the same picture. This challenge is the same thing,
but with a QR code.

Remember: very little effort was put into crossing out this QR code, so
there might be a low-effort way to recover it as well.