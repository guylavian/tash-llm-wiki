---
title: "KB5046616 on Domain Controller ->  rdp to hostname fails ip address works"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196945/kb5046616-on-domain-controller-rdp-to-hostname-fai
question_id: 2196945
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# KB5046616 on Domain Controller ->  rdp to hostname fails ip address works

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196945/kb5046616-on-domain-controller-rdp-to-hostname-fai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

KB5046616 on Domain Controller -> connect rdp to hostname fails ip address works

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-05*

Unfortunately, it happened again. All those who logged into this server, by name, do not work. When the server is turned off, everything starts working.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-03*

Hello, 

Thanks for your reply. 

I am glad that your problem has been solved. 

Thank you very much for your support of Microsoft products and your selfless sharing.

Best Regards,

Yanhong Liu

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-03*

Thank you.

DNS is OK.

The domain controller was just installed (Windows server standart 2022). Updates were installed.

Time is synchronized. No problems with this.

NLA did not help.

I have not removed the updates yet. It was enough to turn off the installed DC for a while. Then turn it on. So far everything works by name and IP

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-02*

Hello, 

Thank you for posting in Microsoft Community forum. 

It sounds like you're experiencing an issue where Remote Desktop Protocol (RDP) connections to a domain controller using the hostname fail, but connections using the IP address work. Here are a few potential solutions you can try: 

DNS Issues: Ensure that the DNS records for the domain controller are correct. You can use nslookup to verify that the hostname resolves to the correct IP address. Also, check for any duplicate DNS entries. 

Kerberos Authentication: This issue might be related to Kerberos authentication. Sometimes, a domain controller might lose its Kerberos token. You can try running the following commands on each domain controller: 

nltest /sc_query:your_domain 

Test-ComputerSecureChannel -Server "DC_Name" 

If you find a problem with the security channel, you can try using the Reset-ComputerMachinePassword command to reset the computer account password. 

Time Synchronization: Kerberos requires that the clocks on the client and server are synchronized within a few minutes. Check for any time drift between the domain controller and the client machine. 

Credential Manager: Clear any cached credentials for the hostname in the Credential Manager on the client machine. 

Network Level Authentication (NLA): Disabling NLA on the RDP target might help but be aware that this could pose a security risk. 

Windows Update Issues: Some updates can cause issues with RDP. Ensure that all your systems are fully updated. If the problem started after a specific update, you might need to consider uninstalling that update. 

I hope the information above is helpful. 

Best Regards, 

Yanhong Liu
