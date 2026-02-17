<!-- # Manage software licenses -->
Your Lansweeper installation allows you to track any software licenses you've purchased for your Windows computers.

You can create a license item that consists of just one software package or group several packages together under one license item. Additional information can then be submitted, such as number of licenses purchased, license type, price per license, expiration date and order details. Purchase and other documents can be uploaded and linked to license items as well.

When you've configured software license compliance, Lansweeper will compare the number of licenses you've indicated were purchased against the number of software installations in your network. A calculation is made of the number of missing licenses as well as the cost of filling in these licenses.

To create a license item:

1. Browse to the following section of the web console: **Software > Windows > Edit Purchased Licenses**.![menu-software-windows-edit-purchased-licenses.jpg](/docs/.document360/assets/article_141/image_001.jpg)
2. Select **Add new License**.
3. Select a software package you want to track from the list of scanned software in the pop-up window. Alternatively, select **Add Software** **to list** to submit a software package that hasn't been scanned yet.  
   ![managing-software-licenses-1.jpg](/docs/.document360/assets/article_141/image_002.jpg)
4. Optionally, you can add more software to the license item by select **Add software** in the item's **Software** tab. Note that you can edit the license item's name as well.  
   ![managing-software-licenses-2.jpg](/docs/.document360/assets/article_141/image_003.jpg)

   You can track all versions of a software package by placing your cursor in the **Version** column, typing "%" and pressing Enter. You can use the "%" wildcard in the **Software** column as well to look for partial software name matches.
5. You can now add additional info in the **Information** tab. Don't forget to **Save** when finished.  
   ![managing-software-licenses-3.jpg](/docs/.document360/assets/article_141/image_004.jpg)
   - Enter the price per license and select the license type from the available dropdown.
   - Optionally, add comments regarding the license type.
   - If the license item is subscription based, tick the **License contract** checkbox and enter a license expiration date into the available field.
   - Enter a contact, owner and comments into the available fields.
6. In the **Orders** tab, add info on any license orders you've placed by select **Add order**. In the pop-up window, enter the number of licenses purchased and the price per license. You can add an order date, number, comment and license key.  
   ![managing-software-licenses-4.jpg](/docs/.document360/assets/article_141/image_005.jpg)
7. In the **Docs** tab, select **Add document** to upload any related purchase or other documents. Select **Choose File** in the pop-up window to launch Windows Explorer and select your file. Enter a display name for the file into the Document Name field and add a comment to the file.   
   The following file formats are allowed: .7z, .bin, .cab, .csb, .csv, .doc, .docx, .dotx, .gif, .ini, .iso, .jpeg, .jpg, .log, .msg, .nfo, .odp, .ods, .odt, .ost, .pcc, .pdf, .png, .potx, .ppt, .pptx, .pst, .rar, .rtf, .tar, .tar.gz, .txt, .vsd, .vsdx, .xls, .xlsx, .xltx, .xml and .zip.  
   ![managing-software-licenses-5.jpg](/docs/.document360/assets/article_141/image_006.jpg)

   Uploaded license files are stored in the following folder, found on the computer hosting your web console: `Program Files (x86)\Lansweeper\Website\DOCS\licenses`
8. You can verify whether you're exceeding the number of licenses purchased by selecting **License report**.   
   ![managing-software-licenses-6.jpg](/docs/.document360/assets/article_141/image_007.jpg)  
   The resulting page lists the number of software installations detected in your network, the number of licenses you've purchased and the number of licenses that are missing. It also calculates the cost of filling in any missing licenses, based on the price per license you submitted. The license compliance report can be exported to an Excel file using the available button.  
   ![managing-software-licenses-7.jpg](/docs/.document360/assets/article_141/image_008.jpg)
