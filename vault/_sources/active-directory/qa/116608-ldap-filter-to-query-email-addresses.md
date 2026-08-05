---
title: "LDAP filter to query email addresses"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/116608/ldap-filter-to-query-email-addresses
question_id: 116608
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# LDAP filter to query email addresses

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/116608/ldap-filter-to-query-email-addresses (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am new to LDAP filters but I have a requirement to create an LDAP filter that queries members of a security group in AD and gets members' email address. I do have the filter that queries members and returns their Name but I have no clue on how to modify the filter that it returns email addresses instead of name. Please help or suggest.  

Thanks in advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-18*

Hi @Rams       

Just providing a followup post of your question.      

It is possible to write a query that will return the attributes of the members of a group. However, you can't do this with standard query, you need to use a server side control to get your desired outcome.  The server side control is the Attribute Scope Query control, this control takes an attribute name, which must be a Object(DN-DN) based attribute and for each member of the Object(DN-DN) attribute it will return the specified attributes of each member.    

In the case of a group, the Object(DN-DN) attribute is the member attribute, and then by specifying the attributes you would like to be returned in the attribute list, you can return the email address for each member.    

With the standard AD admin tools this is not easy to perform this type of query as there is no options to add the ASQ server side control to the query.  LDP does have the ability to do, but it can be quiet complicated to configure.      

NetTools includes a LDAP Client which will allow you to select and run ASQ based queries by just selecting one check box.  The query input below can be imported into NetTools and run, it's pre-configured to ask for the group name and it will then details for each of the members. Details on how to input the query below can be found here    

```
[Get group member details]  
Options=880030209934413  
Server=  
BaseDN={getdn:{userinput:Enter group's SamAccountName}}  
Filter=(objectclass=*)  
Attributes=member,sAMAccountName, displayname, mail, pwdlastset,accountExpires,userAccountControl  
DisplayFilter=  
Filename=  
Sort=  
Controls=  
Authentication=1158  
Separator=,
```

For more information on how to use ASQ queries in NetTools see this post    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-29*

Hi,  

   

Just checking in to see if the information provided was helpful. Please let us know if you would like further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-22*

Hi,  

   

Just want to confirm the current situations.  

   

Please feel free to let us know if you need further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-08*

Hi,  

Thank you for posting in our forum, maybe the article in the link can help you  

Hope this information can help you  

Best wishes  

Vicky  

https://www.webspy.com/blog/useful-ldap-search-queries/  

https://www.websense.com/content/support/library/web/hosted/dsc_admin/example_schema.aspx

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-06*

You should use attrlist to enumerate necessary attribute  

Good point to start https://www.oreilly.com/library/view/active-directory-cookbook/9780596156305/ch04.html
