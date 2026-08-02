---
title: "Software update management documentation — pages 321-321"
type: reference
domain: sccm
slug: sccm-intune-configmgr-sum-p0321-0321
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-sum-p0321-0321
family: sccm
documentKind: "doc"
abstract: "There are several methods for configuring Group Policy on computers in the environment. For computers that are not on the domain, a registry key setting can be configured that allows signed content from an intranet Microsoft Update service location. The following procedures prov"
---

# Software update management documentation — pages 321-321

<!-- p.321 -->

There are several methods for configuring Group Policy on computers in the
environment.

For computers that are not on the domain, a registry key setting can be configured that
allows signed content from an intranet Microsoft Update service location.

The following procedures provide the basic steps that can be used to configure Group
Policy for computers on the domain and a registry key value on computers that are not
on the domain.

To configure Group Policy to allow WUA to scan for
published updates
   1. Open the Group Policy Object Editor Microsoft Management Console (MMC) snap-
     in with a user that has the appropriate security rights to configure Group Policy.

   2. Click Browse and select the domain, OU, or GPOs linked to the site where the
     configured Group Policy will propagate to the desired client computers. Click OK,
     click Finish, click Close, and then click OK.

   3. Expand the selected policy setting in the console tree, expand Computer
     Configuration, expand Administrative Templates, expand Windows Components,
     and then click Windows Update.

   4. In the results pane, right-click Allow signed content from intranet Microsoft
     update service location, click Properties, click Enabled, and then click OK.

Feedback
Was this page helpful?      Yes    No

Provide product feedback
