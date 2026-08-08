---
title: "User unable to edit OWA signature"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/378886/user-unable-to-edit-owa-signature
question_id: 378886
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# User unable to edit OWA signature

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/378886/user-unable-to-edit-owa-signature (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a user that when she tries to edit her OWA signature, it is greyed out and shows that it is loading but won't allow her to add a signature. She can add one via the mobile app or desktop app but not OWA. When making a settings change and then trying to save, it says:  

Couldn't save your signature  

If the problem continues, please remove any images and try again.  

She used to have a signature set and it never included any images. Additionally, when trying the edit the signature through https://outlook.office365.com/ecp/ it gives her the following error:  

error  

The value '{"id":"AAMkADIyMTkzNDFjLTJlMjAtNGQ3NC1hMTk5LTc2YTFkOTQxNzk3NAAuAAAAAAA3dABzXGDtS724sFIuV7HeAQAukTveU/f5R4wM3n+PEsjnAAAAAAEpAAA=","type":0}' is already present in the collection.  

Any help would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-04*

I too am having this problem (with a couple additional troubles) with just one user.  About two weeks ago she reported that she couldn't sign into an unrelated website, cleared her chrome cache and cookies and now her OWA is all kinds of weird. She can't make any changes to her OWA signature like what Eric reported. We can't turn it on/off, and if you try and make any changes we get the same "couldn't save your signature" error. We can make changes in Outlook app on her computer, but she hates it and this is a VIP so we have to make sure she's happy.  

In addition to this signature issue, if she tries to reply or FWD an email, the reading pane or the break out window will not show any of the original content or if there are attachments.  She can reply and fwd the email and it will go through successfully, but if she wants to edit the prior email content, she can't because it simply just doesn't show in the email window.  Again, Outlook app works fine.  I've tried this user's OWA from multiple systems (mac and PC, and multiple browsers) and the problem follows just this one user account.   

I thought that maybe something in her signature might be the culprit and wasn't allowing original email content to show when she was trying to reply/fwd an email. I actually created an Exchange Admin policy disabling her ability to have a signature in OWA, but all remains the same on her end in OWA.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-03*

Hi @Anonymous   ,  

Only one user have this issue or all users have this issue?  

If you clear the signature and click save, will the same error appear?  

Has the user or administrator changed the any settings of mailbox before this issue occurred?

1.Please try to using another browser to login the mailbox and edit signature.

2.Please check the Outlook Web App policies in the permissions in Exchange admin center.  

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-30*

That is an issue that has already been solved. See EX252201 in the Service Health History in the Microsoft 365 Admin Portal.  

If you are still experiencing this issue, use the Admin portal to report it so they can check whether the fix has been applied successfully to your tenant users.
