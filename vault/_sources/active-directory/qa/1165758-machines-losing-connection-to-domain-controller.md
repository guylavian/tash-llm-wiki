---
title: "Machines losing connection to domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165758/machines-losing-connection-to-domain-controller
question_id: 1165758
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Machines losing connection to domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165758/machines-losing-connection-to-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a windows 2019 domain controller

Some machines are losing connection to the domain. Others not. When I look at the DNS server entries (ipconfig /all) in those machines which are losing connection a misformed guid is shown  fd00::de39:6fff:fe60:f64a first, followed by the domain controller (192.168.1.3) and then another misformed guid entry as above. 

On those machines that are OK these are not shown. How do I ansure the domain controller DNS is shown first and the others deleted?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Hello there,

The first thing you should look for and this is usually the culprit is a duplicate IP address on the network.  Usually you can spot these by simply looking on your DHCP server for "BAD_ADDRESS".

Is it possible that the server is simply overloaded at times?

When NLA starts to detect the network location, the machine will contact the domain controller via port 389. If this detection successful, it will get the domain firewall profile (allowing for correct ports) and we cannot change the network location profile.

If the domain was not found or process failed, NLA will let you to determine which firewall profile will be used, private or public.

So I'd check the domain controller and problem client have the static address of DC listed for DNS and no others such as router or public DNS

Similar discussion here https://social.technet.microsoft.com/Forums/windowsserver/en-US/3711b370-af03-4916-9356-096d68649d64/server-loses-connection-with-domain-dns-issue?forum=winserverNIS

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-31*

Hi,

If you want keep IPv6 enabled on your machines , you can prioritise IPv4 over IPv6 through registry key :

You can use Group Policy Preference to deploy this registry key:

A reboot is required .

Please don't forget to mark helpful answer as accepted
