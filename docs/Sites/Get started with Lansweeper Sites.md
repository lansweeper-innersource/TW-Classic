<!-- # Get started with Lansweeper Sites -->

**Learn how to install and configure Lansweeper for efficient IT asset management in just a few simple steps.**

Follow the steps below to install and configure Lansweeper Sites to provide insights in your IT asset environment.

## 1. Verify requirements

To begin, verify your system meets Lansweeper's requirements.

- [Windows domain scanning requirements](/docs/windows-domain-scanning-requirements)
- [IT Agent installation requirements](/docs/install-it-agent-discovery#Requirements)
- [Linux and Unix agentless scanning requirements](/docs/linux-and-unix-agentless-scanning-requirements)
- [Apple Mac scanning requirements](/docs/apple-mac-scanning-requirements)
- [Network device scanning requirements](/docs/network-device-scanning-requirements)

## 2. Install Lansweeper Sites

Follow our training guide to determine which i[nstall path is right for you](https://elearning.easygenerator.com/7735fbac-b4e9-4ea9-8cf9-887fb716bb16/#/). This will help you decide whether you require an easy or advanced installation, and walk you through the installation steps.

You can also review our [trial installation guide](/docs/install-the-lansweeper-trial).

## 3. Add your first credential(s)

Add a credential to access additional information about your assets.

1. In your Lansweeper Site, go to **Discovery > Discovery credentials > Add new credential**.
2. Enter a display name to identify the credential.
3. Choose the vault to store the credential. The vault is located in each hub of a Network Discovery and enables linked sensors to use the credential during discovery.
4. Choose the type that applies to the credential.
5. Enter the credential details.
6. Select **Save and exit**.

**Additional resources:**

- [Bandwidth usage during scanning](/docs/bandwidth-usage-during-scanning)
- [Overview of discovery targets and methods](/docs/comparing-lansweeper-sites-and-lansweeper-on-premises#toc-hId--1328578280)

## 4. Rediscover your targets through Discovery Actions

Now that you've added your first credential, add or update your discovery actions, assign the credential to them, and rerun the discovery action to discover the latest information.

1. Go to **Discovery > Discovery actions > Add new action > Agentless action**.
2. Submit the computer’s IP range, name, or FQDN in the target list.
3. Assign the previously created credential to get more detailed information during the discovery of your asset.
4. Optionally set a trigger for a frequently repeated discovery.
5. Save the action and exit to return to the discovery action list.
6. Wait for your trigger to activate or select **Discover now** next to the discovery action in **Discovery > Discovery actions**.
7. Check for new/updated assets in **Inventory > All assets**.

## 5. Run your dashboard

To ensure your dashboard shows the latest and most accurate data, refresh the reports on the dashboard.

1. Go to **Dashboard > General overview**.
2. Select **Run all board reports** (top-right corner).

This might take a few minutes. Once the dashboard is updated, you can review the various reports to learn more about your environment.

## 6. Get more accurate insights

Want to improve the accuracy of the insights provided? Follow these quick tips:

- **Rediscover your asset:** Check when an asset was last discovered at the top right of its summary page. If needed, select **Rescan asset**.
- **Optimize device ports for discovery:** Ensure the following ports are open to retrieve data from Windows devices:
  - 135/TCP: DCOM to establish the initial WMI session
  - 139/TCP: NetBIOS Session Service
  - 445/TCP: SMB
  - 1025-5000 or 49152-65535: Random ports for WMI data
- **Review general discovery requirements:** Ensure you maximize your discovery results by reviewing the [requirements](/docs/ports-scanned-or-used-by-lansweeper).

**Additional resources:**

- [WMI Access is denied. 0x80070005](/docs/wmi-access-is-denied-0x80070005)
- [RPC server is unavailable. 0x800706BA](/docs/rpc-server-is-unavailable-0x800706ba)
- [Troubleshoot device discovery issues with Network Discovery hub](/docs/install-network-discovery#startnetworkdiscovery)

## 7. Explore Lansweeper Sites

Now that you have Lansweeper Sites installed and configured, you can explore everything it has to offer! For example, you can:

- [Visualise your IT asset data with Diagrams](/docs/diagrams)
- [Learn about our vulnerability risk assessment](/docs/introduction-to-vulnerability-risk-assessment)
