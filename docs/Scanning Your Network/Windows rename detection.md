<!-- # Windows rename detection -->
This article explains the effect of enabling Windows rename detection. When a network asset is being scanned, Lansweeper needs to determine whether the asset is already present in the Lansweeper database.

This is accomplished by comparing some specific data pulled from the asset being scanned with data already present in the database. This point of comparison is called the "unique key" or "internal ID" of the asset. It's what Lansweeper uses to uniquely identify the asset.   
The unique key of a [Windows computer](/docs/how-to-scan-a-windows-computer) is: <NetBIOS domain or workgroup name>\<NetBIOS computer name>\1. The unique key of computer LAN-001 in the LANSWEEPER domain is the following for instance: LANSWEEPER\LAN-001\1.

Considering a Windows computer's unique key includes its name and domain, a name or domain change would presumably lead to a new asset being generated for the computer. However, a setting called **Detect when a Windows computer has been renamed** ensures that name or domain changes do not lead to new assets. This setting is enabled by default and can be found in the following section of the web console: **Configuration > Server Options**.

![menu-configuration-server-options.jpg](/docs/.document360/assets/article_248/image_001.jpg)

![windows-rename-detection-5.jpg](/docs/.document360/assets/article_248/image_002.jpg)

## Effect of name or domain changes when rename detection is enabled

In recent Lansweeper releases, the main rename detection setting is enabled by default. This ensures that when a Windows computer is renamed or moved to a different domain, the computer's existing Lansweeper webpage is updated instead of a new asset being generated.

To identify a name or domain change, rename detection by default compares the MAC address, model and serial number of the computer being scanned with MAC address/model/serial combinations already present in the Lansweeper database. From Lansweeper 9.2 onward, you can optionally enable a sub-setting of rename detection to only compare model and serial number, not MAC address. This can be useful in situations where your computers' network adapters also change.

When rename detection sees a change in name or domain, the **Assetname** and **Domain** values on the Windows computer's existing Lansweeper webpage are automatically updated to reflect this. The Windows computer's unique key is also automatically changed to <new domain name>\<new computer name>\1 and a comment regarding the name/domain change is added to the computer's **Comments** tab. No further changes are made to the computer's asset page, which is updated as normal upon rescanning. Any history and custom data associated with the asset remain intact.

Rename detection only affects Windows computers. As a non-Windows device's name is never used as part of its unique key anyway, name changes of non-Windows devices will never cause new assets to be generated.   
The below requirements must be met for rename detection to successfully detect a Windows computer name or domain change. The below list assumes the rename detection sub-setting is not enabled. If you do enable the sub-setting, the requirements are very similar but simply exclude MAC address.

- The machine being renamed or moved to a different domain must be a Windows computer.
- The Windows computer must have the following: a MAC address, model and serial number.
- The MAC address, model and serial number must be retrievable from the machine itself. Rename detection cannot work if you manually submit the model or serial in Lansweeper for instance.
- The MAC address, model and serial number must be the same before and after the computer name or domain change.
- The MAC address, model and serial number must be successfully scanned by Lansweeper before and after the computer name or domain change. Rename detection cannot work if the computer generates a scanning error under its new name or domain, e.g. due to an incorrect credential.

  ![windows-rename-detection-2.jpg](/docs/.document360/assets/article_248/image_003.jpg)

  ![windows-rename-detection-3.jpg](/docs/.document360/assets/article_248/image_004.jpg)

  ![windows-rename-detection-4.jpg](/docs/.document360/assets/article_248/image_005.jpg)

## Effect of name or domain changes when rename detection is disabled

Rename detection is enabled by default and it is recommended that you keep this setting enabled. If you do disable rename detection, be aware that changing a Window computer's name or moving it to a different domain will cause a new asset to be generated in Lansweeper.

If you disable rename detection and want to prevent name or domain changes from generating new assets, you must first rename/move the computer within Lansweeper and then rename/move the machine itself. If you do not rename/move the machine in Lansweeper first, a new asset page will be generated for it under the new domain or computer name and its original webpage will no longer be updated upon rescanning. Any history or custom data will only be associated with the original (and not the new) webpage.

To rename a computer within Lansweeper or move it to a different domain, browse to its webpage, click the **Edit asset** button, update the **Assetname** or **Domain** field and select **Save asset**.
