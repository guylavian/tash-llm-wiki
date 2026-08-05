---
title: "Integrate a new Viva Engage network into SharePoint Server - SharePoint Server"
description: "Learn how to integrate a new Viva Engage network into an existing SharePoint Server environment."
ms.topic: integration
---
Note

Integrate a new Viva Engage network into SharePoint Server

# Integrate a new Viva Engage network into SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This scenario describes the prerequisites and recommended steps to integrate a new Viva Engage network together with your existing SharePoint Server environment.

Scenario prerequisites

## Scenario prerequisites

For this scenario, we assume that:

You have SharePoint Server 2019, SharePoint Server 2016, or SharePoint Server 2013 SP1 or later installed.

You don't use the SharePoint Server Newsfeed social feature.

You use Active Directory Domain Services (AD DS) as your identity provider and Active Directory Federation Services (AD FS) 2.0 for identity federation.

You are ready to use a Viva Engage network.

Step 1: Purchase Viva Engage Enterprise

## Step 1: Purchase Viva Engage Enterprise

Viva Engage is included in many Microsoft 365 subscriptions, which means that you might already have licenses for the service.

Step 2: Create your Viva Engage network

## Step 2: Create your Viva Engage network

To set up a Viva Engage network, see Viva Engage admin help.

When you set up your network, enforce Microsoft 365 identity for Viva Engage users.

For information about how users are managed in Viva Engage Enterprise, see Manage Viva Engage users across their life cycle from Microsoft 365.

Step 3: Set up directory synchronization

## Step 3: Set up directory synchronization

Microsoft 365 uses Microsoft Entra ID for identity management, and Viva Engage can be set up to enforce Microsoft 365 identity. If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Microsoft Entra ID by using Microsoft Entra Connect.

For more information, see Plan for directory synchronization for Microsoft 365 and Integrate your on-premises directories with Microsoft Entra ID.

Step 4: Disable default SharePoint Server social features

## Step 4: Disable default SharePoint Server social features

After you set up directory synchronization, disable the default SharePoint Server social features.

Step 5: Use Viva Engage Embed

## Step 5: Use Viva Engage Embed

After you disable the default SharePoint Server social features, you should use the Viva Engage embed widget to include Viva Engage feeds on SharePoint pages.

See also

## See also

Concepts

#### Concepts

Integrate Viva Engage with on-premises SharePoint Server environments

Social scenarios with Viva Engage and SharePoint Server

Other Resources

#### Other Resources

Manage Viva Engage users across their life cycle from Microsoft 365

Viva Engage - Admin Help

Additional resources

## Additional resources

- Last updated on 
		2023-10-11
