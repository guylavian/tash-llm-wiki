---
title: "Exchange Server 2016 CU 15 - OWA Http Error 440 on Chrome !"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/112907/exchange-server-2016-cu-15-owa-http-error-440-on-c
question_id: 112907
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange Server 2016 CU 15 - OWA Http Error 440 on Chrome !

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/112907/exchange-server-2016-cu-15-owa-http-error-440-on-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We use Exchange Server 2016 ( CU 15 ) on-premise. We have problems with OWA these days.    

The error we received is "Exchange Server 2016 OWA Http Error 440"    

As a result of my research, I read that some sources are about the CU version. Some sources write that there is a problem specific to chrome.    

I think the problem is with chrome because there are no problems with other browsers.    

Is there anyone who has a problem with this and can solve their problems?    

We found that chrome does not work on the latest version, Version 85.0.4183.121, but works in the previous version.    

If you uninstall chrome and re-install the old version while using the new version, access to OWA fails. I tried this.    

Also, I found this information;    

https://learn.microsoft.com/en-us/answers/questions/89744/chrome-brower-version-85-error-with-adfs-30-when-r.html    

Thank you in advance for your answers,    

Regards,

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-10-01*

Hi @Yusuf Gokkaya  ,    

I did some research about this issue and found some similar reports as well, such as the link below:    

OWA 440 error in Chrome    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

According to the discussion over there, this problem could be temporarily fixed for one launch by deleting the The "Local State" file located at C:\Users\username\AppData\Local\Google\Chrome\User Data    

    

Disabling the chrome://flags/#reduced-referrer-granularity has also been reported to be useful by several users:    

    

Personally I assume this method(disable the flag) is worth trying as it's mentioned as a solution in the link you shared too.    

Last but not least, agree with Andy that it's highly recommended to upgrading to Exchange Server 2016 CU17 or the latest CU18. This official document talks about some effects on customer websites and Microsoft services with the Chrome version 80 or later, as indicated in the Recommendations section, Exchange CU 16 is listed as "must be upgraded":    

    

Hope you can find the above information useful.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-02*

Hi,  

I installed the CU17 version on the exchange servers. Owa HTTP 440 problem has been resolved.  

No action was required on ADFS.  

OWA can be used in the latest version of the chrome browser.  

Regards,
