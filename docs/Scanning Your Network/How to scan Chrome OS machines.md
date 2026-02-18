<!-- # How to scan Chrome OS machines -->
Chrome OS scanning is a feature introduced in Lansweeper 7.2 You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

Not all Lansweeper licenses include this feature. If your particular license does not support this feature, please visit [this page](https://www.lansweeper.com/chromebook-scanning/) for more information.

From version 7.2 onward, Lansweeper can retrieve data of Chrome OS (e.g. Chromebook) devices managed by your Google organization. Once scanned, these assets can be accessed through the **Assets** menu in your web console. Scanned data includes basic system information, disk info and recently logged in users.

This article explains how to scan your Chrome OS devices in three steps.



### Step 1: make sure you meet the scanning requirements

Before scanning your Chromebook devices, verify that you meet the scanning requirements. More information on Lansweeper's Chrome OS scanning requirements can be found in [this knowledge base article](/classic/docs/chrome-os-scanning-requirements).

### Step 2: add your scanning target

To add your Chrome OS scanning target, click **Add Scanning Target** under the **Scanning > Scanning Targets** section of the web console.  


Select **Chrome OS** from the drop-down menu, submit a credential name, username and the JSON key. The name field is for your reference, the username field requires a user with the Services Admin role in your Google environment. The JSON key is the credential you created in step 1. Configure the scanning schedule and click **Ok** to create your scanning target.  

### Step 3: view your Chrome OS assets

When the scanning target has been added, it will immediately start scanning. You can view your scanned assets by selecting the Chrome OS asset type under the **Assets** tab. 
