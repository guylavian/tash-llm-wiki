---
title: "Built-in accounts are used as application pool or service identities (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-built-in-accounts-are-used-as-application-pool-or-service-identities
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/built-in-accounts-are-used-as-application-pool-or-service-identities
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Built-in accounts are used as application pool or service identities, for SharePoint Server."
---

# Built-in accounts are used as application pool or service identities (SharePoint Server) - SharePoint Server

Note

Built-in accounts are used as application pool or service identities (SharePoint Server)

# Built-in accounts are used as application pool or service identities (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Built-in accounts are used as application pool or service identities.

**Summary:** Built-in or local computer accounts are used as an application pool identity or service identity.

**Cause:** Using built-in accounts as application pool identities or as service identities is not supported in a farm configuration. Built-in accounts include Network Service, Local Service, and Local System.

**Resolution: Change the identity that is used for the service or application pool**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Security**.

On the Security page, in the **General Security** section, click **Configure service accounts**.

On the Service Accounts page, in the **Credential Management** section, in the upper drop-down list, click the service or application pool for which you want to change the identity.

In the **Select an account for this component** list, click the domain user account that you want to associate with the service or application pool.

If you want to register the account that you selected on the SharePoint Server farm, click **Register new managed account**.

Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
