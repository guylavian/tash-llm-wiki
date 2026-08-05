---
title: "Use a sample MIM solution in SharePoint Server - SharePoint Server"
description: "How to configure SharePoint Server profile synchronization with Microsoft Identity Manager (MIM)."
ms.topic: how-to
---
Note

Use a sample MIM solution in SharePoint Server

# Use a sample MIM solution in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The article outlines a solution that helps you to install and synchronize accounts to SharePoint Server using Microsoft Identity Management, or MIM. MIM 2016 is the successor to a profile synchronization technology used by previous versions of SharePoint Server that was known as Forefront Identity Manager, or FIM. FIM is no longer included as part of the product from SharePoint Server 2016. However, MIM isn't the only synchronization solution that SharePoint Server offers. If you would prefer to use the Active Directory Direct Import that is built in with SharePoint Server, please see the configuration article here. Otherwise, follow the steps in this article to configure a new installation of MIM for your User Profile Synchronization.

Download the solutions files that you need

Gather the configuration details you need

The Microsoft PowerShell to install the SharePoint Server Synchronization Configuration file

The Microsoft PowerShell to start the SharePoint Synchronization Configuration

Important

The solutions files referenced in this article are available for download here. You will need a GitHub account for access. See the section 'Download the solutions files that you need' for more details. > Microsoft Identity Manager 2016 is available for download from the Microsoft Volume Licensing Center. (Log in and search on the product name.) > On your MIM server, be sure to install Service Pack 1 (https://aka.ms/mim2016sp1upgrade).

Download the solutions files that you need

## Download the solutions files that you need

Download the files used by this solution into a folder on MIM Synchronization Server. Make certain you're logged in as a Farm Administrator and have a local administrator right on this server.

**SharePointSync.psm1** - Microsoft PowerShell module for deploying and starting the synchronization solution.

**MA-AD.xml** - This is the MIM management agent for Active Directory.

**MA-SP.xml** - This is the MIM management agent for SharePoint Server.

**MV.xml** - This XML file contains more User Profile Synchronization configuration.

Gather the configuration details you need

## Gather the configuration details you need

To run the Microsoft PowerShell commands involved in this solution, you need to catalog some information from your Active Directory and your SharePoint Server configuration as well. You should include this information in any build-documentation you keep on the User Profile Synchronization process.

**Active Directory**

| **Item** | **Description** |
| --- | --- |
| ForestDnsName | This is the DNS name of the Active Directory forest to be synchronized. |
| ForestCredential | This is the username and password of the account that will be used to read objects from Active Directory. This account must have Replicate-Directory-Changes permissions in the Active Directory that is to be synchronized. |
| OrganizationalUnit | This is the distinguished name of the Active Directory container to be synchronized. You can add more containers after the configuration is loaded. To add more containers, use the Synchronization Service Manager GUI interface to modify the 'AD' management agent. |

**SharePoint Connection Details**

| **Item** | **Description** |
| --- | --- |
| SharePointUrl | This is the URL of the SharePoint Server running the User Profile Service application, for example, http://SharePoint01:8080. |
| SharePointCredential | The username and password of the account used to read and write objects into the SharePoint User Profile. |

The Microsoft PowerShell to install the SharePoint Server Synchronization Configuration file

## The Microsoft PowerShell to install the SharePoint Server Synchronization Configuration file

Once you've downloaded the solution files and cataloged the configuration details you can begin running the Microsoft PowerShell command for installing the SharePoint Synchronization Configuration.

The configuration is installed by loading SharePointSync.psm1 and calling Install-SharePointSyncConfiguration as shown in the following code.

```
### Load the SharePoint Sync Module
Import-Module C:\SharePointSync\SharePointSync.psm1 -Force
### Install the SharePoint Sync Configuration
Install-SharePointSyncConfiguration `
  -Path C:\SharePointSync `
  -ForestDnsName litware.ca `
  -ForestCredential (Get-Credential LITWARE\adSyncAccount) `
  -OrganizationalUnit 'ou=Litwarians,dc=Litware,dc=ca' `
  -SharePointUrl http://SharePointServer:5555 `
  -SharePointCredential (Get-Credential LITWARE\spUserProfileAdmin) `
  -Verbose 
```

Preview the impact of your SharePoint Synchronization

## Preview the impact of your SharePoint Synchronization

Once the synchronization configuration is installed, it's ready to be started. Before you make further changes, you can examine the impact your synchronization has by running the Start-SharePointSync cmdlet with '-WhatIf'.

```
### Run the Synchronization Service management agents
Start-SharePointSync -WhatIf -Verbose 
```

The Microsoft PowerShell to start the SharePoint Synchronization Configuration

## The Microsoft PowerShell to start the SharePoint Synchronization Configuration

To start the SharePoint Server synchronization service on-demand, run the Start-SharePointSync cmdlet.

```
### Run the Synchronization Service management agents 
Start-SharePointSync -Verbose 
```

How to add more Active Directory Domains

## How to add more Active Directory Domains

Now that you've loaded the initial configuration, you can add more domains for synchronization. Follow these steps in the Synchronization Service manager.

**1. Add another domain or domains**

Open the Synchronization Service Manager.

In the Management Agents tab, select the ADMA management agent > **Properties** > **Actions**.

In the **Properties** dialog > **Configure Directory Partitions**.

In the list of directory partitions, select any domain you want to synchronize (and remember that credentials for these domains may be required).

Select **OK** to save the management agent properties.

Each run profile for the ADMA management agent must be updated for each domain that was added. To update your profiles, do the following:

**2. Update your run profile**

In the **Management Agents** tab > select **ADMA Management** agent > select **Configure Run Profiles**.

Select **FullImport** run profile > New Step.

Choose a step type of **Full Import (Stage Only)** > **Next**.

Choose the partition that matches the domain you just added and select **Finish**. The run profile should now have two steps.

Select the **FullSync** run profile next > New Step.

Choose a step type of **Full Synchronization** > **Next**.

Choose the partition that matches the domain you just added > **Finish**. The Run profile will now have two steps.

Select **DeltaImport** in the run profiles next > New Step.

Choose a step of type **Delta Import (Stage Only)** > **Next**.

Choose the partition that matches the domain that was added > **Finish**. The run profile should now have two steps.

Select the **DeltaSync** run profile > **New Step**.

Choose a step of type **Delta Synchronization** > **Next**.

Choose the partition that matches the domain that was added > **Finish**. The run profile should now have two steps.

Select **Apply** to save all the run profile changes > **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
