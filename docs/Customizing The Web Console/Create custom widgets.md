<!-- # Create custom widgets -->
Creating a custom data widget in Lansweeper On-premises is a straightforward process, especially when displaying data like SQL query results that don't require user input.

In this article, we'll walk you through building a basic widget. We'll start from basic data retrieval, and then explore enhancing your widget with images, links, and additional functionality such as auto-refresh.

If you want to create a widget using external sources, you may need to update your appsettings. For more information, see [Secure your Lansweeper On-premises setup](/classic/docs/secure-your-lansweeper-on-premises-setup).

## Create a custom widget

Whether you're showcasing asset groups or providing quick links to configuration pages, these steps will help you craft an informative and visually appealing widget for your Lansweeper setup.

### Custom data widget

The simplest widgets to create are those that display data, such as the results of a SQL query, without needing user input.

In this first example, we'll demonstrate how to create a basic widget and add it to Lansweeper On-prem.

1. Create or copy an aspx-page in the `/WidgetsCustom/` folder.  
     
   The first part of the aspx-file should always look something like this:  

   ```
   <%@ Page Language="C#" AutoEventWireup="true" Inherits="LS.BaseControl" %>
   <%@ Import Namespace="System.Data" %>
   <%@ Import Namespace="LS.Enums" %>
   <%@ Import Namespace="LS" %>
   <% Response.CacheControl = "no-cache";%>
   <% Response.AddHeader("Pragma", "no-cache"); %>
   <% Response.Expires = -1; %>
   <% LS.User.Current().CheckUserWebsiteAccess(); %>
   ```
2. Next, add the look up of data you want to show.   
   For example if you want to show all existing asset groups, and the amount of assets assigned to each group, you can use this line of code:  

   ```
   var dsAssets = DB.ExecuteDataset("SELECT tblAssetGroups.AssetGroup, tblAssetGroups.AssetGroupid, COUNT(tblAssetGroupLink.AssetID) AS Count FROM tblAssetGroups INNER JOIN tblAssetGroupLink ON tblAssetGroups.AssetGroupID = tblAssetGroupLink.AssetGroupID GROUP BY tblAssetGroups.AssetGroup, tblAssetGroups.AssetGroupid");
   ```
3. Finally, check if any data was gathered. You can then visualize the data in a table:  

   ```
   if (dsAssets.Rows.Count != 0)
   {%>
   <table width="100%" border="0" cellpadding="0" cellspacing="0">
   <% foreach (DataRow myrow in dsAssets.Rows)
   {%>
   <tr>
   <td align="left" valign="top">
   <%:myrow["AssetGroup"]%>
   </td>
   <td align="right" valign="top">
   <%:myrow["Count"]%>
   </td>
   </tr>
   <% }%>
   </table>
   <%}%>​
   ```

### Create a visual widget

In addition to displaying data, you can enhance your widget by including images or links to other pages. This not only makes the widget more visually appealing, but also adds extra functionality. You can use images from the existing `/images/` folder or add your own images to the `/WidgetsCustom/images` folder.

1. Provide the correct path in an image tag, ensuring all paths begin with the prefix `<%=ResolveUrl("~/")%>`.  
   For example, to add an image in front of each row in your table, you could insert the following code into the table row:  

   ```
   <td width="10" align="left" valign="top">
   <img src="<%=ResolveUrl("~/")%>images/tag_green.png" width="16" height="16" hspace="2" vspace="2" />
   </td>​
   ```
2. A useful link for this widget would direct users to the page where they can manage asset groups, including adding or removing assets. However, it's important to verify the user's permissions, as only certain roles can make adjustments to asset groups. The code snippet below demonstrates how to check the user's web role before displaying the link:

   ```
   <%if (LS.User.Current().IsInRole(Permission.EditConfiguration))
   {%><div style="float:right">
   <a href="<%=ResolveUrl("~/")%>configuration/AssetGroups/" class="sml">config</a>
   </div><% } %>​
   ```
3. For a more advanced link, you could link to a report that lists all assets with a specific group. To achieve this, use the database object "web50getassetgroups" along with the asset group ID:

   ```
   <td align="left" >
   <a href="<%=ResolveUrl("~/")%>report.aspx?det=web50getassetgroups&@assetgroupid=<%:myrow["AssetGroupid"]%>&title=Assets in group <%= HttpUtility.UrlEncode(myrow["AssetGroup"].ToString()) %>"><%: myrow["AssetGroup"] %></a>
   </td>​
   ```
4. There are additional improvements you can make to your widget, such as changing the title displayed at the top of the widget, or making the widget refresh every few seconds. Auto-refresh is particularly useful for widgets displaying frequently changing data, like the scanning status widget.   
   To change the title, use the following:

   ```
   <script type="text/javascript">
   $('#WTitle<%=TabControlID %>', window.top.document).text("Just a simple test widget");
   </script>​
   ```

   For auto-refresh to function properly, ensure that your control inherits from `LS.BaseControl` in the heading:  

   ```
   <%=AutoRefresh(10) %>​
   ```

### Finalize your custom widget

Putting all previous steps together gives us the following:

```
<%@ Page Language="C#" AutoEventWireup="true" Inherits="LS.BaseControl" %>

<%@ Import Namespace="System.Data" %>

<%@ Import Namespace="LS.Enums" %>

<%@ Import Namespace="LS" %>

<% Response.CacheControl = "no-cache";%>

<% Response.AddHeader("Pragma", "no-cache"); %>

<% Response.Expires = -1; %>

<% LS.User.Current().CheckUserWebsiteAccess(); %>



<%var dsAssets = DB.ExecuteDataset("SELECT tblAssetGroups.AssetGroup, tblAssetGroups.AssetGroupid, COUNT(tblAssetGroupLink.AssetID) AS Count FROM tblAssetGroups INNER JOIN tblAssetGroupLink ON tblAssetGroups.AssetGroupID = tblAssetGroupLink.AssetGroupID GROUP BY tblAssetGroups.AssetGroup, tblAssetGroups.AssetGroupid");



if (dsAssets.Rows.Count != 0)

{%>

<table width="100%" border="0" cellpadding="0" cellspacing="0">



<% foreach (DataRow myrow in dsAssets.Rows)

{%>

<tr>

<td width="10" align="left" valign="top">

<img src="<%=ResolveUrl("~/")%>images/tag_green.png" width="16" height="16" hspace="2" vspace="2" />

</td>

<td align="left" ><a href="<%=ResolveUrl("~/")%>report.aspx?det=web50getassetgroups&@assetgroupid=<%:myrow["AssetGroupid"]%>&title=Assets in group <%= HttpUtility.UrlEncode(myrow["AssetGroup"].ToString()) %>"><%: myrow["AssetGroup"] %></a></td>

<td align="right" valign="top">

<%:myrow["Count"]%>
```
