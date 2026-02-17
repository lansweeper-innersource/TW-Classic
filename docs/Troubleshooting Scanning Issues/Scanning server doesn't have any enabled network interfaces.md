<!-- # Scanning server doesn't have any enabled network interfaces -->
In order for a Lansweeper scanning server to access the network and pull data from your assets, it must have a network interface enabled. If no interface is enabled, you will not be able to scan your IP ranges.

If a network interface is not enabled, you may receive the following error message in Lansweeper's First Run Wizard:

*The Lansweeper scanning server doesn't have any enabled network interfaces! You need to add a new or enable an existing network interface. Afterwards you need to restart the Lansweeper scanning service and reopen the Lansweeper First Run Wizard.*



To resolve this warning and successfully scan an IP range:

1. On your Lansweeper server, open your Start menu and select **Run**.
2. In the input box, enter *ncpa.cpl* and select **OK**. This opens the Network Connections menu and shows you the network interfaces your scanning server has available.

   
3. If your scanning server does have a network interface available that is currently disabled, right-click it and select **Enable**.

   
4. If your scanning server does not have a network interface available:
   1. Open your Start menu and select **Run**.
   2. In the input box, enter *hdwwiz.exe*, select **OK** and then **Next** in the pop-up window.
   3. Select **Install the hardware that I manually select from a list (Advanced)** and select **Next**.
   4. Select **Network adapters,**then **Next**.
   5. Choose a network adapter for installation. Ideally, your scanning server has a physical network adapter and you can simply select the adapter that matches your hardware. In the example below, we are installing the Microsoft Loopback Adapter. This will only allow us to scan the scanning server itself but will still give us a feel for the type of scanning Lansweeper can perform. Select **Next** and then **Next** again.

      
5. On the Windows computer you are attempting to scan, open **Windows Services**.
6. Find the Lansweeper Server, right-click it, then select **Restart**.  

   
7. Refresh the web browser tab that was displaying the First Run Wizard and select an IP range for scanning.

   
