---
title: "Exchange 2019 PublicFolders are visible even though no PublicFolderMailbox appears as primary"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/272966/exchange-2019-publicfolders-are-visible-even-thoug
question_id: 272966
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 PublicFolders are visible even though no PublicFolderMailbox appears as primary

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/272966/exchange-2019-publicfolders-are-visible-even-thoug (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,  

I am having an issue with our Exchange 2019 PublicFolder Mailboxes. Public folders appear to the Users in Outlook Clients but are not writable, as no new folder can be created. In Exchange Admin Center only two public folder mailboxes appear as "secondary hierarchy".   

When I check into ADSI edit,  the msExchRootPublicFolderMailbox attribute appears to be set to the object GUID of one of the "secondary hierarchies", so there is an existent RootPublicFolderMailbox linked, however it cannot be edited. Also it is not locker for migration.  

Does anyone have an idea what to do or check rather than just recreate the whole public folder hiearchy from scratch with backed-up mails ?  

Thank You !  

(Sorry for any typos;))

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-16*

When I check into ADSI edit, the msExchRootPublicFolderMailbox attribute appears to be set to the object GUID of one of the "secondary hierarchies".    

-Just to confirm, do you mean "MsExchDefaultPublicFolderMailbox" in ADSI-Configuration –Services – Microsoft Exchange – “Your Exchange Org Name”?    

If yes, (make a backup) clear “MsExchDefaultPublicFolderMailbox” and create a PF mailbox again, see if it holds primary hierarchy.    

If not, check the path and what is set there?    

Besides, can new folder be created in EAC?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
