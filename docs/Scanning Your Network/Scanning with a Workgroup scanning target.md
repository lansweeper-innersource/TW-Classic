<!-- # Scanning with a Workgroup scanning target -->
Due to their reliance on the old SMB1 protocol, scanning targets of the type Workgroup are marked as deprecated. It is strongly advised to use other types of scanning, e.g. [IP Range](/classic/docs/scanning-with-an-ip-range-scanning-target) targets, to scan workgroup assets.

The Workgroup target is an agentless, fully automated scanning target that scans any Windows workgroup submitted by you. The computers must be visible in your Network browser which you can access using Windows Explorer, to be scanned by a Workgroup scanning target.   
Every 15 minutes, the Workgroup target retrieves a list of computers that are visible in the Network browser and that belong to the workgroup you've specified. Newly logged on computers that have not been scanned in the last 20 hours are added to your scanning queue.



You can submit an unlimited number of these targets for scanning. To submit a Workgroup target for scanning, select **Add Scanning Target** in the **Scanning > Scanning Targets** section of the web console and choose the Workgroup scanning type in the resulting pop-up. You'll need to submit the name of the workgroup to be scanned.   
You can submit a description for the target as well. If you have multiple scanning servers, there will be multiple configuration tabs on the **Scanning Targets** page, one for each server. As agentless scanning of Windows computers requires credentials, make sure to submit and map your Windows scanning credentials as well, by following the instructions in [this knowledge base article](/classic/docs/create-and-map-scanning-credentials).

 
