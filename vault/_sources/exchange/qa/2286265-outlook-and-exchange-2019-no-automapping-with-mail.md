---
title: "Outlook and Exchange 2019 no Automapping with mail of second domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2286265/outlook-and-exchange-2019-no-automapping-with-mail
question_id: 2286265
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Outlook and Exchange 2019 no Automapping with mail of second domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2286265/outlook-and-exchange-2019-no-automapping-with-mail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi dear Experts!

we have an Exchange Server 2019 and Outlook (365) on the Client.

We use a Domain domain1.de for 90% of our mailboxes and a second domain domain2.de for a few mailboxes.

Everything worked fine till a couple of month ago.

Now, if i give a user full access to a mailbox with the second domain, the mailbox is not shown in outlook.

I even can not add it manually if i configure an additional mailbox in extended settings of my mailbox.

Then outlook freezes!

Automapping script under Outlook configuration test, shows, that it should be connected, like other mailboxes with full access.

Mailboxes that was configured "full access" a long time ago, still work fine. But if i disable full access and enable it again. It won't work anymore. 

If i connect the domain2.de-mailbox with adding a new account name+password, it doesn't find the mailbox. If the mailbox has an alias with domain1.de and i put in that, then it finds the mailbox and connects it. Then it shows the mailbox even as ******@domain2.de in outlook (as it is correct).

Therefore i can not use shared mailboxes with domain2.de.  Only the ones that was configured long ago.

Is there somthing you can help me with?

Thank you very much, Alexander Knubben

IT-Admin, FHD-GmbH

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-07-03*

Thank you TiNo-T,

i tried out. In Outlook Web Access (OWA) i can add a shared mailbox in the tree left side. No error.

But in outlook on Desktop-PC in options of account ->advanced ->additional mailbox, if i add a mailbox with domain2.de it stucks and than outlook closes.

Automapping doesn't work. In E-Mail Autoconfiguration test: in XML there is an entry for all mailboxes with domain2.de.  But do not appear in outlook.

If i try to add a seperate account with ******@domain2.de it doesn't find the mailbox. i had to use an alias mail with ******@domain1.de. Than its resolved and shown in outlook as ******@domain2.de.

So maybe i have a DNS problem or something?

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-06-24*

Dear @Alex-FHD  

Thank you so much for contacting Microsoft Q&A Support. 

I saw you're having trouble getting the shared mailbox to show up in Outlook on your desktop. I ran a few tests and found a workaround that might help. 

Could you please try adding the shared mailbox through Outlook Web? Once it's added there, open your Outlook desktop app and give it a refresh. Then, you can check it should pop up automatically. 

That method worked for me, so hopefully it'll work for you. 

Please understand that our forum is a public platform, and we will modify your question to hide your organization domain name in the description. Please notice to hide these personal or organization information next time you post error or some information to protect personal data. 

-  Web version: 

-  Desktop app version: 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
