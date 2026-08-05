---
title: "Hybrid self-service site creation - SharePoint Server"
description: "Hybrid self-service site creation redirects the default self-service site creation page in SharePoint Server to the SharePoint in Microsoft 365 Group Creation page. By configuring this feature, you can help your users to create their sites in SharePoint in Microsoft 365 instead of SharePoint Server."
ms.topic: article
---
Note

Hybrid self-service site creation

# Hybrid self-service site creation

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Hybrid self-service site creation redirects the default self-service site creation page in SharePoint Server (/_layouts/15/scsignup.aspx) or (/_layouts/16/scsignup.aspx) to the SharePoint in Microsoft 365 Group Creation page. By configuring this feature, you can help your users to create their sites in SharePoint in Microsoft 365 instead of SharePoint Server.

Hybrid self-service site creation respects your hybrid audience settings. If you use a hybrid audience, members of the hybrid audience will be redirected to SharePoint in Microsoft 365 for self-service site creation, while on-premises only users will continue to be directed to self-service site creation in SharePoint Server.

This setting can be configured independently for each web application in your farm.

Hybrid self-service site creation is available in SharePoint Server 2013 with the March 2017 PU. 
 Hybrid self-service site creation is available in SharePoint 2016 with November 2017 PU.

Configure hybrid self-service site creation using the Hybrid Configuration Wizard

## Configure hybrid self-service site creation using the Hybrid Configuration Wizard

Configuring hybrid self-service site creation is done by using the Hybrid Configuration Wizard in the SharePoint admin center.

Note

If you've previously configured other hybrid features with the Hybrid Configuration Wizard, you can go directly to the SharePoint Central Administration website to manage hybrid self-service site creation. In this case, the hybrid connection has been made and there's no need to run the Hybrid Configuration Wizard again.

**To configure hybrid self-service site creation**

Log on to a server in your SharePoint Server farm as the farm administrator.

From your SharePoint Server computer, open a web browser.

Go to **More features** in the SharePoint admin center, and sign in with an account that has admin permissions in Microsoft 365.

Under **Hybrid picker**, select **Open**.

On the hybrid picker page, select **Hybrid Picker**.

Follow the wizard, and when prompted, select **Hybrid self-service site creation**.

When prompted, select the web application with which you want to use hybrid self-service site creation.

When the Hybrid Configuration Wizard completes, hybrid self-service site creation will be enabled for the web application that you selected.

Manage hybrid self-service site creation

## Manage hybrid self-service site creation

Once you have configured hybrid self-service site creation, you can manage it in the SharePoint Central Administration website.

**To manage hybrid self-service site creation**

In Central Administration, select **Application Management**.

On the **Application Management** page, under **Site Collections**, select **Configure self-service site creation**.

In the **Web Application** section, select the web application where you want to manage hybrid self-service site creation, and then select or clear the **Create Site Collections in SharePoint** check box.

Note

While hybrid users of this web application will be redirected to SharePoint in Microsoft 365 for self-service site creation, the other settings on this page continue to apply to any on-premises only users.

Select **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-03-14
