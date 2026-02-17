<!-- # Windows custom file scanning -->
Lansweeper allows you to scan specific files on your Windows computers. Custom file scanning retrieves various properties (version, company, size, creation date, last accessed date and last modified date) of a specific file.

This is useful to detect software packages not listed in Add/Remove Programs for instance, i.e. software not detected by Lansweeper's built-in software scanning procedure. If you submit vRD.exe (Visionapp executable) for file scanning for instance, Lansweeper will scan the aforementioned properties of the file.  
![scanning-file-properties-with-custom-file-scanning-1.jpg](/docs/.document360/assets/article_247/image_002.jpg)

## Custom file scanning

1. Browse to the **Scanning > Scanned Item Interval** section of the web console.
2. Open the dropdown menu for the "FILES" item and select your preferred scanning option.  
   ![File and directory scanning Windows 1.png](/docs/.document360/assets/article_247/image_003.jpg)  

   If you want to scan for files during every scan, set the interval to “**0**”.
3. Browse to the **Scanning > File & Registry Scanning**section of the web console.
4. In the **File Scanning** section of the page, select **Add File Scan**.![File and directory scanning Windows 2.png](/docs/.document360/assets/article_247/image_004.jpg)
5. In the pop-up, enter the file path of the file you want to scan and select **Ok**.  

   Available parameters are: %programfiles%, %programfiles(x86)% and %windir%.   
   You can use these parameters in your file paths to make Lansweeper search for the Program Files, Program Files (x86) or Windows directory in any drive on your machines.
   - If you use the %programfiles(x86)% parameter and a computer's OS is 32-bit, scanned data will be the same as if you were using the %programfiles% parameter.
   - To retrieve properties of files in any directory other than Program Files, Program Files (x86) or the Windows directory, you must submit the exact file path, including the drive.   
     For performance reasons, file scanning only queries specific file paths. Scanning all files within a folder or listing all files with a specific extension (extension based scanning) is not possible with file scanning, though you could use a deployment package to perform such file searches.
6. If you plan on scanning your Windows computers with our LsPush scanning agent and without a direct connection to your Lansweeper server, select **Export Files.tsv for LsPush** to export your file scanning configuration. You can then place the Files.tsv file in the same folder as your LsPush executable to have LsPush retrieve the file data as well.  
   ![scanning-file-properties-with-custom-file-scanning-4.jpg](/docs/.document360/assets/article_247/image_005.jpg)  

   Exporting file scanning settings is only necessary if you are scanning with our LsPush scanning agent and if your LsPush command does not reference your Lansweeper server, i.e. if LsPush is not connecting directly to your Lansweeper server.   
   If LsPush is connecting to your server, it will automatically retrieve your settings and an export is not required. More info on how to scan Windows computers with LsPush can be found in [this knowledge base article](/docs/introduction-to-the-lspush-scanning-agent-for-windows).
7. Rescan your Windows computers with LsPush, or by going to the **Assets** section of the web console, selecting the Windows asset and selecting **Rescan asset(s)**.
8. To view scan results, browse to the **Scanning > File & Registry Scanning** section, and select **Report**.  
   ![File and directory scanning Windows 3.png](/docs/.document360/assets/article_247/image_006.jpg)  

   Alternatively, you can run a [custom report](#post39292) or view an individual computer's scan results in the **Config > Scanned Info > File Info** section of the computer's Lansweeper webpage.

   ![scanning-file-properties-with-custom-file-scanning-6.jpg](/docs/.document360/assets/article_247/image_007.jpg)
   - If a file's **Found** value is set to **True**, that means the file was found on the computer and you can view the file's properties.
   - If a file's **Found** value is set to **False**, that means the file was not found on the computer.
