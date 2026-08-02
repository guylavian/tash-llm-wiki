---
title: "ldapfilter returns less result than expected despite changing ldap policies"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/864741/ldapfilter-returns-less-result-than-expected-despi
question_id: 864741
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# ldapfilter returns less result than expected despite changing ldap policies

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/864741/ldapfilter-returns-less-result-than-expected-despi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In our active directory 2016 we have 90k users and required to fetch all on a single ldapfilter query. Initially query returned 1k users.  

After changing MaxPageSize in LDAP policy from 1000 to 90000, we were expecting 90k users to be returned. Instead of 90k we received 20k.  

Kindly let us know what changes to be done to make sure we get all the users on ldapfilter.  

Below is our ldap policy table with increased values   

Policy                          Current(New)  

MaxPoolThreads                  4  

MaxPercentDirSyncRequests                       0  

MaxDatagramRecv                 8000  

MaxReceiveBuffer                        1  

InitRecvTimeout                 120  

MaxConnections                  5000  

MaxConnIdleTime                 900  

MaxPageSize                     90000  

MaxBatchReturnMessages                  0  

MaxQueryDuration                        240  

MaxDirSyncDuration                      0  

MaxTempTableSize                        80000  

MaxResultSetSize                        762144  

MinResultSets                   0  

MaxResultSetsPerConn                    0  

MaxNotificationPerConn                  5  

MaxValRange                     90000  

MaxValRangeTransitive                   0  

ThreadMemoryLimit                       0  

SystemMemoryLimitPercent                        0

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-05-26*

Hi @Ashwini Palankar      

You should use paged queries for queries that could return more than 1000 entries, rather than change the MaxPageSize, as this could significantly impact the performance or operation of your DCs.  See this page for details on paged queries  https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ldap/paging-search-results    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-30*

Hi AshwiniPalankar-0239,  

I would imagine that the process is timing out before it reaches more than 20k results.    

Paged results are indicated as a control on the ldap_search_ext function call. Use ldap_create_page_control to construct this control, and then call ldap_search_ext to add the control. This control structure must then be added to the list of server controls in the ldap_search_ext call. When the server returns the first page of results, it includes the resume cookie in the controls field of the SearchResultDone message. The client must then extract the cookie from the search result by retrieving the server controls by using ldap_parse_result and parsing the control with ldap_parse_page_control. The client then uses the cookie in the next call to LDAP_create_page_control to retrieve the next page of results.  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-30*

Hi AshwiniPalankar-0239,  

I would imagine that the process is timing out before it reaches more than 20k results.    

Paged results are indicated as a control on the ldap_search_ext function call. Use ldap_create_page_control to construct this control, and then call ldap_search_ext to add the control. This control structure must then be added to the list of server controls in the ldap_search_ext call. When the server returns the first page of results, it includes the resume cookie in the controls field of the SearchResultDone message. The client must then extract the cookie from the search result by retrieving the server controls by using ldap_parse_result and parsing the control with ldap_parse_page_control. The client then uses the cookie in the next call to LDAP_create_page_control to retrieve the next page of results.  

--If the reply is helpful, please Upvote and Accept as answer--
