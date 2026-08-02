---
title: "What does this DSID  LdapErr: DSID-0C090AFF error code mean"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/570480/what-does-this-dsid-ldaperr-dsid-0c090aff-error-co
question_id: 570480
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# What does this DSID  LdapErr: DSID-0C090AFF error code mean

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/570480/what-does-this-dsid-ldaperr-dsid-0c090aff-error-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an LDAP integration failing with the LDAP error code   

 LdapErr: DSID-0C090AFF  

But when searching the net seems like this DSID reference has never been posted before   

Does anyone know what this DSID reference code stand for ?   

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-30*

Hello @Mark Goodall  ,    

I believe that DSID-0C090AFF encodes the directory, file and line number of the source code file where the error was detected. The information is mostly of use to someone with source code access.    

If you are familiar with debuggers, disassembly, etc. then you could search the LDAP server binary for that number and disassemble the code near it until a call to DoSetLdapError is encountered.    

Your binary is different from mine (so I don't have an error reported on line 0xAFF of file 9 in directory 12), but here is an example with DSID-0C090A90:    

```
ntdsai!LDAP_CONN::SearchRequest+0x845:  
00000001`80087ee1 488b4c2478      mov     rcx,qword ptr [rsp+78h]  
00000001`80087ee6 48894c2428      mov     qword ptr [rsp+28h],rcx  
00000001`80087eeb c7442420900a090c mov     dword ptr [rsp+20h],0C090A90h  
00000001`80087ef3 ba8f200000      mov     edx,208Fh  
00000001`80087ef8 41b805000000    mov     r8d,5  
00000001`80087efe 8bc8            mov     ecx,eax  
00000001`80087f00 eb20            jmp     ntdsai!LDAP_CONN::SearchRequest+0x886 (00000001`80087f22)  
  
ntdsai!LDAP_CONN::SearchRequest+0x886:  
00000001`80087f22 4533c9          xor     r9d,r9d  
00000001`80087f25 e8d2dafcff      call    ntdsai!DoSetLdapError (00000001`800559fc)
```

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-30*

Hello,  

Microsoft makes a program named err.exe that you can download and use to look up error codes. More officially named the Microsoft Error Lookup Tool:  

https://www.microsoft.com/en-us/download/details.aspx?id=100432  

Use the Error Code Lookup tool to determine error values from decimal and hexadecimal error codes in Microsoft Windows® operating systems. The tool can look up one or more values at a time. All values on the command line will be looked up and presented to you. If available, informational data associated with the value or values will also be shown.  

It provides error codes for Windows, SQL, Exchange, etc.  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-29*

Hi Mark,

I don't have any additional information on the meaning of the DSID error code but this error text is normally part of the extended error message returned by the LDAP client. With the MS LDAP client there is normally additional text after the DSID error text that provides more information, as shown below:

```
Server Error: 0000216B: AtrErr: DSID-03140561, #1:
    0: 0000216B: DSID-03140561, problem 1004 (WRONG_MATCH_OPER), data 0, Att 90515 (tokenGroups)
, Ext Error: (8555) A Filter was passed that uses constructed attributes.
```

If you are using the MS LDAP client, call the LdapGetLastError function which will return the short error code, which is searchable. For the above example the short error code is:

```
Error: (0x12) There was an inappropriate matching
```

I hope that helps.

Gary.
