<!-- # Scan untrusted domains -->

If you'd like to submit a domain for scanning other than the one your Lansweeper server is located in and there is no trust between these two domains, you will need to ensure that your Lansweeper server can correctly resolve the domain you're trying to scan. Follow these steps to scan an untrusted domain:

1. On your Lansweeper server, open your **Start** menu and select **Run**.
2. In the input box, type ncpa.cpl and select **OK**.
3. Right-click your network connection and select **Properties**.
4. Select **Internet Protocol Version 4 (TCP/IPv4)** and select **Properties**.
5. Click the **Advanced...** button and select the **DNS** tab.
6. Select the upper **Add...** button in the **DNS** tab, enter the DNS server of the untrusted domain you'd like to scan and click **Add**.
7. Tick **Append these DNS suffixes (in order)**, select **Add...**, enter the DNS suffix of the untrusted domain you'd like to scan and click **Add**.
8. Submit the untrusted domain for scanning as normal, e.g. by following the instructions in [this knowledge base article](/classic/docs/scan-a-windows-computer-scanning-target).
