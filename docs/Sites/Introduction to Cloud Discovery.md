<!-- # Introduction to Cloud Discovery -->

Lansweeper’s Cloud Discovery identifies and catalogs all assets within your cloud infrastructure, includingvirtual machines, storage buckets, databases, and more.

Managing cloud environments manually has become increasingly challenging due to their growing size and complexity. Lansweeper’s cloud asset inventory service forms the foundation of your security, compliance, and resource optimization strategies. Achieving full visibility of your IT estate, including cloud assets, is crucial for promptly identifying and addressing security risks.

## Scan your cloud infrastructure

You can start discovering your cloud assets by setting up Cloud-type discovery actions. Discovery actions define which discovery systems (hub or sensors) should discover what and when. These actions function similarly to scan targets used in Lansweeper On-premises installations.

Cloud Discovery uses the Cloud discovery action to scan for assets in your cloud infrastructure. Currently, you can select either Microsoft Azure, Amazon Web Services (AWS), or Google Cloud Platform (GCP) as your cloud provider. Additionally, you can collect asset data using Intune, and retrieve organization data through Microsoft 365.

Lansweeper retrieves all available fields exposed by the manufacturer's API. For more details, refer to the following resources:

- Microsoft Azure: [Virtual Machines - Get - REST API (Azure Compute)](https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/get?view=rest-compute-2024-07-01&tabs=HTTP), and similar references for other Azure resources.
- Amazon Web Services (AWS): [Data Types - Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Types.html) and [Data Types - RDS Data API](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_Types.html), along with similar references for other AWS resources.
- [Google Cloud Platform (GCP)](https://cloud.google.com/storage/classic/docs/json_api/v1)
- [Microsoft Intune](https://learn.microsoft.com/en-us/graph/api/intune-devices-manageddevice-get?view=graph-rest-1.0)
- [Microsoft 365](https://learn.microsoft.com/en-us/graph/overview-major-services?view=graph-rest-1.0)

Before scanning your cloud provider, you’ll first need to configure your infrastructure to allow Cloud Discovery to access your environment. Depending on your cloud provider, these steps may differ, but setting up authentication to your cloud environment is crucial.

For more information on preparing your cloud environment, see [Set up Cloud Discovery access](/classic/docs/set-up-cloud-discovery-access).

For an overview of all discoverable resources, see [Discover workloads](/classic/docs/discover-workloads "Discover workloads").

## Manage your cloud assets

After scanning your cloud environment, you can view your cloud assets by navigating to **Inventory > Cloud assets** in your Lansweeper Site. The default view focuses on the most useful properties of your cloud assets: the cloud provider, any cloud tags or labels, tenant and environment information, and the region.   
You can quickly find your cloud assets by searching for any value related to the asset, including tags and labels.

You can also try out various configuration options to organize your assets in a way that best suits your environment. For more information on how you can manage your inventory, take a look at [View assets](/classic/docs/view-assets).

Since multiple cloud providers are supported, the **Tenant/Org.** column groups the Azure Tenant, AWS Organization, and GCP Organization, while the **Environment Name** column groups the Azure Subscription, AWS Account and GCP Project.

While scanned cloud properties are not editable in this phase of Cloud Discovery, cloud assets can be edited to configure any custom fields, asset relations or asset groups.

### Cloud tags and labels

Cloud tags and labels are a powerful feature of the cloud inventory, allowing you to group cloud assets from any provider under a single business application concept. For example, a business application using cloud resources from both Azure and GCP environments can be visualized in a single view in Lansweeper Sites.

Cloud tags and labels are configured in the cloud providers' portals, and are not assigned to cloud assets in Lansweeper Sites.

Select any cloud tag or label to open an inventory view showing all cloud assets assigned that tag or label. Cloud assets with multiple cloud tags or labels will display them as a clickable list.



Make sure to consistently follow your organization’s capitalization policy when adding cloud tags or labels to your assets, as cloud providers may have different policies.
