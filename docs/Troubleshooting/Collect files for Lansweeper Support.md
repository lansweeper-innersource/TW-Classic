<!-- # Collect files for Lansweeper Support -->
When contacting Lansweeper Support, it's always preferred to provide information from files stored on your Lansweeper installation. To make this process easier, the GatherLogs tool has been created.

The GatherLogs tool, which is included in every Lansweeper installation, will collect log files and other relevant information and compress the data in a Zip file.

When sent to Lansweeper Support, these files will provide the necessary information for the technical support engineers to start troubleshooting your case.

GatherLogs is available for both Windows and Linux. The steps to run it vary depending on your operating system.

## GatherLogs on Windows

You can gather information from:

- A Lansweeper server
- Windows assets with LsAgent installed
- A Network Discovery installation
- An IT Agent Discovery installation

### Run GatherLogs

1. Depending on what information you want to gather, the location of the GatherLogs tool will differ:
   - Lansweeper server:  
     Go to `Program Files (x86)\Lansweeper\Tools` and run **GatherLogs.exe**.
   - LsAgent:  
     Go to `Program Files (x86)\Lansweeper\Tools` on your Lansweeper server, and copy both **GatherLogs.exe**and `ICSharpCode.SharpZipLib.dll` to the LsAgent asset. Afterwards, run **GatherLogs.exe**.
   - Network Discovery:  
     Go to `Program Files\Lansweeper Network Discovery\Tools\GatherLogs`, right-click **GatherLogs.ps** and select **Run with PowerShell**.
   - IT Agent Discovery:  
     Go to `Program Files\Lansweeper IT Agent Discovery\Tools\GatherLogs`, right-click **GatherLogs.ps** and select **Run with PowerShell**.
2. A command prompt window will show you the progress of the log file collection.
3. After completion, the collected data is compressed into a Zip file. The Zip file will be named per the following format: `GatherLogOutput-$computername-$datetime.zip`  
   An additional log file will be generated as well, containing information on the execution of the tool.  

   The GatherLogs tool will generate a Zip file containing all files, placed in separate folders. This Zip file should be sent to Lansweeper Support to help troubleshoot your case.

### Lansweeper server

Depending on the installed Lansweeper components (scanning service, website, database), the GatherLogs tool will collect data based on what is present on the server.   
The output file will be stored in the same folder where GatherLogs was executed.

The following list provides an overview of the information collected from the Lansweeper server.

Lansweeper license and database information:

- License.csv
- Top10Tables.csv

Lansweeper configuration information:

- tblLsAgentRelayConfig.csv
- tsysAsServers.csv
- tsysCloudConfiguration.csv
- tsysCloudPrerequisitesCheck.csv
- tsysConfig.csv

Event viewer exports filtered for the last 7 days:

- Application.evtx
- System.evtx

Log files generated during the Lansweeper installation/upgrading process:

- Install\*.log

Multiple installation log files may be present depending on the number of times Lansweeper has been upgraded since the initial installation.

Lansweeper service logs:

- errorlog.txt
- Lansweeper.LocalDB.Service.txt
- Lansweeper.TestTools.Errorlog.txt
- sync\_errorlog.txt

IIS Express service logs:

- web\_errorlog.txt

### Windows assets with LsAgent installed

The GatherLogs tool can be moved and executed from a Windows asset with LsAgent installed. Both the executable and the accompanying DLL `ICSharpCode.SharpZipLib.dll` must be moved together to achieve this.   
The output file will be stored in the same folder where GatherLogs was executed.

If the DLL is missing, the collection of information will fail because the tool cannot compress and create a Zip file.



The following list provides an overview of the information collected from LsAgent on a Windows asset.

Event viewer exports filtered for the last 7 days:

- Application.evtx
- System.evtx

LsAgent information and logs:

- LsAgent.ini
- lsagentconfiguration.xml
- LsAgentlog.txt

The GatherLogs tool will generate a Zip file containing all files, placed in separate folders. This Zip file should be sent to Lansweeper Support to help troubleshoot your case.

### Network Discovery installation

The output file will be stored in `%LOCALAPPDATA%\Temp\Lansweeper Network Discovery\GatherLogs`.

The following list provides an overview of the information collected from the Network Discovery installation.

Discovery Hub information:

- Lansweeper.Discovery.Hub.log

Log files generated during the installation/updating process:

- Lansweeper\_Network\_Discovery\_installer.log
- Lansweeper\_Network\_Discovery\_uninstaller.log
- Lansweeper.Discovery.SelfUpdate.log
- Lansweeper.Discovery.Update.log

IT and OT sensor information:

- Lansweeper.IT.Sensor.log
- Lansweeper.OT.Sensor.log

Service logs:

- Eventlogs.csv

System information:

- SystemInfo.log

### IT Agent Discovery installation

The output file will be stored in `%LOCALAPPDATA%\Temp\Lansweeper IT Agent Discovery\GatherLogs`.

The following list provides an overview of the information collected from the IT Agent Discovery installation.

Discovery Hub information:

- Lansweeper.Discovery.Hub.log

Log files generated during the installation/updating process:

- Lansweeper\_IT\_Agent\_Discovery\_installer.log
- Lansweeper.Discovery.SelfUpdate.log
- Lansweeper.Discovery.Update.log

IT and OT sensor information:

- Lansweeper.IT.Sensor.log
- Lansweeper.OT.Sensor.log

Service logs:

- Eventlogs.csv

System information:

- SystemInfo.log

---

## GatherLogs on Linux

You can gather information from:

- A Network Discovery installation
- An IT Agent Discovery installation

### Run GatherLogs

1. Depending on what information you want to gather, the location of the GatherLogs tool will differ:
   - Network Discovery:  
     **gatherLogs.sh** can be found in `/opt/lansweeper-network-discovery-hub/tools/gatherlogs`.
   - IT Agent Discovery:  
     **gatherLogs.sh** can be found in `/opt/lansweeper-it-agent/tools/gatherlogs/`.
2. Open a terminal and execute the script with appropriate permissions, for example:   

   ```
   sudo bash /opt/lansweeper-network-discovery-hub/tools/gatherlogs/gatherLogs.sh
   ```

   or  

   ```
   sudo bash /opt/lansweeper-it-agent/tools/gatherlogs/gatherLogs.sh
   ```
3. After completion, the collected data is compressed into a Zip file. The Zip file will be named per the following format: `gatherlogs.zip`  
   An additional log file will be generated as well, containing information on the execution of the tool.  

   The GatherLogs tool will generate a Zip file containing all files, placed in separate folders. This Zip file should be sent to Lansweeper Support to help troubleshoot your case.

### Network Discovery installation

The output file will be stored in `/tmp/lansweeper-network-discovery-hub/gather-logs/`.

The following list provides an overview of the information collected from the Network Discovery installation.

Discovery Hub information:

- Lansweeper.Discovery.Hub.log
- Lansweeper.Discovery.Hub.clef

### IT Agent Discovery installation

The output file will be stored in `/tmp/lansweeper-it-agent/gather-logs/`.

The following list provides an overview of the information collected from the IT Agent Discovery installation.

Discovery Hub information:

- Lansweeper.Discovery.Hub.log
- Lansweeper.Discovery.Hub.clef

IT and OT sensor information:

- Lansweeper.IT.Sensor.log
- Lansweeper.IT.Sensor.clef
