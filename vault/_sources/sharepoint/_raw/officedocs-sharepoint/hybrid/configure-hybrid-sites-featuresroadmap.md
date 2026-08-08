---
title: "Configure hybrid sites features - roadmap - SharePoint Server"
description: "Learn how to configure hybrid sites features for SharePoint in Microsoft 365 hybrid with Microsoft 365."
ms.topic: how-to
---
Note

Configure hybrid sites features - roadmap

# Configure hybrid sites features - roadmap

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article provides a roadmap for configuring hybrid sites features. Follow these steps in the order shown. If you already completed a step when you followed a different roadmap, skip that step, and go to the next one.

| **Step** | **Description** |
| --- | --- |
| 1. Configure Microsoft 365 for SharePoint in Microsoft 365 hybrid | Configure your Microsoft 365 for enterprises organization for a hybrid environment, including registering your domain, configuring UPN suffixes, and synchronizing your user accounts. |
| 2. Set up SharePoint in Microsoft 365 services for hybrid environments | Configure the needed SharePoint in Microsoft 365 services for hybrid search, including User Profiles, MySites, and the Application Management service. |
| **3. (SharePoint Server 2013 only) Install the September PU for SharePoint Server 2013** | Install the September 2015 PU or higher for SharePoint Server 2013. (We recommend installing the latest PU.) |
| 3. Run Hybrid Configuration Wizard | Configure hybrid sites features by running the Hybrid Configuration Wizard in Microsoft 365. |
| 4. Quick test | Check to make sure hybrid sites features are working:  
  Log in to a SharePoint Server as a regular user. (Be sure you're a member of the correct audience if you used audiences.)  
  Select the Follow link at the top of the page.  
  You should see a small pop-up under **Follow** letting you know that you're following the site. Select this pop-up and note that it navigates to your personal site, and the list of sites you're following in SharePoint in Microsoft 365. |

The extensible hybrid app launcher

## The extensible hybrid app launcher

The app launcher is included as part of SharePoint Server 2016. If you want to add it to SharePoint Server 2013, open the SharePoint 2013 Management Shell and run the following cmdlet:

```
install-SPFeature SuiteNav
```

For each site collection where you want to use the feature, run the following cmdlet:

```
Enable-SPFeature suitenav -url <SiteCollectionURL>
```

Video demonstration

## Video demonstration

This video shows a walkthrough of configuring sites features.

**Video: Configure hybrid sites features**

See also

## See also

Concepts

#### Concepts

Hardware and software requirements for SharePoint in Microsoft 365 hybrid

Accounts needed for hybrid configuration and testing

Additional resources

## Additional resources

- Last updated on 
		2023-03-14
