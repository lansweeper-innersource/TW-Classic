<!-- # Linux scanning error: TTY required -->
A "TTY Required" scanning error can occur if you are running a Linux distribution where `sudo` is configured to require `tty` by default.

To solve the error, disable the `tty` requirement to ensure Lansweeper has `sudo` access and fulfills the [requirements for scanning Linux computers](/docs/linux-and-unix-agentless-scanning-requirements "Linux and Unix scanning requirements").

Take caution when editing system files as incorrect changes might make your system unstable.

To disable the `tty` requirement:

1. Open the Linux terminal. Enter `sudo visudo` then your password, when prompted.
2. Use your keyboard's arrow keys and move your cursor to the start of the `Defaults requiretty` line.
3. Select the **I**key to use insert mode.
4. Enter `#`. The line should now be `#Defaults requiretty`.
5. Select the **Esc** key to exit insert mode.
6. Enter `:wq` and select the **Enter** key to save and exit the editor.

[Run a scan on your Linux computer](/docs/how-to-scan-a-linux-or-unix-computer "How to scan a Linux or Unix computer") to confirm the error is resolved.
