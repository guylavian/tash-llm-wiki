---
title: "Delete email addresses from a deleted Exchange child server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1477453/delete-email-addresses-from-a-deleted-exchange-chi
question_id: 1477453
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Delete email addresses from a deleted Exchange child server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1477453/delete-email-addresses-from-a-deleted-exchange-chi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey, ( sorry for my English )

I work in an offline field, I have several Exchange servers.

One of them was brutally deleted along with the active directory that hosted it.

I keep seeing email addresses on my DAG.

It is impossible for me to delete these addresses, even in powershell.

Even in the adsedit, I don't see these addresses

On the ECP I have the visual on these addresses but when I want to delete them manually, the following message appears :

Calling the Microsoft Exchange Active Directory Topology service on server "TopologyClientTcpEndpoint (localhost)" returned an error.

Error Details None

suitable domain controller found in domain "xxxxxxxxx"

This domain no longer exists

Please Help me

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-07*

indeed but it returns me the following error: "Windows cannot delete the xxxxxxx object because: A reference was returned by the server

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-01-07*

Email Addresses are associated with AD accounts, not servers. 

If you need to remove the email addresses, use ADUC or ADISDIT or PS and remove from the actual AD accounts.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-07*

Hey,

thank you for the answer

But this does not work, because the Database and the server are deleted from ADSEDIT.

When I do a Get-Mailbox, get-mailboxdatabase etc... it doesn't return anything

However, I continue to see it in my mailbox list.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-05*

Hi @anthony monsigny  ,

Welcome to post our Q&A forum!

Based on your description, it seems like the email addresses are still present in the DAG even though the server hosting them has been deleted. Here are some steps you can try to remove these email addresses:

-  Open the Exchange Management Shell (EMS) and run the following command to remove the active database copies from the DAG member server:

```
Remove-MailboxDatabaseCopy -Identity \
```

-  Next, execute the following command in the EMS to remove the DAG member server:

```
Remove-DatabaseAvailabilityGroupServer -Identity  -MailboxServer 
```

If you’re still unable to delete the email addresses, you may want to try removing the DAG member server using the Exchange Admin Center (EAC).

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
