# Solution
This is a guided challenge teaching you about the downside of password policies and using `hashcat` to crack hashes.

Given are the username of the administrator, their hashed password, and a link to the website of the company.

We notice the register page while browsing the company website. The password is apparently hashed using SHA3-512, a very strong hashing algorithm. Despite this, the satirical password policy will help crack the administrator's hash. Based on the rules, we can figure out that passwords must follow a strict pattern, which we encode as follows:
- possible *special* characters: `!$^*@`
- possible *numbers*: `0123456789`
- possible *text* characters: `bcefghjklpquvwxyzBCEFGHJKLPQUVWXYZ`
    - lowercase and uppercase alphabet minus letters from the username `administrator`
- structure: `s|t|s|t|d|st|d|st`
    - where
        - `s`: special character
        - `t`: text character
        - `d`: number

We can use `hashcat`'s mask attack to crack the hash. Translating the above rules into `hashcat` syntax gives the following. Let it run for a few minutes to get the password.
```sh
hashcat --potfile-disable -a 3 -m 17600 '7c1ece085a13012da59241c61faf7ea08ad6be5e4c766b30ece16d7aff7ba494150a47ea8bc995f6a77e02f32f625f167b0bc4cb2908bb642ff933b981703c7e' -1 'bcefghjklpquvwxyzBCEFGHJKLPQUVWXYZ' -2 '!$^*@' -3 'bcefghjklpquvwxyzBCEFGHJKLPQUVWXYZ!$^*@' '?2?1?2?1?d?3?d?3'
```

The password can then be used to log in to the website and get the flag.
