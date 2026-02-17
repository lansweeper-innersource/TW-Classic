<!-- # Scan untrusted domains -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_236/image_001.jpg) **This page explains how you can scan an untrusted domain using Lansweeper by following a couple of steps.**

If you'd like to submit a domain for scanning other than the one your Lansweeper server is located in and there is no trust between these two domains, you will need to ensure that your Lansweeper server can correctly resolve the domain you're trying to scan. Follow these steps to scan an untrusted domain:

1. On your Lansweeper server, open your **Start** menu and select **Run**.
2. In the input box, type ncpa.cpl and select **OK**.![scanning-untrusted-domains-1.jpg](/docs/.document360/assets/article_236/image_002.jpg)
3. Right-click your network connection and select **Properties**.![scanning-untrusted-domains-2.jpg](/docs/.document360/assets/article_236/image_003.jpg)
4. Select **Internet Protocol Version 4 (TCP/IPv4)** and select **Properties**.![scanning-untrusted-domains-3.jpg](/docs/.document360/assets/article_236/image_004.jpg)
5. Click the **Advanced...** button and select the **DNS** tab.![scanning-untrusted-domains-4.jpg](/docs/.document360/assets/article_236/image_005.jpg)
6. Select the upper **Add...** button in the **DNS** tab, enter the DNS server of the untrusted domain you'd like to scan and click **Add**.![scanning-untrusted-domains-5.jpg](/docs/.document360/assets/article_236/image_006.jpg)
7. Tick **Append these DNS suffixes (in order)**, select **Add...**, enter the DNS suffix of the untrusted domain you'd like to scan and click **Add**.![scanning-untrusted-domains-6.jpg](/docs/.document360/assets/article_236/image_007.jpg)
8. Submit the untrusted domain for scanning as normal, e.g. by following the instructions in [this knowledge base article](/docs/scan-a-windows-computer-scanning-target).
