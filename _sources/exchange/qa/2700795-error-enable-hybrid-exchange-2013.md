---
title: "Error enable hybrid exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2700795/error-enable-hybrid-exchange-2013
question_id: 2700795
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Error enable hybrid exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2700795/error-enable-hybrid-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

to try to enable the hybrid environment the following error is displayed:

[12/15/2015 19:17:01]   ERROR : System.Management.Automation.RemoteException: Can't read all of the recipient objects that you want to update update using LDAP recipient filter "(mailNickname=*)" of object "EmailAddress". The following exception occurred: Active
 Directory operation failed on ROKU.ds.iteso.mx. Additional information: Active Directory rejected paged search cookie because a cookie handle was discarded by a Domain Controller or a different LDAP connection was used on subsequent page retrieval. Paged search
 needs to be restarted and will succeed.  

                                Additional information: The parameter is incorrect.  

                                Active directory response: 00000057: LdapErr: DSID-0C090753, comment: Error processing control, data 0, v1db1.  

[12/15/2015 19:17:01]    INFO : Session=OnPrem Cmdlet=Update-EmailAddressPolicy FINISH Time=48061.8472ms  

[12/15/2015 19:17:01]   ERROR : Subtask Configure execution failed: Configure Recipient Settings  

                                Execution of the Update-EmailAddressPolicy cmdlet has thrown an exception. This may indicate invalid parameters in your hybrid configuration settings.  

                                Can't read all of the recipient objects that you want to update update using LDAP recipient filter "(mailNickname=*)" of object "EmailAddress". The following exception occurred: Active Directory operation failed on ROKU.ds.iteso.mx.
 Additional information: Active Directory rejected paged search cookie because a cookie handle was discarded by a Domain Controller or a different LDAP connection was used on subsequent page retrieval. Paged search needs to be restarted and will succeed.  

                                Additional information: The parameter is incorrect.  

                                Active directory response: 00000057: LdapErr: DSID-0C090753, comment: Error processing control, data 0, v1db1.  

                                   at Microsoft.Exchange.Management.Hybrid.RemotePowershellSession.RunCommand(String cmdlet, SessionParameters parameters, Boolean ignoreNotFoundErrors)  

[12/15/2015 19:17:01]    INFO : Task='Configure Recipient Settings' Step='Configure' FINISH Result=False Time=51680.2972ms

## Answers

_No answers on this thread._
