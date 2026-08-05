---
title: "Accounts needed for hybrid configuration and testing - SharePoint Server"
type: reference
domain: sharepoint
slug: hybrid-accounts-needed-for-hybrid-configuration-and-testing
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/hybrid/accounts-needed-for-hybrid-configuration-and-testing
family: hybrid
documentKind: "article"
abstract: "Learn about the accounts you need to use when you configure a SharePoint Server hybrid solution."
---

# Accounts needed for hybrid configuration and testing - SharePoint Server

Note

Accounts needed for hybrid configuration and testing

# Accounts needed for hybrid configuration and testing

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When you configure a SharePoint Server hybrid environment, you need several user accounts in both your on-premises Active Directory and Microsoft 365. These accounts also need different permissions and group or role memberships. Some of these accounts are used to deploy and configure software, and some are used to test specific functionality to help ensure that security and authentication systems are working as expected.

In a hybrid environment, some or all user accounts in Active Directory are synchronized with Microsoft Entra directory services. We refer to these accounts as federated users. SharePoint Server and SharePoint in Microsoft 365 are configured with a server-to-server (S2S) trust relationship, and service applications can be configured to enable federated users to access content and resources from both farms using a single identity. Because user accounts and credentials are synchronized between SharePoint Server and SharePoint in Microsoft 365, list and library content security can be applied in both farms using the same set of users and groups.

Note

This table does not include service accounts, which may have specific requirements for service applications and features in certain SharePoint Server hybrid solutions. For more information about the requirements for each supported solution, see the solution configuration articles at Configure a hybrid solution for SharePoint Server.

Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

**Table: Accounts needed for SharePoint hybrid configuration and testing**

| **Account** | **Identity provider** | **Role** |
| --- | --- | --- |
| Global Admin | Microsoft 365 and Microsoft Entra ID | Use a Microsoft 365 work account that has been assigned to the Global Admin role for Microsoft 365 configuration tasks such as configuring SharePoint in Microsoft 365 features, running Microsoft Entra ID and SharePoint in Microsoft 365 PowerShell commands, and testing SharePoint in Microsoft 365. |
| AD Domain Admin | On-premises AD | Use an AD account in the Domain Admins group to configure and test AD, ADFS, DNS, and certificates and to do other tasks that require elevation. |
| SharePoint in Microsoft 365 Farm Admin | On-premises AD | Use an AD account in the SharePoint in Microsoft 365 Farm Admins group for SharePoint Server configuration tasks such as running PowerShell commands in the SharePoint in Microsoft 365 Management Shell to configure S2S trusts, create and configure web applications and site collections, deploy and configure SQL Server databases, and troubleshoot SharePoint Server.  
  This account must also have additional privileges to use the SharePoint in Microsoft 365 Management Shell:  
  Membership in the **securityadmin** fixed server role on the SQL Server instance.  
  Membership in the **db_owner** fixed database role on all databases that are to be updated.  
  Membership in the Administrators group on the server on which you are running the PowerShell cmdlets. |
| Federated Users | On-premises AD | Use AD accounts that have been synchronized with Microsoft 365 to test access to specific resources in both SharePoint Server and SharePoint in Microsoft 365.  
 These accounts, or groups of which they are members, must have permissions to SharePoint Server site collections and resources in both environments and have the appropriate product licenses assigned in the Microsoft 365 subscription. They also must be set to use the alternative domain UPN suffix that you specify for federated users during the planning process.  
 You can configure multiple federated accounts with different permissions or group memberships to test for appropriate security trimming and access to site resources. |

Additional resources

## Additional resources

- Last updated on 
		2024-07-23
