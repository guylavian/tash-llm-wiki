---
title: "Exchange Server 2013 Compromised Suspicious IIS Modules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/355650/exchange-server-2013-compromised-suspicious-iis-mo
question_id: 355650
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2013 Compromised Suspicious IIS Modules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/355650/exchange-server-2013-compromised-suspicious-iis-mo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey Everyone, hope you're well.

Can someone please confirm for my sanity.

After Hafnium Shell exploit and a run of EOMT scripts and IISRewrites I still have what I expect to be suspicious native modules in IIS.  

A belated update to CU23 did show that the applicationhost.config while was written to, I've not copied all of the globalmodules, but doea anyone know if this UpData  

module is part of the usual IIS modules, looks suspicious to me and until I get rid of it I can't access OWA/EMS/ECP and have errors in event logs.

... <add name="kerbauth" image="c:\Program Files\Microsoft\Exchange Server\V15\Bin\kerbauth.dll" preCondition="bitness64" />  

<add name="WSMan" image="C:\Windows\system32\wsmsvc.dll" />  

<add name="exppw" image="c:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\Owa\auth\exppw.dll" />  

<add name="cafe_exppw" image="c:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\bin\exppw.dll" />  

<add name="UpData" image="C:\Windows\System32\system.dll" />  

<add name="RewriteModule" image="%SystemRoot%\system32\inetsrv\rewrite.dll" />

Please give me some guidance.

Thanks

Neil

## Answers

_No answers on this thread._
