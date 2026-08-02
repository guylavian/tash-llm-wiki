---
title: "LDAP Search on a Global Catalog"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/114174/ldap-search-on-a-global-catalog
question_id: 114174
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# LDAP Search on a Global Catalog

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/114174/ldap-search-on-a-global-catalog (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a parent child domain. Can i do a search on the Global Catalog at the parent domain [test.com] and find objects in the child domain [ax.test.com]?  

is this string correct???  

dc=test, dc=com

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-02*

Hi,@The Exchanger      

Bind to the root of the Global Catalog namespace.    

Enumerate the Global Catalog container. The Global Catalog container contains a single object that you can use to search the entire forest.    

Use the object in the container to perform the search. In C/C++, call QueryInterface to get an IDirectorySearch pointer on the object so that you can use the IDirectorySearch interface to perform the search. In Visual Basic, use the object returned from the enumeration in your ADO query.    

To enumerate the Global Catalog servers in a site, perform an LDAP subtree search of "cn=,cn=sites,", using the following filter string.    

(&(objectCategory=nTDSDSA)(options:1.2.840.113556.1.4.803:=1))    

This filter uses the LDAP_MATCHING_RULE_BIT_AND matching rule operator (1.2.840.113556.1.4.803) to find nTDSDSA objects that have the low-order bit set in the bitmask of the options attribute. The low-order bit, which corresponds to the NTDSDSA_OPT_IS_GC constant defined in Ntdsapi.h, identifies the nTDSDSA object of a Global Catalog server. For more information about matching rules, see Search Filter Syntax.    

The parent of the nTDSDSA object is the server object, and the dNSHostName property of the server object is the DNS name of the Global Catalog server.    

reference:https://learn.microsoft.com/en-us/windows/win32/ad/binding-to-the-global-catalog
