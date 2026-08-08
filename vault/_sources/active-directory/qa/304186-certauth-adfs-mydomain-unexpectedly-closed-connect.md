---
title: "certauth.adfs.mydomain unexpectedly closed connection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/304186/certauth-adfs-mydomain-unexpectedly-closed-connect
question_id: 304186
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "microsoft-security-security-active-directory-federation-services"]
---
# certauth.adfs.mydomain unexpectedly closed connection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/304186/certauth-adfs-mydomain-unexpectedly-closed-connect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone...fairly new to adfs, but I have setup a Sharepoint/ADFS environment currently working using claims based authentication supported by forms authentication. My next task is switch this over to certificate authentication. The WAP server has been created and is publishing the Relying Party (Sharepoint) and I have setup AlternateTLSBinding for the certauth.adfs.mydomain. I believe all certificates are in place.  

As of right now when I type the address to my sharepoint site, I am redirected to the adfs login page, where I can either type in my username/password (which works) OR click login with certificate. When I click the login with certificate link I am brought to the next screen which talks about selecting the certificate then I am forwarded to the certauth.adfs.mydomain and receive a unexpected closed the connection error.  

I am at a loss, I dont know what else to check anymore...  

PS> firewall is wide open for testing on this.  

PS>my external dns entries have adfs pointing to adfs server and certauth.afds pointing to WAP server as I have read in multiple place.  

Thanks for the help!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-09*

Hi, @MattH6935   ,    

Have you checked ULS log and event viewer? There may be related error messages which contain more information.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
