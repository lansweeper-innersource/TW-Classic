<!-- # Scanning commands run on Linux computers -->

When Lansweeper [scans a Linux or Unix computer](/docs/how-to-scan-a-linux-or-unix-computer) with or without a scanning agent, it runs commands to retrieve data. The most basic command Lansweeper needs to be able to run on a Linux computer for data retrieval is the `uname` command.

Depending on your Linux distribution, Lansweeper will also run a selection of the other commands listed below. These commands are used to retrieve data like operating system, processor, memory, software and more. The output of the commands must be in English, as other languages may not be correctly parsed.

Note that there are some deprecated commands listed below, which are only used as a fallback if the more modern commands in the list return no output. Full root access is not necessary for scanning, but using an account with sudo rights is recommended. Sudo is used to run echo, lspci, dmidecode, smbios, lvs, pvs and vgs. If running these commands fails due to a lack of sudo rights, some hardware information may not be scanned. However, the rest of the scanning process will still be executed.

## List of Linux commands

Lansweeper runs a selection of the below commands on a Linux computer during scanning. Not all commands are run on all distributions.

- arp
- bdf
- cat
- command
- df
- dmidecode
- dpkg
- dpkg-query
- echo
- eeprom
- equery
- file
- find
- flatpak
- grep
- hal-find-by-property
- hal-get-property
- hostname
- hostnamectl
- hwinfo
- ifconfig
- ip
- lanscan
- lastlog
- ls
- lsblk
- lscpu
- lshal
- lshw
- lslpp
- lspci
- lvs
- machinfo
- netstat
- oslevel
- pacman
- pciconf
- pkg
- pkginfo
- pkg\_info
- prtconf
- prtdiag
- psrinfo
- pvs
- rpm
- smbios
- snap
- sudo (used for running echo, lspci, dmidecode, smbios, lvs, pvs, vgs)
- swlist
- sysctl
- type
- uname (fundamentally required command)
- uptime
- vgs
- xl
