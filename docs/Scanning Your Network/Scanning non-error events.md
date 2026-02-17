<!-- # Scanning non-error events -->
When Lansweeper scans a Windows computer, it retrieves the events found in the Windows Logs section of the computer's Event Viewer. It's important to note however, to keep your database as small as possible, only error events are scanned by default.

Looking at the screenshot below for instance, the first 3 events will be scanned by default, but the 4th and 5th event will not. Additional event types (warning, information, success audit or failure audit) can be manually enabled for scanning, if required.

![scanning-non-error-events-1.jpg](/docs/.document360/assets/article_227/image_001.jpg)

## Scanning non-error events

To enable scanning of additional (non-error) event types, follow these steps:

1. Browse to the **Configuration > Server Options**section of the web console. If you have multiple scanning servers, there will be a separate configuration tab for each server.

   ![menu-configuration-server-options.jpg](/docs/.document360/assets/article_227/image_002.jpg)
2. Tick the checkboxes of the event types you would like to enable in the **Eventlog scanning** section of the page.

   ![scanning-non-error-events-2.jpg](/docs/.document360/assets/article_227/image_003.jpg)

   Enabling additional event types can greatly increase the size of your database over time and negatively impact performance. It is recommended that you leave as many event types disabled as possible.

   For performance reasons, our LsAgent and LsPush scanning agents only scan error events, regardless of which event types you enable in your Server Options.
3. Lower the **Delete eventlog entries after XX days** setting as much as possible in the **History Cleanup Options** section of the page, to prevent exponential growth of your database.

   ![scanning-non-error-events-3.jpg](/docs/.document360/assets/article_227/image_004.jpg)
4. Wait for your scanning schedules to trigger or manually rescan your Windows computers, e.g. with the **Rescan** buttons found in asset overviews.
5. View scanned events through dashboard widgets, reports or in the **Event log** tab of individual Windows computer webpages. Examples of event log widgets are Event Filter and Event Summary. A sample report that lists all scanned events that occurred in the last 7 days can be found here in our report center. Event log data is stored in the tblNtlog database tables.

   ![scanning-non-error-events-4.jpg](/docs/.document360/assets/article_227/image_005.jpg)
