---
title: "Problem with RODC (Read Only Domain Controller) forwarding to RWDC with WCF Windows Authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/623324/problem-with-rodc-read-only-domain-controller-forw
question_id: 623324
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-dotnet-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Problem with RODC (Read Only Domain Controller) forwarding to RWDC with WCF Windows Authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/623324/problem-with-rodc-read-only-domain-controller-forw (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a problem regarding RODC forwarding.    

There is a WPF Application calling an WCF service configured with Net.Tcp Binding and Windows Authentication (like here) https://learn.microsoft.com/en-us/dotnet/framework/wcf/feature-details/message-security-with-a-windows-client in an off-site scenario.    

In that off-site there is only a RODC installed for security reasons. Now the problem is if WCF asks for the Kerberos-Ticket on client-side (WPF) it asks the RODC and this Controller redirects its requests to the RWDC (that is somewhere else with a slow Connection).    

So the calls get very slow and sometime also have timeouts because of AD-Communication.    

So is there a way to tell WCF to use the RODC with cashed credentials so that the RODC could response with the Kerberos ticket directly    

thanks in advance very much for you input

## Answer (community) — community member

*upvotes: 1 · updated: 2021-11-12*

Hi there,  

When you login to the RODC site using user account, RODC forward this to the writable domain controller in its own domain and then writable domain controller makes it referral to the RWDC in domain and in turn via RWDC in domain A, rodc allows user to authenticate. RODC doesn't store trust password, so it has to contact RWDC to obtain referral ticket. Also, rodc can't issue kerberos ticket.  

You can get more understanding from here https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/understanding-8220-read-only-domain-controller-8221/ba-p/395031  

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-11*

Hi, thanks for the answer,  

that was also what I thought, but the credentials are cached,  

with tracing it seems that KRB_AS_REQ requests has to be used from clientside because the "get me cached kerberos-ticket" protocol for RODC seems to be different and WCF dont support this in my case

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-11*

Hello, thanks for the input,  

but the question is not about replication of RODC or admin-accounts,  

its simply about WCF communication and a Kerberos ticket request from the RODC should not redirect to the RWDC (because right now this is how it works in WCF communication)  

thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-11*

Replication between RWDC & RODC is one way only means changes can only be replicated from writable DC to RODC where as changes do not replicate from RODC to RWDC at all. Rodc contains read-only database. SO, its not possible to replicate changes from RODC to RWDC. Also, you shouldn't be using admin or domain admin accounts to login to RODC for security reasons.
