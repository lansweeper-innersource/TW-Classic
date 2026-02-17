<!-- # View and scan software installations on Windows computers -->
Unless you manually [disable the software scan item](/docs/manage-scanned-item-intervals), Lansweeper scans the Windows computers in your network for installed software. Software info of Linux and Mac computers is also retrieved.

The **Reports** menu of the web console includes built-in reports that list the software installations found on computers in your network, e.g. the "Software: List of software by computer" report that lists Windows computer software.  
![viewing-and-scanning-software-installations-4.jpg](/docs/.document360/assets/article_146/image_001.jpg)

An individual Windows computer's software installations are also listed in the **Software** tab of the computer's Lansweeper webpage.  
![viewing-and-scanning-software-installations-5.jpg](/docs/.document360/assets/article_146/image_002.jpg)

Software data retrieved for Windows computers mimics Add/Remove Programs (Programs and Features) on the client machine itself. In other words, software listed in Add/Remove Programs on a Windows computer will automatically be detected by Lansweeper. This includes MSI and non-MSI software.

There are icons in the **Software** tab of your Lansweeper computer webpages that help distinguish between MSI and non-MSI installations. Lansweeper scans:

- Software installed for the computer as a whole, i.e. for all users configured on the computer.
- Software installed for the user logged into the computer during the last successful computer scan. Some software packages can be installed for individual users on a computer. If a software package is only installed for specific users, it will only be listed on a computer's webpage and in software reports if the user logged into the computer during the last successful computer scan has the software installed. You can easily identify user specific software, software installed only for the last logged on user, in the **Software** tab of your computer webpages.

  ![viewing-and-scanning-software-installations-6.jpg](/docs/.document360/assets/article_146/image_003.jpg)  

  Internet Explorer is always scanned by software scanning, even if it is delivered to a computer as an update and not listed in Add/Remove Programs.

  Other software packages not listed in Add/Remove Programs are not scanned by the default software scanning procedure, but can be detected with [custom file](/docs/windows-custom-file-scanning) or [custom registry scanning](/docs/scan-registry-values-with-custom-registry-scanning) instead.
