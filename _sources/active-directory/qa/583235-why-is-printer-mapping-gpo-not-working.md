---
title: "Why Is Printer Mapping GPO Not Working?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/583235/why-is-printer-mapping-gpo-not-working
question_id: 583235
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-print-jobs"]
---
# Why Is Printer Mapping GPO Not Working?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/583235/why-is-printer-mapping-gpo-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I created a GPO to map a single specific printer to every computer that resides in a specific OU.  I used the Computer Config -> Preferences-> Control Panel Settings --> Printers configuration to attempt this.  

When I review the other 2 GPO's tied to this same OU, I don't see anything in them that seems to contradict this one I'm trying to setup for a print mapping.  

The "Deploy with GPO" option is turned on for the printer inside of the Print Management console.   It is set with "Per Machine" as the Connection Type, since the GPO's printer settings were established as a computer configuration.    

 When I run the gpupdate/re-login to the test computer and run gpresult, the GPO for the printer shows up as successfully loaded, but the printer still isn't mapped to the machine.    

In Event Viewer, it says that 3 Group Policy Objects were detected and applied.  Shortly after that , I see logs regarding WSDScan service and such which makes it look like it's trying to do something with the printer mapping, but it isn't happening.  

In the gpresult.htm, there's no errors in the summary, nor do I see any errors as I scroll down the document, examining all the sections that pertain to printing.  

Since the GPO is showing up as applied on the target machine but the printer still isn't mapped, I reviewed the GPO settings for the printer.    

On the general tab for the printer, the IP address is filled in, with the Use DNS name and IPv6 boxes left unchecked.  In the Printer Path field, I manually added the printer then ran net view to identify the UNC path to the printer.  After filling this information in and doing the gpupdate, I'm still getting the same result, where the GPO is showing as loaded on the target machine but the printer isn't getting mapped.  I confirmed it isn't getting mapped by looking in the registry at HKEYcurrentuser\printers\connections   

I enabled Group Policy Preference tracing and when I search the computer preferences log on the target machine for the Unique Name of my Printer Mapping GPO, it's not in there. I also manually looked-through the log and ran another search for the word "print" (which is in the name of the GPO), and I still find nothing that appears to reference this GPO.    

Any ideas?

## Answers

_No answers on this thread._
