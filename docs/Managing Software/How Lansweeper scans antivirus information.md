<!-- # How Lansweeper scans antivirus information -->

This page is for Lansweeper On-prem. For Lansweeper Sites, see [View antivirus software](/classic/docs/view-software#antivirus).

By default, Lansweeper includes a number of reports that provide information on your Windows computers' antivirus setup, to help you identify vulnerabilities in your network. These reports can be found in the **Reports** menu of the web console.

An individual computer's antivirus information can also be found in the **Summary** and **Software > Antivirus** tabs of the computer's Lansweeper webpage. Lansweeper can detect both whether a Windows computer has antivirus software installed and what the status of the antivirus software is. This article explains how antivirus detection works and how you can customize it.



## Antivirus status detection: enabled/disabled and up-to-date/out-of-date

Lansweeper pulls most Windows computer data from WMI (Windows Management Instrumentation), a management framework built into Windows operating systems.

An antivirus software's status is pulled from the AntiVirusProduct WMI class, found in the `\root\SecurityCenter` or `\root\SecurityCenter2` (Windows Security Center) namespace. WMI stores bit (SecurityCenter) or hexadecimal (SecurityCenter2) values indicating whether the antivirus software is enabled or disabled, and up-to-date or out-of-date. Hex values are converted by Lansweeper to bit values as well. A value of 0 means that the antivirus software is disabled or out-of-date; a value of 1 means that the antivirus software is enabled or up-to-date.

  

The antivirus status is solely pulled from WMI. If WMI reports an incorrect status (in which case Lansweeper will as well), you can try rebuilding the AntiVirusProduct WMI class on the affected machines and rescanning them afterwards. Keep in mind that the AntiVirusProduct WMI class simply does not exist on Windows Server operating systems, which makes it impossible to retrieve the antivirus status of these machines.

## Antivirus installations

Lansweeper uses two methods for detection of installed antivirus software:

- It pulls data from the AntiVirusProduct WMI (Windows Management Instrumentation) class, found in the `\root\SecurityCenter` or `\root\SecurityCenter2` (Windows Security Center) namespace. In the **Software > Antivirus** tab of individual computer webpages, you can identify antivirus records pulled from WMI by the "bug" icon.

  
- It looks at the software list in the **Software** tab of a computer's webpage (which mimics Add/Remove Programs) and verifies whether an installed software package is part of the list of known antivirus software found in the web console under **Software > Anti-Virus Settings**. If a software package listed in a computer's **Software** tab is part of the list of known antivirus software, the computer is deemed to have antivirus software installed.

If neither method finds antivirus software on a machine, but the machine does have antivirus software installed, you can try:   

- adding the software to the list of known antivirus software under **Software > Anti-Virus Settings**if it is listed in the **Software** tab of the machine's Lansweeper webpage,.
- rebuilding the AntiVirusProduct WMI class.

You can use the following as a wildcard under **Software > Anti-Virus Settings**:  

- %Avira\*% marks any AV software whose name starts with the word "Avira".
- %\*Avira% marks any AV software whose name ends in the word "Avira".
- %Avira% marks any  AV software whose name contains the word "Avira".
