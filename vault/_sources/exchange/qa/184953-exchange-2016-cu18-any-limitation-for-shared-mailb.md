---
title: "Exchange 2016 CU18 (Any Limitation for Shared Mailbox connect Outlook?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/184953/exchange-2016-cu18-any-limitation-for-shared-mailb
question_id: 184953
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 CU18 (Any Limitation for Shared Mailbox connect Outlook?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/184953/exchange-2016-cu18-any-limitation-for-shared-mailb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support  

We are handling more clients. so we have created 35 Shared Mailbox  

When we give delegate 35 Shared Mailbox to Users.   

Our User facing issues like Outlook Disconnected frequently.  

Some delegates added may not show up automatically in Outlook. Outlook is limited to displaying only the first 32 entries (If a delegate user has an archive, the user counts as 2 entries).  

Is there any limitation of adding Mailboxes in Outlook?  

How can i design as per our requirement?  

What is the best practice? Cached Mode or Online  

Currently i am using Cached Mode in Outlook  

is it good practice to Use Online?  

What are the impacts if i use Online?  

Kindly advise

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-12-03*

Best practice is to have the primary in cache mode and the shared mailbox not cached:    

https://support.microsoft.com/en-us/help/3115602/performance-and-synchronization-problems-when-you-work-with-folders-in    

    

Limitations for on-prem get a bit tougher:    

https://learn.microsoft.com/en-us/exchange/architecture/mailbox-servers/managed-store/managed-store-limits?view=exchserver-2019    

32 sessions sounds about right:    

    

MAPI on the Middle Tier (MoMT)	n/a	32    

However, it can tough to manage that because there are also throttling considerations:    

https://learn.microsoft.com/en-us/exchange/change-user-throttling-settings-for-specific-users-exchange-2013-help    

Bottom Line Recommendations:    

-  Run Outlook in cache mode    

-  Do not download Shared Mailboxes. Uncheck that option.    

-  Limit the number of shared mailboxes uses can open. Consider not auto-mapping them to a user if they require access to more than 10 or so.    

https://learn.microsoft.com/en-us/outlook/troubleshoot/profiles-and-accounts/remove-automapping-for-shared-mailbox#:~:text=To%20disable%20automapping%2C%20use%20Windows,the%20AutoMapping%3A%24false%20parameter.    

```
Add-MailboxPermission -Identity  -User  -AccessRights FullAccess -AutoMapping:$false
```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-04*

Hi @SathishkumarSingh-4967     

As per your concern about the Cached mode and Online mode, basically Cached Exchange Mode is the preferred (and default) configuration in Outlook client. It no longer depends on continuous network connectivity and most users find it works faster than Online mode.     

However, considering the fact that the larger the data file, the more application pauses or performance issues you may experience, agree with Andy that it's recommended to keep running the primary account in Cached mode, and meanwhile, disabling the caching of all shared folders by Clearing the checkbox of "Download shared folders".    

Here's an official document about Cached Exchange Mode and Online Mode for your reference:    

Plan and configure Cached Exchange Mode in Outlook 2016 for Windows    

Regarding the limit of 32 sessions, please refer to the suggestions provided by Andy to disable the auto-mapping. Furthermore, you may consider creating some public folders instead for shared access to information within your organizations. See Public folders.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
