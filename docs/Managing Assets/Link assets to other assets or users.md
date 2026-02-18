<!-- # Link assets to other assets or users -->
Linking assets to AD user groups, AD user OUs and local Windows users is a feature introduced in Lansweeper 7.2. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

Lansweeper Classic allows you to link assets to other assets, Active Directory users, AD user groups, AD user OUs and local Windows users. It also allows you to define the asset/asset or asset/user relationship, the relation start date and relation end date. You can specify that asset A was borrowed by user X this month for instance and that asset B is backed up to asset C. If a relation's end date is older than today, the asset or user page grays out the relation to show its expired status.

There are a number of built-in relation types and you can [create your own](/classic/docs/create-asset-relation-types) as well. Once you've created your relations, you can also report on them using built-in or custom reports in the **Reports** menu.

## Linking one asset to another asset or user

1. Browse to the asset's Lansweeper page and select **Edit asset** in the **Asset options**menu.
2. Define an asset/asset relation:
   - Select a relation type from the fourth dropdown in the **Asset Relations** section of the page. If none of the relation types suit your needs, you can [create a new one](/classic/docs/create-asset-relation-types).
   - Choose **Select asset** from either the third or fifth dropdown, depending on which asset (the source or the target) you want to base the asset relation on.
   - In the resulting pop-up window, tick the checkbox in front of the target asset of your choice and select **Ok**. You can search through one of the columns to easily find the asset you need.
   - Optionally, use the available input boxes to add a custom start date, end date and comment to the relationship. Select **Add** and **Save asset** afterward.
3. Define an asset/user relation:
   - Select a relation type from the third dropdown in the **User/OU/AD group Relations** section of the page. If none of the relation types suit your needs, you can [create a new one](/classic/docs/create-asset-relation-types).
   - Choose **Select user, OU or AD group** from the fourth dropdown.
   - The resulting pop-up lists scanned AD users, AD groups, AD OUs and local Windows users, in several tabs. Select the user entry of your choice and click **Ok**. You can filter and search within the pop-up to find the user entry you need. If an AD user, group or OU is missing from the pop-up, make sure you've scanned it by following the instructions in [this knowledge base article](/classic/docs/how-to-scan-users).
   - Optionally, use the available input boxes to add a custom start date, end date and comment to the relationship. Select **Add** and **Save asset** afterward.

## Linking multiple assets to another asset or user

1. Go to the **Assets** section of the web console to view your list of scanned assets.
2. Tick the checkboxes of the assets you would like to link.
   - You can search through one of the columns to easily find specific assets. In the example above, we filtered the Domain column to only list assets within the Lansweeper domain.
   - You could also tick the checkbox at the very top to select all assets in the current search results.
3. Select **Add relations** in **Asset Actions**menu.
4. Select a relation type from the **Relation Type** dropdown in the pop-up window. If none of the types suit your needs, you can [create a new one](/classic/docs/create-asset-relation-types).
5. To define an asset/asset relation, click **Select Asset**, tick the checkbox of the target asset of your choice and select **Ok**. You can search through one of the columns to easily find the asset you need.

   
6. To define an asset/user relation, click **Select User, OU or AD group**, select the user entry of your choice and select **Ok**. You can filter and search within the pop-up to find the user entry you need.If an AD user, group or OU is missing from the pop-up, make sure you've scanned it by following the instructions in [this knowledge base article](/classic/docs/how-to-scan-users).   
   Instead of choosing a specific user entry, you can also select **Top Console User**. Lansweeper will then automatically determine for each Windows computer which user it should be linked to. Each Windows computer will be linked to the domain user with the most logins to the machine.

   

   **Top Console User** only adds relations to Windows computers and only Windows computers that domain users have logged into.
7. Optionally, use the available input boxes to add a custom start date, end date and comment to the relationship. Select **Add Relation(s)** afterward.
