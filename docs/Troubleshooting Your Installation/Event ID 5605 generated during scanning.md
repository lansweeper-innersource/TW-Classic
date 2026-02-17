<!-- # Event ID 5605 generated during scanning -->

When you've installed Lansweeper and start scanning your network, you may start seeing event ID 5605 entries in the Event Viewer of some of your client machines. These events are caused by a bug in Windows and can be ignored.

Lansweeper pulls Windows computer data from WMI (Windows Management Instrumentation), a management framework built into Windows operating systems. Since version 5.1, Lansweeper scans the [Win32\_Tpm](https://docs.microsoft.com/en-us/windows/win32/secprov/win32-tpm) WMI class on your computers. This class stores Trusted Platform Module information and requires special access permissions. Lansweeper does use the correct authentication level to scan the WMI class, but a bug in some Windows versions causes event ID 5605 to be generated every time Win32\_Tpm is accessed, even successfully.

Event ID 5605 does not point to a failure to scan Win32\_Tpm, nor does it point to an underlying issue with Lansweeper or your client machine. Lansweeper automatically [excludes the event from scanning](/docs/excluding-events-from-scanning) so it doesn't show up in your Lansweeper web console, but you may still see it in your Event Viewer.

The root\cimv2\Security\MicrosoftTPM namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt\_Privacy and run the script or application again.

![event-id-5605-generated-during-scanning-1.jpg](/docs/.document360/assets/article_284/image_002.jpg)
