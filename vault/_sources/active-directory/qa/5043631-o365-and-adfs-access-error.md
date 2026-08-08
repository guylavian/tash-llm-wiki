---
title: "O365 and ADFS Access error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5043631/o365-and-adfs-access-error
question_id: 5043631
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# O365 and ADFS Access error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5043631/o365-and-adfs-access-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

  I have finished setting up a hybrid environment for my O365 migration test lab.  The Azure  lab consists of  followings and  followed this

http://superhybridcloud.com/how-to-create-your-hybrid-exchange-lab-in-azure/

 AD Server / Sync- xxxxx.lan

Exchange 2010 SP3 : xxxxx.com.au - mail.xxxxx.com.au --xxxx

    autodiscover--->autodiscover.outlook.com.    MX -->xxxxx-com-au.mail.protection.outlook.com.

ADFS :  10.0.0.12

ADFS Proxy: 10.0.1.5 (DMZ)

  sts.xxxxx.com.au-->xxxxxtadfsps01.xxxxx.cloudapp.azure.com.

   1. Can not send and receive emails from externally?   

          Attempting to test potential Autodiscover URL https://autodiscover.xxxxx.com.au:443/Autodiscover/Autodiscover.xml - failed

   I have a name in external DNS  CNAME point to autodiscover.outlook.com. so I cannot create a new A record to 52.xxx.252.76 ?

    2.  When I try to login to any portal its directing to my company portal and giving me this error externally? internally SSO is working?

  https://sts.xxxxx.com.au/adfs/ls/?client-request-id=88d3fc72-da9b-4c63-be72-da11bd8e260d&wa=wsignin1.0&wtrealm=urn%3afederation%3aMicrosoftOnline&wctx=LoginOptions%3D3%26estsredirect%3d2%26estsrequest%3drQIIAY2Ty4vbVhTGLXvGcYamnZYQsosXIZSC5CvpSn5ASOSxO5ZHsixbjiJ3IfS4su-MXqPH2NZfkGxC6LLdlUJhloVCKbR\_wKwC3c2yq5JNS1dddBFNoPtsDhzO953F7zvn4BZHsRSgwBc1hgK9hw6ENgQdlmRtG5Cw69CkDdsu2W1DxLGO7XqsM65zgIYsSD47OEz--\_3Ft9eO9Fty\_emvrx7duSQerbMsTnutVhwlmeVTVpEniHKioJXiVYjDFg5dtG39TBBvCOJPgrispjzbZgFgu3y3zfIdwNAsJWvCblKoxWSgZoqmbmUMwIRRN5K2opcDIVsOVqyh-dhgjMI4dQpFcxg5WAZGIJczYbMs9UtdhZJ2xsmDs0zWDVoODNbQZ4GsPwuuq58oQp6tmZsSJbhAb6sfp8hHTmZajhPlYfZP9bYXJYEZR2n2Te3rqhKjUHSPojAsRdSND4UZdqwMR-E0iWKUZBilj0dz059YzNgsnFl\_wFresNwh5el8TRauHXj8ZquKc9M8JRe7lLxICq1Pe2IqTjduV1hs3RN12AXDYazgI0bnRMRbRl9i9CKWxnCrXngMP1Jk5TwU8rmezJid2Vmqz2dtP2BLrgIQ-hx0GR46z8Xt0XHCmmOwGMw2C2XiDsBJxI\_g\_HQSeLPjwrTSMDY1W3aeHdHIE6cejIvzyckKF7oyXs1Vab51El4cfun3d5GUahKpcraqzrK1vZmK5BBe1h7-H3ZghdYKBSWRMuoy702ZcrRJqRBlrR9rd6JkZYW4eM8qvapJH2Jr5SlKTByUYNMofG9tlpRD7DZRYGG\_GSeRh330R-1eau3yAD-18rQ04ptdAWXlb\_aIt3v3GvuHtfuVZuXzu6DWazQODis33b97xHf75f2-\_GlmrY\_\_En\_46MGTr75vVK72W3IXt6G\_Xi1GAxREXidag7BNn23Ph67Aj5kpWEqZql8ko678GPbo13Xidb1-VW-IA3My1CD3d514cavyy-0PfITrg7sMYAAJ2iRNNwHswU6P5ZbvAA2&cbcxt=&username=xxxx%40xxxxx.com.au&mkt=&lc=

How do I fix the above two issues?   

<*** Private Message was removed by Sylvie Liang MSFT for privacy ***>

## Answers

_No answers on this thread._
