<!-- # Apple Mac scanning requirements -->
Ideally, an Apple Mac computer is scanned through SSH. Enabling SSH on the computer allows Lansweeper to run the `system_profiler` command on the machine. **System Profiler** is an interface built into macOS that stores a variety of system data.

In order for Lansweeper to scan macOS, you need to set up a user with SSH access to the computer. To retrieve installed software, you also need to ensure that Spotlight is enabled on the computer.

To set up an Apple Mac computer for agentless scanning:

1. Open **System Preferences...** on the Mac computer.

   
2. Select **Users & Groups** and, if necessary, click the lock icon to unlock the menu.

   

   
3. Select the "**+**" button to create the user that will access and scan the computer. Submit your preferred username in the first and second input box, your preferred password in the third and fourth input box and select **Create User**.

   

   Once created, the user account should log in locally on the machine at least once to be able to scan the machine remotely afterwards. Alternatively, the user account should have sudo privileges.
4. Select the back button to go back to your **System Preferences**.

   
5. Select the **Sharing** menu.

   
6. Enable **Remote Login**, which will enable SSH, and **Only these users**.

   
7. Hit the "**+**" button, select the user you created earlier and **Select** to grant the user access to SSH.

   
8. Double-check that Spotlight is enabled on the computer, as the `system_profiler` command Lansweeper uses to retrieve software information doesn't work without it.
9. Your Mac computer should now be ready for scanning. Start scanning the machine by following the instructions in [this knowledge base article](https://www.lansweeper.com/kb/33/How-to-scan-Apple-Mac-computers.html).
