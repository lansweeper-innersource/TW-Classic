<!-- # Overview of Discovery components and configuration -->

You can set up Lansweeper Discovery by using the discovery configuration menu, which revolves around four components: [discovery actions](#actions), [discovery systems](#systems), [discovery credentials](#credentials), and [discovery groups](#groups).

Discovery actions dictate what and when to scan, discovery systems provide an overview of all linked components bringing in data, and discovery groups allow you to apply uniform settings across multiple systems.

## Discovery actions

Discovery actions instruct which discovery systems should discover what and when. These actions are similar to scan targets used in Lansweeper On-premises installations, albeit more dynamic.

There are three different types of discovery actions, depending on the method used to perform a scan.

### IT Agent-based discovery actions

The IT Agent-based discovery action allows you to configure the discovery settings for IT Agents from within your Lansweeper Site, allowing you to determine what to scan and when the scans should take place.

For more information on setting up IT Agent-based discovery actions, take a look at [Configure IT Agent Discovery](/docs/configure-it-agent-discovery).

### Agent-less discovery actions

The Agent-less discovery action allows you to remotely discover more information about your IT and OT assets with Lansweeper's Network Discovery.

For more information on setting up Agent-less discovery actions, take a look at [Configure Network Discovery](/docs/configure-network-discovery).

### Cloud discovery actions

The Cloud discovery action allows you to discover all assets within your cloud infrastructure. Currently, you can select either Microsoft Azure, Amazon Web Services (AWS), or Google Cloud Platform (GCP) as your cloud provider.

For more information on setting up Cloud discovery actions, take a look at [Configure Cloud Discovery](/docs/configure-cloud-discovery).

## Discovery systems

The Discovery systems menu gives you an overview of all linked components bringing in data to your site. A discovery system is used to decide who or what should run the discovery action.   
To find your discovery systems, go to **Scanning > Discovery systems > All systems**.

There are three types of discovery systems:

- **IT Agent-based**: overview of all linked IT Agent installations
- **Agent-less**: overview of all linked Network Discovery installations
- **Cloud**: overview of all linked Cloud Discovery systems

Cloud systems are automatically added when running a Cloud discovery action and cannot be manually linked.

If you want to link a new discovery system:

1. Go to **Scanning > Discovery systems**.
2. Select **Link Discovery System**.
3. If you haven’t created a linked code yet, select **Create new code**.
4. Use the linking code to add IT Agent Discovery or Network Discovery installations.

To link your site to discovery systems, use the linking code you previously created.

## Discovery credentials

Discovery credentials can be used to add the necessary credentials for conducting accurate, credential-based discoveries using Network Discovery.   
To find your discovery credentials, go to **Scanning > Discovery credentials**.

The **Discovery credentials** view shows you the encrypted credential vaults stored on your Network Discovery Hub systems. You can use these credential definitions in your discovery actions to get more asset details.

## Discovery groups

Discovery groups enable you to apply the same settings to multiple discovery systems, such as auto update behavior.   
For an overview of your discovery groups, go to **Scanning > Discovery groups**.

If you want to add a new discovery group:

1. Go to **Scanning > Discovery groups**.
2. Select **Add new group**.
3. Enter a name and description for the discovery group.
4. Select a time for when the update should take place.
5. Select **Manage systems** to choose which discovery systems to include in the group.
6. Select **Save group**.
