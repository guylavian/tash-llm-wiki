---
title: "How does one disable NTLM in Windows Server 2019?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/395930/how-does-one-disable-ntlm-in-windows-server-2019
question_id: 395930
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# How does one disable NTLM in Windows Server 2019?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/395930/how-does-one-disable-ntlm-in-windows-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dcdiag gives:    

Microsoft Windows Server has detected that NTLM authentication is presently being used between clients and this server. This event occurs once per boot of the server on the first time a client uses NTLM with this server.    

```
NTLM is a weaker authentication mechanism. Please check:  

           

              Which applications are using NTLM authentication?  

              Are there configuration issues preventing the use of stronger authentication such as Kerberos authentication?  

              If NTLM must be supported, is Extended Protection configured?  

           

        Details on how to complete these checks can be found at http://go.microsoft.com/fwlink/?LinkId=225699.
```

If I look up how to disable online I get something that looks like     

    

https://techdirectarchive.com/2020/04/01/how-to-prevent-ntlm-credentials-from-being-sent-to-remote-servers-2/    

I do not see the same settings in Windows Server 2019.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-14*

If I use your link, Microsoft Edge will block. I will substitute Your link   

Your link gives wrong location. You   

Your link says “Open the Group Policy Management Editor (gpmc.msc) and edit the Default Domain Policy.”  The correct location is Default Domain Controllers Policy.  

The way I reached the location is by Forest, Domains, domain name, Group Policy Objects. Right click Default Domain Controllers Policy and select edit. Now I can go select Computer Configuration, Policies, Windows Settings, Security Settings, Local Policies, Security Options as shown in Your link  Then I can set LAN Manager authentication level to Send NTLMv2 response only. Refuse LM & NTLM as well as the other settings listed
