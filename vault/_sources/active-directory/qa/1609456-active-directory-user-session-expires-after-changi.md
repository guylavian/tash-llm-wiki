---
title: "Active Directory User Session Expires After Changing Password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1609456/active-directory-user-session-expires-after-changi
question_id: 1609456
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-business-platform-windows", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory User Session Expires After Changing Password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1609456/active-directory-user-session-expires-after-changi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day,

We have a SharePoint site that has a customized web part for changing a user password. The accounts are from Active Directory. The web part is added to a page and allows user to change their password. But every time a user change their password, their session expires and prompts a login. Users are unable to see the Success message unless they log in again using the new password. What is the reason behind this? Is this a normal behavior?

This is the code I used to change the AD user password:

```
PrincipalContext _context = null;
//Get context en user object
                _context = new PrincipalContext(ContextType.Domain,
                    Domain,
                    SearchString,
                    AdminUser,
                    AdminPass
                    );
                UserPrincipal user = UserPrincipal.FindByIdentity(_context, username);
                //User does not exist
                if (user == null)
                {
                    lblError.Text = "Username and/or password incorrect. Password was not changed.";
                    return;
                }
                //Check if password is expired
                bool isOldPassValid = false;
                DateTime? PasswordExpDate;
                if (user.LastPasswordSet != null)
                    PasswordExpDate = ((DateTime)user.LastPasswordSet).AddDays(int.Parse(PasswordExpiresInDays));
                else
                    PasswordExpDate = new DateTime(1970, 01, 01);
                if ((user.LastPasswordSet == null || PasswordExpDate < DateTime.UtcNow) && !user.PasswordNeverExpires)
                {
                    //Temporarly unexpire password and check credentials
                    user.RefreshExpiredPassword();
                    isOldPassValid = _context.ValidateCredentials(user.SamAccountName, oldPass);
                }
                else
                    isOldPassValid = _context.ValidateCredentials(user.SamAccountName, oldPass);
                //Old password not correct
                if (!isOldPassValid)
                {
                    lblError.Text = "Username and/or old password incorrect";
                    return;
                }
                //Everything OK, change pass
                user.SetPassword(newPass1);
                user.Save();
                lblSuccess.Text = "Your password has been changed successfully. Please close your browser and log in using your new password.";
```

## Answers

_No answers on this thread._
