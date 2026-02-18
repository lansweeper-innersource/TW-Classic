<!-- # Copy Lansweeper scanning server configuration to a different server -->
Copying your Lansweeper server configuration manually from one scanning server to another can be straightforward but results in the source server being removed. This article introduces a more accessible method that achieves the same result by running a database script. The advantage of this script is that the source server will not be removed.

If you want to move your entire Lansweeper installation to a different server, follow the steps in [this knowledge base article](/classic/docs/move-your-lansweeper-installation-to-a-different-server).

The script copies the configuration (threads, cleanup settings, and active scanning options) from the source server to the destination server. Your scanning server configuration can be found in the **Configuration > Server options** menu.

For this script to work correctly, the destination server's service must have started successfully at least once.

This process can easily break your installation. We recommend backing up your database before continuing, as explained in [this knowledge base article](https://www.lansweeper.com/knowledgebase/backing-up-your-installation/).

1. Open SQL Server Management Studio and connect to the SQL Server instance hosting your Lansweeper database.
2. Modify the script below with the name of the source server you're copying the config from.
3. Modify the script below with the name of the destination server you're copying the config to.
4. Stop the **Lansweeper Server** **service** on your destination server.
5. Execute the following script via a **New Query** window.

```
Use Lansweeperdb

 UPDATE tsysASServers

  SET

      [Listenport] = existing.listenport,

      [ConcurrentThreads] = existing.[ConcurrentThreads],

      [IPscanThreads] = existing.[IPscanThreads],

      [RMADCOMP] = existing.[RMADCOMP],

      [NAADCOMP] = existing.[NAADCOMP],

      [RMADUSER] = existing.[RMADUSER],

      [MAKEACTIVE] = existing.[MAKEACTIVE],

      [DELHIST] = existing.[DELHIST],

      [DELHISTDAYS] = existing.[DELHISTDAYS],

      [DELCOMP] = existing.[DELCOMP],

      [DELCOMPDAYS] = existing.[DELCOMPDAYS],

      [NACOMP] = existing.[NACOMP],

      [NACOMPDAYS] = existing.[NACOMPDAYS],

      [DELEVENTDAYS] = existing.[DELEVENTDAYS],

      [DELSYSLOGDAYS] = existing.[DELSYSLOGDAYS],

      [REFRADCOMP] = existing.[REFRADCOMP],

      [REFRADUSERS] = existing.[REFRADUSERS],

      [RMDIUSER] = existing.[RMDIUSER],

      [RMDICOMP] = existing.[RMDICOMP],

      [NADICOMP] = existing.[NADICOMP],

      [Scanuser] = existing.[Scanuser],

      [EVinfo] = existing.[EVinfo],

      [EVsuccess] = existing.[EVsuccess],

      [DELUptimeDays] = existing.[DELUptimeDays],

      [EVwarning] = existing.[EVwarning],

      [EVfailure] = existing.[EVfailure],

      [DELLOGONINFO] = existing.[DELLOGONINFO],

      [renamedComputerDetection] = existing.[renamedComputerDetection],

      [MaxDeploymentThreads] = existing.[MaxDeploymentThreads],

      [DELDEPLOYMENTLOGDAYS] = existing.[DELDEPLOYMENTLOGDAYS],

      [ScanHistoryDays] = existing.[ScanHistoryDays],

      [ActiveScanningMaxRescanTime] = existing.[ActiveScanningMaxRescanTime],

      [ActiveScanningMinRescanTime] = existing.[ActiveScanningMinRescanTime],

      [ActiveScanningInterval] = existing.[ActiveScanningInterval],

      [Delconfigurationlogdays] = existing.[Delconfigurationlogdays],

      [Delloginlogdays] = existing.[Delloginlogdays],

      [DoFallbackScanning] = existing.[DoFallbackScanning],

      DelPerformanceCounterDays = existing.[DelPerformanceCounterDays]

FROM tsysasservers

     INNER JOIN tsysasservers existing ON existing.servername = 'sourceserver'

WHERE tsysasservers.servername = 'destinationserver';
```

If you want to move your entire Lansweeper installation to a different server instead of the configuration, please follow the steps in [this knowledge base article](/classic/docs/move-your-lansweeper-installation-to-a-different-server).
