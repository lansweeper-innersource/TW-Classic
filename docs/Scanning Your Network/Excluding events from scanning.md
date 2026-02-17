<!-- # Excluding events from scanning -->
All Windows computer scanning methods scan events found in the Windows Logs section of a client machine's Event Viewer. Error events and any [additional event types](/docs/scanning-non-error-events) you may have enabled are scanned. It is possible to exclude individual events from scanning, however.

## Excluding events

To exclude events from scanning, follow these steps:

1. Browse to the **Scanning > Scanning Targets**section of the web console.

   
2. Click the **Add Exclusion** button in the **Scanning Exclusions** section of the page.
3. Select the **Windows Event** option in the resulting pop-up window, select an event that was already scanned and click **Ok**.   
   New instances of the specified event will no longer be scanned or added to the database. Any previously scanned instances of the event will remain in the database until removed by [your database cleanup options](/docs/perform-automated-database-cleanups). Alternatively, you can manually submit an event source and event ID in the available input boxes. This approach can be used to exclude events that haven't been scanned yet.

   

   Some DCOM errors are excluded by default. If you scan without an agent, Lansweeper uses DCOM to establish the initial connection to your Windows computers. If your Lansweeper server tries to connect to a client machine that is offline or firewalled, an error is automatically logged by DCOM in the server's Event Viewer. These events are informational and can be ignored.
