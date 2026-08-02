---
title: "Microsoft Exchange is no longer pushing contacts to my devices (nor can the contacts be fetched by the devices)."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182759/microsoft-exchange-is-no-longer-pushing-contacts-t
question_id: 1182759
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# Microsoft Exchange is no longer pushing contacts to my devices (nor can the contacts be fetched by the devices).

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182759/microsoft-exchange-is-no-longer-pushing-contacts-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In early January 2023, Microsoft Exchange stopped syncing contacts to my Apple iPhone or Windows 10 laptop / MS Outlook. Email still works fine, though. I can delete my profiles on both devices and redownload everything (as an extremely time-consuming workaround), but new individual contacts (or updates to old contacts) are both not getting pushed out by Microsoft Exchange, nor can they be fetched by iPhone or Outlook.

ALL of the obvious fix attempts have been done already. Devices rebooted, software and IOS updated, and all settings verified (everything worked fine for years until just 6 weeks ago, with nothing altered on my end). Both iPhone and MS Outlook can send new contacts to Microsoft Exchange (where I've verified that all of the contacts do correctly reside), but Exchange is not sending them back out to other devices. And any new contacts created within Exchange are also not getting sent out.

The testing I've done suggests there is something internal within Exchange that is not sending the new and revised contacts back out.  Outlook and iPhone can send contacts to the Microsoft Exchange server, but nothing comes back.  I have Microsoft 365 through GoDaddy -- I've gone through their tech support twice with nothing fixed, suggesting it's an issue that is deeper within the Microsoft servers.

This is becoming increasingly frustrating because new contacts are needed for my job. As much as I'd love to get this to happen automatically like it used to, I'd be happy at this point just to have some kind of sync button I can click within Exchange to make it do what it's supposed to do. Please advise!

--- Scott

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-02-22*

Hi @Scott Trimble  ,

Both iPhone and MS Outlook can send new contacts to Microsoft Exchange (where I've verified that all of the contacts do correctly reside), but Exchange is not sending them back out to other devices. And any new contacts created within Exchange are also not getting sent out.

Are you referring to "Outlook on the web"(outlook.office.com) by "Microsoft Exchange"? 

So, the current situation is that, if you add a new contact in the Outlook client for Windows, you can see it in Outlook on the web, but it won't show up on other devices like Outlook on your iPhone; and if new contacts are created in OWA, they won't be reflected to either Outlook for Windows or iPhone, right?

For Outlook on your Windows 10 laptop, if you are currently using Exchange cached mode, please try switching to Online mode by clearing the checkbox of Use Cached Exchange Mode:  

If the issue persists, it's suggested to try creating a new Outlook profile and readd the email account to check the result. See Overview of Outlook e-mail profile for information on creating new Outlook profiles.

For Outlook on the iPhone, I'd also suggest trying to remove the account and add it back to see if there would be any difference.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
