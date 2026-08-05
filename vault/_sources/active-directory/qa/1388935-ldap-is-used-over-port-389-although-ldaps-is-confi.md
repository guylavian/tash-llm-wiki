---
title: "LDAP is used over port 389 although LDAPS is configured in AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1388935/ldap-is-used-over-port-389-although-ldaps-is-confi
question_id: 1388935
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# LDAP is used over port 389 although LDAPS is configured in AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1388935/ldap-is-used-over-port-389-although-ldaps-is-confi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Short summary

I set up a lab environment with an active directory based on domain functional level 2016 and windows server 2022. I also configured the domain controller (just a single dc) do use LDAPS and reject inbound unsecure LDAP connections. Nevertheless ldap over port 389 still communicates.

 

More detailed overview

On the domain controller i activated (in the Default Domain Controllers Policy) the following policies

-  Domain controller: LDAP server signing requirements to Require signing 

-  Domain controller: LDAP server channel binding token requirements to Always

On the client side (lets call it server X) (in this case windows server 2022) i configured the following settings in a gpo

-  Network security: LDAP client signing requirements to Require signing

CA is installed on another server. The certificate chain is fine and the FQDN of the dc is also configured as SAN. Long story short the root CA is known to the dc and to server X. To sum up, everything should be fine.

 

That's the output from a ldap test script from server X regarding the available ports on the dc.

I also installed the AD DS tools on server x to validate ldap and ldaps communication to the dc. I performed the following tests in ldp.exe tool from server x 

-  If i connect to the dc over port 389 (SSL and Connectionless is not checked) and perform a simple bind afterwards i get (as expected) the following error  

Server error: 00002028: LdapErr: DSID-0C090254, comment: The server requires binds to turn on integrity checking if SSL\TLS are not already active on the connection, data 0, v4f7c  

Error 0x2028 A more secure authentication method is required for this server.

-  If i connect to the dc over port 636 (SSL is checked) and perform a bind with credentials afterwards i am authenticated successfully.

Long story short - i configured LDAPS correctly in active directory, but for whatever reason, following szenarios appear, i do not understand.

 

Problems

-  If the MMC (for example Active Directory Users and Computers) is used, the connection is still made via port 389.

-  From a third-party application which uses the PowerShell commandlet Get-GPOReport (more details here) the active directory port is configured with 636 but in wireshark you only see connections over port 389. The commandlet Get-GPOReport seems not to have the possibility to specify a parameter using only port ldaps.

Questions

-  Did i forget something important to validate concerning the use of LDAPs?

-  From my point of view, the usage of ldap or ldaps does not rely on a native configuration in the operating system itself. The application layer is the only layer where you can specify if ldap or ldaps should be used. Is this correct?

-  But if the dc is configured to require signing, the connection setup should not behave in such a way that ldaps over port 636 is tried first? And if that fails, ldap will be used?

-  Independent from the fact that port 389 is still shown in wireshark, why does it even work? DC was configured to require signing.

-  Does each MMC uses port 389?

-  Does the Get-GPOReport commandlet only use port 389? I need to push that communication over port 636.

-  How does the prioritization even work if ldap or ldaps is used?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-10-12*

Hi, justdoit531

This is Chaboon.

My answer may disappoint you.

I understand, you cannot replace all of Active DIrecory's LDAP connections with LDAPS. Active DIrecory's LDAPS connection is intended for specify applications that require LDAPS, and is not meant to override Active DIrectory.

Therefore, there is no way to change the LDAPS port from 636 to 389. You can do it easily with OpenLDAP!

Similarly, from my understanding, Active DIrectory's client components are all implemented to use 389 by default (User Authentication, MMC snap-ins etc,etc). If you want to use StartTLS or LDAPS, you need to do it programmatically (using an application or script) on the client side.

Does your objective mean you want to encrypt all LDAP connections?　It's probably not what you want, but in that case you can consider "Domain Isolation". In summary, it is a method of encrypting all communications using IPsec. The following articles may be helpful.

https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/domain-isolation-policy-design

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-12*

Hi @justdoit531 •

-  If the MMC (for example Active Directory Users and Computers) is used, the connection is still made via port 389.

-  From a third-party application which uses the PowerShell commandlet Get-GPOReport (more details here) the active directory port is configured with 636 but in wireshark you only see connections over port 389. The commandlet Get-GPOReport seems not to have the possibility to specify a parameter using only port ldaps.

Unfortunately, it's not possible to force some administration tools like dsa.msc to use LDAPS instead of LDAP.

dsa.msc - can it use LDAPS port 636? How?

-  Did i forget something important to validate concerning the use of LDAPs?

You should check if the right certificate with the correct SAN is alreday installed on each domain controller to ensure LDAP over SSL

-  From my point of view, the usage of ldap or ldaps does not rely on a native configuration in the operating 

system itself. The application layer is the only layer where you can specify if ldap or ldaps should be used. Is this correct?

Yes , by default each application can use LDAP if it need to send LDAP request to domain controller.  

If you want force LDAPS , you should check if the application support it and if it's the case you can configure it to use LDAPS

1. 

-  But if the dc is configured to require signing, the connection setup should not behave in such a way that ldaps over port 636 is tried first? And if that fails, ldap will be used?

-  Independent from the fact that port 389 is still shown in wireshark, why does it even work? DC was configured to require signing.  

Because the operating system still needs to use LDAP to contact domain controller and unable to switch all LDAP request to LDAPS. 

-  Does each MMC uses port 389?  

Unfortunately, it's not possible to force some administration tools like dsa.msc to use LDAPS instead of LDAP.

dsa.msc - can it use LDAPS port 636? How?

-  Does the Get-GPOReport commandlet only use port 389? I need to push that communication over port 636.  

I think it's not possible. It's Powershell command and there is no option to force the port 636

-  How does the prioritization even work if ldap or ldaps is used?  

it depend on how you configure your application to use LDAP or LDAPS.

Please don't forget to accept helpful answer

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-10-12*

Hi, justdoit531

This is Chaboon.

If you want to SSL over LDAP on port 389 forcing, you can not. you can use StartTLS from Client-side, you get encript session over port 389.  Just to be sure, check the article below for how to set it up.  

https://social.technet.microsoft.com/Forums/Lync/en-US/86a91af3-8586-4ea6-ba2c-8ace5769cd6e/how-to-configure-and-use-starttls-on-windows-ad-server-2008-r2-or-2012-

I seem, if you want to starttls form client including windows os, you need to use a third party tool or develop a program that meets your specifications.
