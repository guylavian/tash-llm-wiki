---
title: "on-premise activesync not working with iPhone"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/425815/on-premise-activesync-not-working-with-iphone
question_id: 425815
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# on-premise activesync not working with iPhone

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/425815/on-premise-activesync-not-working-with-iphone (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is a new on-premise exchange install. Still in the testing phase wanting make active soon. At this point everything is working except iPhone integration. I would appreciate any help in locating and correcting the problem  

Exchange 2016 CU20 in small 3 server DAG  

Desktop outlook clients work for any users I have tested for both internal and external email.  

Latest HealthChecker.ps1 reports everything clean.  

As recommended external URLs are the same as internal and made to work  in DNS  

External email, in and out goes through a spam checking proxy (MailCleaner).  

As far as ActiveSync is concerned it does not go through the above proxy, I have port 443 forwarded from the mailcleaner DMZ to the exchange server and this seems to work for everything except iPhone.  

what works with activesync:  

-  OWA webmail (including on iPhones) to send and receive internal and external email  

-  Autodiscover works  

-  activesync test work on https://testconnectivity.microsoft.com/tests/exchange, so does the SSL server test  

-  Android mail apps work on all accounts tested  

-  iPhone mail app works initially to connect to server and populate inbox with all current messages  

-  Once iPhone account is set up any new incoming messages automatically pop into inbox display  

-  in both iPhone and Android the "Outlook for ios and android" app can connect to server to create the new mail account on the app.  

what does not work:  

-  in iPhone, clicking on a message in the inbox to try to read it just displays the message headers and where the message body should be is text saying "This message has not been downloaded from the server"  

-  In iPhone attempting to send mail fails  

-  in both iPhone and Android the "Outlook for ios and android" app does not populate the inbox with any existing or new messages  

-   in both iPhone and Android the "Outlook for ios and android" app fails on sending mail  

This in not specific to any user or device, it is the same with all users and devices tested.  

Exchange Mobile Device Access and Mobile Device Mailbox policies are still at the defaults for the new exchange install

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-08*

Hi ZhengqiLou-MSFT  

Well that is interesting, the ActiveSyncConnectivity test fails:  

Well, OK, I see it fails with a certificate error and of course it will because I am not passing it a server name that is on my SAN certificate. If instead I test with:  

```
Test-ActiveSyncConnectivity -MailboxCredential $credential -URL https://my.exchange.servername.ca/Microsoft-Server-ActiveSync | fl
```

then It passes. I see it does 7 different tests and each one results in "Success"  

As for your link to the article on fixing the iphone. I have tried all of those suggestions already except for deleting and then re-installing the mail app. I will do this though just to be complete but I don't expect it will change. I have been testing on new phones (old phones that I have done factory reset) and I have repeatedly deleted the mail accounts on these phones, removed the mobile devices from exchange server accounts and then set them all up again.  

None of my test users are administrators, they are simple "Domain Users"

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-08*

Hi @Bill Leuze   ,    

I think you could test ActiveSync with the follow cmdlet:    

```
$credential = Get-Credential  
Test-ActiveSyncConnectivity -MailboxCredential $credential
```

Note you should use Domain\User and the password to sync, if you use the UPN or email address to authentication, you may result in a Ping Failure.    

If the result is failure, please use this cmdlet to check if there are any useful information in the Error blank.    

```
Test-ActiveSyncConnectivity -MailboxCredential $credential | FL
```

For the error, you can refer to this article:    

This message has not been downloaded from the server error, fix    

In addition, are the accounts you used administrator accounts? Such as Organization management, Enterprise Admins or others? If so, please try with a normal account.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
