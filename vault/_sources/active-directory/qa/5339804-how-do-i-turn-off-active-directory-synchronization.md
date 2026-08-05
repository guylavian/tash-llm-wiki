---
title: "How do I turn off Active Directory synchronization on a destroyed 2102 server?  Then it will allow me full administrative access for users add/remove."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5339804/how-do-i-turn-off-active-directory-synchronization
question_id: 5339804
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# How do I turn off Active Directory synchronization on a destroyed 2102 server?  Then it will allow me full administrative access for users add/remove.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5339804/how-do-i-turn-off-active-directory-synchronization (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have had the 2012 server destroyed after it being in place for many many years  My Office 365 domain is pc2fix.com.  So if you don't have the physical server anymore how can I make this complicatedly simple change.  I have looked through all of my office 365 admin settings and I found no way of completing this.  I get there may be security verifications and since I am the actual owner of that Office 365 and domain on GoDaddy.  Please help me complete this change.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-18*

Hello PC2Fix**,**

Good day!!

If you no longer have access to the server, you can disable Active Directory synchronization by using the Azure Active Directory Connect tool. 

Once the synchronization is disabled, you should have full administrative access to add and remove users in Office 365. Please note that disabling synchronization will remove all synced users and groups from Office 365, so you may need to re-create them manually.

I understand your concern but since your problem is related to Active Directory synchronization, I would also like to suggest you post your concern in the related community i.e., Ask a question - Welcome to the Azure Community (microsoft.com) to get the detailed help from the experts.

Apologies for redirecting you to different community as the members in the category posted focus on the users with out of the box concerns on Microsoft 365 and have limited knowledge on the Azure Active Directory; so, to get the fast and better assistance, we have redirected you in the correct path.

Appreciate your patience and understanding. Have a great day!!

Best Regards,

S M Nazmun Nur
