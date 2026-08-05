---
title: "Active Directory updates delay"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2077656/active-directory-updates-delay
question_id: 2077656
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory updates delay

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2077656/active-directory-updates-delay (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If we amend details for a user (eg: user dept or job title) in our internal HR and AD it seems to be fairly fast. However, the changes to filter through to Azure AD and Sharepoint can often take several days or even 2 weeks.

This causes a lot of headaches as users keep chasing us in support.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-24*

Hello

It sounds like you're experiencing delays when changes made in your internal HR and AD systems are reflected in Azure AD and SharePoint. Based on the information I found, here are a few insights:

 

Synchronization Delays: Changes in Azure AD, such as updates to user details or security groups, can take some time to reflect in SharePoint Online. The synchronization process is not instantaneous and can vary based on workloads and the specific changes being made.

 

User Profile Sync: When you update user properties in Azure AD, these changes are reflected in SharePoint Online User Profile Application (UPA). However, the profile properties that are synced by the UPA sync process are not configurable, and synchronization times can vary.

 

Security Group Changes: If you add a user to a security group in Azure AD, it may take some time for these changes to be reflected in SharePoint Online. This delay can be due to the time it takes for the synchronization job to run and update the permissions in SharePoint.

 

Manual Refresh: In some cases, you might need to manually refresh or re-sync the user profiles in SharePoint Online to expedite the process. This can be done using PowerShell commands or through the SharePoint admin center.

 

If you continue to experience significant delays, it might be helpful to reach out to your IT support team for further assistance. They can provide more specific guidance based on your organization's setup and any potential issues that might be causing the delays.
