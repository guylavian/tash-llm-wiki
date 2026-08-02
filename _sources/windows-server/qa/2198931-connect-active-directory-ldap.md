---
title: "Connect Active Directory LDAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198931/connect-active-directory-ldap
question_id: 2198931
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Connect Active Directory LDAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198931/connect-active-directory-ldap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello together,

i have a strange issue with our Active Directory Connection. As far as the Client or Server is connected to the Domain, everything works fine.

I am able to use ldp.exe to connect to the domain with 389 or 636.

But if i use a Server without domain connection, i receive an error message 0x51. Doesn´t care what port used.

If i test the same in our lab, all is god.

I have done some test with dns diag but all fine so far. Also i try whireshark check what happen and i´ve got the message

"Standard query response 0x4b35 No such name A <servername>.<domain> SOA <servername>.<domain>"

Also

"Standard query response 0x4b35 No such name SRV _ldap._tcp.<servername>.<domain> SOA <servername>.<domain>"

There is no firewall in between. I am able to resolve all names. Also i am able to do a powershell tnc of both ports (389 and 636) to the domain controller.

Anyone an idea what id could be? If i where not able to use ldaps with 636 then it could be an certificate issue. But 389 shoud be possible at all.

There is also no domain restriction gpo for unrestricted ldap access.

We are in our way to limit that access. But for that, all application mus work first.

Frank

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-06*

Hello

Good day!  

Based on the article, I can see:

Performs operations such as connect, bind, search, modify, add, delete against any Lightweight Directory Access Protocol (LDAP)-compatible directory, such as Active Directory Domain Services (AD DS). Ldp is an LDAP client that you use to view objects that are stored in AD DS along with their metadata, such as security descriptors and replication metadata.

Ldp | Microsoft Learn

I think if you want to connect one domain on one machine, this machine should be in the domain or can access the domain (please check the DNS setting and the AD ports on the machine).

In the screenshot above I provided, it is two different forests (a.com and lad.com) without any trust, it should be no any connection or access permissions to each other.

Best Regards，  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-05*

Ok.

And do you have an idea why?

Frank

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-05*

Hello

Good day!  

If I use the domain name instead of an explicit server, I got the same error message.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-02*

Yes,

i found out some minutes ago, that you have to use the domain name instead of an explicit server.

Frank

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-02*

Hello Frank Müller (frank.mueller),  

Thank you for posting in Microsoft Community forum.

Based on the description "But if i use a Server without domain connection, i receive an error message 0x51.", do you mean the server is not in domain or the server is in one workgroup?  

If so, in my lab, it seems I have the same error message as you mentioned when I connect server via LDP port 389.

 

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
