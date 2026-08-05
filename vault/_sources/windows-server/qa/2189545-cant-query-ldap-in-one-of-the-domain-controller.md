---
title: "Can't query LDAP in one of the domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189545/cant-query-ldap-in-one-of-the-domain-controller
question_id: 2189545
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Can't query LDAP in one of the domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189545/cant-query-ldap-in-one-of-the-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For over a few days now, I've noticed that a domain controller is not responding to LDAP queries queries anymore, it's as if its directory was empty. From the domain controller itself teh directory data is browsable in ADAC, ADUC, ADSIedit.

I can send the exact same query only changing the name of the controller to another controller, a 1 character change (DCs are named "ZZ", "Z1", "Z2"…), and LDAP works again. It's only on a single domain controller where it is failing. I already checked the service certificate, I ran dcdiac, I verified the GPOs can replicate without issues, and that all DCs behave the same, and it seems like the all do but the fact remains the same, one DC fails to resolve LDAP queries, while the others can effortlessly process the exact same thing. It doesn't matter if the connection is plaintext, StartTLS or LDAPS, they all connect (ie. successfully) with the server but the server returns an empty directory.
https://learn-attachment.microsoft.com/api/attachments/25b2241e-1b92-4018-a4ec-f91af47cdb7c?platform=QnA"https://learn-attachment.microsoft.com/api/attachments/b98964dd-e9b8-4ed1-98f5-8e1846683617?platform=QnA" title="filestore.community.support.microsoft.com" rel="ugc nofollow">  

How can I fix this? Is my server done?

The servers can't connect to the Internet, there have not been any updates that might've triggered this, I'll start an SFC+DISM image cleanup in the meantime.

There one last detail that might have some consequences: the bad server holds all the FSMOs… but it's Windows so it may be tied to lunar cycles for all I know— nothing works as advertised. I'll just seized them if need be, I guess.

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-21*

Well… the good news it that I fixed it, didn't lose any information either.

The bad news is that I gained no new information either. I demoted the DC, which didn't remove it from the directory at all yet it was not only demoted: it also left the directory on the same step. Then I had to undo all the safeguards it had against deletion which after this seem completely pointless so I could delete fully the DC from the domain in order to reattach it. For a minute I thought the directory data was bad, but it wasn't. It's just Windows Server's messages are really unhelpful and misleading. Once I deleted the DC and its relations on Sites and Services, I rejoined the machine to AD, and promoted it again. Its AD permissions (e.g; running NPS) seem to be for some reason still valid. It seems they are applied to the name of the machine rather to its unique object identifier or whatever it's called.

There must be like a dozen security flaws there, then again I expect this from Microsoft hence the reason these systems are completely siloed and can never connect to the Internet.

Once the DC was online again, I tried connecting from Apache DS and all the information was identical to the one on the other DCs, except for its own references of course.

I know nothing about why it happened or how to prevent it. But I guess, I should be content with the results because as Microsoft products go, this counts as a huge success. "Hashtag celebration" and "stuff"…

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-18*

I apologize, I couldn't find the post, I didn't know I had to manually subscribe to be notified or it seems to have the question in my own account because there's nowhere to be found.

First of all, thank you for answering. :) It's serves at the very least as encouragement not to give up.

All domain controllers literally come from the same image.

As for the rest of the questions, most of them I answered already. I kind of already answered most of the questions. But I'm happy to repeat myself as long as it gets me anywhere.

I know FSMO roles can be transfer before seizing them ("if need be"), thanks anyway. I can connect to LDAP using ldapsearch and Apache DS, the server responds and all, only that is says the directory is empty, which I think that would answer that the service is indeed up. As you may know, is not exactly easy changing things like the firewall, or even the time in domain-join machines, specially domain controllers. The firewall is enabled because otherwise some software expecting it (such as SQL Server, for instance) throws a tantrum if it's not. But it set the most permissive, basically everything is green. These machines are segregated and offline. Security is not a concern. Clients can connect using plaintext, StartTLS (port 389) and TLS (port 636) to the service. The problem is what they get from it, not connection success. Replication, at least of directory data, SYSVOL, all that is OK. As I mentioned earlier, I ran the basic tests (e.g. dcdiag, repadmin).

As for LDAP logs, that's the only thing I'm not sure, because I would assume Microsoft would prefer Active Directory or "directory [service]" over generic LDAP. Which is the closest I got to that information in the Event Viewer under the Applications and Service Logs node there's a directory called Directory Service but there are basically no error event, most seem informational, e.g; 

Event ID 2001; "Shadow copy instance 3 freeze started."

Event ID 3027; "Event ID 2001; "Shadow copy instance 3 freeze started."

Event ID 2001; "The shadow copy backup for Active Directory Domain Services was successful."

Event ID 1162, 701, etc.

Nothing stands out.

One thing I changed was increasing the security requirements of LDAP binds, but that was after the domain controller stopped responding to them, or rather responding something useful in them.

Thanks again, I'll start transferring the roles in the meantime. Disk and system integrity scans completed each twice and successfully, but weren't useful this time.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-17*

Hi vondervita,

Thank you for posting in the Microsoft Community Forums.

You can transfer or seize all the FSMO held by the server before you do it. Transfer and seize FSMO roles - Windows Server | Microsoft Learn

Is the system version of the domain controller you have problems with the same as the system version of the other domain controllers? 

You need to confirm that the LDAP service is up and running on that DC. Check the service's dependencies and logs for any errors or warnings. 

It is also possible for a firewall or security group policy to block LDAP queries. 

Use telnet or network diagnostic tools to check if the LDAP port (389 or 636) is open and accessible. Check whether the firewall and security group policy allow LDAP traffic. 

Check the syslogs, application logs, and security logs on the DC for any errors or warnings related to the LDAP query. Pay special attention to any entries related to LDAP services, replication, or permissions. 

Try restarting the DC to see if the issue is resolved.

Best regards

Neuvi Jiang
