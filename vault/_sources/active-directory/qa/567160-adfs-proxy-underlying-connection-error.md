---
title: "adfs proxy underlying connection error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/567160/adfs-proxy-underlying-connection-error
question_id: 567160
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# adfs proxy underlying connection error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/567160/adfs-proxy-underlying-connection-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i am trying to setup adfs proxy server and got the below error. note adfs server installed on AD DC server.  

ADFS Server Hostname: riy01-abc00  

ADFS proxy hostname: riy01-FS02  

adfs service name is: adfs.abc.com  

wildcard certificate installed on both servers.  

between adfs and adfs proxy only port 443 is open  

adfs server does not have iis not sure it should be there or no. i am using Windows Server 2012 R2  

i am getting below error when setting up ADFS proxy  

"An error occurred when attempting to establish a trust relationship with the federation service. The remote name could not be resolved adfs.abc.com"  

when I edit the host file  192.168.12.3 adfs.abc.com I got below error   

An error occurred when attempting to establish a trust relationship with the federation service the underlying connection was closed. an unexpected error occurred"  

please help me to solve this issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-28*

Hello @Akbarali-4925,    

Thank you for your question.    

There is a topic with a problem similar to yours, I recommend that you consult it through the link below:    

https://social.technet.microsoft.com/Forums/en-US/557f2257-993f-40aa-8483-c6ad54467bf3/adfs-and-web-application-proxy-error-the-underlying-connection-was-closed- an-unexpected-error?forum=sfbfr    

-------------------------------------------------------------------------------------------------------    

If the answer is helpful, please vote positively and accept as an answer.
