---
title: "Exchange 2016 EWS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/344083/exchange-2016-ews
question_id: 344083
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 EWS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/344083/exchange-2016-ews (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I'm trying to understand why only certain servers are being returned in the xml response file for autodiscover. I have dedicated servers which are to be used to service external connections for EWS, as such, I want only those servers to be resolvable externally. The internall MBX servers are configured for internal EWS using abc.com/ews and I'd like the external connections to use def.com. I created said A for def.com and pointed that towards my External public facing IP which it finds no issue. The query to autodiscover.abc.com also resolves fine and returns an xml response but has mentioned it does not include the required servers/url's.  

I have AD site A which as the internet facing MBX servers located in and which resolves to the AD site currently hosting the live mailboxes. I have AD site B which in a DR site and contains inactive DB instances. The external connections come in to a CAG and are routed to a MBX server in site B. Site B MBX servers have external url's set to null.   

My understanding was that if i set an external url on the EWS servers in Site A that I wished to use and the query hit a AD site B by way of CAG that because the mailboxes are hosted in Site A the query would first attempt to connect to a server in Site A since this was hosting the live mailboxes. I also thought that when it made that query it would look for any servers that had their external url set and return those servers in preference and hence the xml response file would contain those exchange mbx servers. In getting that response the externals connection would then use that external url which would then resolve to an external A record which in turn would hit the CAG and then be routed back to the desired EWS servers.  

Both url's are valid in regards to the certificate so should be no issue there.  This should be really simple but for reasons not yet understood its not working out that way so if anybody can point me in the direction of a document that will explain in-depth how the query works, how it decides which servers should be returned as part of the autodiscover i would be greatful.

## Answers

_No answers on this thread._
