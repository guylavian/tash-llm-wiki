---
title: "Running Exchange Hybrid Configuration Wizard, unable to create endpoint"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/229949/running-exchange-hybrid-configuration-wizard-unabl
question_id: 229949
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Running Exchange Hybrid Configuration Wizard, unable to create endpoint

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/229949/running-exchange-hybrid-configuration-wizard-unabl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm running Exchange 2016 CU16 and am trying to set up a Hybrid environment with Microsoft Exchange Online in order to start a migration to 365 services.    

When running the Hybrid Configuration Wizard, I get the error HCW8078 - Migration Endpoint could not be created    

    

I've also run Test-MigrationServerAvailability and the output indicates that no MRSProxy was found running at the host indicated (this host being our autodiscover URL).    

    

If manually go to the MRS Proxy URL (either internally or externally) I'm prompted for authentication. After putting in an admin login credential, I get the following page:    

    

However, I have confirmed both via the EAC and via PowerShell (via Test-MRSHealth and Get-WebServicesVirtualDirectory) that the MRSProxy is enabled and responding to a ping.    

    

    

I've done the following to try to resolve this:    

-  I've simply issued an IISRESET command and tried again: still fails    

-  I set the MRSPRoxy configuration on the EWS site to $false, issued IISRESET, then set it back to $true, and issued another IISRESET: still fails    

-  I've recycled the MSExchangeServicesAppPool in IIS: still fails    

I'm not sure what else to try? The Microsoft Connectivity Analyzer indicates everything on my server looks good, the only warning being that I have a GoDaddy cert that requires clients to be running their Windows Updates in order to trust the root cert provider. Does the account provided for this require certain privileges? I'm using the general domain admin account I use for all of my Exchange management.

## Answers

_No answers on this thread._
