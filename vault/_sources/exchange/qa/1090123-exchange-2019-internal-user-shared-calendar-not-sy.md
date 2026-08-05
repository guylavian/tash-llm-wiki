---
title: "Exchange 2019 : Internal User shared calendar not syncing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1090123/exchange-2019-internal-user-shared-calendar-not-sy
question_id: 1090123
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 : Internal User shared calendar not syncing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1090123/exchange-2019-internal-user-shared-calendar-not-sy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Recently we updated the SSL cert for an Exchange 2019 server, this broke Autodiscover and we had to reset some virtual directories and add SAM's to SSL to get working. Long story short, external autodiscover is working and passes the Exchange AutoDiscover MS checker tool. However there are some weird left-over bugs.    

All internal users now have a certificate pop-up that has the internal server name instead of the name on the certificate. Running     

```
Get-ClientAccessServer -Identity (Server) | fl
```

shows that -AutoDiscoverServiceInternalUri is set to the correct https://mail.externalserver.com/AutoDiscover/AutoDiscover.xml so I'm not sure where the internal network user is getting the internal address or cert after resetting the profile. This may be a separate issue, and aside from the pop-up may not be causing issues.    

The other issue is that even though mail flow is working fine desktop/mobile both internally and externally, the internal user who we reset the profile now is not syncing on shared calendars. Strangely enough, OWA works (accessing OWA from internal) and she can access and update events and they show for all other users of that shared calendar. But even though she has access to the shared calendar via Outlook on her desktop, no changes/updates/new events she adds sync to any other user.    

Verified permissions to the calendar correct by adding same permissions to another user that accesses shared calendar externally and they can change/update/add events just fine and they propagate for all users of that shared calendar.    

Any thoughts or pointers would be much appreciated, thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-30*

For future reference: the final fix for the certificate popup was ensuring all VirtualDirectory internal URL/Uri's pointed to the same external, as well as setting the external site record for DNS to the internal server (not internal to external as might be assumed), seems counter-intuitive but it worked and we now no longer get the internal certificate pop-ups.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-16*

If you want to let multiple users in your organization use the same calendar, try the shared calendar included in the Shared Mailbox. The shared calendar is made for multiple users using the same calendar. Any member of the shared mailbox can create, view, and manage appointments on the calendar, just like they would their personal appointments. Everyone who is a member of shared mailbox can see their changes to the shared calendar. To learn more about Shared mailbox in Office 365, here for your reference:    

Create a shared mailbox    

Open and use a shared mailbox in Outlook    

Otherwise, if you still want to use the same Exchange account for multiple users, I suggest you try to use Outlook Web App (OWA) that connects directly to the Exchange server to see how it goes.
