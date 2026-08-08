---
title: "An Azure Active Directory call was made to keep object in sync between Azure Active Directory and Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4552836/an-azure-active-directory-call-was-made-to-keep-ob
question_id: 4552836
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 43
qa_tags: []
---
# An Azure Active Directory call was made to keep object in sync between Azure Active Directory and Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4552836/an-azure-active-directory-call-was-made-to-keep-ob (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

An Azure Active Directory call was made to keep object in sync between Azure Active Directory and Exchange Online. However, it failed. Detailed error message: Resource '27878033-846b-4e54-94ae-b4299c5e9184' does not exist or one of its queried reference- property objects are not present. RequestId : 17957a88-b7b1-4ebb-ad56-f4c47dc83a81 The issue may be transient and please retry a couple of minutes later. If issue persists, please see exception members for more information.

Seeing this error when creating a new mail contact then adding them to a distribution group. We had a powershell script running this for a very long time with no issue then around the beginning of April 2021 this error started appearing when running the Add-DistributionGroupMember line. If I wait a few minutes then manually run it in powershell then it adds that contact. It seems there is now a lot of latency between when you create a contact and when you can add them to a distribution group. Something had to have changed on Microsoft's backend to cause this. I'd love a solution because a lot of my automation scripts are failing now because it creates the member then immediately tries to add them to the group. I'd like to reiterate that this was just working a little over a month ago and we haven't changed our scripts.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-14*

Hello GavinBarnes7,

Based on your description, I did a lot of more research and tests on Mail Contact between Azure AD and Exchange Online, First created a test mail contact with command New-MailContact, when it successfully, navigate to Azure AD PowerShell with command Get-AzureADContact/Get-MSOlContact immediately, however it seems has some minutes delay to find it from Azure AD side. I tried to do more research and see if there is any specific sync cycle time between Azure AD and Exchange Online, generally as far as I know when the new objects provisioned in Exchange Online, it may take some minutes to make the new objects provisioned in Azure AD.  However, I can find limited Official information details on the Sync Cycle.

On another hand, for the objects provisioned from backend, currently we have limited resource in the forum to help check it, if you concerned about the new objects provisioning between Exchange Online and Azure AD, it is recommended that please escalate this case to Microsoft 365 backend team, and the scenario you got need further check from the backend side.  For some more information I will send to you via Private Message (PM), please check it at your convenience, thanks.

Your understanding and patience will be highly appreciated.

Best Regards,

Oliver
