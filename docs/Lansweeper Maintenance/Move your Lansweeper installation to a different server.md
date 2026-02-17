<!-- # Move your Lansweeper installation to a different server -->
If required, you can migrate your Lansweeper installation from one computer to another. The exact migration procedure you should follow depends on which database server you are using, SQL Compact or SQL Server.   
A possible reason for moving your installation might be moving from a 32-bit server to a 64-bit server.

If you're planning to move your Lansweeper installation to a different server, we recommend updating your current installation first, if possible.   
For detailed instructions on updating your Lansweeper installation, check out [Update your Lansweeper On-prem installation](/docs/update-lansweeper-on-premises).

If you are unsure which database server you are using, browse to the **Configuration > Your Lansweeper License**section of the web console.   


If you only want to copy your Lansweeper scanning server configuration to a different server, follow the steps in [this knowledge base article](/docs/copy-lansweeper-scanning-server-configuration-to-a-different-server).

## Moving your installation if you are using SQL Compact

SQL Compact is no longer supported as a Lansweeper database provider. The final Lansweeper version that supports SQL Compact is version 7.2.107.4. Before moving your installation, we recommend [migrating your SQL Compact installation to SQL Server or SQL LocalDB](/docs/convert-a-deprecated-sql-compact-database).

## Moving your installation if you are using SQL Server or SQL LocalDB

Before moving your installation to a new server, make sure that server you want to move to a new computer is running the same version as the new server.

1. Make sure your new server has .NET Framework 4.8 or a more recent .NET version installed. This is a Lansweeper installation requirement from Lansweeper 8.2.200 onward.  

   Updating your .NET Framework to version 4.8 manually or via the Lansweeper installer often requires a reboot. Whether or not a reboot is required is determined by the Microsoft .NET Framework installer, this process is not Lansweeper-specific.
2. Create a full backup of your Lansweeper installation by following the steps in [this knowledge base article](/docs/back-up-your-installation "Backing up your installation").
3. Download [the latest Lansweeper installer](https://www.lansweeper.com/install-lansweeper/) and run it on the Windows computer you want to install Lansweeper on.
4. Perform an **Advanced install** of Lansweeper on the computer you want to migrate to and select SQL Server or SQL LocalDB as your database server. Installation instructions can be found in [this knowledge base article](/docs/install-lansweeper-on-prem#heading2 "Installing Lansweeper").
5. Restore your backup over the new Lansweeper installation by following the steps in [this knowledge base article](/docs/restore-your-installation-from-a-backup#heading2).
6. If necessary, update the **Action Path** in the **Configuration > Asset Pages** section of the web console, replacing the old computer name in the path with the new one. Your Action Path determines where Lansweeper will try to locate scripts and executables used by asset and user actions.
7. If the scanning configuration of the old scanning server should be migrated to the new scanning server, run the DatabaseMaintenance tool on the new server, found at `Program Files (x86)\Lansweeper\Tools\DatabaseMaintenance.exe`.   
   Otherwise, skip to step 9.  
   
8. If the scanning configuration of the old scanning server should be migrated to the new scanning server, execute the script below in the **Script Execution** tab of the tool. You'll need to replace "OldServer" with the NetBIOS name of the old scanning server and "NewServer" with the NetBIOS name of the new scanning server, leaving the single quotes in place. The script deletes the new, empty tab that will have been generated for the new scanning server under **Scanning > Scanning Targets** in the web console and transfers the old scanning server settings to the new server.

```
DELETE FROM tsysasservers
WHERE servername = 'NewServer';
GO

UPDATE tsysasservers
SET
servername = 'NewServer'
WHERE servername = 'OldServer';
GO

UPDATE tblassets
SET
scanserver = 'NewServer'
WHERE scanserver = 'OldServer';
GO
```

9. Finally, restart the **Lansweeper Server** service in Windows Services.

If you are scanning client machines using LsAgent and migrating your Lansweeper installation, there are some things to keep in mind to ensure your clients continue to scan successfully. [This article](/docs/impact-of-a-lansweeper-migration-on-lsagent-scanning) explains the impact of migrating the Lansweeper server on LsAgent scans.
