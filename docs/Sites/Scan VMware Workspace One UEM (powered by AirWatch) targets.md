<!-- # Scan VMware Workspace One UEM (powered by AirWatch) targets -->
Lansweeper can scan VMware Workspace One UEM (powered by AirWatch) devices including Android, iOS (iPhone and iPad), Chrome OS, and Windows Phone mobile devices. Scanned data includes the device name, enrollment date, model, OS version, IMEI, serial number, installed applications, network details, user info, and more.

For more information about Lansweeper's various scan targets, see the [Scanning Guide](https://www.lansweeper.com/resources/lansweeper-scanning-guide/).

## Prerequisites

- Verify that you meet [VMware Workspace One UEM scanning requirements](/docs/vmware-workspace-one-uem-powered-by-airwatch-scanning-requirements).
- Ensure you save the API key created in Generating the API key.
- Ensure your selected scan server belongs to an installation [capable of encrypting credentials](https://www.lansweeper.com/trust/security/).

## Add VMware Workspace One UEM as a scan target

In Lansweeper Sites, VMware Workspace One UEM (powered by AirWatch) is referred to as AirWatch.

1. In your Lansweeper Site, go to **Scanning > Targets > Add scanning target**.



2. Choose the scan server to configure the target from the dropdown list.
3. Under **Select a target type**, select **AirWatch**.  
   
4. Select **Add target**.
5. Enter the following information:
   - Name: Enter a name to identify the target. Must be unique to the installation and can not contain "<" or ">".
   - Username: Enter a valid username. Must not contain / : ; , ? " < > | [ ] +.
   - Password: Enter a password.
   - Server URL: Enter the server URL.
   - API key: Enter or paste the API key created in Generating the API key.
   - Schedule: Create a scan schedule. Can be scheduled to run every few minutes, hours, daily, or weekly. It can also not be run on a schedule.  
     
6. Select **Save and exit**.

## Scan VMware Workspace One UEM devices

If you do not want to wait for the scan to run as scheduled, you can trigger it immediately.

1. In your Lansweeper site, go to **Scanning > Targets > All targets**.
2. Find your AirWatch scan target, and select **Scan**.



## View VMware Workspace One UEM assets

1. In your Lansweeper site, go to **Inventory > Asset types**.
2. Select your VMware Workspace One UEM (powered by AirWatch) device, which could be an **Android**, **Chrome OS**, **iPhone**, or **Windows phone**.  
   
