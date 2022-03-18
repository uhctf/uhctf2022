# Solution
This part requires completion of part 1 and an interactive session via a reverse shell. We are dropped into a generic Ubuntu installation as the user `webadmin`. We want to get `root` access, that is the highest level of privilege, in order to fully "pwn" the box.

Sometimes elevated privileges are required to perform everyday tasks. The de factor utility providing this functionality in Unix is `sudo`. It temporarily elevates the current user's privileges to that of the `root` user. Checking the `sudo` config for the current user can be done with `sudo -l`. This shows us that `webadmin` is allowed to run `apt-get`, the Ubuntu package manager, with elevated privileges. Note the `NOPASSWD` option.

We now know that the user `webadmin` can acquire `root` privileges temporarily. But this only applies to the `apt-get` command. How can this be used to gain unlimited access? [GTFOBins](https://gtfobins.github.io/) lists common Unix utilities and how they can be abused to escape restricted environment. For `apt-get` it shows that the command `sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh` will give us a shell while maintaining the elevated privileges.

The flag can be found in the `root` user's home directory (`/root/flag.txt`).