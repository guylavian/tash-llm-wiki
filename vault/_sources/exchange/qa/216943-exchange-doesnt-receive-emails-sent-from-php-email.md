---
title: "Exchange doesn't receive emails sent from php emailer."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/216943/exchange-doesnt-receive-emails-sent-from-php-email
question_id: 216943
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange doesn't receive emails sent from php emailer.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/216943/exchange-doesnt-receive-emails-sent-from-php-email (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello we have contact form on website, if I direct it to Office 365 account it works, but if it is directed to any account on our Exchange 2010 on premises server then emails don't go through. How to fix? Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-04*

@Alexander L      

Exchange 2010 end of support now. Here are some SMTP ways(Using 25 or 587) for Exchange 2016: How to Configure Exchange Server 2016 for SMTP Application Relay    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If you want to use Exchange server relay emails, you need to make sure your mail server could be accessed by your computer that running code first. Such as, I you relay from external of Exchange server, you need to publish Exchange server to Internet to make sure your client could access Exchange server first.    

Then, you need to create a relay connector to accept mail requests. I don't know how your code works and what type of mail server it supports, but the above article shows all the relay methods supported by Exchange, you could have a try with it.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-03*

Hi @Alexander L       

From your description, it looks like you are submitting emails from your application to the Exchange 2010 server and its not working. If my understanding is incorrect, please provide more details.    

For that to work, please create a custom receive connector for application relay with the IP address of your application (php emailer) and then try submitting emails. Share the error message by removing personal information if its still not working.    

https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/allow-anonymous-relay?view=exchserver-2016#step-1-create-a-dedicated-receive-connector-for-anonymous-relay    

https://practical365.com/exchange-server/how-to-configure-a-relay-connector-for-exchange-server-2010/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Also, Kindly note that Exchange 2010 is out of support. Please upgrade to the Exchange 2016 to stay in supported version.     

https://learn.microsoft.com/en-us/lifecycle/announcements/exchange-server-2010-support-extended#:~:text=Please%20go%20here%20to%20search,2010%20and%20SharePoint%20Server%202010.    

https://assistants.microsoft.com/    

If the above suggestion helps, please click on "Accept Answer" and upvote it
