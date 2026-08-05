---
title: "The Application Discovery and Load Balancer Service is not running in this farm (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-the-application-discovery-and-load-balancer-service-is-not-running-in-this-farm
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/the-application-discovery-and-load-balancer-service-is-not-running-in-this-farm
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: The Application Discovery and Load Balancer Service is not running in this farm, for SharePoint Server."
---

# The Application Discovery and Load Balancer Service is not running in this farm (SharePoint Server) - SharePoint Server

Note

The Application Discovery and Load Balancer Service is not running in this farm (SharePoint Server)

# The Application Discovery and Load Balancer Service is not running in this farm (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The Application Discovery and Load Balancer Service is not running in this farm.

**Summary:** The Application Discovery and Load Balancer service provides information about the topology of the farm to users who are using services offered by the farm. Users can use this information to perform load balancing. The Application Discovery and Load Balancer Service should be running on at least one server in the farm.

**Cause:** The Application Discovery and Load Balancer service is stopped.

**Resolution: Start the Application Discovery and Load Balancer service on at least one server in the farm.**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the Microsoft PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

`Get-SPServiceInstance -ALL`

For more information, see Get-SPServiceInstance.

Find the GUID of the Application Discovery and Load Balancer service.

Type the following command:

`Start-SPServiceInstance [-Identity]`

Where  *[-Identity]* is the GUID for the Application Discovery and Load Balancer service. You can run the Get-SPServiceInstance cmdlet to see the GUID of the service instance. For more information, see Start-SPServiceInstance.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
