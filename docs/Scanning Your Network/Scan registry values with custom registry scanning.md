<!-- # Scan registry values with custom registry scanning -->

Lansweeper allows you to scan values in your Windows computers' registries, through custom registry scanning. Registry scanning checks what a specific registry value is set to across your Windows computers.

As a lot of data and settings are stored in a computer's registry, there are an endless number of things you can report on. If you submit the Version value seen below (Flash plugin version) for registry scanning for instance, Lansweeper will scan the data stored in this value, e.g. 11.5.502.135.



## Retrieve data stored in a specific registry value

1. Browse to the **Scanning > Scanned Item Interval**section of the web console.
2. Enable registry scanning by choosing **Scan Server and LsAgent**, **LsAgent Only**, or **Scan Server Only**.  
   
3. Browse to the **Scanning > File & Registry Scanning**section of the web console.
4. Select **Add Registry Scan** in the **Registry Scanning** section of the page. Select the registry value's root key from the Rootkey dropdown, enter the remainder of the registry path into the Regpath field, enter the name of the registry value into the Regvalue field and select **Ok**.
   - To avoid typos, copy the Regpath directly from regedit.exe on a Windows computer. You can right-click the key in regedit.exe and select **Copy Key Name** in the dropdown.
   - No parameters are currently available for registry scanning. You must submit an exact registry value.   
     For performance reasons, registry scanning only queries specific registry values. Retrieving all values within a key or searching the entire registry for a specific value is not possible.
   - To scan a (Default) value, leave the Regvalue field blank when submitting your registry scan. Keep in mind that only (Default) value names that have a value can be scanned. (Default) value names whose value is not set will not be detected.
5. If you plan on scanning your Windows computers with our LsPush scanning agent and without a direct connection to your Lansweeper server, select **Export Registry.tsv for LsPush** to export your registry scanning configuration. You can then place the Registry.tsv file in the same folder as your LsPush executable to have LsPush retrieve the registry data as well.  

   Exporting registry scanning settings is only necessary if you are scanning with our LsPush agent and if your LsPush command does not reference your Lansweeper server, i.e. if LsPush is not connecting directly to your Lansweeper server.   
   If LsPush is connecting to your server, it will automatically retrieve your settings and an export is not required. More info on how to scan Windows computers with LsPush can be found in [this knowledge base article](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows).
6. Rescan your Windows computers with LsPush, or by going to the **Assets** section of the web console, ticking the checkboxes in front of the computers and selecting **Rescan**.
   - You can search in one or multiple columns to easily find specific assets. In the example above, we filtered the Domain column to only list assets within the Lansweeper domain.
   - You could also tick the top checkbox to select all assets in the current search results.
7. View scan results under **Scanning > File & Registry Scanning** by selecting the **Report** button.   
   Alternatively, you can run a [custom report](https://www.lansweeper.com/report/custom-registry-key-audit/) or view an individual computer's scan results in the **Config > Scanned Info > Registry Keys** section of the computer's Lansweeper webpage.
   - If a registry key is displayed on a computer's webpage, that means the key was found on the computer and you can view the key's value.
   - If a registry key is not displayed on a computer's webpage, that means the key was not found on the computer.
