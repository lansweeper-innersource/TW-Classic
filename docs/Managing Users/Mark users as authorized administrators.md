<!-- # Mark users as authorized administrators -->
The **Reports** menu of the Lansweeper Classic web console includes a built-in report called "Computer: Unauthorized Administrators" that lists unauthorized members of your computers' local administrator group. By default, all local and domain users that are in the local admin group on your computers are listed in this report, except for built-in local admins. You can then mark certain users as authorized to narrow down the report results further and find users who should not in fact be administrators on their computers.  


To mark a user as an authorized administrator and remove them from the report results:

1. Browse to the **Configuration > User Pages**section of the web console.  
   
2. Select **Add allowed administrator** in the **Allowed administrators** section of the page.
3. Submit the username of the user you want to authorize and the NetBIOS name of the domain or computer you want to authorize the user for and select **Ok**.  
   
   - You can authorize a domain user for an entire domain and a local user for a specific computer. Authorizing a domain user for a specific computer is not currently possible.
   - You can use % as a wildcard in the computer, domain or username. In the example above, localuser1 is authorized for any computer whose name starts with the word "LAN", localuser2 is authorized for any computer whose name ends in the word "LAN" and localuser3 is authorized for any computer whose name contains the word "LAN".
