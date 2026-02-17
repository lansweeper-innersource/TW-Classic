<!-- # Adding owners to a Cloud site -->
A Cloud site can have one or more site owners. A site owner is the most privileged type of user in a site. In addition to being an administrator, a site owner has special rights over the site that regular administrators don't have. By default, the creator of a site is the only owner of that site. For redundancy and security reasons, a site ideally has more than one owner. That way, you are not dependent on a single person to manage the site.

This article explains what it means to be a site owner and how you as a site creator can add more owners to your site.

## What it means to be a site owner

A site owner is the most privileged type of user in a site. All owners of a site have the same rights. A site owner:

- Has the Administrator role. This means the user has all available permissions in the site and access to all assets. A site owner's role and asset access cannot be modified, nor can an owner be added to a group with more limited permissions.
- Can enforce MFA in the site.
- Can enforce SSO in the site.
- Can change the software display setting for the site.
- Can delete the site.
- Can manage user accounts within the site, including other owners. A site owner can promote regular users to owners and can demote owners to regular users.

## How to add owners to a site

You can add an unlimited number of owners to your site but choose your site owners carefully.   
A site owner can perform highly privileged operations on your site. They can demote other site owners or even delete the site.

### 1. Invite future owners to site

For a user to become an owner of a site you created, that user must first be a member of your site. Invite any users to your site that you want to make site owners. The users must accept the invitation before you can promote them to site owners. Follow the steps in [this knowledge base article](/docs/add-users-to-a-cloud-site "Adding users to a Cloud site") to invite users to a site.

### 2. Make invited users owners

Have your site selected and browse to the **Configuration** **>****Account** **management** **>****All accounts** menu.  
Select the user you want to make a site owner. Looking at the user's individual account, click **Enable this account as a site owner**.   
You will see a pop-up informing you of the implications of making the user a site owner. Once you've confirmed that you understand the implications, click **Save and exit**. Repeat the same process for any other users you want to make owners.   
The new owners will receive an email informing them that they were made an owner of your site. They are now listed in the **Site owners** section of your site's **All accounts** menu.

A site must always have at least one owner and cannot be orphaned. If you want to give up your ownership of a company site, first make someone else an owner. Only then can the new owner revoke your ownership rights.   
Deleting your Cloud account requires you to either transfer ownership of your sites to someone else or to delete your sites.

![add-cloud-site-owner.png](/docs/.document360/assets/article_328/image_001.jpg)
