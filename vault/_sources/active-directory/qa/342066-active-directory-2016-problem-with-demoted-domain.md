---
title: "Active directory 2016 problem with demoted domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/342066/active-directory-2016-problem-with-demoted-domain
question_id: 342066
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active directory 2016 problem with demoted domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/342066/active-directory-2016-problem-with-demoted-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We had a failing domain controller which holding PDC FSMO role, and lots of services (firewall, proxy, application authentication...) depend on its dns name or ip address.  

We cleaned up, its metadata from NTDSUTIL, DNS and every possible location. But we were not to promote a newly created vm ad a new domain controller, with same name, and same ip address.  

We find too, that in repadmin /replsum, we still find a trace of this failed domain controller, (1722) The RPC server is unavailable.  

We tried to promote the new vm with another vm, and same ip adderss, and it didn't work. As if the metadata cleanup is not completely successful.  

On internet, i found that there might be some stale objects in ADSI, configuration partition, LostAndFound folder, cleared that folder, but still the same thing.  

I'd like if anyone can give me a hint or steps to do that might help to bring things up and running again.  

Thank you in advance,

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-06*

Hello @LotfiBOUCHERIT-4930,  

Thank you for your update.  

Anyway, if you can still see the name of the failed domain controller from the command result, it indicates that it has not been deleted from the AD domain environment. You need to carefully find and delete it according to the method I mentioned above.  

Should you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou  

============================================  

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-02*

even if i run, dsquery computer -name ***, i don't find the domain controller that is failing in repadmin...

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-02*

Hello @Anonymous       

And thank you for this relevant explanation.. Just want to let you know, that we did cleaning using NTDSUTIL, cleaned ad sites and services, ad users and computers, dns...    

But server still figures in the repadmin /replsum command    

We fail to add a new server using the same name, and we fail to assign its ip address to another domain controller    

For results of the command you requested:    

83949-showrepl.txt83950-replsum.txt83955-dcdiag-v.txt    

Thank you in advance

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-02*

Hello @LotfiBOUCHERIT-4930,

Thank you for posting here.

As I understand, you have transferred or seized the FRMO roles from the failed domain controller you mentioned.

And now you want to demote the failed domain controller and perform the metadata cleanup for the failed domain controller completely, but it seems there is still stale objects for this failed DC.

We can try the following method.

On one good and running DC, we can run the following command to perform the metadata for this failed DC.

After that, we can check the following information:

1.To remove the failed server object from the domain controllers container.  

2.To remove the failed server object from the sites.  

3.To remove the failed server object from DNS manager.  

Remove all the DNS records corresponding to this failed DC name.  

For more information above failed domain controller, we can refer to the link below.

Delete Failed DCs from Active Directory  

https://petri.com/delete_failed_dcs_from_ad

Also, consider the following information before deleting one DC in the domain:

1.If the removed DC was a Flexible Single Master Operation (FSMO) role holder, relocate those roles to a live DC.  

2.If the removed DC was a DNS server, update the DNS client configuration on all member workstations, member servers, and other DCs that might have used this DNS server for name resolution. If it is required, modify the DHCP scope to reflect the removal of the DNS server.  

3.If the removed DC was a DNS server, update the Forwarder settings and the Delegation settings on any other DNS servers that might have pointed to the removed DC for name resolution.

After we clean up the DC, we can run the following commands on one good and running dc.

Dcdiag /v /a >c:\dcdiag.txt

repadmin /replsum >c:\repsum.txt

repadmin /showrepl * /csv >c:\repsum.csv

If there is no any entry about the failed DC in the result after running the three commands above, then the failed DC is removed complately.

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
