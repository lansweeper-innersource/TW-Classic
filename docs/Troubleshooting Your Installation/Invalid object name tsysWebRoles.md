<!-- # Invalid object name tsysWebRoles -->
The databases of 5.x versions of Lansweeper contain a table called "tsysWebRoles", which stores information on your website access configuration. As the website permissions system changed in Lansweeper 6.0, the tsysWebRoles table was removed and replaced with other fields.

If you update a server hosting the **Lansweeper Server** service to version 6.0 or install the 6.0 service on a new server and connect it to your database, your database is updated by the service to Lansweeper version 6.0 and the tsysWebRoles table is removed. When this happens, it is important that your web console and any other servers hosting a Lansweeper component are updated to version 6.0 as well. If your web console remains on a 5.x version of Lansweeper, it will continue to look for the now non-existent tsysWebRoles table in the database and will throw the error below.



The solution to this error is to update your web console and any other servers hosting a Lansweeper component to the latest Lansweeper release by following [these instructions](/classic/docs/update-lansweeper-on-premises). Running mismatched Lansweeper components can cause other issues as well, so it is always recommended that you update all servers to the same Lansweeper release.
