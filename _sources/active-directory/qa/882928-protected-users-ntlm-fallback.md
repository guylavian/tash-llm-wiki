---
title: "Protected users - Ntlm fallback"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/882928/protected-users-ntlm-fallback
question_id: 882928
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# Protected users - Ntlm fallback

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/882928/protected-users-ntlm-fallback (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,     

I'm testing the protected users group in Active directory with a highly privileged user which is not able to access a remote machine using RDP at the moment, by reviewing the logs it looks like the user falls on NTLM ( I am aware that NTLM is not allowed for members of the protected users group)     

The user is trying to login via RDP to a remote machine by FQDN and not an IP address.     

In the event logs of the remote machine (a domain controller) I couldn't find any event log, such as event log 4771 which will shed some light over the reason for the Kerberos ticket to be denied. Kerberos audit logs were  enabled in the group policy.  there are 4771 events just not one which is related to this user.    

What can I do to further troubleshoot this?    

Thanks in advance for the help.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-10*

Hi there,    

Members of the Protected Users group must be able to authenticate by using Kerberos with Advanced Encryption Standards (AES). This method requires AES keys for the account object in Active Directory. The built-in Administrator does not have an AES key unless the password was changed on an Active Directory Domain Controller that runs Windows Server 2008 or later. Additionally, any account object, which has a password that was changed at an Active Directory Domain Controller that runs an earlier version of Windows Server, is locked out.    

Here is a thread as well that discusses the same issue and you can try out some troubleshooting steps from this and see if that helps you to sort the Issue.    

Microsoft Store RDP App won't allow connection when protected users group enabled    

https://learn.microsoft.com/en-us/answers/questions/372142/microsoft-store-rdp-app-wont-allow-conenction-when.html    

--------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-09*

Thanks @Gary Reynolds   for your reply.    

NLA is already enabled.    

So if the 4 hours lifetime are over during an RDP session (idle) won't that logoff the session of that user? and now when the user tries to login via RDP why will he get an authentication error?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-09*

Hi @Tmrgboxxe      

You can allow members of Protected Users group to use RDP by enabling Network Level Authentication (NLA) of the server. Details on how to enable NLA here  https://www.virtuesecurity.com/enable-network-level-access-windows-rdp/    

Other other issue you may face is that members of the Protected Users group have a 4 hour Kerberos access token life, which can expire while using an RDP session which will cause authentication errors for the user after the access token has expired.  It requires the user to logoff and back on to reset the access token.    

Gary.
