<!-- # Scan mobile devices through VMware Workspace One UEM (powered by AirWatch) -->
AirWatch scanning is a feature introduced in Lansweeper 7.2. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

From version 7.2 onward, Lansweeper is capable of scanning mobile devices that are enrolled in VMware Workspace One UEM (powered by AirWatch). Specifically, Android, iOS (iPhone and iPad), Chrome OS and Windows Phone mobile devices can be scanned. Scanned data includes device name, enrollment date, model, OS version, IMEI, serial number, installed applications, network details, user info and more.

In the Lansweeper console, VMware Workspace One UEM (powered by AirWatch) is referred to as AirWatch.

### Step 1: make sure scanning requirements are met

Before you attempt to scan VMware Workspace One UEM devices, make sure you meet [the scanning requirements](/docs/vmware-workspace-one-uem-powered-by-airwatch-scanning-requirements).

### Step 2: create a scanning target

Submit your VMware Workspace One UEM scanning target by clicking **Add Scanning Target** in the **Scanning > Scanning Targets** section of the console and select the AirWatch scanning type. Enter a name for your scanning target, your username, password, server URL and API key. At the bottom of the window you can set the scanning schedule.  


### Step 3: scan your devices

Wait for your scanning schedules to trigger or initiate an immediate scan by clicking **Scan now** next to the AirWatch scanning target under **Scanning > Scanning Targets**. VMware Workspace One UEM scans do not visually show up in your scanning queue, as they're processed silently in the background.

### Step 4: view scanned data

View scanned data by hovering over the **Assets** menu at the top of the web console and clicking any of the Android, Chrome OS, iPhone, iPad and Windows Phone asset types. This section will take you to an overview of your mobile devices, from where you can click through to those assets' webpages as well. Alternatively, you can view scanned data using the built-in AirWatch reports or custom reports you've created.  

