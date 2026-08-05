---
title: "Web.config file has incorrect settings for the requestFiltering element (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-web-config-file-has-incorrect-settings-for-the-requestfiltering-element
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/web-config-file-has-incorrect-settings-for-the-requestfiltering-element
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Web.config file has incorrect settings for the requestFiltering element, for SharePoint Server."
---

# Web.config file has incorrect settings for the requestFiltering element (SharePoint Server) - SharePoint Server

Note

Web.config file has incorrect settings for the requestFiltering element (SharePoint Server)

# Web.config file has incorrect settings for the requestFiltering element (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Web.config file has incorrect settings for the requestFiltering element.

**Summary:** To support file names that contain the + character, the requestFiltering element in the Web.config file must have the allowDoubleEscaping attribute set to **True** and it must have a requestLimits element that has a maxAllowedContentLength value set to 2147483647 to avoid interfering with file upload.

**Cause:** The settings of the requestFiltering element in the Web.config file are incorrect.

**Resolution: Change the requestFiltering settings in the Web.config file in Internet Information Services (IIS).**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

Identify the server on which this event occurs. On the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** column. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server.

Verify that the user account that is performing the following steps is a member of the Administrators group on the local computer that you identified in the previous step.

Log on to the server on which this event occurs.

On **Server Manager**, click **Tools**, and then select **Internet Information Services (IIS) Manager**.

In the Internet Information Services management console, in the **Connections** pane, expand the tree view of the server name, expand **Sites**, and then click the site for which you want to change the requestFiltering settings.

On the site Home page, switch to **Features View**, and then in the **Management** section, double-click **Configuration Editor**.

In the **Section** list, expand **system.webServer**, expand **security**, and then click **requestFiltering**.

On the Configuration Editor page, ensure the following attributes or elements exist and are configured correctly:

The allowDoubleEscaping attribute is set to **True**.

The requestLimits element exists.

The requestLimits element has a maxAllowedContentLength attribute and its value is set to **2147483647**.

For more information, see How to: Add and Remove Web.config Settings Programmatically.

- After you have made changes to these settings, in the **Actions** pane, click **Apply**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
