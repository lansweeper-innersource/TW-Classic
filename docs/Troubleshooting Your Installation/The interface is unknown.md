<!-- # The interface is unknown -->
Listed below are two possible causes of (and solutions for) the following error, which you may see on the Lansweeper webpages of scanned assets:

The interface is unknown. (Exception from HRESULT: 0x800706B5)

- If the machine hosting your Lansweeper installation is running Windows Server 2008 R2, the likely explanation for the problem is the absence of Windows hotfix KB2401588 on your Lansweeper server. Windows Server 2008 R2 has some known issues. Make sure Service Pack 1 is installed and hotfix KB2401588 is applied as well.
- If the machine hosting your Lansweeper installation is not running Windows Server 2008 R2 and the scanning errors are limited to specific Windows computers, it is also possible that WMI (Windows Management Instrumentation) is corrupt on those client machines. More info on resolving WMI corruption errors can be found in [this knowledge base article](/docs/repair-a-corrupt-wmi-installation).
