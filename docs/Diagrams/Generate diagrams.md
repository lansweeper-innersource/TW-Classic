<!-- # Generate diagrams -->
All available diagrams are listed in the Diagrams module and are preconfigured based on your installations and IP locations in Lansweeper Sites (in the cloud). To view the content of one of the preconfigured diagrams, you must generate it first.

For more information about Diagrams and its features, see [Diagrams](https://www.lansweeper.com/feature/diagrams/).

On this page:

- [Prerequisites](#prerequisites)
- [View available types of diagrams](#types)
- [Templates](#templates)
  - [Virtual environments](#virtual)
  - [Network topologies](#network)
- [Scope](#scope) 
  - [Inventory](#inventory)
  - [Installation](#installation)
  - [IP Location](#location)
- [Generate a diagram](#generate)
- [Regenerate diagrams](#regenerate)
- [Check diagram generation status](#status)
- [Next steps](#next)

## Prerequisites

Diagrams provide a snapshot of your Installations and Inventory. Therefore they must be configured correctly to provide an accurate picture of your environment. Before generating a diagram, ensure the following prerequisites are met.

- Installations: To confirm your installations are correctly configured and synchronized, go to **Configuration > Installations > All installations** and check the **Sync status**. If your installation is not synced with your Lansweeper Site, related diagrams won’t be listed in the Diagrams module. If your installation is not synced properly and shows sync issues, related diagrams could display outdated content.  
  ![sophie_13-1686147619709.png](/docs/.document360/assets/article_068/image_002.jpg)

- IP location: Ensure you’ve configured your IP locations. To update the IP locations, go to **Inventory > IP locations > Manage locations**. From there, you can edit or add a new IP location.  
  ![sophie_14-1686147619712.png](/docs/.document360/assets/article_068/image_003.jpg)

## View available types of diagrams

Go to **Diagrams**. A list of all available diagrams is shown in **All Diagrams**. These diagrams are organized based on templates and scopes.  
![sophie_15-1686147619720.png](/docs/.document360/assets/article_068/image_004.jpg)

### Templates

Templates dictate how your Inventory’s information is organized within Diagrams. Currently, templates are available for network topologies and virtual environments. These templates are broken down into various scopes.

#### Network topologies

This template is a visual arrangement of the various elements of a communication network. Network diagrams illustrate the components of a computer or telecommunications network, including firewalls, devices, and routers. They also show how network components relate to and interact with each other.

View your network topology diagrams by going to **Diagrams > Network Topology**.  
![network-diagrams.png](/docs/.document360/assets/article_068/image_005.jpg)

#### Virtual environments

This template is a visual arrangement focusing on the virtual resources available in your Inventory. They illustrate virtual components such as hypervisors and virtual machines. Virtual environments also display some of your virtual assets' shared properties, such as clusters, disks, and more. This gives you more context and can help you in decision-making.

View your virtual environment diagrams by going to **Diagrams > Virtual Environment**.  
![sophie_17-1686147619727.png](/docs/.document360/assets/article_068/image_006.jpg)

### Scope

A scope further specifies the information included in your diagrams. Your Inventory configuration directly impacts scopes.

To view your diagrams' scopes, go to **Diagrams** and check the **Scope** column.  
![sophie_18-1686147619732.png](/docs/.document360/assets/article_068/image_007.jpg)

#### Inventory

Diagrams with an Inventory scope provide the broadest overview by including all IT assets that are available in the Inventory. This holistic view lets you see the entire IT estate, offering comprehensive insights and control.

Additionally, diagrams with an Inventory scope offer the capability to [filter by IP location](/docs/filter-assets-on-diagrams).

#### Installation

Diagrams with an Installation scope encompass all assets from a specific installation that has been configured and synced in Lansweeper Site. These diagrams are shown only if more than one installation has been configured in your site. Each additional installation in your site will add a new preconfigured diagram specific to that installation.

Additionally, diagrams with an Installation scope offer the capability to [filter by IP location](/docs/filter-assets-on-diagrams).

#### IP Location

Diagrams with the IP Location scope include the assets connected to a specific IP location configured in your Inventory. These diagrams are affected by how you configure your IP locations. Therefore, another preconfigured diagram will be available if you add another IP Location to your Inventory.

## Generate a diagram

Diagrams must be manually generated before you can view them. To generate a diagram:

1. Ensure your Installations are synchronized and your Inventory is configured correctly.
2. In your Lansweeper Site, go to **Diagrams**.
3. To access your desired diagram, select **All diagrams**, **Network topology**, or **Virtual environment**.
4. From the list, select the diagram you want to generate based on the available types of diagrams.
5. In the **Status** column select ![generate.png](/docs/.document360/assets/article_068/image_008.jpg) to generate a diagram.  
   ![sophie_19-1686147619735.png](/docs/.document360/assets/article_068/image_009.jpg)Alternatively, you can select the name of the diagram, then **Generate Diagram**.  
   ![sophie_20-1686147619737.png](/docs/.document360/assets/article_068/image_010.jpg)

Once a diagram is generated, you can check the diagram's generation status.

## Regenerate diagrams

Diagrams are not automatically updated or generated, so it’s essential to regularly regenerate your diagrams to ensure the information on the diagram is up-to-date. Remember to regenerate your diagram if you’ve updated your Inventory, such as by adding assets or [asset relations](/docs/discover-asset-relations-with-diagrams).

You can regenerate your diagram using two methods:

- Go to **Diagrams**, find your desired diagram, then select ![generate.png](/docs/.document360/assets/article_068/image_011.jpg) under the **Status** column.
- Go to **Diagrams** and open your diagram by selecting the name of your desired diagram. In the bottom right-hand corner, select ![generate.png](/docs/.document360/assets/article_068/image_012.jpg).  
  ![sophie_21-1686147619741.png](/docs/.document360/assets/article_068/image_013.jpg)

## Check diagram generation status

1. Go to **Diagrams**.
2. To view your diagram, select **All diagrams**, **Network Topology**, or **Virtual environment**.
3. From the list, find the diagram you want to check the status of.
4. In the **Status** column, the diagram status is represented by the following icons:

|  |  |  |
| --- | --- | --- |
| **Icon** | **Action** | **Details** |
| sophie_22-1686147619742.png | **Generate/Regenerate** | Clicking on this icon will start generating/regenerating your diagram. This option is available from the diagram list and the diagram itself. |
| sophie_23-1686147619742.png | **Queued** | The queue icon should only be displayed briefly before Lansweeper Sites generates the diagram. This step occurs directly after the diagram generation/regeneration request. |
| sophie_24-1686147619742.png | **Generating** | This icon indicates that the diagram is being built. Depending on the size of your Installation/IP location, this step may take several minutes. |
| sophie_25-1686147619742.png | **Error** | When there are errors in generating your diagram, this icon is displayed. Clicking on it prompts you to regenerate your diagram to avoid further errors. |

## Next steps

Once you’ve generated a diagram, you can [navigate your diagrams](/docs/navigate-diagrams).
