---
title: "Active directory/domain controller issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2736548/active-directory-domain-controller-issues
question_id: 2736548
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active directory/domain controller issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2736548/active-directory-domain-controller-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a problem with my server.

1.I have one single server. Had an issue with the name so we had to change it but failed because it gave errors

-  we eventually resorted to just removing it using dcpromo and then reinstall

After that i run dcdiag and i get the below.

PLEASE HELP

C:\Users\Administrator.APPLSRV01_REPRO.000>dcdiag  

Directory Server Diagnosis  

Performing initial setup:  

   Trying to find home server...  

   Home Server = APPLSRV01_REPRO  

   [APPLSRV01_REPRO] Directory Binding Error 5:  

   Access is denied.  

   This may limit some of the tests that can be performed.  

   * Identified AD Forest.  

   Done gathering initial info.  

Doing initial required tests  

   Testing server: Default-First-Site-Name\APPLSRV01_REPRO  

      Starting test: Connectivity  

         The host 6e28fae2-6aab-40cf-bbb2-efa9a32ec1a1._msdcs.internal.repro.co.zm could not be resolved to an IP
 address. Check  

         the DNS server, DHCP, server name, etc.  

         Got error while checking LDAP and RPC connectivity. Please check your firewall settings.  

         ......................... APPLSRV01_REPRO failed test Connectivity  

Doing primary tests  

   Testing server: Default-First-Site-Name\APPLSRV01_REPRO  

      Skipping all tests, because server APPLSRV01_REPRO is not responding to directory service requests.  

   Running partition tests on : Schema  

      Starting test: CheckSDRefDom  

         ......................... Schema passed test CheckSDRefDom  

      Starting test: CrossRefValidation  

         ......................... Schema passed test CrossRefValidation  

   Running partition tests on : Configuration  

      Starting test: CheckSDRefDom  

         ......................... Configuration passed test CheckSDRefDom  

      Starting test: CrossRefValidation  

         ......................... Configuration passed test CrossRefValidation  

   Running partition tests on : internal  

      Starting test: CheckSDRefDom  

         ......................... internal passed test CheckSDRefDom  

      Starting test: CrossRefValidation  

         ......................... internal passed test CrossRefValidation  

   Running enterprise tests on : internal.repro.co.zm  

      Starting test: LocatorCheck  

         Warning: DcGetDcName(GC_SERVER_REQUIRED) call failed, error 1355  

         A Global Catalog Server could not be located - All GC's are down.  

         [APPLSRV01_REPRO] DsBindWithSpnEx() failed with error 1722,  

         The RPC server is unavailable..  

         Warning: DcGetDcName(TIME_SERVER) call failed, error 1355  

         A Time Server could not be located.  

         The server holding the PDC role is down.  

         Warning: DcGetDcName(GOOD_TIME_SERVER_PREFERRED) call failed, error 1355  

         A Good Time Server could not be located.  

         Warning: DcGetDcName(KDC_REQUIRED) call failed, error 1355  

         A KDC could not be located - All the KDCs are down.  

         ......................... internal.repro.co.zm failed test LocatorCheck  

      Starting test: Intersite  

         ......................... internal.repro.co.zm passed test Intersite

## Answer (community) — community member

*upvotes: 0 · updated: 2016-09-23*

This question is outside the scope of this site (for consumers) and to be sure you get the best answer it should be asked either on Technet (for IT Pro's) or MSDN (for developers)

http://social.technet.microsoft.com/Forums/en-us/home s/en-US/home

http://social.msdn.microsoft.com/Forum

If you give us a link to the new thread we can point some resources to it
