---
title: "Active Directory problems, replication. Help!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/62329/active-directory-problems-replication-help
question_id: 62329
fetched: 2026-07-25
answer_count: 14
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory problems, replication. Help!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/62329/active-directory-problems-replication-help (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello:  

After the "typical" domain lost connectivity error between two domain controllers in different sites (with I dont know if lingering objects), after trying an autorithy restore (D4 in the main site and D2 in the secondary), and after trying to migrate fsmo roles and create a new domain controller to recover all, i have a difficult situation now, problems with clients that cannot access to network resources from sometimes ip, sometimes name:  

-  DC01 (main site, we will love to do this the main one again, the right database): DNS problems, nslookup is not working and DFSR -1202 errors are in the event viewer (and 13562 NTFRS errors). You cann add the dns console only from DC03. Can resolve DC02 from ping but not DC03. you cannot edit GPOs (error the system cannot find the path), and it is displayed an error that cannot find one GPO (cannot say which one, one of the tops). Errors 1865, 1311 and 1566 in the directory service event viewer.  

-  DC02 (secondary site): DNS ok. Cannot access some GPos, event viewer 1058 and 4. Event viewer errors 1925 and 1645, about DC01 not to be recognise as an account (SPN). Cannot access the gpos too.  

-  DC03: new DC in the main site. DNS ok, but you cannot access ibchdc00 from here. Cannot access the gpos too.  

We stuck in the middle of fsmo migration, so at this moment DC02 see a different fsmo role assingment than the other 2. We tried again with ntdsutil the migration, it was not displayed error, but still the same:  

From DC01: all roles are in DC03  

From DC02: Master of schema, Domain Names and PDC, are in DC03. RID and infraestructure are in DC02.  

From DC03: all roles are in DC03  

From the site and services you can replicate from DC01 to DC02, but not to DC03. From DC02 to DC03 yes, but not from DC03 to DC01 or DC02. From DC03 you cannot replicate to anyone.  

I can show you dcdiag,   

thanks at all.  

SP

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-08-09*

Not a recommended method. When there are multiple domain controllers the recommended method for failed domain controller is to seize roles (if needed) to a healthy one.      

https://support.microsoft.com/en-us/help/255504/using-ntdsutil-exe-to-transfer-or-seize-fsmo-roles-to-a-domain-control      

then perform cleanup to remove remnants of failed one.      

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup      

then rebuild failed one from scratch.      

I'd use dcdiag / repadmin tools to verify health correcting all errors found before starting any operation. Then stand up the new one, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health.    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-08*

When NLA starts to detect the network location, the machine will contact a domain controller via port 389. If this detection is successful, it will get the domain firewall profile (allowing for correct ports) and we cannot change the network location profile.   

If the domain was not found or process failed, NLA will let you to determine which firewall profile will be used, private or public.   

The Network Location Awareness (NLA) service expects to be able to enumerate the domain’s forest name to choose the right network profile for the connection. The service does this by calling DsGetDcName on the forest root name and issuing an LDAP query on UDP port 389 to a root Domain Controller. The service expects to be able to connect to the PDC in the forest domain to populate the following registry subkey:   

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\NetworkList\Nla\Cache\IntranetForests   

If something hinders the DNS name resolution or the connection attempt to the DC, NLA is not able to set the appropriate network profile on the connection.  

So I'd check the domain controller and problem client have the static address of DC listed for DNS and no others such as router or public DNS  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-08*

Ok, sounds like ports 42,  88, 137, 138 and 139 are not listened locally on DC01.   

I have the print and file share enabled, but whenever I try to change in the network adapter (private profile) the enable network detection, you save it, but its not saved....  

any ideas?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-08*

Hi Patrick, we tought that but we checked that windows firewall and antivirus software is disabled, and there is no firewall traffic analizer beetwen sites, i will test again with that tool anyway.  

thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-08*

Sounds like ports are not currently flowing between sites.    

https://support.microsoft.com/en-us/help/179442/how-to-configure-a-firewall-for-domains-and-trusts    

https://www.microsoft.com/en-us/download/details.aspx?id=24009    

--please don't forget to Accept as answer if the reply is helpful--
