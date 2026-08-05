---
title: "Unavailability of one Domain Controller causes loss of Internet  even though Secondary DNS was configured"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2076529/unavailability-of-one-domain-controller-causes-los
question_id: 2076529
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unavailability of one Domain Controller causes loss of Internet  even though Secondary DNS was configured

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2076529/unavailability-of-one-domain-controller-causes-los (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a network with a domain controller that manages DNS settings for all connected client PCs. The primary DNS server is configured on the domain controller, and a secondary DNS server is also set in the Advanced TCP/IP Settings of each client PC. It was observed that, for a short duration when Domain controller was unavailable, all the client PCs were not able to access internet. Upon inspection, I found that the IP address of the secondary DNS server was present in the DNS entries on the client machines, but it did not function correctly to maintain internet connectivity when the primary DNS was down.

Note : We do not use DHCP for internal reasons also we used AD integrated DNS setup. And the temporary working solution was to switch the IPv4 DNS address order that is primary to secondary and secondary to primary and it worked.

Here are the steps I've tried so far: Troubleshooting DNS Problems:

-  Tried different web browsers to rule out cache issues, but no luck there.

-  Temporarily disabled the firewall to ensure it wasn’t blocking DNS services, yet no internet service.

-  Cleared the DNS cache on the client PCs, but the issue persisted.

Reference Link - https://www.hostinger.in/tutorials/dns-server-not-responding

Also, found recommendations to configure PCs to use public DNS servers as their primary DNS. However, I’m unsure if this would interfere with domain-related DNS queries and implement without disrupting domain functionality.

Is there any other recommended methods that can ensure that the client's PC can maintain internet access even if the primary domain controller is down, that is , secondary DNS should work when primary is down. Your input will be much appreciated

Thank you in advance

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-25*

Hello Researcher,

Thank you for posting in Q&A forum.

It is not recommended to set secondary DNS server as a public DNS server, you should use Forwarder to set public DNS server.

Here are some steps to troubleshoot Domain Controller (DC) DNS issues:

- 	Ensure that the DNS zone is correctly configured to integrate with Active Directory Domain Services (AD DS). Verify that the zone is set to store its data in AD DS and that the DNS server is properly configured to load the zone data from AD DS.

- 	Use tools like nslookup or dig to query the DNS records and ensure they are present and correct.

- 	Ensure that the necessary permissions are in place for the DNS server to read and write the DNS records in AD DS. This includes checking the permissions on the DNS zone and the AD DS objects.

- 	Use the dcdiag tool to check the health of your domain controllers and replication status.

- 	On the affected domain controller, open a command prompt and run the following commands to flush and register DNS:

ipconfig /flushdns

ipconfig /registerdns

- 	Use the repadmin tool to force replication across all domain controllers:

repadmin /syncall

- 	Look for any errors or warnings in the Event Viewer on your domain controllers that might indicate issues with DNS or AD replication.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-23*

Hello @Researcher  , is recursion enabled on the secondary server, and what forwarders are set? If this second server points to the first as forwarder, that would cause issues.

Have you compared all options for the server that works as expected and matched them on the other server? Is this second server allowed exactly the same internet access as the first?
