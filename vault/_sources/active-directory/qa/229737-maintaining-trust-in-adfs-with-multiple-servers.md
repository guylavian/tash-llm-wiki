---
title: "Maintaining Trust in ADFS with Multiple Servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/229737/maintaining-trust-in-adfs-with-multiple-servers
question_id: 229737
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Maintaining Trust in ADFS with Multiple Servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/229737/maintaining-trust-in-adfs-with-multiple-servers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have seen some similar posts but never with a solution. In the case of two ADFS servers using wid (adfs1 and adfs2) load balanced and two ADFS Proxy servers (proxy1 and proxy2) also load balanced. An error message was logged on proxy1 that "the federation proxy server could not renew its trust with the Federation Service" (event id 394).   

The fix seems to be to make sure proxy1 is talking to the primary ADFS server adfs1 (instead of the VIP which load balanced adfs1 and adfs2 as adfs.domain.com) and to re-register it. I did this by setting the FQDN adfs.domain.com to point to adfs1 in the hosts file on proxy1. I expect it will keep wanting to renew the trust so I should leave it that way. This would seem to break the full mesh redundancy of having 2x2 since proxy1 will only talk to adfs1. Is there a better way to deal with this issue in this configuration?   

I understand moving to SQL server may be an option but is another single point of failure I would like to avoid since this is not a huge deployment. Any other ideas?  

Thank you for your help!  

Mike

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-01-14*

WAP certificate renewal can be handled by any node. It does not need to be handled by the primary. When a secondary received the request, it forwards it to the primary. Secondaries and the primary sync every 5 minutes. Which means that 5 minutes later, the new certificate can be used on the secondary. And because the renewal takes place before the current certificate expires, you should not see any interruptions.  

Obviously, if you see that's not working as described above, it means something else is not working in this process. Maybe some communication error between the primary and secondaries. Can you make sure the last sync took place without error? Maybe some TLS errors with the secondary? Some network traces should clear that out. If your load balancer is doing SSL inspection, it will also break this mechanism.   

Also, you can use this tool to check the configuration of your farm.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-14*

I have the diags returning all green now. I had the internal servers using our EntCA cert but now have the public wildcard cert across all 4 servers. I tested taking the primary adfs server out of service in NLB and then re-running the proxy config wizard and it seems to work. I guess we will now in about 20 days!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-14*

I see the ProxyTrust certificates are part of this process. Do you know if I can trigger that renewal and monitor it somehow?  

I checked and the last sync seems to have taken place without error. Sync messages on the secondary server in the AD FS admin log look reflect that.  

I ran that diagnostics tool and it came back pretty green. I saw and fixed a couple of minor issues. I am left with one issue I cannot seem to figure out how to resolve. The test says it "Verifies that the AD FS SSL certificate is trusted by the server. AD FS requests and trust renewals will fail if the SSL certificate is not trusted." One proxy1 it reports "The certificate chain is not trusted." The remediation information is unfortunately not helpful but I will dig deeper with fresh eyes tomorrow.
