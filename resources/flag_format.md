# Flag Format
There are two flag formats:
* **uhctf{...}** is the default, easily recognizable format
* **free-form** can be anything

Flags of the form **uhctf{...}**:
* Must match the regex `uhctf{([a-z0-9]+-)*[0-9a-f]{6}}`:
    * Contain only lowercase letters, numers and dashes (no underscores)
    * End with 6 random hex characters
* Examples:
    * `uhctf{this-is-a-flag-dc9db8}`
    * `uhctf{another-example-4e90ca}`
    * `uhctf{5ed804}`
* Generate random lowercase hex strings:
    * Web: https://www.browserling.com/tools/random-hex
    * Bash: `cat /dev/urandom | xxd -p | head -c 6`