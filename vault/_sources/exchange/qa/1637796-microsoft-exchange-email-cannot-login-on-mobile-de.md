---
title: "Microsoft Exchange Email cannot login on mobile devices"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1637796/microsoft-exchange-email-cannot-login-on-mobile-de
question_id: 1637796
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Microsoft Exchange Email cannot login on mobile devices

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1637796/microsoft-exchange-email-cannot-login-on-mobile-de (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I have encountered a problem when trying to log in to my exchange email via mobile devices (Android/iOS), I have found that I can log in on Gmail app with the exchange option but cannot log in automatically, I need to setup manual login then I succeeded to login.

On the other hand, I've tried to log in using the Outlook Mobile App using automatic login and manual login but both method completely failed.

There was no problem when I tried to log in using a mail client on a PC/Laptop such as Outlook or Thunderbird. I have tried to test the Exchange server settings using testconnectivity.microsoft.com, the result was no problem with Autodiscover or ActiveSync setting.

I never changed or updated any settings on the Exchange server, and there was no Windows update either that was installed. Do you have any experience with this issue, the main issue is that I can't log in Exchange email on mobile devices especially on the Outlook Mobile App automatically or manually.

Waiting for your answer, thanks.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-04-01*

Hi @Support Eranyacloud  , 

Do you have any experience with this issue, the main issue is that I can't log in Exchange email on mobile devices especially on the Outlook Mobile App automatically or manually.

Did you see a Domain\UserName field when configuring the account? If so, enter your full email address, such as ******@yourdomain.com in this field and see if it can work.

If what you see is a Domain field, remove the auto populated domain information in this field, leave it empty, just enter the other fields and then go ahead to see if the account can be added successfully.

If the issue persists, since the issue occurs in Outlook for mobile only, you can try to contact the in-app support, see Get in-app help for Outlook for iOS and Android. Or you may visit the dedicated forum for Outlook mobile app: 

https://answers.microsoft.com/en-us/outlook_com/forum/outlk_mob

Thanks for your understanding.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-30*

Hey there, I experienced a similar issue, as a user of both platforms. Unfortunately and fortunately, both are good options for secure authentication, except, I had to authenticate with eye scanning, and finger print on my Tablet, as well as my iPhone. I was afraid of disabling one or the other and being locked out. I would recommend starting at the root of authentication and trace back to that pivotal moment you enhanced your security. I would suggest downloading your passwords securely, preferably, printing them. Of course as a last resort. If you can find your bug and untangle yourself without loosing access to important websites that is. It sounds tricky. I did however found refuge and trust in one platform. So once you find which biometric is causing the glitch I’d  do a split path on your choice of Oauth. 

Hope you get untangled and let me know if you untie your knott.
