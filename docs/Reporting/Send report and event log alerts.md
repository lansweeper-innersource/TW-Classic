<!-- # Send report and event log alerts -->
Lansweeper lets you send two types of asset alerts: alerts for reports listed in the web console's **Reports** tab, which are sent on a scheduled basis, and event log alerts, which are sent as soon as the Windows event log entries specified by you are scanned. Sending alerts is useful for tracking vital network information, software changes, or even server or workstation errors.

Both report and event log alerts can be sent via email. From Lansweeper 6.0 onward, report alerts can also be copied to a directory instead. If you have multiple scanning servers, you can configure event log alerts separately for each server. Each scanning server will send the event log alerts for the assets it's scanning. Report alerts, on the other hand, can and only need to be configured on one scanning server. That scanning server has access to all data in your database and can send any report results you want.

## Submit your email server and groups

If you plan on having your alerts sent via email, be sure to submit your email server settings before configuring your actual alerts. You should also configure the email groups to the alerts that should be sent to.

1. Browse to the **Configuration > Email Alerts**section of the web console.  
   ![menu-configuration-email-alerts.jpg](/docs/.document360/assets/article_152/image_001.jpg)
2. Fill in the fields in the **E-mail Server** section:  
   - SMTP server
   - Port number
   - From address: the email address you would like to send alerts from
   - Display name
   - Optionally, you can load a built-in SMTP configuration, use SSL and/or enable authentication.  
     ![sending-report-and-event-log-alerts-1.jpg](/docs/.document360/assets/article_152/image_002.jpg)
3. Select **Add E-mail Group** in the **E-mail groups** section.
4. Enter a name for the group, and one or more email addresses, separated by semicolons. Select **Ok**. ![sending-report-and-event-log-alerts-2.jpg](/docs/.document360/assets/article_152/image_003.jpg)  

   An email group is a collection of email addresses your alerts will be sent to. You can create multiple email groups to send various alerts to.

## Set up report alerts

1. Browse to the **Configuration > Email Alerts**section of the web console.  
   ![menu-configuration-email-alerts.jpg](/docs/.document360/assets/article_152/image_004.jpg)
2. If you are sending your reports via email, submit your email server and groups.
3. Tick the **Enable report mailing** checkbox.  
   ![sending-report-and-event-log-alerts-3.jpg](/docs/.document360/assets/article_152/image_005.jpg)
4. Select **Add report**, select one or more reports and click **Add**. You can use the search box to find specific reports.  
   ![sending-report-and-event-log-alerts-4.jpg](/docs/.document360/assets/article_152/image_006.jpg)  

   A report is only mailed if it has results. Empty reports are not mailed.
5. For each report, choose whether to have it sent via email or copied to a directory and choose an export type. Available export formats are Excel, CSV, and HTML. If you choose Directory as your Alert Type, the report results will be copied to `Program Files (x86)\Lansweeper\Service\export` on the machine hosting your Lansweeper installation.  
   ![sending-report-and-event-log-alerts-5.jpg](/docs/.document360/assets/article_152/image_007.jpg)
6. Select **Set time schedules** to choose the schedule for the report alert. The resulting pop-up lists several built-in schedules, but you can create your own as well.  
   ![sending-report-and-event-log-alerts-6.jpg](/docs/.document360/assets/article_152/image_008.jpg)
7. Depending on the chosen Alert Type:
   - **E-mail**: choose an email group to send the report alert to.  
     ![sending-report-and-event-log-alerts-7.jpg](/docs/.document360/assets/article_152/image_009.jpg)
   - **Directory**: optionally tick the Overwrite checkbox. If this box is checked, a report's results will be overwritten in the export folder every time the alert is triggered. If this box is unchecked, a new file will be generated in the export folder every time the alert is triggered.  
     ![sending-report-and-event-log-alerts-8.jpg](/docs/.document360/assets/article_152/image_010.jpg)
8. The reports will be sent based on the schedules specified by you. You can immediately have all reports mailed as well by selecting **E-mail all configured reports now**.  
   ![sending-report-and-event-log-alerts-9.jpg](/docs/.document360/assets/article_152/image_011.jpg)

## Set up event log alerts

1. Browse to the **Configuration > Email Alerts**section of the web console:![menu-configuration-email-alerts.jpg](/docs/.document360/assets/article_152/image_012.jpg)
2. Make sure you've submitted your email server and groups.
3. Tick the **Enable eventlog alerts** checkbox.  
   ![sending-report-and-event-log-alerts-10.jpg](/docs/.document360/assets/article_152/image_013.jpg)
4. Select **Add event filter**, select an event from the list of scanned events and click **Ok**. Alternatively, you can manually type an event source and event ID in the pop-up window if you would like to create an alert for an event that hasn't been scanned yet.  
   ![sending-report-and-event-log-alerts-11.jpg](/docs/.document360/assets/article_152/image_014.jpg)  

   Keep in mind that, to keep your database as small as possible, only error events are scanned by default. To generate alerts for non-error events, ensure [the necessary event types are enabled](/docs/scanning-non-error-events) for scanning.
5. Optionally, modify the criteria the event has to meet to generate an alert. Click the pencil-shaped edit button next to the event and select **Add Filter** in the resulting pop-up.![sending-report-and-event-log-alerts-12.jpg](/docs/.document360/assets/article_152/image_015.jpg)
   - **Computer**: NetBIOS name of the computer generating the event.
   - **Domain**: NetBIOS name of the domain/workgroup the event originates from.
   - **EventID**: numeric code identifying the event.
   - **Eventtype**: Error, Warning, Information, FailureAudit or SuccessAudit.
   - **Logfile**: specific log the event belongs to.
   - **Source**: source of the event.
   - **User**: user that was logged into the computer when the event was generated.
   - **Message**: comment included in the event.

     You can use the Like/Not Like operators and the % sign to look for partial matches.
     - "Computer Like LAN%" means any computer whose name starts with LAN.
     - "Computer Like %LAN" means any computer whose name ends in the word LAN.
     - "Computer Like %LAN%" means any computer whose name contains the word LAN.
6. For each event, select the email group you want to send the alerts to.  
   ![sending-report-and-event-log-alerts-13.jpg](/docs/.document360/assets/article_152/image_016.jpg)
7. As soon as a new occurrence of the specified event is scanned on a computer, an email is sent to the mail group of your choice.  
   ![sending-report-and-event-log-alerts-14.jpg](/docs/.document360/assets/article_152/image_017.jpg)  

   Event alerts are best used in combination with [Eventlog Only scanning targets](/docs/scanning-with-an-eventlog-only-scanning-target). Eventlog Only scanning targets allow you to scan event log entries as frequently as once a minute, ensuring that you receive your email alerts near-instantaneously.
