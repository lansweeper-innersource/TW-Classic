<!-- # Scanning with an Eventlog Only scanning target -->
Your Lansweeper Classic installation includes two Eventlog Only scanning targets. These are agentless, scheduled scanning targets that scan the event log entries of Windows domain or workgroup computers specified by you, as frequently as once a minute. Specifically, events found in the Windows Logs of a client machine's Event Viewer are scanned.

Eventlog Only scanning is supported Windows operating systems, and only retrieves event log information; it does not scan any other computer data. Eventlog Only scans allow you to scan computer containers, OUs and individual (domain or workgroup) computers and specify a separate scanning schedule for each scanning target.

To submit a container, OU or individual computer for Eventlog Only scanning:

1. Go to the **Scanning > Scanning Targets**section of the web console.  
   
2. Select **Add Scanning Target**.  
   
3. Choose one of the Eventlog Only scanning types in the resulting pop-up.
   - The first scanning type allows you to submit one specific Windows domain or workgroup computer for Eventlog Only scanning.
   - The second scanning type allows you to submit all computers in a specific OU.
4. If you have multiple scanning servers, there will be multiple configuration tabs on the **Scanning Targets** page, one for each server.

As agentless scanning of Windows computers requires credentials, make sure to submit and map your Windows scanning credentials as well, by following the instructions in [this knowledge base article](/classic/docs/create-and-map-scanning-credentials).

All Windows scanning targets, not just Eventlog Only types, scan event log information. Eventlog Only scans simply allow you to scan events more frequently, so you can monitor important servers or workstations more closely. You can review events as they happen and optionally [configure real-time email alerts](/classic/docs/send-report-and-event-log-alerts).

## Eventlog Only settings

Below is an overview of available Eventlog Only scanning options and settings. Each scanning target can be configured differently.



- **Target** or **Adsi Path**: depending on which scanning type you choose, the NetBIOS name of the individual Windows computer or the computer container or organizational unit whose event log information you want to scan should be entered.  

  When you submit a CN/OU for Eventlog Only scanning, Lansweeper scans the event log entries of the computers in the CN/OU you've submitted and any sub-OUs contained within.
- **Domain/Workgroup (Netbios)**: the NetBIOS name of the domain or name of the workgroup your computer CN/OU or individual computer belongs to should be entered.
- **Description**: a custom description of the scanning target can be entered.
- **Recurring every**: determines how often (every X number of minutes or hours) the scanning target will be scanned.
- **Enable**: toggle this option to enable or disable scanning of the scanning target.  

  To keep your database as small as possible, only error events are scanned by default. [Additional event types](/classic/docs/scanning-non-error-events) (warning, information, success audit or failure audit) can be manually enabled for scanning, if required.
