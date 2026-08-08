---
title: "External DNS queries on AD Domain controller failing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/784812/external-dns-queries-on-ad-domain-controller-faili
question_id: 784812
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# External DNS queries on AD Domain controller failing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/784812/external-dns-queries-on-ad-domain-controller-faili (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Windows domain with a single AD domian controller (Server 2019) and a bunch of WIndows 10 clients. I also have a firewall (192.168.1.3) . I am unable to resolve external sites on my server but all the clients are fine.  The server is getting it's IP from the firewall DHCP (the IP is reserved for the server). How do I fix this so I am able to resolve external hostnames on the server.  

ipconfig on the server is shown below  

```
Default Gateway . . . . . . . . . : 192.168.1.3
DHCP Server . . . . . . . . . . . : 192.168.1.3
DHCPv6 IAID . . . . . . . . . . . : 143933641
DHCPv6 Client DUID  . . . . : 00-01-00-01-25-92-C5-E1-94-45-e4-11-20-VB
DNS Servers . . . . . . . . . . . :  ::1
                                             192.168.1.3
NetBIOS over Tcpip. . . . . . . . : Enabled
```

On all the clients (all are part of the domain), I am able to resolve fine.  

```
Default Gateway . . . . . . . . . : 192.168.1.3
    DHCP Server . . . . . . . . . . . : 192.168.1.3
    DNS Servers . . . . . . . . . . . : 192.168.1.134
                                        192.168.1.3
    NetBIOS over Tcpip. . . . . . . . : Enabled
    Connection-specific DNS Suffix Search List :
                                        ark.local
```

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-03-27*

The domain members should not have the router or public DNS on connection properties. This causes great confusion for active directory. Domain members use domain DNS to find and logon to domain. Internet queries are forwarded to public DNS via configured forwarders or if none were configured then to the 13 root hint servers.   

You could probably use the firewall appliance as the configured forwarder. If 8.8.8.8 as forwarder works but firewall appliance address doesn't then it seems some problem in the firewall appliance configuration.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-26*

What I see is the following for the root hints section. All rows point to something that is not my IPv4 address.  

Root hints are a list of top level DNS servers on the Internet that your DNS servers can use to resolve queries for names that it does not know.  

When forwarders are configured then the root hints don't really matter, but the domain controller and all members must use domain DNS only so you should remove the router address on clients and add the domain controller's own address listed for DNS. Domain members use domain DNS to find and logon to domain. Domain controller should also always have a static ip address.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-26*

@Anonymous   Thank you for your response. Sorry was sick and unable to get to my server remotely. I was able to finally go into the office.    

What I see is the following for the root hints section. All rows point to something that is not my IPv4 address.    

    

In my Forwarders tab, I just see my local firewall address. When I added 8.8.8.8, it starts working.     

I was thinking all the external DNS address resolutions will be performed by my firewall. All my clients are able to resolve external IP addresses by using the firewall.
