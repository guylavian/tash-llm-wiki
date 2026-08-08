---
title: "icon previews missing in explorer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3912221/icon-previews-missing-in-explorer
question_id: 3912221
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# icon previews missing in explorer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3912221/icon-previews-missing-in-explorer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello!

i removed the default for opening .cur files, and now they show as blank files in explorer, as opposed to showing what the icon looks like. how to fix?

windows 11, newest version

second pic is what id like it to show, the image content, first is what it is currently.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-04*

Hello, k9left04 3000 k9left04 3000

Welcome to Microsoft Community.

It looks like the registry settings have been changed. You can manually delete the registry entries at the specified path.

-  Search for `regedit` in the Start menu and open it.

-  In the Registry Editor, navigate through the tree structure on the left to the following path:

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.cur
```

-  Right-click the `.cur` folder.

-  Select "Delete". In the confirmation dialog, click "Yes" to confirm the deletion.

Additionally, navigate to this path:

```
HKEY_CLASSES_ROOT\.cur
```

Check if the default value is empty. If it is, double-click the default value and change it to `anifile`. If there's no default value at all, you can manually add one:

-  Right-click the `.cur` folder and select "New" > "String Value".

-  Name the new string value `(Default)` or `Default`.

-  Double-click the new `(Default)` value and set its data to `anifile`.

Finally, restart your computer to ensure the changes take effect.

Warning: Be very careful when using the Registry Editor. Incorrectly editing the registry can cause serious problems that may require you to reinstall your operating system and result in data loss. To protect yourself, make sure to back up the registry before making any changes. This way, you can restore the registry if something goes wrong.

How to back up and restore the registry in Windows - Microsoft Support

Yuhao L

Microsoft Community Technical Support
