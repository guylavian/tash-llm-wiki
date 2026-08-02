---
title: "Delete a service application in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-delete-a-service-application
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/delete-a-service-application
family: administration
documentKind: "how-to"
abstract: "Learn how to delete a service application in SharePoint Server."
---

# Delete a service application in SharePoint Server - SharePoint Server

Note

Delete a service application in SharePoint Server

# Delete a service application in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can delete a SharePoint Server service application by using the SharePoint Central Administration website or by using Microsoft PowerShell cmdlets.

Caution

The act of deleting a service application is permanent — you cannot undo this operation.

Before you delete a service application, verify that its removal won't adversely affect users. We recommend, that you ensure that no web applications are currently consuming the service application that you are going to delete. For information about how to disconnect a service application from a web application, see Add or remove service application connections from a web application in SharePoint Server.

When you delete a service application, you have the option of also deleting the service application database. Some service applications don't have databases. If you plan to create the service application again in the future, don't delete the service application database. If the service application is temporary, you'll most likely want to delete the database during this operation.

To ensure that the service application is available for potential future use, consider backing up the service application before you delete it. For more information, see Back up service applications in SharePoint Server and Restore service applications in SharePoint Server.

To delete a service application by using Central Administration

### To delete a service application by using Central Administration

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

On the SharePoint Central Administration website, click **Application Management**, and then click **Manage service applications**.

On the **Manage Service Applications** page, click the row that contains the service application that you want to delete. The ribbon becomes available.

On the ribbon, click **Delete**.

In the confirmation dialog, select the check box next to **Delete data associated with the Service Applications** if you want to delete the service application database. If you want to retain the database, leave this check box cleared.

Click **OK** to delete the service application, or click **Cancel** to stop the operation.

To delete a service application by using PowerShell

## To delete a service application by using PowerShell

Verify that you meet the following minimum requirements:

You must have membership in the **securityadmin** fixed server role on the SQL Server instance

You must have membership in the **db_owner** fixed database role on all databases that are to be updated.

You must be a member of the Administrators group on the server on which you're running the PowerShell cmdlet.

Note

If these permissions aren't satisfied, contact your Setup administrator or SQL Server administrator to request these permissions.

For additional information about PowerShell permissions, see Permissions and Add-SPShellAdmin

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following commands.

To retrieve the service application that you want to delete, type the following command:

```
$spapp = Get-SPServiceApplication -Name "<Service application display name>"
```

Where  *<Service application display name>* is the display name of the service application that you want to delete.

The service application information will be stored in the **$spapp** variable.

Important

You have to type the display name within quotation marks, and you have to type the exact service application display name. This includes capitalization. We recommend that you don't create multiple service applications that have the same display name. If you do have this situation, you can use the **Get-SPServiceApplication** cmdlet to list all service applications. You can then use the service application GUID and the **-Identity** parameter to specify the service application that you want to delete. For more information, see Get-SPServiceApplication.

To delete the selected service application, run either of the following commands. In both cases, you are prompted to confirm the deletion.

- To delete the selected service application without removing the service application database, type the following command:

```
Remove-SPServiceApplication $spapp
```

- To delete the selected service application and also delete the service application database, type the following command:

```
Remove-SPServiceApplication $spapp -RemoveData
```

Example

### Example

```
$spapp = Get-SPServiceApplication -Name "Contoso BDC Service"
Remove-SPServiceApplication $spapp -RemoveData
```

In this example, the service application "Contoso BDC Service" information is stored in the **$spapp** variable. After the action is confirmed, the service application and its database are permanently deleted.

For more information, see Get-SPServiceApplication and Remove-SPServiceApplication.

See also

## See also

Other Resources

#### Other Resources

Remove-SPServiceApplicationProxyGroup

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
