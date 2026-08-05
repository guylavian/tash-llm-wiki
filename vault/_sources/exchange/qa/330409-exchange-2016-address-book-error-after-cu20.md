---
title: "Exchange 2016 address book error after CU20"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/330409/exchange-2016-address-book-error-after-cu20
question_id: 330409
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 address book error after CU20

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/330409/exchange-2016-address-book-error-after-cu20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi to All,   

Updated Exchange 2016 for Hafnium patch with CU20. All fine. But unable to join a new outlook client or an old outlook client to an existing mailbox. All already attached are working. ERCA give error in mapi over http.   

I'm in the same case of that post.  

https://techcommunity.microsoft.com/t5/exchange/an-ehttps://rror-occurred-while-trying-to-get-the-address-book-server/m-p/2198330  

Is there somekind of answer about that?? Thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-25*

Hi @Alessandro Vannini  ,    

ERCA give error in mapi over http.    

Are you getting the exactly same error message as mentioned in the link you shared above? If not, you can remove all personal information and share a screenshot of the error at your end for further analysis.    

By "unable to join a new outlook client or an old outlook client to an existing mailbox", do you mean you cannot configure the Exchange account in Outlook? Does it occur both inside and outside the coporate network?     

Please follow the steps below to have a look at the AutoConfiguration Status in Outlook:    

-  While Outlook is running, hold down the CTRL key and then right-click the Outlook icon in the system tray, select “Test Email Autoconfiguration”.    

-  Enter the username and password, uncheck “Use Guessmart” and “secure Guessmart authentication” boxes. Then click the “Test” button.    

-  Once it runs, Check the Log tab.    

Furthermore, it's suggeste to tun the command below to check the authentication methods enabled on the mapi virtual directory:    

```
Get-MapiVirtualDirectory | fl server, Name, *URL*, *auth*
```

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
