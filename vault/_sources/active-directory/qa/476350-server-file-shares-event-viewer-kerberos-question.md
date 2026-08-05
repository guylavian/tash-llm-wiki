---
title: "Server file shares + Event Viewer + Kerberos question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/476350/server-file-shares-event-viewer-kerberos-question
question_id: 476350
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Server file shares + Event Viewer + Kerberos question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/476350/server-file-shares-event-viewer-kerberos-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello there!    

I'm figuring out how to completely disable NTLM in my domain and have a couple questions. My environment, for now, is a single DC running on Server 2019 (forest/domain functional level still on 2008 R2, but planning on raising it soon) + couple of servers running WS 2008 R2 + couple of Debian servers. All workstations are running Windows 10 Pro.    

I have 2 main file shares in the network, one of them based at the 2008 R2 (Server A) and the other on a Debian with Samba 4 (Server B, which is configured to use Kerberos 100%). Both of these file shares are mapped via GPO for every user, by their DNS names (\fileshare1.domain.com\Share and \fileshare2.domain.com\Share).    

I'm using this link as source: http://woshub.com/disable-ntlm-authentication-windows/    

I have enabled NTLM Audit and based on the event viewer I'm pretty sure all my workstations/domain users authenticate with Kerberos on the DC, and my main problem is the network share mappings, which are causing the audit logs about NTLM.    

Example: I have an application server (Server C) the users access via RDP or RemoteApp. When they do that, I get 2 logs on the event viewer pointing the NTLM requests, like that:    

```
  
  SERVER_A   
  john   
  CONTOSO   
  SERVER_C   
  2   
  
  
  
  SERVER_B   
  john   
  CONTOSO   
  SERVER_C   
  2   

```

My question is: how do I enforce Kerberos onto these servers and/or file shares? Also, at any workstation if I try to log via RDP into any server I get asked for password, which I believe is a NTLM behavior thing, so it's like my workstations use Kerberos just fine to log the user in, but they don't use it to log into other services.    

I had a look into this option but didn't quite understand if I can enforce this via GPO or it'll cause any problems in my environment: https://learn.microsoft.com/en-us/microsoft-desktop-optimization-pack/appv-v4/how-to-configure-the-server-to-be-trusted-for-delegation    

Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-19*

Hey Hannah. Sorry I haven't had the time to look into this on the weekend, I will today and get back here with the results. Thanks again!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-16*

Hello @Paulo Diego  ,    

Thank you so much for your kindly reply.    

Greatly appreciate the provided information. Apologize that I do not have the similar lab to do the testing. I have found the below documentation, and hope it could be of some help for you.     

https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/ntlm-blocking-and-you-application-analysis-and-auditing/ba-p/397191    

It stated that "NTLM blocking does not totally turn off NTLM on a computer". We could kindly have a check of this documentation.    

Besides, as for another question, I have SQL server in my lab which is logged with a service account. If blocking NTLM, it will be able to log on. If I tried to access this SQL server via RDP with the service account. It could also access this server. If possible, we could do the testing in our lab environment.     

Thank you so much for your understanding and support.    

Best regards,    

Hannah Xiong

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-15*

Hello Hannah, thanks for your insights.    

First of all, I'm quite new to the whole authentication protocol management business so I apologize for any concepts I got wrong.    

I assumed my machines were using NTLM based on these events (also, my environment is in portuguese, but I think it's understandable which information is which based on their positions):    

-  Log from the event viewer > Windows logs > Security - Event 4624. I get one of these for each machine in my domain, so I assume they are using Kerberos with no trouble. Further down I have confirmation in the "AuthenticationPackageName" that it's Kerberos authenticated.    

    

-  From the event viewer > App and services logs > Microsoft > Windows > NTLM > Operational, I get examples like this one:    

    

-  SU20-FILESERVER is a Ubuntu server in my netowrk with fileshares using Samba 4.    

-  MW10-007867 is that user's workstation.    

-  So I assume that, when the user "jair.campos" opens the fileshare, his workstations is using NTLM authentication for some reason.    

-  I get logs like this for other fileshares and the RemoteApp server.    

Also, I was wondering about this matter during the night and I have another question. I have this one server in my environment, which is domain joined, but I have to access it via RDP with a specific service account (also from my domain), not my user account. If I block NTLM will I be able to access this server with the service account? In my mind I assume that my workstation doesn't have a Kerberos ticket for that account, so it would ask me for credentials when I try to log in.    

Thanks again for all the help!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-15*

Hello @PauloDiegodaSilva-8951,    

Thank you so much for posting here.    

Normally, for AD environment, the Kerberos authentication will be tried firstly, and if it fails, then falls back to NTLM.     

I tried to disable NTLM authentication and enabled the audit in my lab. When trying to authenticate with NTLM, there will be warning that NTLM authentication requests to this server have been blocked.    

    

As for the NTLM request we mentioned, would you please kindly provide us more information or more screenshots about the event logs?     

Q1: how do I enforce Kerberos onto these servers and/or file shares?    

I did the test as shown below:     

Domain user accesses the server (domain joined server) via RDP, and then access the file server by their DNS names, for example: \PDC.book.com\DocStore. It could be successful.    

    

Q2: Also, at any workstation if I try to log via RDP into any server I get asked for password, which I believe is a NTLM behavior thing, so it's like my workstations use Kerberos just fine to log the user in, but they don't use it to log into other services.    

It is hard to say it is a NTLM behavior. In my previous tests, I tried to log via RDP and it also asked for the password.     

Q3: I had a look into this option but didn't quite understand if I can enforce this via GPO or it'll cause any problems in my environment.    

The option should be assigned only if there is a clear need for its functionality. When you assign this right, you should investigate the use of constrained delegation to control what the delegated accounts can do.     

Reference: https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/enable-computer-and-user-accounts-to-be-trusted-for-delegation    

For any question, please feel free to let me know.    

Best regards,    

Hannah Xiong
