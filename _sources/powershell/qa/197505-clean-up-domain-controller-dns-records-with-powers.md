---
title: "Clean up Domain Controller DNS Records with Powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/197505/clean-up-domain-controller-dns-records-with-powers
question_id: 197505
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Clean up Domain Controller DNS Records with Powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/197505/clean-up-domain-controller-dns-records-with-powers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I was going through this page:  

https://devblogs.microsoft.com/scripting/clean-up-domain-controller-dns-records-with-powershell/  

However, it only mentions the zone _msdcs.contoso.com. What about the zone contoso.com and reverse lookup zones? Don't we have to delete that too after a DC is forcefully removed? It is not in the script.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-17*

@Gloria Gu       

The microsoft link https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup mentions:     

When you use Remote Server Administration Tools (RSAT) or the Active Directory Users and Computers console (Dsa.msc) that is included with Windows Server to delete a domain controller computer account from the Domain Controllers organizational unit (OU), the cleanup of server metadata is performed automatically. Before Windows Server 2008, you had to perform a separate metadata cleanup procedure.    

You can also use the Active Directory Sites and Services console (Dssite.msc) to delete a domain controller's computer account, which also completes metadata cleanup automatically. However, Active Directory Sites and Services removes the metadata automatically only when you first delete the NTDS Settings object below the computer account in Dssite.msc.    

So it means we can EITHER use Active Directory Sites and Services or Active Directory Sites and Services to delete metadata of dead DC? We don't have to use BOTH?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

@Gloria Gu    Hi,    

So it means if I use Active Directory Users and Computers to delete the DC as per https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup, then all DNS records of the DC will be automatically removed also? No need to manually clean/remove DNS records of this DC?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

@Rich Matheisen   So it means yes we have to delete dns records from both zones: _msdcs.contoso.com & contoso.com.    

In this case, how can we modify the powershell command to run for zone contoso.com after running for zone _msdcs.contoso.com.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-15*

@Nabeel   Hi,    

Thank you for posting in Q&A!    

Do you want to perform metadata cleanup on a domain controller? If you want to achieve this, I would suggest you to use the GUI tools. Procedures should be done in Active Directory Users and Computers, Active Directory Sites and Services& DNS Entries.    

Using this method, it wold be a thoroughly clean up of the remain metadata of the old DC including DNS record.    

For more details, please refer to:    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

Hope you have a nice day : )    

Gloria    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.    

https://learn.microsoft.com/en-us/answers/articles/67444/email-notifications.html

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-14*

Treat them the same way you'd treat any A, AAAA, CNAME, etc. DNS records for any machine you remove from your organization.
