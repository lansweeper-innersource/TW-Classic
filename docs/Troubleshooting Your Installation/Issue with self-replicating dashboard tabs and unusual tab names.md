<!-- # Issue with self-replicating dashboard tabs and unusual tab names -->
If you have Netsparker, Rapid7 or other vulnerability management software running in your network, you may start seeing randomly generated tabs with odd tab names in your Lansweeper web console's dashboard.

This display issue is due to your vulnerability management software scanning your web console and injecting false data in an effort to identify security issues. To get rid of the duplicate dashboard tabs and prevent this problem from occurring again, try one of these solutions:

- Restrict access to the Lansweeper web console by following the instructions in [this knowledge base article](/docs/restrict-access-to-the-web-console). Restricting access prevents your vulnerability management software from making changes to the web console and will automatically get rid of existing false dashboard tabs, as a new dashboard will be generated for each user that logs into the web console.
- Prevent your vulnerability management software from scanning the Lansweeper web console and run the script below in the **Script Execution** tab of the `Program Files (x86)\Lansweeper\Tools\DatabaseMaintenance.exe` tool on your Lansweeper server. This will reset your dashboard and remove the duplicate dashboard tabs.

  ```
  delete from tsysWebUsers where Username Like '%.\Unauthenticated'
  ```

  

  
