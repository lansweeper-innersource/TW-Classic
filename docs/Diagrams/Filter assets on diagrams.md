<!-- # Filter assets on diagrams -->
Filters allow you to choose which objects are displayed on your diagram based on categories such as asset type, IP address, and state.

For more information about Diagrams and its features, see [Diagrams](https://www.lansweeper.com/feature/diagrams/).

Filters are kept in memory for the user handling them so they are still active when the diagram is consulted later.

To filter your assets:

1. In your Lansweeper Site, go to **Diagrams** and select the diagram you want to filter.
2. Select **Filters** .
3. Select the filter category you desire, including if the filtered items should be reduced or hidden.

Your diagram is automatically updated.

You can also select **Reset filters to default values** to apply the default values suggested by the diagram type.  


## Filter categories

### Asset type

Filter by the types of assets available on your diagram

Quickly select or unselect all your asset types with **Select all** or **Unselect all**.

To find specific asset types:

1. Scroll through the list of asset types or use the search bar to locate a specific type.
2. Toggle the type **On** or **Off**.
3. Decide to hide or reduce filtered items.



### IP address

Filter your assets based on their IP address.

Objects without an IP address that have a known relationship with an asset are considered to belong to the IP location of the related asset. They are displayed on the diagram if the filter allows displaying the related asset.

It is not possible to filter by IP address on diagrams where the scope is set to [IP location](/docs/generate-diagrams#location).

You can filter your assets by IP location or by IP range.

To filter by IP location:

1. Select **By IP Location**.
2. Either:
   - Quickly select or unselect all your IP locations with **Select all** or **Unselect all**.
   - Scroll through the list of IP locations or use the search bar to locate a specific location, then toggle the location **On** or **Off**.
3. Decide to hide or reduce filtered items by selecting **Reduced** or **Hidden**.



To filter by IP Range:

1. Select **By IP Range**.
2. Select either:
   - **Enter Start IP Address and End IP Address**: Enter the start and end IP addresses.
   - **Ender a range of IP Addresses**: Enter the IP range or a CIDR block by using - or / to define the location.
3. Decide to hide or reduce filtered items by selecting **Reduced** or **Hidden**.

### State

Filter your assets depending on their state, such as active or broken. You can update your states in the Inventory.

If you want to filter all assets based on their state, select **Select all** or **Unselect all**.  


To find specific asset states:

1. Scroll through the list of states or use the search bar to locate a specific state.
2. Toggle the state **On** or **Off**.
3. Decide to hide or reduce filtered items by selecting **Reduced** or **Hidden**.

### Filtered items

Decide how you want to display your filtered objects. This setting can be individually configured for each filter category. You can filter your items based on the following settings:

- **Hidden**: If you select the hidden option, the assets are removed from your diagram. This does not remove them from the scope of your diagram; filtered assets are just not displayed. If you hide your filtered assets, their relations to other assets are also not shown.
- **Reduced**: If you select the reduced option, your assets are still displayed on the diagram but in a miniature form without any of their information displayed. This option allows you to continue to view the relations between your filtered and unfiltered assets, which helps to better understand your network without overwhelming your diagram with too much information.



## Next steps

Once you’ve found and filtered your assets, you can [personalize your diagrams](/docs/personalize-diagrams).
