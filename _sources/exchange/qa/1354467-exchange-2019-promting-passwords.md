---
title: "Exchange 2019 promting passwords"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1354467/exchange-2019-promting-passwords
question_id: 1354467
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 promting passwords

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1354467/exchange-2019-promting-passwords (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon!

Outlooks 2010, 2013, 2016 constantly ask for a password. Some users today, others tomorrow. I tried to add registry entries about Autodiscover, I tried to clean saved credentials in Windows- it doesn't help. Could there be a problem on the server side ?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-08-30*

Hi @Иван Галашов ,

Outlook password prompting issues could be caused by various factors, so it might be hard and time consuming to troubleshoot. 

With that being said, since from the description, multiple versions of Outlook clients are affected, it indeed could be an issue on the Exchange server side. Could you please provide more details so that we can better understand the situation?

-  Does this issue affect all users in your organization? Any difference inside or outside the organization's network?

-  What are users doing when the password prompts, launching Outlook or doing any particular task in Outlook?  

-  Will the password pop up stop if the user input the correct credentials? 

-  Could you try to catch a screenshot of the Connection Status in Outlook when the issue occurs? Do remember to remove all personal information like domain name, email addresses involved when posting the image.  

While Outlook is running, click the CTRL key and then right-click the Outlook icon in the system tray, select “Connection Status”.  

Besides, it's recommended to patch both Outlook clients and Exchange server to the latest build. This can make sure we are not troubleshooting an issue here that has already been solved.

By the way, Outlook 2010 and Outlook 2013 have already reached the end of lifecycle. Actually, according to this document, Outlook 2010 is not listed as the supported clients for Exchange 2019. So, it's highly recommended to upgrade to the supported versions of Outlook as soon as possible.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
