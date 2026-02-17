<!-- # Lansweeper Discovery -->

Lansweeper Discovery is an all-in-one asset discovery solution that identifies IT, OT, and cloud assets and catalogues them into a single inventory. This streamlines asset and user management, allowing you to manage your entire asset inventory through Lansweeper Sites.

On this page:

- Benefits
- What’s included in Lansweeper Discovery
  - Network Discovery (IT & OT Sensor)
  - IT Agent Discovery
  - Cloud Discovery
- Lansweeper Discovery vs. Lansweeper On-premises scanning
- Frequently asked questions

## Benefits

- **Comprehensive discovery**: Gain insights into your network by discovering all IT, OT, and cloud assets, as well as expanded data such as fingerprints (enriched device identifiers), open ports, and Mac users.
- **Enhanced control**: Control when and where your assets are scanned, providing greater flexibility and management over your discovery processes.
- **Future-proofed**: Use lighter, more secure discovery systems that accommodate both cloud and on-premises environments.
- **Usability**: Download Lansweeper Discovery on Windows, Linux, or Mac. Enjoy automatic updates and reduced maintenance time.

## What’s included in Lansweeper Discovery

Lansweeper Discovery comprises three discovery systems, each with unique capabilities and features.

Each discovery system shares similar configuration components, which you can learn more about in [Discovery configuration](/docs/overview-of-discovery-components-and-configuration).

![Lansweeper-Discovery-Diagram.png](/docs/.document360/assets/article_308/image_002.jpg)

Depending on your requirements and specific needs, you may want to install a specific discovery system, or a combination of multiple discovery systems. The table below provides additional information to help guide your decision.

|  | Network Discovery | IT Agent Discovery | Cloud Discovery |
| --- | --- | --- | --- |
| **Summary** | Discover all IT assets in your network | Collect all details of the computers that have IT Agent Discovery installed and running as a background service or daemon | Identify and catalog all assets within your cloud infrastructure |
| **Asset reach** | Tracks both the machine running Network Discovery and remotely discovers IT assets | Tracks local computers where IT Agent Discovery is running | Tracks cloud environments with authentication set up |
| **Credentials** | Requires credentials to remotely get all asset details | Does not require credentials | Requires authentication to access cloud environments |
| **Network access** | Requires specific ports to be open on the assets to discover.  See [Ports scanned or used by Lansweeper](/docs/ports-scanned-or-used-by-lansweeper) for more information. | Few connectivity requirements.  See [Install IT Agent](/docs/install-it-agent-discovery#Requirements) for more information. | No specific network access required |

### Network Discovery (IT & OT Sensor)

Discover your network's IT and OT assets and view them in a single inventory.

- [Install Network Discovery](/docs/install-network-discovery)
- [Configure Network Discovery](/docs/configure-network-discovery)

### IT Agent Discovery

Discover comprehensive data on your local devices using a lightweight scanning agent.

- [Install IT Agent Discovery](/docs/install-it-agent-discovery)
- [Configure IT Agent Discovery](/docs/configure-it-agent-discovery)

### Cloud Discovery

Identify and catalogue all assets within your cloud infrastructure, including virtual machines, storage buckets, databases, and more.

- [Introduction to Cloud Discovery](/docs/introduction-to-cloud-discovery)
- [Set up Cloud sensor access](/docs/set-up-cloud-discovery-access)
- [Configure Cloud Discovery](/docs/configure-cloud-discovery)

## Lansweeper Discovery vs. Lansweeper On-premises scanning

Lansweeper On-premises scanning consists of LsAgent, LsPush and the OT scanne and requires a Lansweeper On-premises installation.   
Lansweeper Discovery is the successor of Lansweeper On-premises and is fully supported by Lansweeper Sites.

Depending on your situation and your needs, you may want to install a specific discovery system, or perhaps a combination of multiple discovery systems.   
For a full comparison of their capabilities, check out [Comparing Lansweeper Sites and Lansweeper On-premises](/docs/comparing-lansweeper-sites-and-lansweeper-on-premises), which provides more information to aid you in your decision

## Frequently asked questions

If you have any questions about Lansweeper Discovery, check out our frequently asked questions for [Network Discovery](/docs/network-discovery-frequently-asked-questions), [Cloud Discovery](/docs/cloud-discovery-frequently-asked-questions), and [IT Agent Discovery](/docs/it-agent-discovery-frequently-asked-questions).
