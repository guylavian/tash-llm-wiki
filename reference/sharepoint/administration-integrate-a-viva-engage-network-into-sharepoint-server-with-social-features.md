---
title: "Integrate a Viva Engage network into SharePoint Server with social features - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-integrate-a-viva-engage-network-into-sharepoint-server-with-social-features
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/integrate-a-viva-engage-network-into-sharepoint-server-with-social-features
family: administration
documentKind: "integration"
abstract: "Learn how to integrate a Viva Engage network together with the SharePoint Server environment where you already use SharePoint social features."
---

# Integrate a Viva Engage network into SharePoint Server with social features - SharePoint Server

Note

Integrate a Viva Engage network into SharePoint Server with social features

# Integrate a Viva Engage network into SharePoint Server with social features

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This scenario describes the prerequisites and recommended steps to integrate a Viva Engage network together with the SharePoint Server environment where you already use SharePoint social features.

Scenario prerequisites

## Scenario prerequisites

For this scenario, we assume that:

You have SharePoint Server 2019, SharePoint Server 2016 or SharePoint Server 2013 SP1 or later installed.

Users already use the SharePoint Server Newsfeed social feature.

You're ready to switch to your Viva Engage network.

Scenario challenges

## Scenario challenges

Many organizations already use social features in their SharePoint Server installation and have active and engaged communities that use these features. If you're ready to move towards Viva Engage, you have to manage both the technical implementation and the migration of users from one system to another.

Important

There are no tools or processes available to help you move content from a Community Site to a Viva Engage Group. Going forward, you can keep the data in a Community Site and put a link on the SharePoint Community Site that points to the Viva Engage group where future discussions will occur.

Some communities might not want to immediately move to Viva Engage Groups. It's okay to let them continue to use the Community Site.

For new or old team sites, there's no option to automatically enable Viva Engage. Each site owner has to add Viva Engage using Viva Engage Embed or another custom integration. For information about how to use Viva Engage Embed to add a Viva Engage feed to a SharePoint page, see Add the Viva Engage embed widget to a SharePoint page.

SharePoint Server 2013

### SharePoint Server 2013

A common problem in SharePoint Server 2013 installations is that social features don't work across multiple farms. When you move to a single Viva Engage network, you eliminate this problem.

Many customers have active SharePoint Communities based on the Community Site Collection template. After you deploy SharePoint Server 2013 SP1, the Community Site Collection template is still available to use. A Community Site resembles a Viva Engage Group. We recommend that you have the users in these sites start conversations in new Viva Engage Groups. By using a Viva Engage Group, a community can share information, ask questions, and seek answers to problems.

Step 1: Set up directory synchronization

## Step 1: Set up directory synchronization

Microsoft 365 uses Microsoft Entra ID for identity management, and Viva Engage can be set up to Enforce Microsoft 365 identity for Viva Engage users. If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Microsoft Entra ID by using Microsoft Entra Connect.

For more information, see Plan for directory synchronization for Microsoft 365 and Integrate your on-premises directories with Microsoft Entra ID.

Step 2: Disable default SharePoint Server social features

## Step 2: Disable default SharePoint Server social features

After you set up directory synchronization, disable the default SharePoint Server social features.

Step 3: Use Viva Engage Embed

## Step 3: Use Viva Engage Embed

After you disable the default SharePoint Server social features, use the Viva Engage embed widget to include Viva Engage feeds on SharePoint pages.

See also

## See also

Concepts

#### Concepts

Integrate Viva Engage with on-premises SharePoint Server environments

Social scenarios with Viva Engage and SharePoint Server

Other Resources

#### Other Resources

Integrate Viva Engage with other applications

Viva Engage - Admin Help

Additional resources

## Additional resources

- Last updated on 
		2023-10-11
