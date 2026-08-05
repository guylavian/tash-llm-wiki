---
title: "an Active Directory integrated DNS Zone and must be available"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1167844/an-active-directory-integrated-dns-zone-and-must-b
question_id: 1167844
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# an Active Directory integrated DNS Zone and must be available

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1167844/an-active-directory-integrated-dns-zone-and-must-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Noticed the following DNS error in when I logged into the server and can't seem to resolve it. FYI this domain has been upgraded multiple times from Server 2000. Perhaps I need to delete the _msdcs zone that's under my domain to recreate it as a new primary zone?

"DNS: Zone _msdcs.sample.domain.com is and active directory integrated DNS zone and must be available"

I ran DCDIAG /TEST:DNS /e /v and it comes back with everything passed. I then opened the DNS management console and under forward lookup zone I only see my domain, not another zone starting with _msdcs.sample.domain.com.

I attempted to create the zone manually and got the following error:

```
Summary of DNS test results:

                                            Auth Basc Forw Del  Dyn  RReg Ext
            _________________________________________________________________
            Domain: xxx.sample.com
               DC3                          PASS PASS PASS PASS PASS PASS n/a
               2012R2-DC                    PASS PASS PASS PASS PASS PASS n/a
               OSTDC                        PASS PASS PASS PASS PASS PASS n/a
```

What can I do to resolve this?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-05*

Seems like that's how DNS did it back in the day so it's prob ok to leave as but would like to get other opinions.

[[SOLVED] _msdcs.domain[.]com at the root of forward lookup zone? - DNS - Spiceworks](https://community.spiceworks.com/topic/2310568-_msdcs-domain-com-at-the-root-of-forward-lookup-zone"Link: https://community.spiceworks.com/topic/2310568-_msdcs-domain-com-at-the-root-of-forward-lookup-zone")

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-02-05*

Hi,

I will suggest you to follow this troubleshooting steps to setup the msdcs zone and this should help to resolve the DNS issue.

https://servergurunow.wordpress.com/2017/09/29/recreate-the-_msdcs-dns-zone/

Hope this helps.

JS

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
