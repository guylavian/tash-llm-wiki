---
title: "Exchange Online photo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/283591/exchange-online-photo
question_id: 283591
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange Online photo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/283591/exchange-online-photo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our user's corporate photos are not displaying in Exchange Online, therefore not in Outlook. We thought we had this resolved from a prior issue, but it might be related. We have a hybrid setup with AD, SharePoint, and Exchange 2013 on-prem, and Azure AD, Exchange Online, Teams, etc in the O365 cloud. For security purposes we have user corporate photos in on-prem AD and are displayed in SharePoint. These photos were also in all O365 platforms. With the adoption of Teams, users found they could update their photos through the client to whatever they want (cartoon, pets, etc) and that would update the O365 platforms, but not on-prem. This would cause an issue with the security purpose when we move to SharePoint Online. I opened a case with Premier support (22561262) to resolve this issue, and this was done with the "classic" Exchange admin center that does not display photos, the "new" Exchange admin center that does display photos was not available at that time, or at least I don't recall the option. First on the Default OWA Policy, I set SetPhotoEnabled to False to prevent users from updating their photo. We then did the following steps in mass with a script, I did this on my own account last week and my photo is still not in EXO: 1. removed my photo from on-prem AD. 2. run a couple AAD syncs, confirmed my photo was not displayed in any O365 platforms. 3. ran this command against my O365 mailbox: Remove-UserPhoto -Identity <userid> -ClearMailboxPhotoRecord. The -ClaearMailboxPhotoRecord is supposed to set the mailbox to sync the photo from AAD again. 4. upload my photo into on-prem AD. 5. run more AAD synces, confirmed my photo displayed in all O365 except EXO. The odd thing is, for a while new employees had their photo in EXO, it was only existing employees that were affected. After applying our newly purchased E5 license all employees are affected. I can't be positive they are related, but the timing is suspect.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-23*

@Shepherd, J       

From this article, we can know that:    

    

The picture between local AD and AAD only sync one time, it will not sync later.    

So, you need to change/set photo from AAD rather than local AD. The OWA policy can only prevent user from change photo from OWA, they still could change from teams, SharePoint and other Office 365 products. If you want to prevent user from modifying photo, you still need to do limitation from those products.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
