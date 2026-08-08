---
title: "Kerberos configuration issue in Windows server 2012 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1118535/kerberos-configuration-issue-in-windows-server-201
question_id: 1118535
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Kerberos configuration issue in Windows server 2012 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1118535/kerberos-configuration-issue-in-windows-server-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We tried to perform the password less connectivity from Windows 2012 (R2) Application and Linux Servers. Both the server configuration is same. In Linux server working as expected, but In windows server observed the following issue. Could you please check and suggest what is additionally required at Windows Server side?     

Ticketing from Windows/Linux Server:    

C:\Users\raju>okinit UserName@keyman  .Name.COM    

Kerberos Utilities for 64-bit Windows: Version 19.0.0.0.0 - Production on 06-DEC-2022 10:45:51    

Copyright (c) 1996, 2019 Oracle.  All rights reserved.    

Configuration file : C:\app\client\product\19.0.0\client_1\network\admin\krb5.conf.    

Password for UserName@keyman  .Name.COM:    

C:\Users\raju>oklist    

Kerberos Utilities for 64-bit Windows: Version 19.0.0.0.0 - Production on 06-DEC-2022 10:46:08    

Copyright (c) 1996, 2019 Oracle.  All rights reserved.    

Configuration file : C:\app\client\product\19.0.0\client_1\network\admin\krb5.conf.    

Ticket cache: FILE:C:\temp\krb5cc    

Default principal: UserName@keyman  .Name.COM    

Valid starting     Expires            Service principal    

12/06/22 10:46:04  12/06/22 20:46:04  krbtgt/Domain.Name.COM@keyman  .Name.COM    

        renew until 12/13/22 10:45:51  

C:\Users\raju>set KRB5CCNAME=C:\temp\krb5cc    

C:\Users\raju>sqlplus /@DBSroce_Name    

SQL*Plus: Release 19.0.0.0.0 - Production on Tue Dec 6 10:46:57 2022    

Version 19.3.0.0.0    

Copyright (c) 1982, 2019, Oracle.  All rights reserved.    

ORA-24550: signal received: Unhandled exception: Code=c0000005 Flags=0    

Encountered exception while getting args for function:0x00007FF90B51EC35    

kpedbg_dmp_stack()+377<-kpeDbgCrash()+129<-kpeDbgSignalHandler()+125<-skgesig_Win_UnhandledExceptionFilter()+158<-0x00007FF908AC0062<-0x00007FF90B51EC73<-0x00007FF90B5018B6<-0x00007FF90B512F3D<-0x00007FF90B4D4557<-0x00007FF90B5120CA<-0x00007FF8EDB6864A<-0x00007FF8EDA9911D<-0x00007FF8EDB69E0E<-0x0000    

7FF8EDA99B37<-0x00007FF8ED792D2C<-0x00007FF8ED783A12<-0x00007FF8ED781572<-0x00007FF8EDA5A59F<-0x00007FF8ED735FF5<-0x00007FF8ED72DB64<-0x00007FF8ED7292C0<-0x00007FF8ED99484F<-0x00007FF8ED990A8B<-0x00007FF8ED9667B3<-0x00007FF8ED962FDD

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-12*

Hello    

Do you have any other questions?    

If the above reply is helpful to you, please mark it as answer.    

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-08*

Hello    

ORA-24450 error, refer to the platform-specific signal code, and check whether the error is caused by the application code.    

This is usually related to the Oracle database. It is recommended to contact Oracle support personnel for assistance.    

Best Regards,    

Wesley Li
