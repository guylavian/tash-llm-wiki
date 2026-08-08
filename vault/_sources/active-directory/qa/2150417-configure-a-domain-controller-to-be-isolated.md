---
title: "Configure a domain controller to be isolated"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2150417/configure-a-domain-controller-to-be-isolated
question_id: 2150417
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Configure a domain controller to be isolated

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2150417/configure-a-domain-controller-to-be-isolated (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to validate what I think I need to do.  Here is the situation.

Company is selling a location that has an onprem Domain Controller, this domain controller has no schema roles assigned to it.  It is the DHCP and DNS server locally as well.  The company that is buying requires the domain to still be active as they integrate into their system.

What I have gathered for steps are the following.

-  Disable inbound and outbound replication on the domain controller.

-  Remove all domain controllers from ADUC, remove all domain admin accounts except the one create specifically for the buyer.  Remove all servers,computers,users that do not belong to the location that is being sold.

-  On PDC remove the Domain Controller that is associate to the location being sold.

-  Remove all DNS entries of items not from location being sold

This is just a temporary until the buyer is able to get their domain services setup.  Is there anything that I am missing?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-22*

This is a risky operation from the security standpoint - having access to a domain controller by a third party can be exploited (even if you delete the existing object - keep in mind these can be restored within the tombstone interval - even without relying on Recycle Bin) - so be aware of the security implications. But if you're willing to accept the risk, here is what you can try:

-  Prepare the domain controller for isolation  

-  Disable inbound and outbound replication on the domain controller to ensure changes are not propagated.  

-  Following isolation, perform metadata clean-up on both sides. Follow https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup 

-  Remove all domain admin accounts except one created specifically for the buyer.  

-  Remove all servers, computers, and users that do not belong to the location being sold.  

-  On the PDC Emulator, remove the domain controller associated with the location being sold.  

-  Clean up DNS entries to remove references to resources not part of the sold location.  

-  Review/address some of the more obvious security risks  

-  Built-in Accounts: Accounts like Administrator, Guest, and krbtgt require special handling to mitigate security risks. Reset their password multiple times. For example, for the krbtgt account:  

```
# First Reset
       Set-ADAccountPassword -Identity krbtgt -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "StrongPassword1!" -Force)

       # Second Reset
       Set-ADAccountPassword -Identity krbtgt -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "StrongPassword2!" -Force)
```

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
