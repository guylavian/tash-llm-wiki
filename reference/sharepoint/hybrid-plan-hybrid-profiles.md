---
title: "Plan hybrid profiles - SharePoint Server"
type: reference
domain: sharepoint
slug: hybrid-plan-hybrid-profiles
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/hybrid/plan-hybrid-profiles
family: hybrid
documentKind: "concept-article"
abstract: "When you have both SharePoint Server and Microsoft 365, by default, users have a different profile in each location. This can lead to a confusing profile experience for your users. With hybrid profiles, users have a single profile in Microsoft 365 where they can maintain all of their profile information."
---

# Plan hybrid profiles - SharePoint Server

Note

Plan hybrid profiles

# Plan hybrid profiles

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When you have both SharePoint Server and Microsoft 365, by default, users have a different profile in each location. This can lead to a confusing profile experience for your users. With hybrid profiles, users have a single profile in Microsoft 365 where they can maintain all of their profile information.

If Office Delve is part of your Microsoft 365 organization, user profiles will be integrated with Delve and users can discover info and documents and see what their teammates are working on. If you've deployed cloud hybrid search, users can also find on-premises documents through Delve.

Profile redirection in SharePoint hybrid deployments

## Profile redirection in SharePoint hybrid deployments

Hybrid profiles redirects hybrid users to their profiles in Microsoft 365. This ensures that hybrid users have a single place for their profile information. Hybrid profiles is available with both SharePoint Server 2013 and SharePoint Server 2016.

Profile redirection works as follows:

Profiles for all hybrid users are in Microsoft 365. Selecting a hybrid user's profile in SharePoint Server redirects you to their profile in Microsoft 365 (even if you're not a hybrid user yourself).

If you choose to use a SharePoint in Microsoft 365 audience when you configure hybrid sites features, non-hybrid users (those not in the audience) retain their SharePoint Server profiles, and they also have profiles in Microsoft 365 if they are licensed users.

Moving custom profile properties to Microsoft 365

## Moving custom profile properties to Microsoft 365

Many enterprises have business requirements to replicate custom attributes to the SharePoint in Microsoft 365 user profile service. Some user attributes are synchronized from Active Directory Domain Services to Microsoft Entra ID. You can select which attributes are replicated from Active Directory Directory Services to Microsoft Entra ID. However, a standard set of attributes are replicated from Microsoft Entra ID to the SharePoint in Microsoft 365 user profile store in Microsoft 365. This set of attributes cannot be customized like it can in SharePoint Server.

Where in SharePoint Server you might use Business Connectivity Services or Microsoft Identity Manager to import custom profile properties that are not located in Active Directory Directory Services, SharePoint in Microsoft 365 does not support these solutions. For custom properties in SharePoint in Microsoft 365, a user profile bulk update API is available.

The bulk update process works like this:

You compile the needed profile data from SharePoint Server, your line-of-business system, or any other external system, into a JSON formatted file.

The tool uploads the JSON file to Microsoft 365 and queues an import process.

A timer job running in SharePoint in Microsoft 365 checks for queued import requests and performs the import operation based on the API calls and information in the provided file.

For more info about the bulk update API, see Introducing Bulk UPA Custom Profile Properties Update API for SharePoint in Microsoft 365.

Working with Delve in SharePoint hybrid deployments

## Working with Delve in SharePoint hybrid deployments

If Delve is part of your Microsoft 365 organization, user profiles will be integrated with Delve, otherwise you'll have standard Microsoft 365 profiles. If you haven't used Delve before, you'll want to learn more about it and how to administer it. Delve user profiles contain the same properties as SharePoint in Microsoft 365 profiles and can be imported in the same manner, as described above in Moving custom profile properties to Microsoft 365.

Setting up hybrid profiles

## Setting up hybrid profiles

Hybrid profiles is part of several hybrid feature bundles for SharePoint Server. For details, see Hybrid sites features and OneDrive.

See also

## See also

Other Resources

#### Other Resources

About user profiles in SharePoint in Microsoft 365

Additional resources

## Additional resources

- Last updated on 
		2023-10-11
