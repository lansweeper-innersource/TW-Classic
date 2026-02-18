<!-- # Scan an Azure cloud environment -->
Lansweeper is capable of scanning resource groups and virtual machines hosted on the Microsoft Azure cloud computing platform. An asset is created for each resource group and for each virtual machine. Scanned data includes resource groups, virtual machines and their types, disks, extensions, IDs, network interfaces, regions, security groups, subnets, tags and more.

## Scan a resource or virtual machine from Microsoft Azure

1. Make sure you meet [the Azure scanning requirements](/classic/docs/azure-scanning-requirements).
2. Submit your Azure subscription for scanning by clicking  **Add Scanning Target** in the  **Scanning > Scanning Targets**  section of the web console. If you have multiple scanning servers, there will be a separate configuration tab for each server. When submitting your subscription, you will be asked to specify a scanning schedule. You can filter the scanning target so that only specific resource groups are scanned, by submitting the groups with the  **Add Resource Group Filter**  button.

   

   
3. Submit your Azure Active Directory (tenant) ID, application ID and application password as a credential in the  **Scanning > Scanning Credentials**  section of the web console.

      
   You can use the same credential for all Azure subscriptions by editing the Global Azure credential or submit a non-global credential with the  **Add new Credential**  button. 
4. If the credential you set up is not a global credential, map the credential to your subscription by clicking the  **+ Credential**  button next to the subscription on the same page.

   
5. Wait for your scanning schedules to trigger or initiate an immediate scan by clicking  **Scan now** next to the Azure target under  **Scanning > Scanning Targets**. Azure scans do not visually show up in your scanning queue, as they're processed silently in the background.  
   
6. View scanned data by hovering over the **Assets** menu at the top of the web console and clicking Azure asset types. This takes you to overviews of your resource groups and virtual machines, from which you can click through to those assets' webpages as well.  
   

   Alternatively, you can view scanned data using built-in or custom reports or using the Azure dashboard widget.

   
