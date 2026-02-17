<!-- # SQL Server Information not scanned -->
When Lansweeper scans a Windows computer, it automatically retrieves software information found in Add/Remove Programs (Programs & Features) on the client machine itself. As information listed in Add/Remove Programs for installations of Microsoft SQL Server is limited, Lansweeper retrieves additional SQL Server data from Windows Management Instrumentation.

WMI (Windows Management Instrumentation) is a management infrastructure built into Windows operating systems. Scanned SQL Server data includes SQL edition, version, service pack, service names and statuses, authentication mode, language, installed databases, database sizes, cluster information (from Lansweeper 7.1 onward) and more.

If SQL Server data is not listed in the **Software > SQL Server Information** tab of your Windows computers, the WMI provider storing the SQL Server information may be missing and you may need to recompile it. Instructions on how to do this can be found further down this article.



  To recompile the WMI provider storing SQL Server information, follow these steps:

1. On the client machine whose SQL Server information isn't scanned, locate the folder that contains the .mof file of the SQL Server installation. This file contains the definitions of the WMI classes Lansweeper uses to retrieve SQL Server information. While the exact directory depends on the installed SQL Server version, the path should be similar to `Program Files (x86)\Microsoft SQL Server\<version>\Shared`.  
   In the following screenshot, SQL Server 2016 is installed which means that the .mof file can be found in the 130 folder.  
   

   The following is a list of folder numbers and the SQL Server versions they belong to:   
   • 80: SQL Server 2000  
   • 90: SQL Server 2005  
   • 100: SQL Server 2008 and SQL Server 2008 R2   
   • 110: SQL Server 2012   
   • 120: SQL Server 2014   
   • 130: SQL Server 2016   
   • 140: SQL Server 2017   
   • 150: SQL Server 2019
2. Run Command Prompt as an administrator.

   
3. Submit the command below and press **Enter**, replacing <version> with the folder number containing your specific .mof file.  

   ```
   mofcomp "%programfiles(x86)%\Microsoft SQL Server\<version>\Shared\sqlmgmproviderxpsp2up.mof"
   ```

   The screenshot below uses the folder path for SQL Server 2016.  
   
4. Rescan the client machine by going to the **Assets** section of the web console, ticking the checkbox in front of the machine and selecting **Rescan**.  

     

   If you are scanning your assets using LsAgent, there are three options to rescan the asset:
   - Modify the LsAgent.ini file to force a rescan, by removing the data from the LastScan and LastSent fields so both are empty.
   - Restart the **Lansweeper Server** service in **Windows Services**.
   - Wait until the next scheduled LsAgent scan.
5. If after the rescan SQL Server information is found, but certain databases are not listed, make sure **Auto Close** is turned off for these databases. Right-click the databases in SQL Server Management Studio, select **Properties**, then the **Options** tab and make sure **Auto Close** is set to "False". Rescan the client machine afterwards.

   
