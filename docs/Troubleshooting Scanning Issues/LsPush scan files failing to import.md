<!-- # LsPush scan files failing to import -->
If you choose to store [LsPush](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows "Introduction to the LsPush scanning agent for Windows") results in files, these files must be placed in the import folder on your Lansweeper server, where they are automatically processed. When the files have disappeared from the import folder, the import process has completed and the machines can be found in the web console.

However, import may fail for a variety of reasons. To resolve import failures, follow the troubleshooting steps below.

## Update Lansweeper

1. In the web console, go to **Configuration > Your Lansweeper license**.
2. Select **Check for updates now**.
3. If your Lansweeper installation is out of date, select **Download now** to update your installation.

## Use the latest LsPush executable

When you update your Lansweeper installation, the latest version of the LsPush executable is also updated. If you are using a logon script, group policy, or scheduled task:

1. In **File explorer**, navigate to **Program Files (x86)\Lansweeper\Client**.
2. Copy **lspush.exe** to your clipboard.
3. Paste the executable to the folder referenced by your script, policy, or task.

## Ensure the Lansweeper Server service is running

By default, the Lansweeper Server service automatically starts and scans your data. However, it may have been manually stopped, meaning no LsPush data can be imported or processed.

1. Navigate to **Windows Services**.
2. Locate and right-click **Lansweeper Server** from the list.
3. If the server has stopped, select **Start**.



## Ensure LsPush files are in the correct folder

If the machines you're scanning do not connect to your Lansweeper installation, scanned data can be saved in text files. 

Before importing the files, ensure no changes are made to the extension or contents of the LSPush files, as this can cause import failures.

LsPush files are compressed and not human-readable in their raw form. The Lansweeper scanning service decompresses and reads the data when the files are imported.

In your Lansweeper scanning server, navigate to **Program Files (x86)\Lansweeper\Service\import** and place your files.



## Ensure the number of assets does not exceed your license limit

1. In the Lansweeper Classic web console, go to **Configuration > Your Lansweeper license**.
2. Ensure the **Licensed assets** count does not exceed the **Asset limit**.

   Most Lansweeper licenses limit the number of assets you can scan. Once you've reached [your licensed asset limit](/classic/docs/assets-that-count-toward-your-licensed-asset-limit), you can not scan new or existing assets until you [delete assets](/classic/docs/delete-assets "Delete assets") or [upgrade your license](https://www.lansweeper.com/pricing/ "Pricing & Plans").

## Ensure the machine is not excluded from scanning

1. In Lansweeper Classic's web console, go to **Scanning > Scanning targets**.
2. Navigate to the **Scanning exclusions** section of the page.
3. Check the machine has not been excluded based on name, domain, IP address, IP range or asset type. No assets are created for machines that are excluded from scanning.

   

Pay attention to wildcards used in Windows Computer exclusions. In the example above, any Windows computer whose name contains the word "LAN" will not be scanned.

## Ensure anti-virus scanners have not changed the LsPush files

If your LsPush files are sent via email, it's possible that your anti-virus software may have scanned the LsPush files and added a line to indicate they're safe. This will cause the import to fail.

Exclude LsPush files from anti-virus scanning or send the files your Lansweeper server using an alternative method.

## Check Window's log files

1. In your Lansweeper server, navigate to the following folder: Program Files (x86)\Lansweeper\Service\Errorlog.txt. The log may contain errors similar to:  

   ```
   Cannot import file  
   Cannot import: Data at the root level is invalid. Line 1, position 1.  
   Could not retrieve AssetID from Assetunique  
   Failed to construct a huffman tree using the length array. The stream might be corrupted.  
   Found invalid data while decoding.  
   The CRC in GZip footer does not match the CRC calculated from the decompressed data.  
   The magic number in GZip header is not correct. Make sure you are passing in a GZip stream.
   ```
2. Search for your Window's computer name in the log file.

If your Window's computer appear in the file, the LsPush files are likely to have corrupted.

## Rescan the Windows computers

To generate new files, [rescan the Windows computers with LsPush](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows "Introduction to the LsPush scanning agent for Windows") to generate new scan files, and replace them in the import folder.
