---
title: "ldp.exe ADLDS Error<94>: ldap_parse_result failed: No result present in message"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/381295/ldp-exe-adlds-error-94-ldap-parse-result-failed-no
question_id: 381295
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ldp.exe ADLDS Error<94>: ldap_parse_result failed: No result present in message

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/381295/ldp-exe-adlds-error-94-ldap-parse-result-failed-no (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When using ldp.exe and clicking on the objects in the tree, I get this:

Expanding base 'CN=Durnal\, Joseph,OU=Accounts,DC=adlds'...  

Error<94>: ldap_parse_result failed: No result present in message  

Server error:  

Getting 0 entries:

Other than these errors using the ldp.exe utility and clicking the tree, everything seems to be working fine with the adlds instance. I'm not sure what is causing this, any ideas?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-04*

Hi,  

Usually, it is a port issue.  

Check if the Firewall was set on the DCs and try to disable it and then confirm the result.  

Similar case or your reference:  

https://www.reddit.com/r/sysadmin/comments/1x6qp1/help_windows_dc_stops_servicing_ldap_requests/  

https://serverfault.com/questions/190011/unable-to-query-ldap-server-on-port-389-on-the-win2k-domain-controller-from-a-di  

This response contains a third-party link. We provide this link for easy reference. Microsoft cannot guarantee the validity of any information and content in this link.  

Best Regards,
