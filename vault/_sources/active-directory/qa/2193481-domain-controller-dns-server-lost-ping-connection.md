---
title: "Domain Controller/DNS Server lost ping connection to my Sonicwall Router"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193481/domain-controller-dns-server-lost-ping-connection
question_id: 2193481
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Domain Controller/DNS Server lost ping connection to my Sonicwall Router

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193481/domain-controller-dns-server-lost-ping-connection (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

I hope you can help me identify what is possibly happening on my network.

I have my ISP modem, then I connect a small 4-port switch (just for test ISP connection in case of internet issues), from here I connect my SonicWall Router/Firewall with DHCP service, then I have a 48-port switch for all my computers and my Domain Controller and DNS server.

I’ve been having disconnections on my computers to the shared files on the server and also lose internet for a few minutes.

Last week, when it happened I pinged from my DC-DNS server to the IP Router/Firewall and I noticed that some packets were lost… then I checked the cable and changed the 48 port switch and the packets in the ping were no longer lost.

Yesterday it happened to me again, I checked the ping from my server to the IP of SonicWall Router/firewall and some packets are lost a some timeouts. (I disconnected the cable from the server and reconnected and no more packets were lost, but I don’t know if this worked or it was just the minutes that passed and it was just a coincidence)

What could be happening?  

I see that the DNS configured on the SonicWall Router is my DNS server, but would this be related to losing packets with the ping from the server to the Router? or is this not related to that happening?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-31*

Hello,

Thank you for posting in Microsoft Community forum.

Based on your description, here are the possible causes of these problems and the recommended steps to check:

Check the health status and configuration of network devices, such as switches and routers. Aging or improperly configured devices can lead to network instability. Replace the network cables to make sure they are not broken or in poor contact.

Make sure your network topology is concise and straightforward. The connection between multiple switches should be stable, and the router should be configured correctly. Check for network loops and broadcast storm issues. These issues can lead to network congestion and packet loss.

Check the configuration of the SonicWall to ensure that firewall rules and traffic management policies are not accidentally blocking or restricting legitimate traffic.

Make sure the DNS settings are correct. If the SonicWall's DNS is configured as an internal DNS server, verify that the server is healthy and that the internal DNS server is capable of resolving external domain names.

Check the server's network configuration to make sure there are no incorrect static routes or unnecessary network bindings.

Monitor the server's resource usage (CPU, memory, network, etc.) to ensure that there are no resource bottlenecks.

Use network diagnostic tools (such as ping, tracert, etc.) to check the stability of your network connection. Try testing from different devices and different network paths to determine if the issue is related to a specific device or path.

Record when the problem occurred in an attempt to find out if there is a pattern or a specific trigger.

Check the logs on the SonicWall and the server for possible errors or warning messages.

Configure a network monitoring tool to monitor network traffic and device status in real time.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

﻿

Regards,

Jill Zhou
