---
title: "IT governance in SharePoint - SharePoint Server"
description: "Learn about key factors in governing a SharePoint service and what to include in a service-level agreement."
ms.topic: article
---
Note

IT governance in SharePoint

# IT governance in SharePoint

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

How will you control the services that you offer? What will you provide with each service? What will you include in service-level agreements for each service? And how do you prevent proliferation of unmanaged servers? These questions should be answered as part of your IT governance plan.

We recommend that you develop a good governance plan when you create an IT service to support SharePoint. A good governance plan ensures that the service meets the business needs of your organization securely and cost-effectively. When you add to the service, a good governance plan helps you do so seamlessly. A good governance plan to run a successful IT service should include:

A Governance team defines the initial offerings of the service and its ongoing policies, and meets regularly to evaluate success.

The policies you develop are communicated to your organization and are enforced.

Users are encouraged to use the service and not create their own solutions. Installations are tracked and rogue installations are blocked.

What is a SharePoint service?

## What is a SharePoint service?

A SharePoint service is an IT service that offers hosted sites based on SharePoint. The benefits of a SharePoint service include backup and recovery, content storage, support for customizations, security, and service levels based on speed and availability as show in the following illustration.

Elements of a successful service

## Elements of a successful service

As you plan and implement your SharePoint service, consider the following elements that can contribute to the success of the governing effort:

**Form and use a governing group.** Your IT service for SharePoint should be governed by a group that includes executive stakeholders, business division leaders, influential information workers, IT managers, and IT technical specialists, among others. The goal of the governing group should be to oversee the service. In this capacity, the governing group defines the initial offerings of the service, defines the service's ongoing policies, and meets regularly to evaluate success.

**Communicate the policies.** The governance policies that you develop must be publicized to your organization. Maintain a website that describes the service.

**Encourage use of the service.** Discourage or block users from deploying their own servers. Instead, encourage them to use the service. Isolated servers may not be configured according to IT security policy and the organization's regulatory requirements. Furthermore, users who deploy their own servers may not properly back up their servers or keep servers up-to date with software patches and updates. Finally, content on servers that are not governed by the service may not be detected by the organization's indexing service, which may create isolated pockets of content.

What to govern in a SharePoint service

## What to govern in a SharePoint service

Determine limits and policies for the areas shown in the following table.

**Areas that should have limits or policies in a governance plan**

| **Area** | **Recommendation** |
| --- | --- |
| Security, infrastructure, and web application policies | How is the system and infrastructure maintained and who has access at what levels? What's the maximum upload size you want to allow? Are you controlling the use of fine-grained permissions? |
| Data protection (backup and recovery) | Vary the level of data protection that you offer based on service levels. Plan how often you back up the farms and how quickly you can guarantee the data is restored. |
| Site policies | Use site policies to help control site proliferation. A site policy defines the life cycle of a site by specifying when the site will be closed and when it will be deleted. When you close or delete a site, any subsites are also closed or deleted. If an Exchange mailbox is associated with a site, the mailbox is deleted from Exchange Server 2013 when the site is deleted. |
| Quotas | Quota templates define how much data can be stored in a site collection and the maximum size of uploaded files. Associate different quota templates with site collections at different service levels. |
| Asset classification | Classify sites and content by value and impact of the content to the organization (such as high, medium, or low business value/impact). That classification then controls other requirements, such as encryption for high business impact information.  
  Impact = Exposure  
  If this leaks, will it hurt my business?  
  Value = Availability  
  If this isn't available, can my business run? |

Service-level agreements

## Service-level agreements

Your organization should create appropriate service-level agreements for each service you provide. A good service-level agreement should include:

The approval process, including the length of time and approvals necessary to create a site.

Costs for users or departments.

Operations-level agreement, which specifies which teams perform which operations and how frequently.

Policies around problem resolution through a support team.

Negotiated performance targets for first load of a site, subsequent loads, and performance at remote locations.

Recovery, load balancing, and failover strategies.

Customization policies.

Storage limits for content and sites.

How to handle inactive or stale sites.

Multilingual support.

Deployment governance

## Deployment governance

In addition to governing services that you offer, you also need to govern installations of SharePoint in your environment.

**Track installations** An Active Directory Domain Services (AD DS) marker named Service Connection Point identifies the SharePoint servers in an organization. Set this marker for each domain in your organization if you want to track installations in all domains. See Track or block SharePoint Server 2010 installations.

**Block installations** You can block installations of SharePoint Server 2016 to prevent users from installing it to unauthorized servers that you don't want to support. Use a Group Policy in Active Directory Domain Services (AD DS) to set a registry key on all servers to block installations. This registry key existed by default in SharePoint Server 2010, but is not included in SharePoint Server 2016. You can create it yourself in the registry if you want to block installations. See Track or block SharePoint Server 2010 installations.

**Keep current with software updates** Keep your servers current. Test and install recommended software updates. See the Updates Resource Center for SharePoint Server 2016.

**Site collection upgrades** Site collections can now be upgraded independently from the content databases. Determine who, when, and how to upgrade site collections when a new version or an update is available. See Plan for site collection upgrades in SharePoint 2013.

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
