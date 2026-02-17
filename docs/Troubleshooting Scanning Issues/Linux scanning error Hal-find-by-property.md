<!-- # Linux scanning error: Hal-find-by-property -->
Lansweeper uses a HAL (hardware abstraction layer) to scan hardware information on Linux computers. If a HAL is not installed on your Linux distribution by default, a "Hal-find-by-property" scanning error can occur.

To resolve the Linux scanning error:

1. Verify whether a HAL is installed on your computer through a graphical package manager, or by entering one of the following commands in the terminal:
   - Debian, Linux Mint, Ubuntu: `dpkg -s hal`
   - Fedora, Mageia, Red Hat: `rpm -q hal`
   - Sabayon: `equery list hal`
2. If it's not already, install a HAL. Use a graphical package manager or enter one of the following commands in the terminal:
   - Debian, Linux Mint, Ubuntu: `apt-get install hal`
   - Fedora, Mageia, Red Hat: `sudo yum install hal`
   - Mageia: `sudo urpmi hal`
   - Sabayon: `sudo equo install hal`
3. To rescan your asset, go to **Assets**, select the asset you want to scan, then select **Rescan** **asset**.

Your "Hal-find-by-property" error should now be resolved.
