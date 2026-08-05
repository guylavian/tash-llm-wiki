---
title: "Discrepancy Between Azure AD Connect Configuration JSON and GUI: Outdated OU Listed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1853189/discrepancy-between-azure-ad-connect-configuration
question_id: 1853189
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Discrepancy Between Azure AD Connect Configuration JSON and GUI: Outdated OU Listed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1853189/discrepancy-between-azure-ad-connect-configuration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have encountered an issue with Azure AD Connect's configuration export functionality. When I navigate to "View or export current configuration" and select "Export settings," the resulting .json file contains a section called "containerInclusions" which lists all containers being synced.

However, I noticed a discrepancy between the containers listed in the .json file and those displayed in the GUI under "Customize synchronization options." Specifically, the .json file includes the following entry:

```
"OU=WindowsVirtualDesktop,OU=Service,OU=Manual,OU=Groups,DC=OUR,DC=DOMAIN,DC=COM"
```

Upon inspecting this location within the tool, there is no "WindowsVirtualDesktop" option available to select. Additionally, a search of our Active Directory confirms that there is no reference to "WindowsVirtualDesktop," which is an Organizational Unit that was deleted several months ago.

Could you please help me understand why the .json output is showing this outdated information? Any insights or steps to resolve this discrepancy would be greatly appreciated.

## Answers

_No answers on this thread._
