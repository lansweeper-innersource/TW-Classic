<!-- # Software installations vs. software license keys  -->
Lansweeper scans both the software installations and the software license keys found on Windows computers in your network. It's important to note that, from a Lansweeper point of view, these two pieces of scanned data are completely unrelated.

Installations and license keys are stored in different locations within the client machine's registry and different tables within the Lansweeper database. There are no naming conventions for installations or keys. A software publisher can add a software installation as "Software ABC" to Add/Remove Programs, while adding the license key for the same software as "Software DEF" to the registry. This makes it impossible for Lansweeper to link the two.

Lansweeper uses two separate scanning procedures and two separate database tables (that cannot be linked) for installations and keys.

A report cannot list both software installations and license keys; it can only list one or the other. To report on installations, use a software installation report, e.g. the built-in "Software: List of software by computer" in the **Reports** tab. To report on license keys, use a license key report, e.g. the built-in "License: Software licensekey overview".

License key reports should not be used to report on software installations. If software is uninstalled from a computer, it is removed from installation reports upon rescanning. If the key associated with the program remains in the computer's registry however, that key will continue to be listed in license key reports. It is expected behavior for license keys present in the registry to still be detected, even if the corresponding program is uninstalled.

## Software installations

Software installations are listed in both the **Software** section of a Windows computer's **Software** tab, and in the built-in Lansweeper report "Software: List of software by computer".  
Software installation scanning mimics the Add/Remove Programs (Programs and Features) section of the control panel on the computer itself, as explained in [this knowledge base article](/docs/view-and-scan-software-installations-on-windows-computers).



## Software license keys

Software license keys are listed in both the **License Keys** section of a Windows computer's **Software** tab, and in the built-in Lansweeper report "License: Software licensekey overview".   
License keys are pulled from various locations within the registry, as explained in [this knowledge base article](/docs/view-and-scan-software-license-keys-on-windows-computers), and are often left behind when the corresponding software is uninstalled.

  

To reduce network traffic, scanning of most license keys is disabled by default, but this can be enabled manually.
