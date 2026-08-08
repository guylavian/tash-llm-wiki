---
title: "How to access ADFS externally with web app"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/15471/how-to-access-adfs-externally-with-web-app
question_id: 15471
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# How to access ADFS externally with web app

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/15471/how-to-access-adfs-externally-with-web-app (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

   I really need someone to help me out now since i spent days learning and doing labs and i finally made it but not completely. I have 3 VMs, 1 DC, ADFS server and ADFS proxy server with 2 NICs. Internally i can reach the ADFS login page with https://adfs.domain.com/adfs/ls/idpinitiatedsignon.aspx and its working. But i want to be able to reach the ADFS externally, so i created a public DNS record for adfs.domain.com and pointed it to my public ip and in my router i configured port forwarding so that when the request comes in, it should be sent to my ADFS proxy server which will pass it to the ADFS server and etc.   

       But when i try to reach the ADFS https://adfs.domain.com/adfs/ls/idpinitiatedsignon.aspx externally i get error message this site cant be reached. adfs.domain.com took too long to respond.

So i need help to be able to reach the ADFS over the internet, can someone help me out with what to do and how ?  

   Thanks thanks

## Answers

_No answers on this thread._
