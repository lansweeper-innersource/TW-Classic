<!-- # Linux scanning error: Dmidecode -->
Lansweeper uses the dmidecode command-line utility to scan BIOS information on Linux computers. If dmidecode is not installed on your Linux distribution by default, a dmidecode scanning error can occur.

To resolve the Linux scanning error:

1. Verify whether a HAL is installed on your computer through a graphical package manager, or by entering one of the following commands in the terminal:
   - Debian, Linux Mint, Ubuntu: `dpkg -s dmidecode`
   - Fedora, Mageia, Red Hat: `rpm -q dmidecode`
   - Sabayon: `equery list dmidecode`
2. If it's not already, install the dmidecode utility. Use a graphical package manager or enter one of the following commands in the terminal:
   - Debian, Linux Mint, Ubuntu: `apt-get install dmidecode`
   - Fedora, Mageia, Red Hat: `sudo yum install dmidecode`
   - Mageia: `sudo urpmi dmidecode`
   - Sabayon: `sudo equo install dmidecode`
3. To rescan your asset, go to **Assets**, select the asset you want to scan, then select **Rescan** **asset**.

Your dmidecode  error should now be resolved.
