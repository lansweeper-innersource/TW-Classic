<!-- # Linux scanning error: LinuxNoSudoRights -->
If your scanning credential does not have the sudo rights to scan the required Linux information, you may receive a LinuxNoSudoRights error during a [Linux scan](/docs/how-to-scan-a-linux-or-unix-computer "How to scan a Linux or Unix computer").

Different Linux distributions may require different configuration commands.

To resolve the Linux scanning error:

1. Navigate to your Linux **Terminal**.
2. If necessary, create a new group by running `sudo groupadd groupname`, replacing `groupname` with your preferred group name:
3. Add a user to the group by running `sudo usermod -a -G groupname username`, where `groupname` and `username` are replaced by your desired names:
4. Ensure your user has been added to your group by running `grep groupname /etc/group`.
5. Enter `sudo visudo` and a password, if prompted.
6. To give an individual user permission to use sudo, use the arrow keys to navigate through the file and locate a line that looks `username ALL=(ALL) ALL`. To give all users within a group permission to use sudo, locate a line that looks like `%groupname ALL=(ALL) ALL`. Note the "%" before the group name. Common groups with sudo rights are *sudo* and *wheel*.
7. Select **i** to enter insert mode. Use the arrow keys to move the cursor and click **Enter** to insert a new line. Do not remove existing lines from the file. Instead, add "**#**" to the start of a line to ignore that line. This way no information is mistakenly deleted.
8. Add a line for each additional user or group you want to grant sudo rights to. Use the same format as the users and groups already in the file. In the example below, we gave sudo rights to a user called *Lansweeper.*

   
9. When you are done editing the file, click **Escape** to exit insert mode.
10. Type `:wq` then click **Enter** to save and exit the editor.
11. Navigate to the Lansweeper web console and [rescan the client machine](/docs/how-to-scan-a-linux-or-unix-computer "How to scan a Linux or Unix computer") with the user account you granted sudo rights to.

The LinuxNoSudoRights errors should now be resolved. If the issue persists, browse and post in our [Community Forum](https://community.lansweeper.com/t5/forum/bd-p/Lansweeper_General_Forum "Lansweeper Community Forum"), or contact our [support team](https://www.lansweeper.com/contact-support/ "Contact Support") directly.
