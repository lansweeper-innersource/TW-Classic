<!-- # Scan an AWS cloud environment -->
This page is for Lansweeper Classic. For Lansweeper Sites (in the cloud), see [Scan an AWS region](/docs/scan-an-aws-region).

![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_212/image_001.jpg) **This page explains how you can expand your arsenal of AWS scanning tools by using Lansweeper to scan VPCs and instances hosted on the AWS cloud platform.**

---

AWS scanning is a feature introduced in Lansweeper 7.1. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

From version 7.1 onward, Lansweeper is capable of scanning VPCs and instances (virtual machines) hosted on the Amazon Web Services (AWS) cloud platform. An asset is created for each VPC that has instances connected to it and for each instance as well. Any EC2-VPC environment can be scanned. Scanned data includes VPCs, instances and their types, AMIs, elastic GPUs, hosts, IDs, network interfaces, product codes, regions and availability zones, security groups, states, subnets, tags, volumes and more.

![how-to-scan-an-aws-cloud-environment-1.jpg](/docs/.document360/assets/article_212/image_002.jpg)

## Scan a VPC or virtual machine from AWS

1. Make sure you meet [the AWS scanning requirements](/docs/aws-scanning-requirements).
2. Submit your AWS credential in the **Scanning > Scanning Credentials** section of the web console. You can use the same credential for all AWS regions by editing the Global AWS credential or submit a non-global credential with the **Add new Credential** button. You will be asked for your AWS access key and secret key, which you generated while following the instructions in [the AWS scanning requirements article](/docs/aws-scanning-requirements).

   ![menu-scanning-scanning-credentials.jpg](/docs/.document360/assets/article_212/image_003.jpg)

   ![how-to-scan-an-aws-cloud-environment-4.jpg](/docs/.document360/assets/article_212/image_004.jpg)
3. Submit your AWS regions for scanning by clicking **Add Scanning Target** in the **Scanning > Scanning Targets** section of the web console. If you have multiple scanning servers, there will be a separate configuration tab for each server. When submitting your regions, you will be asked to specify a scanning schedule and select a scanning credential.

   ![menu-scanning-scanning-targets.jpg](/docs/.document360/assets/article_212/image_005.jpg)

   ![how-to-scan-an-aws-cloud-environment-10.png](/docs/.document360/assets/article_212/image_006.jpg)

   If you have multiple AWS accounts with overlapping regions, you can scan all of your accounts by submitting a scanning target for each and mapping the appropriate credential to each target. Using multiple targets to scan AWS accounts with overlapping regions is supported from Lansweeper 9.2 onward.
4. Wait for your scanning schedules to trigger or initiate an immediate scan by clicking **Scan now** next to the AWS target under **Scanning > Scanning Targets**. AWS scans do not visually show up in your scanning queue, as they're processed silently in the background.

   ![how-to-scan-an-aws-cloud-environment-6.jpg](/docs/.document360/assets/article_212/image_007.jpg)
5. View scanned data by hovering over the Assets menu at the top of the web console and clicking AWS asset types. This takes you to overviews of your VPCs and instances, from which you can click through to those assets' webpages as well.

   ![how-to-scan-an-aws-cloud-environment-7.jpg](/docs/.document360/assets/article_212/image_008.jpg)

   Alternatively, you can view scanned data using built-in or custom reports or using the AWS dashboard widget.

   ![how-to-scan-an-aws-cloud-environment-8.jpg](/docs/.document360/assets/article_212/image_009.jpg)

   ![how-to-scan-an-aws-cloud-environment-9.jpg](/docs/.document360/assets/article_212/image_010.jpg)
