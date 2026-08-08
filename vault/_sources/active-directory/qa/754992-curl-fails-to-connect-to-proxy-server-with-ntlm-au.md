---
title: "Curl fails to connect to proxy server with NTLM auth when called from a protected process"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/754992/curl-fails-to-connect-to-proxy-server-with-ntlm-au
question_id: 754992
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Curl fails to connect to proxy server with NTLM auth when called from a protected process

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/754992/curl-fails-to-connect-to-proxy-server-with-ntlm-au (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi folks,    

We have a protected service which needs to connect to our backend servers through a proxy server which supports only one method of authentication - NTLM. We use CURL to make the connection but inside CURL, the API acquirecredentialshandle--ntlm fails with an error SEC_E_UNSUPPORTED_FUNCTION. When I make the same call from the same service NOT running as protected process, the call succeeds.    

The error is being returned from within the process i.e., LSASS is not being called in the failure case. My only guess so far is that probably protected processes are not allowed to use NTLM but I can't find it stated anywhere.    

Please help.    

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-08*

Hi @pkk077       

SEC_E_UNSUPPORTED_FUNCTION indicates a potential mismatch between security policy settings on the client and server computers. I am not sure that protected processes are not allowed to use NTLM.    

But for the stated error message ensure that the "Network security: Minimum session security for NTLM SSP based (including secure RPC) clients" policy settings on the computers from which users log on are the same as "Network security: Minimum session security for NTLM SSP based (including secure RPC) servers" policy settings on the server.    

On your Group Policy Editor, expand Local Policies under Computer Configuration and select Security Options. Scroll Down and find the following policies:    

-Network security: Minimum session security for NTLM SSP based (including secure RPC) clients    

-Network security: Minimum session security for NTLM SSP based (including secure RPC) servers    

 Change both policies to have "Require 128-bit encryption" checked    

Hope this resolves your Query!!    

--    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-03*

Hi,    

Which method or tool you have used to protect your processes    

did you used this : https://learn.microsoft.com/en-us/windows/win32/services/protecting-anti-malware-services-    

any screenshot
