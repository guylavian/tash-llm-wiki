---
title: "Exchange Admin Center on line: how to redirect (outside the org) mail sent to a verified Custom domain?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/252698/exchange-admin-center-on-line-how-to-redirect-outs
question_id: 252698
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Admin Center on line: how to redirect (outside the org) mail sent to a verified Custom domain?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/252698/exchange-admin-center-on-line-how-to-redirect-outs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 2 orgs (recently acquired the second one): first one is on Exchange Online (Office365) (call that one abc.ca) and we are migrating the second one (call that one xyz.ca) from GMAIL; users in that organization are using GMail (eg john@xyz  .ca).     

As part of the migration process I added the xyz.ca domain to our abc Azure Active Directory(AAD)'s list of Custom domain names and started creating  users with that domain in our AAD (say john@xyz  .ca).    

These users are still, for now, using the GMail accounts for mail; they still can receive and send emails in the GMail software using their GMail account (eg john@xyz  .ca).    

The problem is: users on Exchange (say lucy@jaswant  .ca) cannot send emails to these users: they get the Recipient not found by SMTP address lookup error.  However users on other domains (say ******@def.com) cans send emails to the users on the xyz.ca domain.    

In simple terms, it looks like Exchange does not even try to forward these mails «to the internet» because it thinks it's a domain local to the AAD. I've looked at the documentation for Remote Domains and for Exchange Connectors but these do not seem to address this issue.    

I think I could remove the xyz.ca domain from our AAD's list of Custom domains but that would be going backward since I would need to delete the users I created (I mentioned earlier). We plan to move all emails from GMail to Exchange in about 6 weeks (for complex reasons we cannot do it before).     

SO: I am looking for a temporary solution that would in essence say to Exchange «yeah, I know you think the john@xyz  .ca address in within our organization and you can't find such an email address in our organization but it's really out there so please send those emails out there».

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-02-01*

I would follow:    

https://learn.microsoft.com/en-us/exchange/mailbox-migration/migrating-imap-mailboxes/migrate-g-suite-mailboxes

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-01*

Thank you very much for your help.    

The connector does not work - unless I'm doing it wrong (I was not clear I tried it before). Here's the log of the verification email (picture):    

    

«  you can keep those mailboxes that you've created  »: I did not create mailboxes; I created new users in the AAD.    

I guess you agree that I do not have a choice but to delete these new users and then remove the domain from the list.    

Thanks.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-01*

You can try creating a dedicated send connector for a partner organization: Set up connectors for secure mail flow with a partner organization    

If it doesn't work, I would remove the domain from the list and create mail contacts for users from xyz.ca: Manage mail contacts in Exchange Online    

Mail contacts is different from mailboxes, you can keep those mailboxes that you've created and test mail flow with mail contacts before you finish the migration.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
