---
title: "Exchange 2019 / http redirect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/385191/exchange-2019-http-redirect
question_id: 385191
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other", "windows-development-iis"]
---
# Exchange 2019 / http redirect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/385191/exchange-2019-http-redirect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

My environment was an exchange 2019 with CU7. I upgraded this after the issues in march, to CU9 and the hotfix.  Before the upgrade, http->https redirect worked fine, all setup in IIS was all done and ok. Also forward  webmail.server.com -> webmail.server.com/owa worked fine  

After the upgrade and patch all these settings are set to default in IIS (default website and exchange backend). But I discover some strange behaviour and want to check with you before I reconfigure IIS again for http-https forward and forward to owa  

At this moment:   

http://webmail.server.com gives access denied . Thats should be ok as that is configured in IIS now. No http-https forward  

https://webmail.server.com gives owa and I can login. That is strange, as I have not configured that in IIS  

http://webmail.server.com/ecp gives redirect to https and I can login to ecp. That is strange as I have not configured that http to https redirect  

Seems something strange happening in IIS so I am little bit scared to change the settings in IIS to what it must be (http-https redrect and to owa)  

Thx

## Answers

_No answers on this thread._
