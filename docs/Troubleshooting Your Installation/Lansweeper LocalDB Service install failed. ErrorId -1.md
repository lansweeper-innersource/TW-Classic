<!-- # Lansweeper LocalDB Service install failed. ErrorId: -1 -->
This article explains how to resolve the "Errorid: -1 error" you may encounter when installing or updating Lansweeper.

One of the available database server options when installing Lansweeper is [SQL LocalDB](/classic/docs/introduction-to-the-sql-localdb-database-server). When you choose to host the Lansweeper database under LocalDB, the Lansweeper installer creates a service that runs the SQL LocalDB database server. Afterwards, this service will run under a user account created by the installer, "NT Service\LansweeperLocalDbService". In order for the aforementioned user account to successfully run the LocalDB service, it must be granted the necessary permission to log on as a service. Lansweeper automatically tries to give NT Service\LansweeperLocalDbService this permission. If you're using the SQL LocalDb database provider, you may encounter the error below when updating or installing Lansweeper.



1. Open **services.msc** and start **Lansweeper LocalDB** **Service**. 
   - If the service started successfully, restart the **Lansweeper Server** service and [connect to the web console](/classic/docs/access-the-web-console).
   - If the **Lansweeper LocalDB Service** failed to start, proceed to step 2.
2. When the **Lansweeper LocalDB Service** starts, it reconfigures local Windows security policy by adding the "NT Service\LansweeperLocalDbService" account to the **Log on as a service** policy. This policy can be found in Windows on your Lansweeper server by going to `Local Computer Policy > Windows Settings > Security Settings > Local Policies > User Rights Assignment` in the Local Computer Policy editor, which is accessible via MMC.  
   
3. Group policy may disable or override local policy in a domain environment. If the LocalDB service was unable to log on, the error below may be thrown.  
   
4. Additionally, an event such as the one below is usually found in the **Event Viewer** of your Lansweeper server under `Windows Logs\Application` or `Windows Logs\System`.  
   
5. You can resolve this by modifying your domain's group policy in Active Directory by adding "NT Service\LansweeperLocalDbService" to the **Log on as a service** policy for your Lansweeper server. Regardless of whether you're in a domain or not, the "NT Service\LansweeperLocalDbService" user must be used, other accounts are not supported.

## Alternative

If you'd prefer not to make group policy changes or would like to use an alternative for any other reason, you could opt to use the SQL Server database provider. This will avoid the Lansweeper LocalDB install failed error entirely.

A comparison between SQL Server and SQL LocalDB from a Lansweeper perspective can be found [in this article](/classic/docs/introduction-to-the-sql-localdb-database-server "Introduction to the SQL LocalDB database server"). For a new installation of Lansweeper, you can perform an [Advanced Install](/classic/docs/install-lansweeper-on-prem#heading2 "Advanced Lansweeper installation") and select the SQL Server database provider. If you're already using SQL LocalDB, you can [migrate to SQL Server](/classic/docs/move-your-database-from-sql-localdb-to-sql-server "Moving your database from SQL LocalDB to SQL Server").

A SQL Server instance must be [configured](/classic/docs/configuring-a-sql-server-instance-to-host-the-lansweeper-database "Configuring a SQL Server instance to host the Lansweeper database") before migrating or installing Lansweeper using the SQL Server database provider. A free Express edition is available.

2.11.0.0    

2.11.0.0
