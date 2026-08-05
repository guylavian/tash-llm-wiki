---
title: "How solve Brute Force through IIS NTLM authentication scheme"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/233220/how-solve-brute-force-through-iis-ntlm-authenticat
question_id: 233220
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# How solve Brute Force through IIS NTLM authentication scheme

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/233220/how-solve-brute-force-through-iis-ntlm-authenticat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone   

Someone know how Can I solve this vulnerability?  

It's associate with the CVE 2002-0419  

My OS is windows server 2016 Datacenter  

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-22*

Yes the security team detected it with scan , the software is qualys    

I am not familiar with Qualys. My experience with having my servers scanned, was that the vulnerability report typically provided a link to "Here's how to fix this vulnerability" where I could go research what I needed to change.     

On the US government web site....   https://nvd.nist.gov/vuln/detail/CVE-2002-0419    

it says:     NOTE: this entry originally contained a vector (1) in which the server reveals whether it supports Basic or NTLM authentication through 401 Access Denied error messages. CVE has REJECTED this vector; it is not a vulnerability because the information is already available through legitimate use, since authentication cannot proceed without specifying a scheme that is supported by both the client and the server.    

In the section "References to Advisories, Solutions, and Tools", I don't see a solution. There are 3 links to other sites, and https://www.securityfocus.com/bid/4235/solution  says "Currently the SecurityFocus staff are not aware of any vendor-supplied patches for this issue".    

https://marc.info/?l=bugtraq&m=101535399100534&w=2    says: "Microsoft was informed of this but didn't consider it to be a problem."    

So.....  for whatever web site you have on the server, how does it authenticate users? Does it even require authentication? In the IIS manager, disable any authentication scheme that is not used.    

    

If that doesn't satisfy your security team, send them an email that says "Thank you for pointing out this vulnerability. Please provide instructions as to how I fix the issue. My research has not found a solution.."

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

Hi,    

Thank you for posting in Q&A!    

May I ask what's your IIS version? According to my research, IIS 6 and 7 are susceptible to this particular vulnerability:    

https://answers.microsoft.com/en-us/protect/forum/protect_other-protect_scanning-windows_other/account-brute-force-possible-through-iis-ntlm/e7f42505-f871-4dd7-a67d-3245f959e61e?auth=1    

And there's a workaroud posted by some user has the same problem, maybe you can try it:    

disable NTLM authentication for your Web server. This can be done by unchecking "Integrated Windows Authentication" within "Authentication Method" under "Directory Security" in "Default Web Site Properties".    

Hope you have a nice day : )    

Gloria    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.    

https://learn.microsoft.com/en-us/answers/articles/67444/email-notifications.html

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-18*

This looks like an old vulnerability. https://nvd.nist.gov/vuln/detail/CVE-2002-0419  

https://www.cvedetails.com/cve/CVE-2002-0419/  

WS 2016 should not be running IIS 4 or 5.1.  

Did someone scan your system and detect this vulnerability?
