---
title: "Insert into Active Directory Using SQL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/287495/insert-into-active-directory-using-sql
question_id: 287495
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Insert into Active Directory Using SQL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/287495/insert-into-active-directory-using-sql (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a User Account that's created using our ERP. Once created the SQL does some stuff to the record and spits out some attributes that later get updated in AD using a Batch job. I want to update the AD records in SQL and avoid he batch job all together to further optimize. Alternative is to build an API and perform the AD update in there using .Net code. However, it makes more sense to us to just update AD in SQL since SQL will already have the attribute data for the record we need to inject. So far not been able to find anything on how to write to AD from SQL. We already can read from AD to SQL. So there must be a way to write to AD from SQL. I assume we just need a connection or something? Anyone have samples or video tuts etc? Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-25*

Hi MicahHolmes-1650,  

Agree with Erland. You can use CLR stored procedure or CLR function with Directory Services object to update the Active Directory.  

Please refer to the following threads which might help:  

Update users in Active Directory form SQL query update  

Syncing Active Directory with my Application  

How to register System.DirectoryServices for use in SQL CLR User Functions  

Best Regards,  

Amelia

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-24*

Nope. If you look at the documentation for the OLE DB provider for Active Directory at https://learn.microsoft.com/en-us/sql/ado/guide/appendixes/microsoft-ole-db-provider-for-microsoft-active-directory-service?view=sql-server-ver15, you will find that it does not support write operations.    

Well, if you are going to do in .NET, you could do that from a CLR procedure, but if you are not using the CLR already, I am not sure that it is worth the complexity.
