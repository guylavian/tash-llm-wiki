---
title: "Active Directory keep generating event ID 4 Security-Kerberos for each VPN connected device"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192105/active-directory-keep-generating-event-id-4-securi
question_id: 2192105
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 4
qa_tags: []
---
# Active Directory keep generating event ID 4 Security-Kerberos for each VPN connected device

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192105/active-directory-keep-generating-event-id-4-securi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have strange issue, when running dcdiag command we find so many events id issue and when check on event viewer found it was flooded with event id: 4 "Security-Kerberos" issue for each VPN connected device, every time user connect to our network using SSL-VPN  they receive different IP from DHCP. see event in detail. but when I ping machine by its NetBIOS name. it ping same IP. 

The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server z1526$. The target name used was cifs/Z1508.GSFC.org. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (GSFC.ORG) is different from the client domain (GSFC.ORG), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server. 

how can we flush out each device from AD so it does register fresh SPN when connected using SSL-VPN, 

BTW: we are using SonicWall NetExtender clients for SSL-VPN

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-23*

Hello Mukeshb1,  

Thank you for posting in Microsoft Community forum.  

Please try to check if there is any Duplicated SPN. Run setspn -X to identify the duplicate SPN.  

And delete the duplicated SPN and check if it helps. Type setspn -D<SPN> <computer_name>, where SPN is the name of the duplicate SPN and computer_name is the name of the computer that is assigned the duplicate SPN.  

Event ID 11 — Service Principal Name Configuration | Microsoft Learn  

Similar thread for your reference.  

[SOLVED] Security-Kerberos System Event ID 4 - Active Directory & GPO (spiceworks.com)  

If it does not work, did the problem come out of nowhere? or did it persist all the time? 

If this issue happened suddenly, have you made any recent changes?  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
