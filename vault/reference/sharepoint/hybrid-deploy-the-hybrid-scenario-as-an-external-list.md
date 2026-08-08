---
title: "Deploy the Business Connectivity Services hybrid scenario as an external list - SharePoint Server"
type: reference
domain: sharepoint
slug: hybrid-deploy-the-hybrid-scenario-as-an-external-list
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/hybrid/deploy-the-hybrid-scenario-as-an-external-list
family: hybrid
documentKind: "install-set-up-deploy"
abstract: "Learn how to manually extract a Business Data Connectivity model, import the model into SharePoint in Microsoft 365, and manually create an external list to surface the on-premises data."
---

# Deploy the Business Connectivity Services hybrid scenario as an external list - SharePoint Server

Note

Deploy the Business Connectivity Services hybrid scenario as an external list

# Deploy the Business Connectivity Services hybrid scenario as an external list

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The procedures in this article show you how to integrate external data by using an external list. Make sure you've already prepared your environment for the Business Connectivity Services hybrid scenario before you follow the procedures in this article.

Manually extract an external content type to a BDCM file

## Manually extract an external content type to a BDCM file

The external content type that you configured must be manually extracted and saved as a file with a .bcdm extension. This is done by using Visual Studio 2012. Follow the procedure in How to: Convert an App-Scoped External Content Type to Tenant-Scoped in the MSDN Library.

You'll need the .bcdm file for the next procedure.

Import the BDCM file into the SharePoint in Microsoft 365 BDC Metadata Store

## Import the BDCM file into the SharePoint in Microsoft 365 BDC Metadata Store

When you import the BDC Model file into SharePoint in Microsoft 365, you must be signed in to the SharePoint admin center with a federated account (an account imported to Microsoft 365 from on-premises using Directory Sync). This federated account should also be given global admin rights in Microsoft 365. When importing the BDC Model to configure Hybrid BCS, certain calls are made to SharePoint Server that will require you use a federated user account. Be aware the account must also have a populated user profile in SharePoint Server.

**To import a BDCM file into the SharePoint in Microsoft 365 BDC Metadata Store**

Go to **More features** in the SharePoint admin center, and sign in with an account that has admin permissions in Microsoft 365.

Under **BCS**, select **Open**.

Under **business connectivity services**, click **Manage BDC Models and External Content Types**.

On the **Edit** tab, click **Import**.

Click **Browse**, and then browse to the .bdcm file that you exported.

Leave the default selections for **File Type** and **Advanced Settings**, and then click **Import**. During the import, BCS validates the XML in the model, queries the connection settings object, and connects to the on-premises OData source.

When you import a BDCM model into the BDC metadata service, you are creating an external content type. This external content type is available for tenant-wide use.

Create an external list for the BCS hybrid scenario

## Create an external list for the BCS hybrid scenario

The next step is to create the external list.

**To create an external list for the BCS hybrid scenario**

Open the site that you prepared by using an account that has site owner permissions and is a federated account.

On the Quick Launch, click **Site Contents**, and then click **add an app**.

Click **External List**, and then provide a name for the list.

Click the **Select External Content Type** link next to the **External Content Type** box.

Select the external content type that you created, click **OK**, and then click **Create**.

Open the external list and confirm that your external data is displayed.

Once the list is created, validate the scenario.

See also

## See also

Concepts

#### Concepts

Deploy a Business Connectivity Services hybrid solution in SharePoint in Microsoft 365

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
