<!-- # Linux and Unix agentless scanning requirements -->
To scan a Linux or Unix computer without an agent, certain requirements must be met. Ideally, an agentless scan of a Linux or Unix computer is performed through SSH. Though other protocols enabled on the computer, like SNMP, may provide some information as well, SSH will return the most detailed data.

In order for Lansweeper to scan a Linux or Unix computer, you must ensure that SSH is enabled on the computer. We recommend using OpenSSH. The account you use to access SSH must at least be able to run the `uname` command.   
Depending on your Linux distribution, Lansweeper will also run [a selection of other commands](/classic/docs/scanning-commands-run-on-linux-computers). These commands are used to retrieve data like operating system, processor, memory, software and more. Full root access is not necessary for scanning, but using an account with sudo rights is recommended. Sudo is used to run certain commands.

To configure a Linux computer for agentless scanning, follow these steps:

1. Verify whether OpenSSH is installed on the computer. Use a graphical package manager or enter one of the commands below in the console.

   - Debian, Linux Mint, Ubuntu: `dpkg -s openssh`

   - Fedora, Mageia, Red Hat: `rpm -q openssh`

   - Gentoo, Sabayon: `equery list openssh`

   - Manjaro (Arch): `pacman -Q openssh`
2. Install the OpenSSH server, if it's not already installed. Use a graphical package manager or enter one of the commands below in the console.

   - Debian, Linux Mint, Ubuntu: `sudo apt-get install openssh-server`

   - Fedora, Red Hat: `sudo yum install openssh`

   - Gentoo: `emerge --ask --changed-use net-misc/openssh`

   - Mageia: `sudo urpmi openssh`

   - Sabayon: `sudo equo install openssh`

   - Manjaro (Arch): `sudo pacman -S openssh`
3. Reboot the computer.
4. To run SSH automatically when the computer starts, enter one of the commands below in the console.

   - Debian, Linux Mint, Ubuntu: `sudo update-rc.d ssh defaults`

   - Fedora, Mageia, Red Hat: `sudo chkconfig sshd on`

   - Gentoo, Sabayon: `rc-update add sshd default`

   - Manjaro (Arch): `sudo systemctl enable sshd.service sudo systemctl start sshd.service`
5. To run SSH once, enter the command below in the console. The SSH service will be started once and then shut down when the machine reboots.  
   `sudo /etc/init.d/sshd start`
6. Verify whether SSH is running by entering the command below in the console. If there's output, SSH is running; if there's no output, SSH is not running.  
   `ps -e | grep sshd`
7. You now meet the requirements for agentless Linux and Unix scanning. Start scanning the computer by following the instructions in [this knowledge base article](/classic/docs/how-to-scan-a-linux-or-unix-computer).

From Lansweeper 6.0 onward, you can use both username/password and certificate-based authentication to connect to SSH on a Linux computer. Older Lansweeper releases only support username/password authentication.
