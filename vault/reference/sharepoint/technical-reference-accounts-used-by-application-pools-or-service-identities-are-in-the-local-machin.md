---
title: "Accounts used by application pools or service identities are in the local machine Administrators group (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-accounts-used-by-application-pools-or-service-identities-are-in-the-local-machin
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/accounts-used-by-application-pools-or-service-identities-are-in-the-local-machin
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Accounts used by application pools or service identities are in the local machine Administrators group, for SharePoint Server."
---

# Accounts used by application pools or service identities are in the local machine Administrators group (SharePoint Server) - SharePoint Server

Note

Accounts used by application pools or service identities are in the local machine Administrators group (SharePoint Server)

# Accounts used by application pools or service identities are in the local machine Administrators group (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Accounts used by application pools or service identities are in the local machine Administrators group.

**Summary:** A user account that is used by application pools or services must have permissions of a domain user account and must not be a member of the Farm Administrators group or a member of the Administrators group on the local computer. Using highly privileged accounts for application pools or services poses a security risk to the farm, and could allow malicious code to execute.

**Cause:** Accounts that are used by application pools or services are members of the Administrators group on the local computer.

**Resolution: Change the user account to a predefined account, or to a domain user account that is not a member of the Administrators group.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the Central Administration home page, in the **Security** section, click **Configure service accounts**.

On the Service Accounts page, in the **Select the component to update** list, click the application pool or service that uses the credentials of a member of the Administrators group on the local computer as its security account.

In the **Select an account** list, click an appropriate account for this component — for example, the predefined account **Network Service** — or click **Register new managed account**, and then on the Register Managed Account page, specify the credentials and the password change settings that you want.

Click **OK**.

For more information, see Account permissions and security settings in SharePoint Server 2016.

See also

## See also

Concepts

#### Concepts

Plan for administrative and service accounts in SharePoint Server

Plan for least-privileged administration in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
