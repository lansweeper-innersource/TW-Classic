<!-- # Scan Chrome OS targets -->
Lansweeper can retrieve data from Chrome OS devices, such as Chromebooks, managed by your Google organization.

For more information about Lansweeper's various scan targets, see the [Scanning Guide](https://www.lansweeper.com/resources/lansweeper-scanning-guide/).

## Prerequisites

- Before scanning your Chrome devices, verify that you meet the scanning requirements specified in [Chrome OS scanning requirements](/classic/docs/chrome-os-scanning-requirements).
- Ensure you save the JSON key that you create in the [step 4: copy service account ID and generate JSON key](/classic/docs/chrome-os-scanning-requirements#heading6).
- Ensure your selected scan server belongs to an installation [capable of encrypting credentials](https://www.lansweeper.com/trust/security/).

## Add Chrome OS as a scan target

1. In your Lansweeper site, go to **Scanning > Targets > Add scanning target**.



2. Choose the scan server to configure the target from the dropdown list.
3. Under **Select a target type**, select **Chrome OS**.  
   
4. Select **Add target**.
5. Enter the following information:
   - Name: Enter a name to identify the target. Must be unique to the installation and can not contain "<" or ">".
   - Username: Enter a valid username. Must be an email address.
   - JSON Key: Enter the JSON key created in [step 4: copy service account ID and generate JSON key](/classic/docs/chrome-os-scanning-requirements#heading6).
   - Schedule: Enter a scan schedule. Can be scheduled to run every few minutes, hours, daily, or weekly. It can also not be run on a schedule.  
     
6. Select **Save and exit**.

## Scan Chrome OS devices

If you do not want to wait for the scan to run as scheduled, you can trigger it immediately.

1. In your Lansweeper site, go to **Scanning > Targets > All targets**.
2. Find your Chrome OS scan target, and select **Scan**.  
   

## View Chrome OS assets

1. In your Lansweeper site, go to **Inventory > Asset types**.
2. Select **Chrome OS** from the list.   
   
