---
title: "USER_NOT_FOUND ADCS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5930812/user-not-found-adcs
question_id: 5930812
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
answer_author_roles: ["Independent Advisor"]
---
# USER_NOT_FOUND ADCS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5930812/user-not-found-adcs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm about at my wit ends with an issue and need some help. 

Some background: We have a enterprise PKI set-up with an offline root, and two online subordinate issuing CAs. Workstations and servers trust these certs and can auto enroll without issue. 

We also have 4x 2012 R2 Domain Controllers(believe me I know)We are standing up new 2022 Servers to replace them. We've got two stood up, but these new DCs won't auto enroll a domain controller authentication certificate from either CA. 

When doing a manual request, I get a 0x80070525 (WIN32: 1317 Error_no_such_user)

I can't seem to find any information online about what that means. I've checked the basic things, DNS is there, AD replication is fine. The odd thing, is 2022 servers that are not domain controllers can get certs without issue. The 2012 domain controllers can get certs without issue. It's only when a 2022 server is promoted to a domain controller does the error appear. There aren't any events on the CAs themselves, just on the DC when attempting to make the request

Any help is greatly appreciated

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-26*

Hi Chris,

The behavior lines up with a permissions gap on the certificate template rather than CA or DNS. When the server is promoted, its computer account leaves the Domain Computers group and relies on Domain Controllers membership; if your “Domain Controller Authentication” template only grants Enroll/Autoenroll to Domain Computers (or a custom group), the request comes in under a principal the CA/template can’t resolve, which surfaces as `0x80070525 (ERROR_NO_SUCH_USER)`.

Open the template on the CA (`certtmpl.msc`) and check the Security tab. Make sure Domain Controllers and ideally Enterprise Domain Controllers have at least Read + Enroll + Autoenroll permissions; also keep Authenticated Users with Read so the template is discoverable. After adjusting, run `gpupdate /force` and `certutil -pulse` on the 2022 DC, or restart the Certificate Services Client – Auto-Enrollment task to trigger a fresh request.

If it still fails, confirm the template isn’t scoped to an older compatibility mode that restricts KSP/CSP usage, and verify the CA’s Security tab allows “Request Certificates” for Domain Controllers. Given that standalone 2022 members enroll fine and 2012 DCs work, this is almost certainly the group permission change post-promotion rather than PKI core issues.

Domic V.
