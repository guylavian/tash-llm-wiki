---
title: "Exchange 2010 OWA Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/144218/exchange-2010-owa-error
question_id: 144218
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2010 OWA Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/144218/exchange-2010-owa-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have 2 Exchange 2010 CAS/HUB servers. recently 1 server was crashed and we rebuilt using restore functionality from AD. currently, email is working fine. but we are facing an issue with owa. let say if we shutdown 1 server which is working fine and then try below it gives us an error  

1-type Http:\webmail.abc.com in browsers then it shows "403 - Forbidden: Access is denied." error not redirecting to https:\webmail.abc.com.  

2- similarly while I use IP of problematic(new server) with Http, it gives the same error "403 - Forbidden: Access is denied."  

3- if I use IP of problematic (new server) with https, then it shows "This site is not secure" then I click on more options and select the nonsecure page then it goes to webmail.abc.com.  

Can anyone please guide me on how to resolve this issue?  

Regards

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-30*

@Sajid Ali Shah       

Hi,    

First of all,please note that Exchange 2010 has reached its end of support in October 13,2020.    

It is strongly recommended to consider upgrading to Exchange 2016 or Exchange 2019 to get better performance and support.    

According to the information,the problem may be resulted from the http redirection in IIS was not configured or lost the configuration.    

Please open IIS manager on the new server and locate Default Web Site-->owa.    

If you don't want to disable HTTP connections and would like to redirect them to HTTPs connections as you mentioned in the post,please follow these steps:    

-  Select SSL Settings and uncheck Require SSL,click apply.    

-  Select HTTP redirect and fill in the blank "Redirect requests to this destination" with "https:\webmail.abc.com" ,click apply.    

-  Then restart IIS service to see if it acts as you expect.    

Here is a document for your reference: Configure http to https redirection for Outlook on the web in Exchange Server    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
