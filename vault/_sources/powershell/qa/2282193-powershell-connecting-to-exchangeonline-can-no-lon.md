---
title: "PowerShell - Connecting to ExchangeOnline - Can no longer add/enable Remote Routing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2282193/powershell-connecting-to-exchangeonline-can-no-lon
question_id: 2282193
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Independent Advisor", "Q&A User"]
---
# PowerShell - Connecting to ExchangeOnline - Can no longer add/enable Remote Routing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2282193/powershell-connecting-to-exchangeonline-can-no-lon (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

First time posting,

Last year I could use the following command on an account without issues (we are a hybrid migration of O365):

Enable-RemoteMailbox TEST -RemoteRoutingAddress ******@OurDomain.mail.onmicrosoft.com -PrimarySmtpAddress ******@OurDomain.org

nor can I even try to set the remote routing with this command:

set-remotemailbox -identity ******@OurDomain.org -RemoteRoutingAddress ******@OurDomain.mail.onmicrosoft.com

Now I cant, I get some error about it not knowing the command or some other rubbish.

For obvious reasons I need to have those remote routing addresses added to the account, which is a lot easier than having to get into the Admin Center and type them in one by one.

I know all about the initial set up (not that I have received a new computer or anything, its the same Windows Laptop), as I still haev all of that documented.  With the initial set up being:

install-module exchangeonlinemanagement

install-module msonline

install-module azuread

Not that I needed the azuread part, as this the accounts were going to be cloud only accounts via an Import into O365 and then a license assignment that included EOL.

When I open up PowerShell as Admin, and run the command "connect-exchangeonline" I get the box for username, password and the authenticator app passcode, and it signs me in without issue, so I am connected to ExchangeOnline.

So, any ideas why this suddenly doesn't work?

Ive tried using the built in Terminal, powershell 7, and one older version of PS and still get the same error.

Any ideas how I can set the remote routing added to an account once connected to ExchangeOnline

because Im bloody lost as to why this no longer works, even though I obviously get authenticated on connection to it.

Any help is appreciated,

JH

## Answer (community) — Independent Advisor

*upvotes: 1 · updated: 2025-06-11*

I have scoped down you answer and make it clearly for you question :

-> Do You Need DisplayName or Password?

No — not in the second CSV that’s only used by PowerShell to add aliases.

You only needed DisplayName and Password in the first CSV when uploading to the Admin Center (which handles creating the users and assigning passwords).

Once the users are created, you only need the fields relevant for the script — so your second CSV can be trimmed to just:

UserPrincipalName,Email1,Email2

@mydomain.org,@mydomain.mail.onmicrosoft.com,*****@mydomain.onmicrosoft.com*

@mydomain.org,@mydomain.mail.onmicrosoft.com,*****@mydomain.onmicrosoft.com*

...

-> Is the script correct? And how does the data fit?

Yes, this script is correct:

Import-Csv "alias-list.csv" | ForEach-Object {

    $UPN = $_.UserPrincipalName

    $Email1 = $_.Email1

    $Email2 = $_.Email2

 

    Set-Mailbox -Identity $UPN -EmailAddresses @{add=$Email1}

    Set-Mailbox -Identity $UPN -EmailAddresses @{add=$Email2}

}

-> And What goes in the CSV?

As your note:

-  Yes, each Email1 and Email2 value should be the full address (e.g., ******@mydomain.mail.onmicrosoft.com).

-  There’s no need to include a display name in this second CSV.

-  Each row is one user; just make sure the values are accurate.

-> So your Workflow it should looks like this steps:

Step 1 — Create users in M365 Admin Center:

-  Download and populate Microsoft’s sample CSV with fields like DisplayName, Username, and Password.

-  Upload that CSV in Admin Center > Users > Add Multiple.

Step 2 — Prepare second CSV (for PowerShell):

-  Create a simple alias-list.csv like this:

UserPrincipalName,Email1,Email2

@mydomain.org,@mydomain.mail.onmicrosoft.com,*****@mydomain.onmicrosoft.com*

@mydomain.org,@mydomain.mail.onmicrosoft.com,*****@mydomain.onmicrosoft.com*

...

Step 3 — Run the PowerShell script:

Open PowerShell as admin, connect to Exchange Online:

Connect-ExchangeOnline

Then run the alias update:

Import-Csv "alias-list.csv" | ForEach-Object {

    $UPN = $_.UserPrincipalName

    $Email1 = $_.Email1

    $Email2 = $_.Email2

 

    Set-Mailbox -Identity $UPN -EmailAddresses @{add=$Email1}

    Set-Mailbox -Identity $UPN -EmailAddresses @{add=$Email2}

}

-> This will add the two aliases for each user automatically

You don’t need to set @mydomain.mail.onmicrosoft.com as a secondary alias (Exchange Online routes via UPN by default), but it's good practice for hybrid-like consistency.

-  You can confirm aliases with:

*Get-Mailbox *****@mydomain.org | Select-Object -ExpandProperty EmailAddresses

-  If aliases already exist, Set-Mailbox won’t overwrite — it just appends.

I hope this information will help you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-06-11*

@ Joseph Tran,

Thank you so much.  First things first, of course that second line should have been this:

Set-Mailbox -Identity @MyDomain.org -EmailAddresses @{add="@MyDomain.onmicrosoft.com"}

Just for clarity, when I posted about importing a csv to create the users, I didnt mean via a PS script.  Basically I'm using the sample template that you get on the Admin>> Active Users>>Add multiple >> id like to upload a csv file with the user information.  I get sent a spreadsheet, and then I copy and paste into the sample sheet I downloaded from the admin center, then upload it.

So Id do that, and then create the csv file and populate it with the data that matches the fields you said?

I did have a question about that.  below are the field names, and underneath that is the data fields:

DisplayName,UserPrincipalName,Password,Email1,Email2

User1,@mydomain.org,YourSecurePwd123,@mydomain.mail.onmicrosoft.com,**@mydomain.onmicrosoft.com

Im not sure why I need DisplayName or the Password in either the field name or data.  Why do I?  Dont I just need the UPN and then Email1 &2 ?

Next, is the script, I get what its doing, looping through using the UPN (ie. ******@MyDomain.org) to identify the account to which the script will add the two routes, but where you have in your script "@{add=$Email1}" and 2, I would still need add the display name to the data field for Email1 and Email2, right?  Meaning those two fields I would still need to enter the full ******@mydomain.mail.onmicrosoft.com and ******@mydomain.onmicrosoft.com in the fields of that cvs file, correct?

Sorry if Im being slow, its a lot of accounts and I want to get it right first time.  Again, thank you, I appreciate you taking time out of your day to help a stranger figure this out, its very kind and I appreciate it.  Best, JH

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-06-10*

Come on, someone else must have run into this issue?  How else are you adding a remote route for a user you created in O365?  dont tell me you are okay with people having an @mail.onmicrosoft.com email address???????
