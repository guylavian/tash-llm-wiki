---
title: "Exchange 2013 and 2010 coexistence - OWA Premium UI touch layout does not automatically load on mobile devices"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/348153/exchange-2013-and-2010-coexistence-owa-premium-ui
question_id: 348153
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2013 and 2010 coexistence - OWA Premium UI touch layout does not automatically load on mobile devices

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/348153/exchange-2013-and-2010-coexistence-owa-premium-ui (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi MS Q&A experts, as an interim migration step, that will last at least for an year, I have an Exchange 2010 server co-existing with an Exchange 2013. Both fully updated with latest Windows and Exchange updates. After moving the DNS namespace to the new Exchange 2013 CAS I was doing some tests with a test mailbox named "xch2013setup" placed on the xch2013 Mailbox DB. I still haven't moved the arbitration mailboxes to xch2013.  

Mailflow (internal and external) is ok. Proxying between Exchange servers is ok. Opening Outlook client or OWA, from a Windows notebook, with the xch2013setup account, correctly connects to 2013 CAS. OWA from the notebook loads the OWA 2013 Premium UI in desktop mode. Connecting to a mailbox residing on Exchange 2010, correctly loads the meant mailbox, and, regarding owa, I'm presented with the owa 2013 login page and, once logged in, I'm proxied to Exchange 2010 OWA. Then, all seems to work flawlessy.  

However, if I try to open the same mailbox from, for example, an iPad or an Android smartphone (tried with some newer and older OS versions), I'm presented with the OWA Premium UI for mouse layout with IOS and the Light layout version (html4) with Android. If, from the same devices, I enter in the browser address bar "https://<Exchange2013CASURL>/owa/?Layout=tWide" (or tNarrow) it loads the correct Premium UI touch optimized layout.  

I know Exchange 2013 is in extended support phase and maybe I cannot pretend too much (even if a supported solution should work as expected I think, like it is proudly said here), but I wanted to know if the behavior is related to the 2013 server side OWA app that is aging, if it's a coexistence problem, or just a matter of an OWA virtual directory setting...  

Thanks for your help.  

Regards,  

Francesco B. B.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-09*

Ok, you just did confirm my thoughts. Newer Exchange versions work just fine and better with mobile devices.   

My Exchange 2013 is already a CU23 and a fresh install.   

IPad does load the owa desktop version, in fact, touch buttons are missing in the bottom part of the interface.  

Android devices, if are told to load the "desktop" version of the owa site, as I told in my previus post, they correcly load the Premium UI in desktop mode.  

Moreover I have got a reply on StackExchange in which, basically, is told that Owa 2013 has compatibility issues with Android devices. (Here the link)  

I hope to be able to migrate as soon as possible my Exchange infrastructure to, at least, 2019 version. In the meanwhile I will tell my roaming OWA users to use the trailing "?Layout=tnarrow" in the OWA URL when using mobile devices.  

Thank you for the help.  

Francesco B. B.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-08*

Hi @Anonymous   ,     

-  In short, I'm saying that, by using a Windows notebook, either I use OWA or Outlook full client to either connect to a mailbox residing on Exchange 2010 or on Exchange 2013, it correctly takes me to the right place with, regarding OWA, the right user interface. As expected.    

-  Correct regarding Android (tried both with android os versions 10 and 6). Regarding IOS, instead, it loads the owa premium UI, but in desktop mode (like as appending "?layout=tmouse" in the URL). To force the expected touch optimized layout I must manually append "?layout=tnarrow|twide" to the URL.    

Regarding the tests you suggest me to perform:    

-  On Android I already tried with Firefox, Chrome and Edge browser apps. Same behavior. Hint: if from within the browser app I switch to "desktop mode", all the browsers correcly load the Premium UI optimized for desktops.     

-  Nope, it just appends something like "path#mail". Nothing else.    

-  It correctly loads Premium UI in desktop mode if I use a desktop device (notebook or pc).    

Concluding, it seems to me that OWA app (server side) isn't able to understand whether I'm using a mobile or a desktop device, either that I use IOS or Android. The only difference is that in the case of IOS it loads the Premium UI in desktop mode, whereas with Android it loads the light html4 version.     

It would be cool if, like it happens on many web sites, the layout automatically changes to touch optimized or desktop optimized basing on the device is being used to browse the web site...     

I'm wondering if this will be achievable at least with newer on premise Exchange servers versions...    

Thank you,    

Francesco B. B.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-08*

Hi @BK IT Staff   ,    

Here are what I understand, please check if these are right:    

-  For the second paragraph, you did the tests with a Ex 2010 mailbox and Ex 2013 OWA URL. If so, then the result is expected.    

-  Then you tried to open mobile OWA from IOS/Android with the "xch2013setup" mailbox, in this case both these terminals should show the OWA 2013 Premium UI. But the Android gave you the Light view.    

If there are something wrong please let me know.    

I think you could do the following tests to target the issue:    

-  Use another browser like Edge/Chrome/Firefox...    

-  Compare the URL suffix after you logging in to OWA, and see if it's redirecting to a different URL.    

-  Try logging in to the desktop OWA to see if it's in the Light version.    

Sorry that I couldn't give you an exact solution for this issue with so many things unclear, and I think the Android system could also be a reason and that is out of our range.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
