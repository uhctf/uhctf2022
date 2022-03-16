# Solution
The binary works as intended on a surface level. However, Ghidra is not able to show any functions or variables. Digging through Ghidra's output, you should notice the string `"UPX"` along with a disclaimer. This explains why Ghidra can't read the binary. It is packaged with UPX. UPX compresses a binary and adds automatic de-compression for when the binary is executed.

Compression can be seen as obfuscation. In terms of securing your application, it is useless. Usually, unpacking a binary with UPX is as simple as `upx -d <binary>`. If we try this, however, we get the error: `CantUnpackException: l_info corrupted`. Researching this error, along with the assumption that the binary is indeed malware, we find that a popular anti-unpacking trick is to tweak the UPX magic bytes. The UPX tool is then not able to recognise the binary as UPX-compressed, and simply errors out.

We can open the binary with a hex editor and look for the intended location of the magic bytes based on offset and surrounding byte patterns. At offset `0xec` we find that the original magic bytes `55 50 58 21 (UPX!)` are replaced with `4D 53 49 21 (MSI!)`.

After fixing the magic bytes we can unpack the binary properly with `upx -d <binary>`. The flag is simply a hardcoded string in the binary and can be found with Ghidra or the `strings` tool.