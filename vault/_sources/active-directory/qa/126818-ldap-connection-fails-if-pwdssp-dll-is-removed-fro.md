---
title: "Ldap connection fails if pwdssp.dll is removed from registry"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/126818/ldap-connection-fails-if-pwdssp-dll-is-removed-fro
question_id: 126818
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Ldap connection fails if pwdssp.dll is removed from registry

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/126818/ldap-connection-fails-if-pwdssp-dll-is-removed-fro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I try to do a LDAP search I get the below error, Though the connection to ldap works fine but LDAP Search fails.  

LDAP: error code 1 - 000004DC: LdapErr: DSID-00000000, comment: In order to perform this operation a successful bind must be completed on the connection., data 0, v2580  

This happens only when pwdssp.dll is removed from SYSTEM\CurrentControlSet\Control\SecurityProviders and only credssp.dll is retained.  

Really appreciate if someone can answer what is going on?   

Does Active Directory (LDAP)Server wants the Ldap Client to use SASL bind?  

Or I can use simplebind but may need to set some other parameters ?  

Thanks  

Girish

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-16*

Hi,  

Based on my research , if the pwdssp.dll is removed ,all simple binds were being treated as "NT Authority\Anonymous Logon" binds.  

Anonymous LDAP operations to Active Directory are disabled by default. Not sure if you want to change it.  

Following article for your reference:  

https://support.microsoft.com/en-us/help/326690/anonymous-ldap-operations-to-active-directory-are-disabled-on-windows  

Or you can considered SASL bind (https://ldap.com/the-ldap-bind-operation/)  

Please note: The given technical support contact information belongs to a third party and may vary without notice. Microsoft does not guarantee the information accuracy.  

Best Regards,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-15*

Hi,  

Based on my research , the pwdssp.dll is necessary for the simple  ldap research, just add the registry back .  

Similar cases for your reference:  

https://social.technet.microsoft.com/Forums/lync/en-US/40755056-45c8-480f-9337-fbe2f18c8c15/ldap-simple-bind-failing?forum=winserverDS  

https://hi.service-now.com/kb_view.do?sysparm_article=KB0754219(Please note: The given technical support contact information belongs to a third party and may vary without notice. Microsoft does not guarantee the information accuracy.)  

Best Regards,
