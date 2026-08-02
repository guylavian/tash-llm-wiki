---
title: "Disable use of NTLMv1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181223/disable-use-of-ntlmv1
question_id: 1181223
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Disable use of NTLMv1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181223/disable-use-of-ntlmv1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We are doing some testing on disabling the use of NTLMv1. (we have also implemented logging for a while), I have configured a GPO with the following settings: Computer Configuration\Windows Settings\Security Settings\Local Policies\Security Options\Network security: LAN Manager authentication level = 5

I have deployed this GPO to one Windows Server 2019 server, and from the local policy I can see that it has been applied. 

If I login to another server then, and try to map a share with IP (\10.0.0.1\c$) it gives me the error below in the event log, and the mapping works. I thought it would fail because when using IP instead of FQDN it uses NTLM.  (If I add the user to protected user group, then the mapping fails since NTLM then is disabled by the user group)

So my question is, do I have to assign this GPO also to the domain controller that the server authenticate against ? I hope not since I want to implement this carefully, and was hoping to take one server at the time, and then when all servers and clients are configured I could then configure the domain controllers. 

Thanks for any reply

/R

Andy

## Answers

_No answers on this thread._
