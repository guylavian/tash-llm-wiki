---
title: "Configure hybrid OneDrive - SharePoint Server"
description: "Connect your on-premises SharePoint Server environment with OneDrive."
ms.topic: how-to
---
Note

Configure hybrid Microsoft OneDrive

# Configure hybrid Microsoft OneDrive

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**This article is part of a roadmap of procedures for configuring SharePoint in Microsoft 365 hybrid solutions. Be sure you're following a roadmap when you do the procedures in this article.**

You can redirect users to Microsoft OneDrive, on the navigation bar or the app launcher, when they select **OneDrive** or **Sites**. This article provides the steps to configure your on-premises environment to connect with OneDrive. You can find an overview of the process in Plan for hybrid OneDrive.

Video demonstration

## Video demonstration

This video shows a walkthrough of configuring hybrid OneDrive.

**Video: Configure hybrid OneDrive**

Note

The SharePoint Migration Tool demonstrated in the video is currently in preview. It is only supported for SharePoint Server 2013. Download the SharePoint Migration Tool.

Configure user permissions

## Configure user permissions

To use OneDrive, your users must have **Create Personal Site** and **Follow People and Edit Profile** permissions. Both are controlled by the user permissions in the User Profile service application.

Verify that the user account that is performing this procedure is a member of the Farm Admins group.

In your on-premises SharePoint Server environment, go to **Central Administration** > **Manage Service Applications**.

Click the User Profile Service Application.

On the **Manage Profile Service** page, under **People**, select **Manage User Permissions**.

In the **Permissions for User Profile Service Application** dialog, select **All Authenticated Users** (or a specific audience that you intend to use as a pilot group of users).

Verify that the **Create Personal Site** and **Follow People and Edit Profile** permission check boxes are selected.

Configure hybrid OneDrive

## Configure hybrid OneDrive

To configure hybrid OneDrive, you must be both a SharePoint Server farm administrator and a Microsoft 365 global admin. Perform these steps on a server in your SharePoint Server farm.

**To configure hybrid OneDrive**

Go to **More features** in the SharePoint admin center, and sign in with an account that has admin permissions for your organization.

Under **Hybrid picker**, select **Open**.

Click **Go to Hybrid Picker Download Page**.

On the SharePoint in Microsoft 365 Hybrid Configuration Wizard page, select **click here**.

Accept the security prompts to install and run the wizard.

On the **SharePoint Hybrid Configuration Wizard** page, select **Next**.

On the **Credentials** page, verify your on-premises credentials and enter your global admin credentials. Select **Validate credentials**, and then select **Next**.

On the **Checking prerequisites** page, select **Next**.

On the **Select the features you want to use in your hybrid environment** page, select the Hybrid OneDrive check box and deselect any other check boxes. Select **Next**.

When the configuration completes, select **Next**.

Add a rating and comments if desired, and then select **Close**.

Create an audience (if necessary)

## Create an audience (if necessary)

If you want to redirect only a specific set of your users from your on-premises environment to OneDrive, you need to use an audience to identify that set of users. If you have an audience set up already that contains just those users, you can use that. Otherwise, you need to create an audience in SharePoint Server. See Create an audience for SharePoint Server for information about how to create an audience for SharePoint. You can also use Microsoft PowerShell cmdlets to create an audience.

**To configure a OneDrive redirection audience**

On the **Central Administration** website, select **Microsoft 365** > **Configure hybrid OneDrive and Sites features**.

Select **Use a specific audience**, and for the audience that contains your Microsoft 365 users, enter the  *audience name*.

Select **OK**.

Verify that then OneDrive links work as expected

## Verify that then OneDrive links work as expected

It can take up to a minute for the changes to be updated in the User Profile service application for your on-premises farm. Because the link may be stored in the user's browser cache, we recommend you wait 24 hours and then verify the links are working.

To check that the links are working as expected, have one of the users in the audience that is using the Microsoft 365 option for OneDrive sign in to your on-premises environment. From the user's personal site, and from the navigation bar or app launcher, have the user select **OneDrive**.

If the user is redirected to Microsoft 365 for OneDrive, everything is working as expected.

If users want to browse to their OneDrive directory directly, they can go to https:// *<yourtenant name>*.onedrive.com in the browser. For example, `https://contoso.onedrive.com` will take users of Contoso tenancy to their OneDrive document library. This is a simple way to bookmark the link for users of OneDrive. Rich clients might not recognize this short URL.

(Optional) Create a search vertical

## (Optional) Create a search vertical

You can set up a search vertical so that you can search content stored in OneDrive. The specific steps to set up the search vertical are in the article Set up Search of OneDrive from SharePoint Server.

(Optional) Customize the Microsoft 365 navigation experience (SharePoint Server 2013)

## (Optional) Customize the Microsoft 365 navigation experience (SharePoint Server 2013)

Now that your users are set up to be redirected to Office 365, you can customize what they see on the navigation bar there. By default, the navigation bar contains the following links: SkyDrive, Viva Engage or Newsfeed, and Sites. If you intend for your users to use only OneDrive, you can remove the other links. If you want to allow your users to interact with Viva Engage or the SharePoint Newsfeed features or to create team sites in Office 365, you can leave those links on the nav bar.

Note

Turn on the appropriate navigation bar links for the set of SharePoint in Microsoft 365 service features that you have purchased. For example, if you have OneDrive with Office on the web, then you would turn on only the OneDrive link, and not the Sites or Newsfeed links. OneDrive with Office on the web does not include the Sites and Newsfeed features and users would see Access Denied messages if they selected the links. You can, however, still choose to turn on Viva Engage as your social network and then turn on the Viva Engage/Newsfeed navigation link.

**To customize the navigation bar**

Log on to Office 365 with an organization administrator account.

On the **Admin** tab, select **SharePoint**.

On the left, select **Settings**.

In the **Top Navigation Bar User Experience** section, specify the links to show or hide on the nav bar.

To save the settings and update the navigation bar, select **OK**.

See also

## See also

Other Resources

#### Other Resources

Plan for hybrid OneDrive

Additional resources

## Additional resources

- Last updated on 
		2023-03-14
