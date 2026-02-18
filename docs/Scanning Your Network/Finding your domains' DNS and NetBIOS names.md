<!-- # Finding your domains' DNS and NetBIOS names -->
[When scanning assets](/classic/docs/scan-an-active-directory-domain-scanning-target) using [Lansweeper](https://www.lansweeper.com/ "Lansweeper"), you sometimes needs to submit your domain's DNS or NetBIOS name as part of the scanning target.

If you're unsure what your domain's DNS or NetBIOS name is, follow these steps:

1. On a Windows server with Active Directory Domain Services or Remote Server Administration Tools installed, open your **Start** menu and select **Run**.
2. In the input box, type "dsa.msc" and select **OK**.
3. In the **Active Directory Users and Computers** configuration window, right-click your domain and choose the **Properties** menu item.  
   
4. Your domain's full DNS name is the first name listed in the **General** tab. Domain DNS names generally contain a period.  
   
5. Your domain's NetBIOS name is the pre-Windows 2000 entry in the same tab. Domain NetBIOS names generally do not contain a period.  
   
