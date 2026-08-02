---
title: "Amend my LDAP query"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/165071/amend-my-ldap-query
question_id: 165071
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-tsql", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Amend my LDAP query

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/165071/amend-my-ldap-query (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have this openquery that I use to extract data from AD and it works fine. However I need to add an additional criteria but am struggling to do so.  

Currently the query looks like this  

OpenQuery (  

ADSI,  

'SELECT mail, mobile, telephoneNumber, title, sn, givenName, SAMAccountName, department FROM ''LDAP://xxxxx'  

WHERE objectClass = ''user'' AND givenName='''' AND sn='''' AND title=''*'' AND ''userAccountControl:1.2.840.113556.1.4.803:''<>2 AND ''userAccountControl:1.2.840.113556.1.4.803:''<>65536 AND Mail = ''*domain1'' OR description =''xxxxx''OR description = ''xxxxx''') AS tblADS

You'll see that I am specifying that an email must be in the format *domain1 (obviously the real values are masked).  

I now need to add the criteria mail = ''*domain2''  

In SQL In would use IN ('x','y') but see no equivalent syntax in LDAP.  

To be clear the domain1 OR domain2 must be separate from the other OR criteria as domain2 must satisfy all the other AND criteria in the select statement.

Any ideas?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-11-18*

Hi,    

Thanks for posting in Q&A platform.    

We noticed that you issue was regarding of OpenQuery and LDAP query, and please understanding we are not familiar with  how to write these queries. Based on discussed with our SQL and AD DS colleagues, we would like suggest you could try to contact Script Forum for further help:    

https://social.technet.microsoft.com/Forums/en-us/home?forum=ITCG&filter=alltypes&sort=lastpostdesc    

The reason why we recommend posting appropriately is you will get the most qualified pool of respondents, and other partners who read the forums regularly can either share their knowledge or learn from your interaction with us. Thank you for your understanding.    

Best Regards,    

Sunny    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
