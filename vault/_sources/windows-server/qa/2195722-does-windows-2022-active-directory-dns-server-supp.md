---
title: "Does Windows 2022 Active Directory DNS Server support encrypted DNS (DoH or DoT)?   I need as much descriptive data available."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195722/does-windows-2022-active-directory-dns-server-supp
question_id: 2195722
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 9
qa_tags: ["windows-business-windows-server-networking-network-connectivity-file-sharing"]
---
# Does Windows 2022 Active Directory DNS Server support encrypted DNS (DoH or DoT)?   I need as much descriptive data available.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195722/does-windows-2022-active-directory-dns-server-supp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to know if DNS server on Windows 2022 domain controllers will support encrypted DNS.

## Answer (community) — community member

*upvotes: 7 · updated: 2023-12-31*

Hello All,

What I understand that you have Active Directory (ADDS) and DNS Services roles installed on Windows 2022 server.

You ask if DNS services are doing secure queries.

Right?

If yes then your question isn't about DNS Client but about DNS services (DNS server). 

I'm asking the same question.

Do Windows 2022 DNS Server role support DoT or DoH? Here are some definitions, what is DoH and DoT: 

https://www.cloudflare.com/learning/dns/dns-over-tls/

DoH - You would have to develop it on IIS. It would work like this:

-  Query your localhost on port 53.

-  IIS transforms query into HTTPS query.

-  Your host queries with HTTPS

DoT - Can anyone confirm if Microsoft implemented anything?

I'm going for what most did in this case. Build your own DNS service on Linux.:

-  Your computers query your Windows DNS the old way

-  Reconfigure your Windows DNS service to query your local linux the old way

-  Your Linux queries in secure way.

## Answer (community) — community member

*upvotes: 1 · updated: 2023-12-19*

Hello,

Yes, Windows Server 2022 Active Directory DNS server supports encryption DNS (DOH or DOT). Specifically.

Windows Server 2022 supports DNS Over HTTPS (DOH) and DNS Over TLS (DOT). These protocols provide a method of encrypted DNS traffic to enhance network security and privacy protection. After the DOH is enabled, the DNS query between the Windows Server's DNS client and the DNS server will be passed through a secure HTTPS connection instead of being passed in the form of pure text. 

Through the encryption connection, the DNS query can be protected from the interception of a third party that is not trusted. Essence DoH helps to prevent eavesdropping and tampering with your DNS data and protect the privacy of traffic as much as possible. Windows Server 2022 also supports TLS -based DNS (DOT). DOT is encrypted by the TLS tunnel on the TLS tunnel on the special port 853.

Thanks,

Shujun

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-22*

I find no evidence that 2022 opens port 853 for DoT.  Additionally, there are some questions about DoH.  If one blocks port 53 (clear text DNS), then PowerShell command Resolve-DnsName no longer works.  Sniffing the traffic to the DNS server it seems all still go on port 53 in the clear.

So I am guessing the Resolve-DnsName does not obey the Group Policy Settings (Require DoH) to only use DNSSEC as that should force it to use ports 443 or 853 as a DNS client.  NSLOOKUP as fails with port 53 blocked.  Browser (Edge) also fails.  (FYI - both the client and server were 2022 Servers.)  Running Wireshark on the client.

Although something is listening on port 443, I cannot find evidence that any Windows 2022 client program uses DoH for DNS resolution.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-20*

Hello, 

You can refer to： https://learn.microsoft.com/en-us/windows-server/networking/dns/doh-client-support

Hope this can help you.

Best Regards,

Shujun

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-19*

Thank you Shujun!  

Can you point me to a URL that explains how this is configured on a domain controller for AD integrated DNS.   The setup I have is several Domain controller, one domain.  Internal DNS is served off the DNS servers on the domain controllers.  Now, I have been tasked with encrypting DNS, but so far, I've not found much information on how that should be configured.  

Thanks in advance!
