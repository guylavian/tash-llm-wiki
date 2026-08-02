---
title: "Adding a new file server on domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/661821/adding-a-new-file-server-on-domain-controller
question_id: 661821
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Adding a new file server on domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/661821/adding-a-new-file-server-on-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After adding a new file server on our domain network, The server Joined without any issues. i logged in with my administrator username and password. logged in fine. updated server and restart, no issues.  after an hour or so, the server doesnt recognize administrators or users, when logging in, its says wrong username and password. If i reboot the server, im able to log in without any issues.  

But after an hour or so or random hours, we are not able to use our credentials. if we reboot we are able to log in. locally is no issues, issue is only when joining to our domain. please any thoughts?  

PS. we are able to access shared data at anytime, we are just not able to log into the server. any other servers have no issue logging in.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-06*

Hello  

Thank you for your question and reaching out.  

Please check if the AD replication health is good in state. and this new File Serve preferred DNS setting should be IP of your PDC.  

Also try to login with DomainName\UserName format or username@ domainname.com  format.  

Disable any Antivirus program or Windows firewall you may have for temporary purpose.  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-13*

I'd check the event logs for clues. Also check the domain controller and problem member both have the static ip address of DC listed for DNS and no others such as router or public DNS.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
