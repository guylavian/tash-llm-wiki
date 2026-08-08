---
title: "ADFS service unavailable"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/912435/adfs-service-unavailable
question_id: 912435
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# ADFS service unavailable

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/912435/adfs-service-unavailable (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello    

I try to follow the below 2 link setup ADFS.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/configure-a-federation-server    

https://www.youtube.com/watch?v=UZ1jHAt8whQ    

After I did all steps and try to access https://adfs.sc.com/adfs, I got service unavailable.    

Would you please provide some advice for me on how to continue checking?    

I had read similar posts but did not found helpful information.    

Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-05*

Hello    

I use the below link and then login to Meraki success by AD account.  not sure does this is a correct step. This sign on page is disabled by default.    

https://adfs.sc.com/adfs/ls/idpinitiatedsignon.aspx    

I also don't know why youtube video teach me use https://adfs.sc.com/adfs.    

Thanks for your reply.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-05*

Hello    

Thank you for your question and reaching out. I can understand you are  having issues related  to ADFS service unavailable.    

Run the below command and see if the endpoint is listed. If not, reboot the server and check again.    

netsh http sh serv | findstr /i /c:"trust/13/usernamemixed"    

When you do you should see something like below if the endpoint is available.    

C:\Windows\system32>netsh http sh serv | findstr /i /c:"trust/13/usernamemixed"    

                HTTPS://+:443/ADFS/SERVICES/TRUST/13/USERNAMEMIXED/  

------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
