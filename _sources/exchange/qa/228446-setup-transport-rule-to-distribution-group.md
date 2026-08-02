---
title: "Setup Transport rule to distribution group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/228446/setup-transport-rule-to-distribution-group
question_id: 228446
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Setup Transport rule to distribution group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/228446/setup-transport-rule-to-distribution-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to bcc all emails send to and from our domain emails into the appropriate Group email account. i.e. All emails sent or received from *@ourdomain.com that come from *@clientdomain.com will be bcc'd to the ******@ourdomain.com group email that was created in SharePoint/Teams. I have tried to set up a rule in the Exchange admin but I receive an error message about transport rules not being allowed for distribution lists....We use Microsoft Online 365

## Answer (community) — community member

*upvotes: 7 · updated: 2023-03-03*

I'm a bit late to the game, but I'm adding this for the benefit of others searching for a solution.

The method I use to reference a distribution group as a recipient is to match on the distribution group's email address in the To header.

In a message header condition, you can specify multiple "words," but reference only one header, so to include the CC header, you'd have to create another rule. Adding another condition to the same rule won't work. In a rule with multiple conditions, Exchange uses AND logic, so the match would have to test positive for both the To and CC headers to trigger the action.

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2021-07-09*

I've run into this same issue and solved it with a different approach.  Since our DL's tend to change membership, updating the transport rule didn't seem like a viable option for me so I did the following:  

-  I created a shared mailbox and set the ForwardingAddress to my DL.  I also set the DeliverToMailboxAndForward to $False since I don't want the email stored in the Shared Mailbox.  

-  Next I created my Transport Rule and set it to BCC my newly created Shared Mailbox.  

I don't like having extra shared mailboxes, but since they don't require a license, I just named them with "FORWARD" so I would know what they were for.  I have about 5 of these accounts for special needs and it has solved my issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-17*

I had similar problem while attempting to put a DG as recipient into a Transport Rule on Exchange Online and the DG is synced from my on-premise environment.

In my case having Exchange on-premise in hybrid deployment was the solution as I just created a contact on EXO with same email address as my DG and added this contact as recipient to the Transport Rule on EXO.
