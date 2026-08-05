---
title: "Risks of changing LDAP Polices - MaxPageSize value?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194979/risks-of-changing-ldap-polices-maxpagesize-value
question_id: 2194979
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Risks of changing LDAP Polices - MaxPageSize value?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194979/risks-of-changing-ldap-polices-maxpagesize-value (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have a developer working with our AD environment who is using LDAP queries from SQL. He currently hits a limit of 901 records that he can pull in a single query. Some recommendations online mention using NTDSUTIL.EXE to modify the LDAP Policies and increase the MaxPageSize value.

The default value appears to actually be 1000. There doesn't seem to be much info online about what else this could affect for AD/LDAP. Can anyone shed some light on possible risks with increasing this value? Or is it completely safe to do so? Is there a maximum value that would be considered safe if not the default?

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-30*

To use paginated queries in LDAP, you can follow these steps: 

1.Set up your LDAP connection: 

conn = Connection (*args) 

2.Create a generator for paged search: 

entry_generator = conn.extend.standard.paged_search ( 

```
search\_base=self.dc,  

search\_filter=query,  

search\_scope=SUBTREE,  

attributes=self.user\_attributes,  

paged\_size=1,  

generator=True
```

) 

3.Get your results: 

results = [] 

for entry in entry_generator:  

```
total\_entries += 1  

results.append (entry)  

if total\_entries % 50 == 0:  

    # do something with results
```

In the above code, paged_size=1 means that the generator will yield one entry at a time. You can adjust this value according to your needs. 

ldap - How to use ldap3 generator for pagination? - Stack Overflow

Please note that the server is free to impose a limit on the number of entries that can be returned in the response to a search request. The LDAP client can request a size limit, but this client-requested limit cannot override the server-imposed limit. Therefore, if you encounter an error like “Size limit exceeded”, it might be due to the server-imposed limit. 

ldap - Paging using ldapsearch - Server Fault

If you’re using Microsoft’s LDAP API, you can use ldap_create_page_control to construct a control for paged results, and then call ldap_search_ext to add the control. 

Paging Search Results | Microsoft Learn

Remember to replace *args, self.dc, query, SUBTREE, and self.user_attributes with your actual parameters. If you’re not sure about these parameters, you might need to refer to your LDAP server’s documentation or consult with your system administrator.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-20*

Hi,

Thanks so much for the detailed response! This is very helpful.

As a final follow up question, do you happen to have links to any resources about how to run a paged query?

Thanks again.
