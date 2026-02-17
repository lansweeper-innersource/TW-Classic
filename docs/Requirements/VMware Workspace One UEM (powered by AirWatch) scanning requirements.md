<!-- # VMware Workspace One UEM (powered by AirWatch) scanning requirements -->
From version 7.2 onward, Lansweeper is capable of scanning Android, iOS (iPhone and iPad), Chrome OS and Windows Phone mobile devices that are enrolled in VMware Workspace One UEM (powered by AirWatch) .

This article explains the requirements for VMware Workspace One UEM scanning and how to generate the API key required for scanning. Once you meet the requirements, you can [start scanning your VMware AirWatch environment](/docs/scan-mobile-devices-through-vmware-workspace-one-uem-powered-by-airwatch).

In the Lansweeper console, VMware Workspace One UEM (powered by AirWatch) is referred to as AirWatch.

## Scanning requirements

To scan mobile devices, the following requirements must be met:

- Your Lansweeper installation must be version 7.2 or higher.
- Your Lansweeper license must support VMware Workspace One UEM scanning.
- Your Lansweeper scanning server must have access to the internet.
- Your mobile devices must be enrolled in VMware Workspace One UEM. Enrollment instructions can be found on the VMware website.
- Your mobile devices must be Android, iOS (iPhone or iPad), Chrome OS or Windows Phone devices.
- You must provide Lansweeper with the API key to access the REST API of VMware Workspace One UEM.

## Generating the API key

### Enabling the API

To enable the API for VMware Workspace One UEM follow these steps:

1. Log into the VMware Workspace ONE UEM using your VMware credentials.
2. Go to **Groups & Settings** and select **All settings**.  
   ![Airwatch-Scanning-requirements-3-1.jpg](/docs/.document360/assets/article_174/image_001.jpg)
3. In the following window, select **System > Advanced > API > REST API**. **![Airwatch-Scanning-requirements-1.jpg](/docs/.document360/assets/article_174/image_002.jpg)**
4. Change the setting to **Override**, select **Enabled** for API access and a new service will appear called AirWatch API. The generated API Key will be used later to create the scanning credentials in Lansweeper.

### Adding a new role

1. To add a new role, select **Accounts > Administrators > Roles** and select **Add role**. **![Airwatch-Scanning-requirements-4.jpg](/docs/.document360/assets/article_174/image_003.jpg)**
2. Fill in a name and description for the role.
3. Select API category on the left and enable the following Read permissions: REST APIs for applications, REST API to provide access to custom attributes, REST APIs for device management, REST APIs for group management and REST APIs for enrollment user accounts.   
   ![Airwatch-Scanning-requirements-5.jpg](/docs/.document360/assets/article_174/image_004.jpg)
4. Go to**Accounts**, then **Administrators** and select **List View**. Select the edit button for the user you want to assign the created role.  
   ![Airwatch-Scanning-requirements-6.jpg](/docs/.document360/assets/article_174/image_005.jpg)
5. Under **Roles**, select **Add role**. Fill in Main OG for the Organization Group, and finally the previously created role under Role and select **Save**.

![Airwatch-Scanning-requirements-7.jpg](/docs/.document360/assets/article_174/image_006.jpg)
