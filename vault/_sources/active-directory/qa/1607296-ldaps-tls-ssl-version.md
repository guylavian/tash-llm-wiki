---
title: "LDAPS tls/ssl version"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1607296/ldaps-tls-ssl-version
question_id: 1607296
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# LDAPS tls/ssl version

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1607296/ldaps-tls-ssl-version (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey,

I am using ADSI COMM interface (CPP) to connect using LDAPS to retrieve objects from Active directory.

How do I know which TLS version it is using? How is it distinguished? I didn't find this configuration in ADSI COMM documentation, I was told to specify only ldaps:// prefix and then it is using LDAPS

Thank you.

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2024-03-03*

Hi,

You can use Wireshark tool.

https://www.wireshark.org/ downlaod and install it.

Open Wireshark. 

Capture LDAPS Traffic: Choose your network interface and start capturing LDAPS traffic.

Filter LDAPS Traffic: Apply a filter to focus only on LDAPS traffic (use "ldap.port == 636").

Trigger Connections: Perform actions in your application that result in LDAPS connections to Active Directory.

Check Handshake: Wireshark captures the traffic, including SSL/TLS handshakes.

Analyze TLS Version: Look at the SSL handshake packets to determine the TLS version being used.

Optional Server Logs: Check logs on the LDAP server to see if TLS versions negotiated during LDAPS connections are logged.

Please accept as answer if it helps.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-12*

Hello a1，

Thank you for posting in Q&A forum.

Based on your description, you can use the Wireshark tool to analyze the TLS version used. First of all, you need to download and install Wireshark on the official website. Open Wireshake and select the network port to start capturing LDAPS traffic. Then enter 'ldap.port==636' in the filter in Wireshark. When Wireshark captures all traffic including the SSL/TLS handshake, you can view the SSL handshake packets to determine which TLS version is being used.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
