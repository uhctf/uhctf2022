# Solution

Looking at the Wireshark PCAP-file, you can get the IP address of the fontlocker website. Also, by looking at the headers, it is possible to get the password required to unlock it.

But, the lock still doesn't work. What's different? Well, if you look at the source code (and the capture), you can see a focus on different fonts. The webserver could be analyzing which fonts were downloaded and which ones are stored offline. In the capture, we can see Chrome as the browser. As of writing, it is possible to fingerprint Chrome by using this technique.

So, in order to unlock the safe, we need to have the exact same fingerprint as the original user. To do this, we can install the fonts locally to ensure that they're not retrieved from the server.

After that, if you open an incognito window (to avoid caching), you can enter the password and view the flag.

