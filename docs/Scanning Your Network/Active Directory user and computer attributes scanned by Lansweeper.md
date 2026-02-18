<!-- # Active Directory user and computer attributes scanned by Lansweeper -->
When performing Active Directory user and computer scanning, Lansweeper retrieves specific attributes from your user and computer objects. In Lansweeper 7.2, the attributes that are retrieved were expanded. Below you can find an overview of all the attributes currently scanned by Lansweeper for both users and computers.

These attributes can be found on AD user and computer pages. You can access AD user pages through one of the following methods: search for a user via the search bar at the top of the web console, via the Active Directory Users OU widget and by clicking users on asset pages, or via reports. In the Lansweeper database, scanned AD attributes are stored in the tblADComputers, tblADusers and tblAdProperty tables. More information on database structure can be found in [our database documentation](/classic/docs/access-lansweeper-database-documentation).

If you haven't scanned your Active Directory users or computers yet, you can check out [this article for further information on how to scan users](/classic/docs/how-to-scan-users) and [this article for further information on how to scan computers](/classic/docs/scanning-with-an-active-directory-computer-path-scanning-target).

## Active Directory user attributes

- City
- Company
- Country
- Country abbreviation
- Countrycode
- Department
- Description
- Displayname
- Division
- Email
- EmployeeID
- EmployeeNumber
- EmployeeType
- ExpirationDate
- ExtensionAttribute1
- ExtensionAttribute2
- ExtensionAttribute3
- ExtensionAttribute4
- ExtensionAttribute5
- ExtensionAttribute6
- ExtensionAttribute7
- ExtensionAttribute8
- ExtensionAttribute9
- ExtensionAttribute10
- ExtensionAttribute11
- ExtensionAttribute12
- ExtensionAttribute13
- ExtensionAttribute14
- ExtensionAttribute15
- Fax
- Firstname
- Groups
- HomeDirectory
- HomePage
- HomePhone
- Info
- Initials
- IpPhone
- Lastchanged
- LastLogon
- Lastname
- LockoutDate
- LogonScript
- Manager and Direct Reports
- MiddleName
- Mobile
- Name
- Office
- OtherFax
- OtherHomePhone
- OtherIpPhone
- OtherMobile
- OtherPager
- OtherTelephone
- OU
- Pager
- PasswordChangeableDate
- PasswordExpirationDate
- PasswordLastSet
- PasswordNeverExpires
- PasswordRequired
- Picture
- PostalAddress
- PostOfficeBox
- ProfilePath
- State
- Status (enabled or disabled)
- Street
- Telephone
- Title
- UPN
- Url
- UserCannotChangePassword
- Userdomain
- Username
- whenChanged
- whenCreated
- Zip

ExtensionAttribute1 through 15 only exist in Active Directory if you've extended your AD schema through the Microsoft Exchange Server setup. These attributes do not exist in a default Active Directory.

LastLogon scanning can be enabled/disabled with the following checkbox in the **Configuration > Server Options** menu: Scan LastLogon attribute of users in Active Directory.

 

## Computer attributes

- BitLocker recovery key
- Comment
- Company
- Description
- Groups
- Location
- Manager
- OU
- Status (enabled or disabled)

The BitLocker recovery keys can only be seen by users with the Access BitLocker Recovery Keys permission. More information on web console permissions can be found in [this article](/classic/docs/web-console-user-roles-and-permissions).


