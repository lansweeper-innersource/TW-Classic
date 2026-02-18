<!-- # Microsoft Office license keys not detected -->
If your Microsoft Office license keys are not appearing in **Software > Scanned license keys**:

- [Upgrade to the latest Lansweeper release](/classic/docs/update-lansweeper-on-premises "Update your Lansweeper Classic installation").
- [Rescan your assets](/classic/docs/how-to-scan-a-windows-computer "Scan your Windows computer").

If Lansweeper can still not locate your license keys, it's likely that they are not stored in the registry.  In Microsoft Office 2013 and newer versions, some license keys are not stored in the registry and can not be scanned by Lansweeper.

To test whether or not your license keys are stored in the registry:

1. Open the **Registry Editor**.
2. Navigate to **HKEY\_LOCAL\_MACHINE > SOFTWARE > Microsoft > Office** or **HKEY\_LOCAL\_MACHINE > SOFTWARE > Wow6432Node > Microsoft > Office (64-bit machines).**
3. Search for **DigitalProductID** or **ProductKeys** in each registry.

If neither values exist, the Microsoft Office license keys are not stored in the registry, so they can not be scanned by Lansweeper.
