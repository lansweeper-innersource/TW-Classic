<!-- # View and scan software license keys on Windows computers -->
[Lansweeper](https://www.lansweeper.com/ "Lansweeper") scans the Windows computers in your network for software license keys, unless you manually [disable the SERIALNUMBER scan item](/docs/manage-scanned-item-intervals).

To reduce network traffic during scanning, only a limited number of keys are scanned by default and most scanning methods only scan keys once every 40 days. However, you can customize which keys are scanned and adjust the item interval of the SERIALNUMBER scan item.

On-demand scans of license keys can also be performed by using one of the Rescan buttons found on asset pages and in asset overviews. The Rescan buttons ignore item intervals and immediately rescan all of a Windows computer's data.

The **Reports** tab of the console includes a built-in report called "License: Software licensekey overview" that lists the keys found on the Windows computers in your network. An individual computer's license keys are also listed in the **Software > License Keys** tab of the computer's Lansweeper webpage.



  

It's important to note that, from a Lansweeper point of view, software installations and software license keys are completely unrelated. You should not use license keys as an indicator of how many software installations exist in your network. [This knowledge base article](/docs/software-installations-vs-software-license-keys) provides more info on the difference between software installations and license keys.

Lansweeper uses two methods to retrieve software license keys:

- It searches the HKEY\_LOCAL\_MACHINE registry locations listed in the Lansweeper web console under **Software > License Key Settings**, for each Windows computer.  
    
  Hundreds of registry locations are built into Lansweeper, though most are disabled by default to reduce network traffic during scanning. To enable scanning of a license key, tick the **Enabled** checkbox. Built-in registry locations are known by the Lansweeper team to store license keys. If you know of additional registry locations that store licenses, ones that are not built-in, you can add your own as well.  
  
  - Some Microsoft keys (Office, SQL, Windows) are not included in the list, but scanned by default. Office licenses are pulled from the DigitalProductID and ProductKeys values under `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office` and `HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Office` (64-bit machines).
  - The Type column indicates whether Lansweeper will read the license key exactly as it is written into the registry (Plain Text) or decrypt it (Adobe and Microsoft keys).
  - The Var. column is only relevant for Microsoft keys and indicates whether Lansweeper will look for variations of the same registry value. For most keys, including any additional keys you may submit for scanning, this setting is not relevant.
  - You can have Lansweeper search additional registry locations for license keys by selecting **Add Product Key**. Submit a product name and the registry key and value that store the license key. Keep in mind that only registry locations within HKEY\_LOCAL\_MACHINE can be searched and don't forget to rescan your machines with one of the Rescan buttons, to immediately update license key information.
- For products by software publisher Adobe specifically, it pulls additional license keys from .swidtag files on the Windows computer. Your Adobe software's .swidtag files should be stored in one of the file locations listed below. The first two are used by both Windows XP and Windows Server 2003, while the third and fourth are used by more recent Windows operating systems. Lansweeper automatically scans Adobe .swidtag files for stored license keys.

  ```
  %ALLUSERSPROFILE%\Application Data\Adobe\ISO-19770
  %ALLUSERSPROFILE%\Application Data\regid.1986-12.com.adobe
  %PROGRAMDATA%\Adobe\ISO-19770
  %PROGRAMDATA%\regid.1986-12.com.adobe
  ```

    

  If you are running the latest Lansweeper release, have recently and successfully rescanned your machines and are unable to find certain license keys, Lansweeper was unable to locate the keys using either of the aforementioned detection methods. Microsoft MAK keys, Microsoft Office 2000 (and lower) keys and some [Microsoft Office 2013 (and higher) keys](/docs/microsoft-office-license-keys-not-detected) are not stored in the registry for instance, which makes these keys impossible to scan.
