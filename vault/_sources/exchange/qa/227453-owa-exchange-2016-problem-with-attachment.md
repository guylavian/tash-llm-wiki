---
title: "OWA Exchange 2016 problem with attachment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/227453/owa-exchange-2016-problem-with-attachment
question_id: 227453
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# OWA Exchange 2016 problem with attachment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/227453/owa-exchange-2016-problem-with-attachment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I will log in on the OWA login page username: (user I have access to) password: (my) RSA code (user to which I have access and I have his RSA token) below I will choose the option - use another login name and enter: (domain \ my username) I will log in to OWA in order I see my email and my calendar I see the emails and calendar of the user I have access to. Please help: in the calendar of the user to which I have access there is an event with an attachment to the word document. When opening, a new window will open in which is the address on the o365 repository, WHICH I BUT I DO NOT USE. the user to whom I have access has created the attachment on his local computer, the user to whom I have access does not have an O365 account (does not use) - WHY DOES THE ATTACHMENT NOT BE STRAIGHT EQUALLY BUT TRYING TO OPEN O365? I will log in to OWA under my account login name: (my) password: (my) RSA: (my) I will not enter an item - log in with a different login name. After logging in, I see my e-mail, my calendar. The problematic event in the calendar will NOT OPEN IN O365, but it will be downloaded to the computer immediately. - That's what I want to achieve no one in the team uses O365, everything is local to the 2016 exchange server

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-01-12*

Hi, what CU is 2016 at? This sounds like a known bug that was fixed in CU19:    

https://support.microsoft.com/en-us/help/4588297/attachments-not-downloaded-or-previewed-from-owa    

You can download CU19 here:    

https://support.microsoft.com/en-us/help/4588884/cumulative-update-19-for-exchange-server-2016    

See:    

https://learn.microsoft.com/en-us/answers/questions/112628/exchange-2016-after-installation-of-cu-18-attachme.html    

One workaround we discovered so far.    

Instead of "Open another mailbox..." you can access the shared mailbox with "Add shared folder..." instead.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

thank you all for the answers  and guidance on the bug in the MS update. Thanks!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-13*

Hi @Lukáš Gajarský  ,    

From your description, agree with Andy that it seems like the known issue mentioned in the first link he provided. Please refer to the information shared by Andy, or you can choose one of the following recommended methods:    

-  Use the Microsoft Outlook client to open or download attachments from additional mailboxes.    

-  Access additional mailboxes by using the OWA light version. To use the OWA light version, add "?layout=light" to the URL of the additional mailbox.    

For example:  https://owa.contoso.com/owa/SharedMbx[@](/users/na/?userId=a28c79c1-c609-48db-b55f-1783d1187afb).com/?layout=light    

Should you have further questions on this, please feel free to post back.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
