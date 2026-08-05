---
title: "Connect to service applications on remote farms in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-connect-to-a-service-application-on-a-remote-farm
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/connect-to-a-service-application-on-a-remote-farm
family: administration
documentKind: "how-to"
abstract: "Learn how to connect to and consume a published service application in SharePoint Server."
---

# Connect to service applications on remote farms in SharePoint Server - SharePoint Server

Note

Connect to service applications on remote farms in SharePoint Server

# Connect to service applications on remote farms in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In SharePoint Server, you can publish some service applications to make them available over remote connections. By publishing a service application, you can optimize resources and avoid redundancy, and provide enterprise-wide services without installing a dedicated enterprise services farm.

You can connect to a service application that has been shared by another farm if you know the address of the farm's discovery service or the address of the service application. Be aware that you can only connect to a service application on a remote farm if the farm administrator for the remote farm has published the service application.

Before you begin this operation, review Share service applications across farms in SharePoint Server for information about prerequisites.

To connect to a service application on a remote farm by using Central Administration

## To connect to a service application on a remote farm by using Central Administration

Verify that you are a member of the Farm Administrators SharePoint group.

On a server in the consuming farm, on Central Administration, click **Application Management**, and then click **Manage service applications**.

On the ribbon, click **Connect**.

On the **Connect** drop-down menu, click the kind of service application to which you want to connect.

On the Connect to a Remote Service Application page, type the appropriate URL in the **Farm or Service Application address** text box, and then click **OK**.

Note

You can obtain the URL from the administrator of the publishing farm. For more information, see Publish service applications in SharePoint Server. There are two kinds of URLs that you can use in this step: either the URL of the service application or the URL of the remote farm's topology service application. If you use the URL of the service application, only the corresponding service application will be listed in Step 6 of this procedure. If you use the URL of the topology service, all service applications in the farm will be listed in Step 6 of this procedure.

The new **Connect to a Remote Service Application** dialog displays the service applications that match the URL that you typed in Step 5. Click the row that contains the name of the service application, and then select the check box to add the service application connection to the farm's default list of service application connections (that is, the default proxy group). Click **OK**.

You are prompted to change the connection name. Type a new name into the **Connection Name** text box or leave the default name, and then click **OK**.

We recommend that you use the instructions in Exchange trust certificates between farms in SharePoint Server to establish trust between the two farms.

After the new connection is created, you must click **OK** to complete the procedure.

Associate the new service application connection with a local Web application. For information about how to do this, see Add or remove service application connections from a web application in SharePoint Server.

To connect to a service application on a remote farm by using PowerShell

## To connect to a service application on a remote farm by using PowerShell

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Receive-SPServiceApplicationConnectionInfo -FarmUrl <PublishingFarmTopologyURL>
```

Where *<PublishingFarmTopologyURL>* is the information that is retrieved by running the **Get-SPTopologyServiceApplication** cmdlet on the publishing farm. For more information, see Publish service applications in SharePoint Server.

At the PowerShell command prompt, type the following command:

```
New-SPServiceApplicationProxy -Name " <ServiceApplicationProxyName>" -Url "<PublishingFarmTopologyURL>"
```

Where:

*<ServiceApplicationProxyName>* is a unique name for a service application connection on the consuming farm.

*<PublishingFarmTopologyURL>* is the service application topology URL that was also used in the previous command.

Each kind of service application has a specific PowerShell cmdlet that should be used instead of  *New-SPServiceApplicationProxy*. (These cmdlets are listed in the See Also section.) For example, the following command creates a new Managed Metadata service application proxy named "MetadataServiceProxy1" that connects to the service application located at the stated URL.

```
New-SPMetadataServiceApplicationProxy -Name "MetadataServiceProxy1" -Uri "
urn:schemas-microsoft-com:sharepoint:service:9c1870b7ee97445888d9e846519cfa27#authority=urn:uuid:02a493b92a5547828e21386e28056cba&amp;authority=https://ua_powershell:32844/Topology/topology.svc  "
```

You must associate the new service application connection with a local Web application. For information about how to do this, see Add or remove service application connections from a web application in SharePoint Server.

See also

## See also

Other Resources

#### Other Resources

New-SPBusinessDataCatalogServiceApplicationProxy

New-SPEnterpriseSearchServiceApplicationProxy

New-SPMetadataServiceApplicationProxy

New-SPProfileServiceApplicationProxy

New-SPSecureStoreServiceApplicationProxy

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
