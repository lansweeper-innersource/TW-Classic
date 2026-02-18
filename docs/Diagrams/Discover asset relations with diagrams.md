<!-- # Discover asset relations with diagrams -->
Gain deeper insights into your IT environment by visualizing the relationships between your assets.

For more information about Diagrams and its features, see [Diagrams](https://www.lansweeper.com/feature/diagrams/).

Remember that Diagrams currently only display IT assets that are synced in your Lansweeper Site (in the cloud). OT assets, software, and users are not yet displayed. You can also create relations from diagrams. To remove relations, go to the asset’s **Summary** page and edit the relation.

On this page:

- Types of relations

- Discovered SNMP relations
- Other discovered relations
- Relations created manually

- How are relations displayed?
- Discovered relations
- Manual relations
- Logical groups

- Assets with a shared IP location
- Locations
- Physical machines hosting virtual machines
- Shared properties on virtual templates

- Groups of relations
- Types of relationship indicators
- Handle orphan assets
- Add relations
- Next steps

## Types of relations

Your diagrams can display three types of relationships.

To control which relations are displayed on your diagram, see [Personalize diagrams](/classic/docs/personalize-diagrams "Personalize diagrams").

### **Discovered SNMP relations**

SNMP relations are discovered automatically based on the network information available in your Inventory. For Discovered SNMP relations to be found, your SNMP credentials must be configured.

To configure SNMP credentials, go to **Scanning** > **Credential Vault** > **My credentials** > **Add new credential**. Select **SNMP** from the credential type list and enter the required information.

You may also want to expose network interface uplinks. By default, if Lansweeper discovers more than 4 devices connected to a switch port, the port will be deemed an uplink. An uplink is a port on a router or switch that is designed to connect to another router, switch, or internet access device. For more information, see [Manage network interface uplinks](/classic/docs/manage-network-interface-uplinks "/classic/docs/manage-network-interface-uplinks").

To learn more about a discovered SNMP relation, select the link to display the relation type, speed, and information port.

By configuring your SNMP credentials correctly, you can improve the discovery and display of these relationships on your diagrams. This limits the number of orphan assets and the number of relations you would have to create manually.

### **Other discovered relations**

Other discovered relations are created by Lansweeper Sites (shown as Asset Relations) based on your scanning settings, mainly from Windows Management Instrumentation (WMI). These relations are stored in your Inventory.

To learn more about this type of discovered relation, select the link to display the relation type, start date, end date, and comments.

#### Printers and print server relations

Diagrams can also display relationships between Print Servers and their printers. This configuration assumes that the **PortName** field (in the Print Server list of printers) contains the IP address of the printer. 

Printers in the Print Server list with a **PortName** matching the IP address of a printer in the network will automatically connect to the Print Server in the diagrams.

These relations are displayed automatically and cannot be removed or manually modified.

### **Relations created manually**

Manual relations are created by users in the Inventory through Asset Relations.

To learn more about a manual relation, select the link to display the relation type, start date, end date, and comments.

## How are relations displayed?

The way relations are displayed depends on the type of relation.

When you select an asset, its relations are highlighted in orange.  


### Discovered SNMP relations

Discovered SNMP relations are represented by a solid blue line with a small dot.  


### Other discovered relations and manual relations

Other discovered relations and relations created manually are represented by a solid blue line with a big dot and icon that relates to the type of relation.  


### Logical groups

Some relations between assets are displayed as logical groups to simplify how you view your diagrams. Relations are shown as logical groups in the following scenarios:

- Assets with a shared IP location
- Location asset type
- Physical machines hosting virtual machines
- Shared properties on Virtual Environment templates

#### Assets with a shared IP location

If you've configured IP locations in your Inventory, your assets will be grouped by these locations, making it easier to read your IT estate.

You can choose not to display IP Locations on your diagram by going to **Settings > Informational** and not selecting the **IP Location** option in the **Grouping behavior** section.



To update the IP locations, go to **Inventory > IP locations > Manage locations**. From there, you can edit or add a new IP location.

If your diagram contains a large number of assets and relationships, grouping by IP location will be activated by default to preserve the overall performance of your diagram.

#### Location asset type

If you have a Location asset type within the scope of your diagram, it will be displayed as a logical group, with the connected assets appearing within the group.

You can choose to not display Location asset types on your diagram by going to **Settings > Informational** and not selecting the **Location (asset)** option in the **Grouping behavior** section.  


To add an asset to a Location, add a relation to your asset. For **Asset**, select the asset with a Location asset type, then for **Relation type** select the **Is located in** option.  


Regenerate your diagram to ensure the asset is displayed within the Location’s logical group.

#### Physical machines hosting virtual machines

Physical assets hosting virtual machines are also displayed as logical groups.  


#### Shared properties on virtual templates

For [Virtual Environment templates](/classic/docs/generate-diagrams#virtual "Virtual Environment templates"), some shared properties are displayed as logical groups. These properties are:

- DataCenters
- ESXi Clusters
- DatastoreClusters
- Datastores
- Disks



## Groups of relations

When multiple relations are detected between two assets or groups of assets, these are displayed grouped together, indicating the number of relations detected. To view details of these relations, select the label.



### Types of relationship indicators

Your diagrams can display relationships in two distinct ways, enhancing your understanding of how assets are connected within your IT estate.

#### Solid line relations

Solid line relations represent direct connections between the objects currently visible on your diagram. These connections are essential for understanding your technology assets' immediate network and dependencies.



#### Dotted line relations

Dotted line relations indicate that the connection involves one or more "child" objects of the entities currently displayed, representing underlying or secondary relationships within your IT infrastructure.



To reveal the objects involved in these dotted line relations, select the dotted line. This will automatically expand the diagram to display the child objects and their connections, offering insights into the deeper layers of your diagram.

## Handle orphan assets

When an asset has no known relationship with other assets, it is identified as an orphan asset.

To minimize the occurrence of orphan assets, it's crucial to accurately configure your SNMP credentials and properly set up your uplink settings.

To view your orphan assets within a diagram:

1. Go to **Diagrams** and select the diagram of your choice.
2. On the diagram, select 



You can search for specific orphan assets by name, IP address, or MAC address from the Orphan Assets list.  


You can also add new relations from the Orphan Assets list.

To add a new relation to the asset, select **> Add new relation**.  


Once a relationship has been manually added to an orphan asset, it will be removed from the list and included in the diagram.

After you add a new relation, [regenerate the diagram](/classic/docs/generate-diagrams#regenerate) to ensure it is displayed correctly.

## Add relations

You can add relations to your assets right from your diagram. To add a relation:

1. Go to **Diagrams** and select the diagram of your choice.
2. Find the asset you want to edit. If you can’t easily see the asset, try [searching](/classic/docs/find-assets-with-integrated-search-on-diagrams) or [filtering](/classic/docs/filter-assets-on-diagrams) for it.
3. Select  in the top right corner of your asset, then select **Add new relation**.  
   
4. In the pop-up window, enter the information required.
5. Select **Add new relationship**.

Your new manual relation is displayed. Select the link to see the manual relation details.

Even if your relation is already created in your Inventory, after you add a new relation [regenerate the diagram](/classic/docs/generate-diagrams#regenerate) to ensure it is displayed correctly.

## Next steps

Once you’ve discovered asset relations, [find](/classic/docs/find-assets-with-integrated-search-on-diagrams) and [filter assets on your diagram](/classic/docs/filter-assets-on-diagrams).
