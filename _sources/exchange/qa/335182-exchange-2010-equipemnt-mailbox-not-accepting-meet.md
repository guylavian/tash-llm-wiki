---
title: "Exchange 2010 Equipemnt Mailbox Not accepting meeting request automatically"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/335182/exchange-2010-equipemnt-mailbox-not-accepting-meet
question_id: 335182
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange 2010 Equipemnt Mailbox Not accepting meeting request automatically

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/335182/exchange-2010-equipemnt-mailbox-not-accepting-meet (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

It worked previously perfect and suddenly last week all equipment mailboxes are not automatically accepting the meeting request so the users not getting the accepted mail and not showing in the equipment mailbox calendar.  

I checked logged to the equipment mailbox OWA and i can see the meeting requests are coming to the Inbox but its not automatically accepting.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-30*

Hi @Abdul Basith   ,    

Agree with Andy, and you could also check if you have enabled automatically accept booking requests and the settings.    

```
Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq 'EquipmentMailbox'" | Get-CalendarProcessing | Format-List
```

Change equipment mailbox properties    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-29*

I suspect its over quota. Check that and clear out some items.  

Best way is to create a new Outlook profile as that room account and open the maibox directly with Outlook.
