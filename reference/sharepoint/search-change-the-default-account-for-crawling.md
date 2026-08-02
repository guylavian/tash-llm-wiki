---
title: "Change the default account for crawling in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-change-the-default-account-for-crawling
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/change-the-default-account-for-crawling
family: search
documentKind: "how-to"
abstract: "Change the user name or password of the account that the SharePoint Server Search service uses by default for crawling."
---

# Change the default account for crawling in SharePoint Server - SharePoint Server

Note

Change the default account for crawling in SharePoint Server

# Change the default account for crawling in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The account that the SharePoint Server Search service uses by default for crawling is called the default content access account. It must be a domain account with a password that is current in Active Directory Domain Services (AD DS). If the password of this domain account expires, the Search service is not able to use the account to crawl content.

The password of the default content access account has two additional dependencies on the domain account password in AD DS:

If you change the password of the account in AD DS, you must make the same change for the password of the default content access account in SharePoint Server.

If you want to change the password of the default content access account in SharePoint Server, you must first change the password in AD DS. This is because the credentials that you enter for the default content access account in SharePoint Server are checked against those in AD DS. If you enter a new password for the default content access account before the account password is changed in AD DS, an error will result and the password of the default content access account will not be changed.

The following procedure changes the user name and password for the default content access account. You can specify a different account for crawling particular URLs by using a crawl rule. If you specify a different account in a crawl rule and you want to change the password of that account, you must change the crawl rule. For more information, see Manage crawl rules in SharePoint Server.

**To change the default content access account**

Verify that the account that performs this procedure is a service application administrator for the Search service application that you want to configure.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Search service application for which you want to change the default content access account.

On the Search Administration page for the Search service application, in the **System Status** section, find the **Default content access account**, which is of the form  *Domain\UserName*.

Click the default content access account name. The **Default Content Access Account** dialog appears.

(Optional) In the **Account** text box, type a new user name.

In the **Password** text box and in the **Confirm Password** text box, type the new password, and then click **OK**.

See also

## See also

Create and configure a Search service application in SharePoint Server 2016

Manage crawl rules in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
