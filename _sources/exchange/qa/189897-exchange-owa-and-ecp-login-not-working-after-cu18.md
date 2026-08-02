---
title: "Exchange OWA and ECP login not working after CU18"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/189897/exchange-owa-and-ecp-login-not-working-after-cu18
question_id: 189897
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange OWA and ECP login not working after CU18

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/189897/exchange-owa-and-ecp-login-not-working-after-cu18 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

We have exchange installed on 4 servers. After installing CU18 no user can login to owa or ecp on any chromium based browser like edge and chrome  

Other browsers like Internet Explorer are working.  

The login page appears but upon entering correct password the page just reloads and nothing is displayed and if password is wrong then it just displays the username/password is wrong.  

But I can login using chrome and edge if I directly give the IP address.. from internal network of course.  

There is one workaround but we cant apply that for all users .... to disable same-site-by-default-cookies & cookies-without-same-site-must-be-secure  

So kindly suggest any solutions.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-09*

Hi,    

Have you published OWA to Internet? In my lab, I've tested this with newest Chrome version but could not reproduce the issue.    

It looks similar to a thread last month: https://learn.microsoft.com/en-us/answers/questions/178432/exchange-2016-cu18-causing-owa-issue-in-chrome-sam.html    

I'll keep monitoring this issue and inform you once I get some updates from official.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-08*

Hi,  

It looks like an issue with SSL flags. Since it works with IP address, do you have any load balancer configured or SSL offloading?  

If yes, check for the options to set the secure flag on the cookies. It depends on the type of load balancer and the product used.  

Sometimes, it could be an issue with SSL hardening on the Exchange server by setting the SSL/TLS protocols and Ciphers. You can use IISCrypto tool to verify.  

https://social.technet.microsoft.com/Forums/en-US/a858858c-71f4-4968-a49b-25559019148f/exchange-2016-owa-will-not-open-in-firefox-or-chrome?forum=Exch2016SD  

https://www.nartac.com/Products/IISCrypto  

Reboot is required on the servers to take effect.  

If the above suggestion helps, please click on Accept Answer and upvote it.
