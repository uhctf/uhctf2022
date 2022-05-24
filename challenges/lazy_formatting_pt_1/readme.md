# Lazy formatting: Part 1
* Category: **websec**

* Flag Format: **uhctf{...}**

* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{why-write-code-if-we-can-use-someone-else-s-a65722}</code></li>
</ul></ul></details>

* Connection Info:
- 1 instance per team
- starting from port 8080
- each team works in a different subnet (123.123.XXX.0/24)
- team instance = 8080 + XXX

* Requirements:

* Credits:
    * mihály

* Hints: <ul><ul>
<li><details>
    <summary><strong>20%</strong>: Helps to discover how the website works.</summary>
    Wow, the error messages for when the format rule's syntax is incorrect are pretty useful. Wait, haven't I seen that error somewhere before?
</details></li>
<li><details>
    <summary><strong>20%</strong>: Helps exploiting the functionality of the website.</summary>
    The developers are shoving their work onto another application! Can we inject our work into the pile?
</details></li>
</ul></ul>

## Description
F2 Software launched their brand new text formatting webapp. The devs are pretty lazy though. They simply re-used someone else's code. Why don't we use their stuff to have some fun with?
