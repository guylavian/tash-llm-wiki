---
title: "How to use this documentation — pages 2961-3000"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2961-3000
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2961-3000
family: powershell
documentKind: "doc"
abstract: "Important block ） Important Essential information required for user success. Caution block Ｕ Caution Negative potential consequences of an action. Warning block ２ Warning Dangerous certain consequences of an action. Markdown extension - Tables A table is an arrangement of data w"
---

# How to use this documentation — pages 2961-3000

<!-- p.2961 -->

Important block

  ） Important

  Essential information required for user success.

Caution block

  Ｕ Caution

  Negative potential consequences of an action.

Warning block

  ２ Warning

  Dangerous certain consequences of an action.

Markdown extension - Tables
A table is an arrangement of data with rows and columns consisting of:

      A single header row
      A delimiter row separating the header from the data
      Zero or more data rows

Each row consists of cells containing arbitrary text separated by pipes ( | ). A leading and
trailing pipe is also recommended for clarity. Spaces between pipes and cell content are
trimmed. Block-level elements can't be inserted in a table. All content of a row must be on a
single line.

The delimiter row consists of cells whose only content are hyphens ( - ), and optionally, a
leading or trailing colon ( : ), or both, to indicate left, right, or center alignment respectively.

For small tables, consider using a list instead. Lists are:

      Easier to maintain and read
      Can be reflowed to fit within the 100-character line limit
      More accessible for users that use screen readers for visual assistance

For more information, see Tables section of Markdown reference for Microsoft Learn.

<!-- p.2962 -->

Hyperlinks
   Hyperlinks must use Markdown syntax [friendlyname](url-or-path) .

   The publishing system supports three types of links:
     URL links
     File links
     Cross-reference links

   All URLs to external websites should use HTTPS unless that isn't valid for the target site.

   Links must have a friendly name, usually the title of the linked article

   Avoid using backticks, bold, or other markup inside the brackets of a hyperlink.

   Bare URLs can be used when you're documenting a specific URI but must be enclosed in
   backticks. For example:

     Markdown

     By default, if you don't specify this parameter, the DMTF standard resource
     URI
     `http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/` is used and the class
     name is appended to it.

   Use link references   where allowed. Link references within paragraphs make the
   paragraphs more readable.

   Link references divide a Markdown link into two parts:
     the link reference - [friendlyname][id]
     the link definition - [id]: url-or-path

URL-type Links
   URL links to other articles on learn.microsoft.com must use site-relative paths. The
   simplest way to create a site-relative link is to copy the URL from your browser then
   remove https://learn.microsoft.com/en-us from the value you paste into markdown.
   Don't include locales in URLs on Microsoft properties (remove /en-us from URL) or
   Wikipedia links.
   Remove any unnecessary query parameters from the URL. Examples that should be
   removed:
      ?view=powershell-5.1 - used to link to a specific version of PowerShell

<!-- p.2963 -->

        ?redirectedfrom=MSDN - added to the URL when you get redirected from an old article

        to its new location
     If you need to link to a specific version of a document, you must add the &preserve-
     view=true parameter to the query string. For example: ?view=powershell-5.1&preserve-

     view=true

     On Microsoft sites, URL links don't contain file extensions (for example, no .md )

File-type links
     A file link is used to link from one reference article to another, or from one conceptual
     article to another in the same docset.
        If you need to link from a conceptual article to a reference article you must use a URL
        link.
        If you need to link to an article in another docset or across repositories you must use a
        URL link.
     Use relative filepaths (for example: ../folder/file.md )
     All file paths use forward-slash ( / ) characters
     Include the file extension (for example, .md )

Cross-reference links
Cross-reference links are a special feature supported by the publishing system. You can use
cross-reference links in conceptual articles to link to .NET API or cmdlet reference.

     For links to .NET API reference, see Use links in documentation in the central Contributor
     Guide.

     Links to cmdlet reference have the following format: xref:<module-name>.<cmdlet-name> .
     For example, to link to the Get-Content cmdlet in the Microsoft.PowerShell.Management
     module.

      [Get-Content](xref:Microsoft.PowerShell.Management.Get-Content)

Deep linking
Deep linking is allowed on both URL and file links.

     The anchor text must be lowercase
     Add the anchor to the end of the target path. For example:
        [about_Splatting](about_Splatting.md#splatting-with-arrays)

<!-- p.2964 -->

         [custom key bindings]
         (https://code.visualstudio.com/docs/getstarted/keybindings#_custom-keybindings-

         for-refactorings)

For more information, see Use links in documentation.

Code spans
Code spans are used for inline code snippets within a paragraph. Use single backticks to
indicate a code span. For example:

  Markdown

  PowerShell cmdlet names use the `Verb-Noun` naming convention.

This example renders as:

PowerShell cmdlet names use the Verb-Noun naming convention.

Code blocks
Code blocks are used for command examples, multi-line code samples, query languages, and
outputs. There are two ways to indicate a section of text in an article file is a code block: by
fencing it in triple-backticks ( ``` ) or by indenting it.

Never use indentation because it's too easy to get wrong and it may be difficult for another
writer to understand your intent when they need to edit your article.

Fenced code blocks can include an optional tag that indicates the language syntax contained in
the block. The publishing platform supports a list of language tags. The language tag is used to
provide syntax highlighting when the article is rendered on the webpage. The language tag is
not case-sensitive, but you should use lowercase except for a few special cases.

      Code fences without tags can be used for syntax blocks or other types of content where
      syntax highlighting is not required.
      When showing output from a command, use a tagged code fence with the language tag
      Output . The rendered box is labeled as Output and doesn't have syntax highlighting.
      If the output is in a specific supported language, use the appropriate language tag. For
      example, many commands output JSON, so use the json tag.
      If you use an unsupported language tag, the code block will render without syntax
      highlighting. The language tag becomes the label for the rendered code box on the
      webpage. Capitalize the tag so that the label is capitalized on the webpage.

<!-- p.2965 -->

Next steps
PowerShell style guide

<!-- p.2966 -->

PowerShell-Docs style guide
Article • 03/30/2025

This article provides style guidance specific to the PowerShell-Docs content. It builds on the
information outlined in the Overview.

Formatting command syntax elements
Use the following rules to format elements of the PowerShell language when the elements are
used in a sentence.

      Always use the full name for cmdlets and parameters in the proper Pascal case

      Only use an alias when you're specifically demonstrating the alias

      PowerShell keywords and operators should be all lowercase

      The following items should be formatted using bold text:

         Type names

         Class names

         Property names

         Parameter names
            By default, use the parameter without the hyphen prefix.
            Use parameter name with the hyphen if you're illustrating syntax. Wrap the
            parameter in backticks.

         For example:

           markdown

            The parameter's name is **Name**, but it's typed as `-Name` when used on
            the command
            line as a parameter.

      The following items should be formatted using backticks ( ` ):

         Property and parameter values

         Type names that use the bracketed style - For example: [System.Io.FileInfo]

<!-- p.2967 -->

       Referring to characters by name. For example: Use the asterisk character ( * ) to as a
       wildcard.

       Language keywords and operators

       Cmdlet, function, and script names

       Command and parameter aliases

       Method names - For example: The ToString() method returns a string representation
       of the object

       Variables

       Native commands

       File and directory paths

       Inline command syntax examples - See Markdown for code samples

       This example shows some backtick examples:

          markdown

          The following code uses `Get-ChildItem` to list the contents of
          `C:\Windows` and assigns
          the output to the `$files` variable.

          ```powershell
          $files = Get-ChildItem C:\Windows
          ```

       This example shows command syntax inline:

          markdown

          To start the spooler service on a remote computer named DC01, you type:
          `sc.exe \\DC01 start spooler`.

       Including the file extension ensures that the correct command is executed according to
       PowerShell's command precedence.

Markdown for code samples
Markdown supports two different code styles:

<!-- p.2968 -->

     Code spans (inline) - marked by a single backtick ( ` ) character. Used within a paragraph
     rather than as a standalone block.
     Code blocks - a multi-line block surrounded by triple-backtick ( ``` ) strings. Code blocks
     can also have a language label following the backticks. The language label enables syntax
     highlighting for the contents of the code block.

All code blocks should be contained in a code fence. Never use indentation for code blocks.
Markdown allows this pattern but it can be problematic and should be avoided.

A code block is one or more lines of code surrounded by a triple-backtick ( ``` ) code fence.
The code fence markers must be on their own line before and after the code sample. The
opening marker can have an optional language label. The language label enables syntax
highlighting on the rendered webpage.

For a full list of supported language tags, see Fenced code blocks in the centralized contributor
guide.

Publishing also adds a Copy button that can copy the contents of the code block to the
clipboard. This allows you to paste the code into a script to test the code sample. However, not
all examples are intended to be run as written. Some code blocks are basic illustrations of
PowerShell concepts.

There are three types code blocks used in our documentation:

   1. Syntax blocks
   2. Illustrative examples
   3. Executable examples

Syntax code blocks
Syntax code blocks are used to describe the syntactic structure of a command. Don't use a
language tag on the code fence. This example illustrates all the possible parameters of the
Get-Command cmdlet.

  markdown

  ```
  Get-Command [-Verb <String[]>] [-Noun <String[]>] [-Module <String[]>]
    [-FullyQualifiedModule <ModuleSpecification[]>] [-TotalCount <Int32>] [-Syntax]
    [-ShowCommandInfo] [[-ArgumentList] <Object[]>] [-All] [-ListImported]
    [-ParameterName <String[]>] [-ParameterType <PSTypeName[]>] [<CommonParameters>]
  ```

This example describes the for statement in generalized terms:

<!-- p.2969 -->

  markdown

  ```
  for (<init>; <condition>; <repeat>)
  {<statement list>}
  ```

Illustrative examples
Illustrative examples are used to explain a PowerShell concept. Yo`u should Avoid using
PowerShell prompts in examples whenever possible. However, illustrative examples aren't
meant to be copied and pasted for execution. They're most commonly used for simple
examples that are easy to understand. You may include the PowerShell prompt and example
output.

Here's a simple example illustrating the PowerShell comparison operators. In this case, we
don't intend the reader to copy and run this example. Notice that this example uses PS> as a
simplified prompt string.

  markdown

  ```powershell
  PS> 2 -eq 2
  True

  PS> 2 -eq 3
  False

  PS> 1,2,3 -eq 2
  2

  PS> "abc" -eq "abc"
  True

  PS> "abc" -eq "abc", "def"
  False

  PS> "abc", "def" -eq "abc"
  abc
  ```

Executable examples
Complex examples, or examples that are intended to be copied and executed, should use the
following block-style markup:

<!-- p.2970 -->

  markdown

  ```powershell
  <Your PowerShell code goes here>
  ```

The output displayed by PowerShell commands should be enclosed in an Output code block to
prevent syntax highlighting. For example:

  markdown

  ```powershell
  Get-Command -Module Microsoft.PowerShell.Security
  ```

  ```Output
  CommandType    Name                            Version     Source
  -----------    ----                            -------     ------
  Cmdlet         ConvertFrom-SecureString        3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         ConvertTo-SecureString          3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Get-Acl                         3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Get-AuthenticodeSignature       3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Get-CmsMessage                  3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Get-Credential                  3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Get-ExecutionPolicy             3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Get-PfxCertificate              3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         New-FileCatalog                 3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Protect-CmsMessage              3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Set-Acl                         3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Set-AuthenticodeSignature       3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Set-ExecutionPolicy             3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Test-FileCatalog                3.0.0.0     Microsoft.PowerShell.Security
  Cmdlet         Unprotect-CmsMessage            3.0.0.0     Microsoft.PowerShell.Security
  ```

The Output code label isn't an official language supported by the syntax highlighting system.
However, this label is useful because our publishing system adds the Output label to the code
box frame on the web page. The Output code box has no syntax highlighting.

Coding style rules

Avoid line continuation in code samples
Avoid using line continuation characters ( ` ) in PowerShell code examples. Backtick characters
are difficult to see and can cause problems if there are extra spaces at the end of the line.

     Use PowerShell splatting to reduce line length for cmdlets that have several parameters.

<!-- p.2971 -->

     Take advantage of PowerShell's natural line break opportunities, like after pipe ( | )
     characters, opening braces ( { ), parentheses ( ( ), and brackets ( [ ).

Avoid using PowerShell prompts in examples
Use of the prompt string is discouraged and should be limited to scenarios that are meant to
illustrate command-line usage. For most of these examples, the prompt string should be PS> .
This prompt is independent of OS-specific indicators.

Prompts are required in examples to illustrate commands that alter the prompt or when the
path displayed is significant to the scenario. The following example illustrates how the prompt
changes when using the Registry provider.

  PowerShell

  PS C:\> cd HKCU:\System\
  PS HKCU:\System\> dir

       Hive: HKEY_CURRENT_USER\System

  Name                       Property
  ----                       --------
  CurrentControlSet
  GameConfigStore            GameDVR_Enabled                       : 1
                             GameDVR_FSEBehaviorMode               : 2
                             Win32_AutoGameModeDefaultProfile      : {2, 0, 1, 0...}
                             Win32_GameModeRelatedProcesses        : {1, 0, 1, 0...}
                             GameDVR_HonorUserFSEBehaviorMode      : 0
                             GameDVR_DXGIHonorFSEWindowsCompatible : 0

Don't use aliases in examples
Use the full name of all cmdlets and parameters unless you're specifically documenting the
alias. Cmdlet and parameter names must use the proper Pascal-cased              names.

Using parameters in examples
Avoid using positional parameters. To reduce the chance of confusion, you should include the
parameter name in an example, even if the parameter is positional.

Formatting cmdlet reference articles

<!-- p.2972 -->

Cmdlet reference articles have a specific structure. PlatyPS   defines this structure. PlatyPS
generates the cmdlet help for PowerShell modules in Markdown. After you edit the Markdown
files, PlatyPS can create the MAML help files used by the Get-Help cmdlet.

PlatyPS has a schema that expects a specific structure for cmdlet reference. The PlatyPS schema
document       describes this structure. Schema violations cause build errors that must be fixed
before we can accept your contribution.

     Don't remove any of the ATX header structures. PlatyPS expects a specific set of headers
     in a specific order.
     The H2 INPUTS and OUTPUTS headers must have an H3 type. If the cmdlet doesn't take
     input or return a value, then use the value None for the H3.
     Inline code spans can be used in any paragraph.
     Fenced code blocks are only allowed in the EXAMPLES section.

In the PlatyPS schema, EXAMPLES is an H2 header. Each example is an H3 header. Within an
example, the schema doesn't allow code blocks to be separated by paragraphs. The schema
only allows the following structure:

  ### Example X - Title sentence

  0 or more paragraphs
  1 or more code blocks
  0 or more paragraphs.

Number each example and add a brief title.

For example:

  markdown

  ### Example 1: Get cmdlets, functions, and aliases

  This command gets the PowerShell cmdlets, functions, and aliases that are
  installed on the
  computer.

  ```powershell
  Get-Command
  ```

  ### Example 2: Get commands in the current session

  ```powershell

<!-- p.2973 -->

  Get-Command -ListImported
  ```

Formatting About_ files
About_* files are written in Markdown but are shipped as plain text files. We use Pandoc     to
convert the Markdown to plain text. About_* files are formatted for the best compatibility
across all versions of PowerShell and with the publishing tools.

Basic formatting guidelines:

     Limit paragraph lines to 80 characters

     Limit code blocks to 76 characters

     Limit blockquotes and alerts to 78 characters

     When using these special meta-characters \ , $ , and < :

         Within a header, these characters must be escaped using a leading \ character or
         enclosed in code spans using backticks ( ` )

         Within a paragraph, these characters should be put into code spans. For example:

           markdown

           ### The purpose of the \$foo variable

           The `$foo` variable is used to store ...

     Markdown tables
         For About_* articles, tables must fit within 76 characters
            If the content doesn't fit within 76 character limit, use bullet lists instead
         Use opening and closing | characters on each line

Next steps
Editorial checklist

<!-- p.2974 -->

Editor's checklist
Article • 03/30/2025

This article contains a summarized list of rules for writing or editing PowerShell documentation.
See other articles in the Contributor's Guide for detailed explanations and examples of these
rules.

Metadata
         ms.date : must be in the format MM/DD/YYYY

            Change the date when there's a significant or factual update
                  Reorganizing the article
                  Fixing factual errors
                  Adding new information
            Don't change the date if the update is insignificant
                  Fixing typos and formatting
         title : unique string of 43-59 characters long (including spaces)

            Don't include site identifier (it's autogenerated)
            Use sentence case - capitalize only the first word and any proper nouns
         description : 115-145 characters including spaces - this abstract displays in the search

         result

Formatting
         Backtick syntax elements that appear, inline, within a paragraph
            Cmdlet names Verb-Noun
            Variable $counter
            Syntactic examples Verb-Noun -Parameter
            File paths C:\Program Files\PowerShell , /usr/bin/pwsh
            URLs that aren't meant to be clickable in the document
            Property or parameter values
         Use bold for property names, parameter names, class names, module names, entity
         names, object, or type names
            Bold is used for semantic markup, not emphasis
            Bold - use asterisks **
         Italic - use underscore _
            Only used for emphasis, not for semantic markup
         Line breaks at 100 columns (or at 80 for about_Topics)
         No hard tabs - use spaces only

<!-- p.2975 -->

    No trailing spaces on lines
    PowerShell keywords and operators should be all lowercase
    Use proper (Pascal) casing for cmdlet names and parameters

Headers
    Start with H1 first - only one H1 per article
    Use ATX Headers      only
    Use sentence case for all headers
    Don't skip levels - no H3 without an H2
    Limit header depth to H3 or H4
    Add blank lines before and after
    Don't add or remove headers - PlatyPS enforces specific headers in its schema

Code blocks
    Add blank lines before and after
    Use tagged code fences - powershell, Output, or other appropriate language ID
    Use untagged code fence for syntax blocks
    Put output in separate code block except for basic examples where you don't intend for
    the reader to use the Copy button
    See list of supported languages

Lists
    Indent properly
    Add blank lines before first item and after last item
    Use hyphen ( - ) for bullets not asterisk ( * ) to reduce confusion with emphasis
    Use 1. for all items in a numbered list

Terminology
    Use PowerShell vs. Windows PowerShell
    See Product Terminology

Cmdlet reference examples
    Must have at least one example in cmdlet reference

    Examples should be only enough code to demonstrate the usage

<!-- p.2976 -->

  PowerShell syntax
     Use full names of cmdlets and parameters - no aliases
     Use splatting for parameters when the command line gets too long
     Avoid using line continuation backticks - only use when necessary

  Remove or simplify the PowerShell prompt ( PS> ) except where required for the example

  Cmdlet reference example must follow the following PlatyPS schema

    markdown

    ### Example 1 - Descriptive title

    Zero or more short descriptive paragraphs explaining the context of the
    example followed by one or
    more code blocks. Recommend at least one and no more than two.

    ```powershell
    ... one or more PowerShell code statements ...
    ```

    ```Output
    Example output of the code above.
    ```

    Zero or more optional follow up paragraphs that explain the details of the
    code and output.

  don't put paragraphs between the code blocks. All descriptive content must come before
  or after the code blocks.

Linking to other documents
  When linking outside the docset or between cmdlet reference and conceptual
     Use site-relative URLs when linking to Microsoft Learn (remove
     https://learn.microsoft.com/en-us )

     don't include locales in URLs on Microsoft properties (remove /en-us from URL)
     All URLs to external websites should use HTTPS unless that's not valid for the target
     site
  When linking within the docset
     Use the relative filepath ( ../folder/file.md )
  All paths use forward-slash ( / ) characters
  Image links should have unique alt text

<!-- p.2977 -->

Product terminology and branding
guidelines
Article • 03/30/2025

When you write about any product, it's important to use the proper product names and
terminology. This guide defines product names and terminology related to PowerShell.
Note the capitalization of specific words or use cases.

PowerShell (collective name)
Use PowerShell to describe the scripting language and an interactive shell.

PowerShell (product name)
The cross-platform version of PowerShell built on .NET (core), rather than the .NET
Framework. PowerShell can be installed on Windows, Linux, and macOS.

PowerShell Core (product deprecated)
The name used for PowerShell v6, built on .NET Core. This name shouldn't be used.

Windows PowerShell (product name)
The version of PowerShell that ships in Windows, which requires the full .NET
Framework.

Guidelines

      First mention - use "Windows PowerShell"

      Subsequent mentions - Use "PowerShell" unless the use case requires "Windows
      PowerShell" to be more specific:

        In PowerShell, the Invoke-WebRequest cmdlet returns
        BasicHtmlWebResponseObject

        In Windows PowerShell, the Invoke-WebRequest cmdlet returns
        HtmlWebResponseObject

<!-- p.2978 -->

PowerShell modules
PowerShell modules are add-ons that contain PowerShell cmdlets to manage specific
products or services.

For example:

     Azure PowerShell
     Az.Accounts module
     Windows management module
     Hyper-V module
     Microsoft Graph PowerShell SDK
     Exchange PowerShell

Guidelines

     Always use the collective name or the more specific module name when referring
     to a PowerShell module
     Never refer to a module as "PowerShell"

Azure PowerShell (collective name)
The branded group of products containing PowerShell modules used to manage Azure.

There are several versions of Azure PowerShell products available. Each product contains
multiple named modules.

Guidelines

     Use "Azure PowerShell" as the collective name for the product
     Always use the collective name, never just "PowerShell"
     Use the more specific product name when referring to a specific version

Az PowerShell (product name)
The currently supported collection of modules for managing Azure resources with
PowerShell.

AzureRM PowerShell (product name)
The previous generation of modules that use the Azure Resource Manager (ARM) model
for managing Azure resources. This product is deprecated, no longer maintained or
supported, and not recommended.

<!-- p.2979 -->

Azure Service Management PowerShell (product name)
The earliest collection of modules for managing legacy Azure resources that use Azure
Service Manager (ASM) APIs. This legacy PowerShell module isn't recommended when
creating new resources since ASM is scheduled for retirement.

Azure-related PowerShell modules
These products are used to manage Azure resources but aren't part of the Azure
PowerShell collective product. They should never be described using the "Azure
PowerShell" collective name.

     Azure Information Protection PowerShell
     Azure Deployment Manager PowerShell
     Azure Elastic Database Jobs PowerShell
     Azure Service Fabric PowerShell
     Azure Stack PowerShell
     Microsoft Graph PowerShell SDK
     Microsoft Entra PowerShell

Guidelines

     Always use the full proper name of the product or the specific PowerShell module
     name

Other PowerShell-related products

Visual Studio Code (VS Code)
This is Microsoft's free, open source editor.

Guidelines

     First mention - use the full name
     Subsequent mentions - you can use "VS Code"
     Never use "VSCode"

PowerShell Extension for Visual Studio Code
The extension turns VS Code into the preferred IDE for PowerShell.

Guidelines

<!-- p.2980 -->

First mention - use the full name
Subsequent mentions - you can use "PowerShell extension"

<!-- p.2981 -->

How to file a PowerShell-Docs issue
Article • 03/30/2025

There are two ways to create an issue:

   1. Use the feedback controls at the bottom of the page.
   2. File an issue in GitHub directly

Using the feedback controls
For a full description of the feedback controls, see the Docs Team blog announcing this feature.

At the bottom of most pages on learn.microsoft.com , there are two feedback buttons. One is
a link for product feedback and one is for documentation feedback. The documentation
feedback requires a GitHub account. Clicking the button takes you in GitHub and presents an
issue template. Enter your feedback and submit the form.

  ７ Note

  The feedback tool not a support channel. It's a way to ask questions to clarify
  documentation or to report errors and omissions. If you need technical support, see
  Community resources.

Filing issues on GitHub
To file a GitHub issue directly, you can select the New issue   button in the PowerShell-Docs
repository. Select the Get started button for the issue you want to create. The GitHub issue
template helps you provide the information needed to address the problem you're reporting.

To avoid duplication, search the existing issues to see if someone else has already reported it. If
you find an existing issue, you can add your comments, related questions, or answers.

Next steps
See Get started writing.

Additional resources
How we manage issues

<!-- p.2982 -->

How to submit pull requests
Article • 03/30/2025

To make changes to content, submit a pull request (PR) from your fork. A pull request must be
reviewed before it can be merged. For best results, review the editorial checklist before
submitting your pull request.

Using git branches
The default branch for PowerShell-Docs is the main branch. Changes made in working
branches are merged into the main branch before then being published. The main branch is
merged into the live branch every weekday at 3:00 PM (Pacific Time). The live branch
contains the content that is published to learn.microsoft.com .

Before starting any changes, create a working branch in your local copy of the PowerShell-Docs
repository. When working locally, be sure to synchronize your local repository before creating
your working branch. The working branch should be created from an up-to-date copy of the
main branch.

All pull requests should target the main branch. Don't submit changes to the live branch.
Changes made in the main branch get merged into live , overwriting any changes made to
live .

Make the pull request process work better for
everyone
The simpler and more focused you can make your PR, the faster it can be reviewed and
merged.

Avoid pull requests that update large numbers of files or
contain unrelated changes
Avoid creating PRs that contain unrelated changes. Separate minor updates to existing articles
from new articles or major rewrites. Work on these changes in separate working branches.

Bulk changes create PRs with large numbers of changed files. Limit your PRs to a maximum of
50 changed files. Large PRs are difficult to review and are more prone to contain errors.

Renaming or deleting files

<!-- p.2983 -->

There must be an issue associated with the PR when you rename or delete files. That issue
must discuss the need to rename or delete the files.

Avoid mixing content additions or changes with file renames and deletes. Any file that you
rename or delete must be added to the appropriate redirection file. When possible, update any
files that link to the renamed or deleted content, including any TOC files.

Avoid editing repository configuration files
Avoid modifying repository configuration files. Limit your changes where possible to the
Markdown content files and any supporting image files needed for the content.

Incorrect modifications to repository configuration files can break the build, introduce
vulnerabilities or accessibility issues, or violate organizational standards. Repository
configuration files are any files that match one or more of these patterns:

       *.yml

       .github/**

       .localization-config
       .openpublishing*

       LICENSE*
       reference/docfx.json

       reference/mapping/**

       tests/**
       ThirdPartyNotices

       tools/**

For safety and security, don't change these files. If you think one of these files should be
changed, file an issue    . After the maintainers triage the issue, they'll make the appropriate
changes.

Use the PR template
When you create a PR, a template is automatically inserted into the PR body for you. It looks
like this:

  Markdown

   # PR Summary

   <!--
          Delete this comment block and summarize your changes and list
          related issues here. For example:

<!-- p.2984 -->

         This changes fixes problem X in the documentation for Y.

         - Fixes #1234
         - Resolves #1235
  -->

  ## PR Checklist

  <!--
         These items are mandatory. For your PR to be reviewed and merged,
         ensure you have followed these steps. As you complete the steps,
         check each box by replacing the space between the brackets with an
         x or by clicking on the box in the UI after your PR is submitted.
  -->

  - [ ] **Descriptive Title:** This PR's title is a synopsis of the changes it
  proposes.
  - [ ] **Summary:** This PR's summary describes the scope and intent of the change.
  - [ ] **Contributor's Guide:** I have read the [contributors guide][contrib].
  - [ ] **Style:** This PR adheres to the [style guide][style].

  <!--
         If your PR is a work in progress, please mark it as a draft or
         prefix it with "(WIP)" or "WIP:"

         This helps us understand whether or not your PR is ready to review.
  -->

  [contrib]: /powershell/scripting/community/contributing/overview
  [style]: /powershell/scripting/community/contributing/powershell-style-guide

In the "PR Summary" section, write a short summary of your changes and list any related issues
by their issue number, like #1234 . If your PR fixes or resolves the issue, use GitHub's
autoclose     feature so the issue is automatically closed when your PR is merged.

Review the items in the "PR Checklist" section and check them off as you complete each one.
You must follow the directions and check each item for the team to approve your PR.

If your PR is a work-in-progress, set it to draft mode   or prefix your PR title with WIP .

Expectations Comment
After you submit your PR, a bot will comment on your PR. The comment provides resources
and sets expectations for the rest of the process. We might update this comment periodically,
so always review the comment, even if this isn't your first contribution.

<!-- p.2985 -->

Docs PR validation service
The Docs PR validation service is a GitHub app that runs validation rules on your changes. You
must fix any errors or warnings reported by the validation service.

The following steps outline the validation behavior:

   1. You submit a PR.

   2. In the GitHub comment that indicates the status of the "checks" enabled on the
     repository. In this example, there are two checks enabled, "Commit Validation" and
     "OpenPublishing.Build":

<!-- p.2986 -->

  The build can pass even if commit validation fails.

3. Select Details for more information. The Details page shows all the validation checks that
  failed and includes information about how to fix the issues.

4. When validation succeeds, the following comment is added to the PR:

<!-- p.2987 -->

  ７ Note

  If you're an external contributor (not a Microsoft employee), you don't have access to the
  detailed build reports or preview links.

When the PR is reviewed, you might be asked to make changes or fix validation warning
messages. The PowerShell-Docs team can help you understand validation errors and editorial
requirements.

GitHub Actions
Several different GitHub Actions run against your changes to validate and provide context for
you and the reviewers.

Checklist verification
If your PR isn't in draft mode    and isn't prefixed with WIP , a GitHub Action inspects your PR to
verify that you selected every item in the PR template's checklist. The maintainers won't review
or merge your PR until you complete the checklist. The checklist items are mandatory.

Authorization verification
If your PR targets the live branch or modifies any repository configuration files, a GitHub
Action checks your permissions to verify that you're authorized to submit those changes.

Only repository administrators are authorized to target the live branch or modify repository
configuration files.

Versioned content change reporting
If your PR adds, removes, or modifies any versioned content a GitHub Action analyzes your
changes and writes a report summarizing the types of changes made to versioned content.

This report can show if there are other versions of the files that you need to update in this PR.

To find the versioned content report for your PR:

   1. Selecting the "Checks" tab on your PR page.
   2. Select the "Reporting" job from the list of jobs.
   3. Select the "..." button in the top right.
   4. Select "View job summary."

<!-- p.2988 -->

Next steps
PowerShell-Docs style guide

Additional resources
How we manage pull requests

<!-- p.2989 -->

Contributing quality improvements
ﾃ   Summarize this article for me

You don't have to be a subject matter expert or a documentation expert to contribute. If you
see an opportunity to improve the documentation, submit a pull request with your proposed
improvement. This guide outlines several simple ways that anyone can contribute quality
improvements to the documentation.

We're focusing on these quality areas:

     Formatting code samples
     Formatting command syntax
     Link References
     Markdown linting
     Spelling

Formatting code samples
All code samples should follow the style guidelines for PowerShell content. Those rules are
repeated in abbreviated form here for convenience:

     All code blocks should be contained in a triple-backtick code fence ( ``` ).
     Line length for code blocks is limited to 90 characters for cmdlet reference articles.
     Line length for code blocks is limited to 76 characters for about_* articles.
     Avoid using line continuation characters ( ` ) in PowerShell code examples.
        Use splatting or natural line break opportunities, like after pipe ( | ) characters, opening
        braces ( } ), parentheses ( ( ), and brackets ( [ ) to limit line length.
     Only include the PowerShell prompt for illustrative examples where the code isn't
     intended for copy-pasting.
     Don't use aliases in examples unless you're specifically documenting the alias.
     Avoid using positional parameters. Use the parameter name, even if the parameter is
     positional.

Formatting command syntax
All prose should follow the style guidelines for PowerShell content. Those rules are repeated
here for convenience:

     Always use the full name for cmdlets and parameters. Avoid using aliases unless you're
     specifically demonstrating the alias.

<!-- p.2990 -->

     Property, parameter, object, type names, class names, class methods should be bold.
        Property and parameter values should be wrapped in backticks ( ` ).
        When referring to types using the bracketed style, use backticks. For example:
         [System.Io.FileInfo]

     PowerShell module names should be bold.
     PowerShell keywords and operators should be all lowercase.
     Use proper (Pascal) casing for cmdlet names and parameters.
     When you refer to a parameter by name, the name should be bold.
     Use parameter name with the hyphen if you're illustrating syntax. Wrap the parameter in
     backticks.
     When you show example usage of an external command, the example should be wrapped
     in backticks. Always include the file extension of the external command.

Link references
For maintainability and readability of the markdown source for our documentation, we're
converting our conceptual documentation to use link references instead of inline links.

For example, instead of:

 Markdown

 The [Packages tab](https://www.powershellgallery.com/packages) displays all
 available
 packages in the PowerShell Gallery.

It should be:

 Markdown

 The [Packages tab][01] displays all available packages in the PowerShell Gallery.

  ７ Note

  When you replace an inline link, reflow the content to wrap at 100 characters. You can use
  the reflow-markdown      VS Code extension to quickly reflow the paragraph.

At the bottom of the file, add a markdown comment before the definition of the links.

 Markdown

<!-- p.2991 -->

  <!-- Link references -->
  [01]: https://www.powershellgallery.com/packages

Make sure that:

   1. Every link points to the correct location.
   2. Don't duplicate link reference definitions. If a link reference definition already exists for a
      URL, reuse the existing reference instead of creating a new one.
   3. The link reference definitions are at the bottom of the file after the markdown comment
      and are in the numeric order.

Markdown linting
For any article in one of the participating repositories, opening the article in VS Code displays
linting warnings. Address any of these warnings you find, except:

      MD022/blanks-around-headings/blanks-around-headers              for the Synopsis header in
      cmdlet reference documents. For those items, the rule violation is intentional to ensure
      the documentation builds correctly with PlatyPS.

Make sure of the line lengths and use the Reflow Markdown          extension to fix any long lines.

Spelling
Despite our best efforts, typos and misspellings get through and end up in the documentation.
These mistakes make documentation harder to follow and localize. Fixing these mistakes
makes the documentation more readable, especially for non-English speakers who rely on
accurate translations.

 Last updated on 02/12/2026

<!-- p.2992 -->

Hacktoberfest and other hack-a-thon
events
Article • 05/29/2025

Hacktoberfest is an annual worldwide event held during October. The event encourages open
source developers to contribute to repositories through pull requests (PR). GitHub hosts many
open source repositories that contribute to Microsoft Learn content. Several repositories
actively participate in Hacktoberfest.

How to contribute
Before you can contribute to an open source repo, you must first configure your account to
contribute to Microsoft Learn. If you're new to this process, start by signing up for a GitHub
account. Be sure to install Git and the Markdown tools.

To get credit for participation, register with Hacktoberfest   and read their participation guide.

Find a repo that needs your help
The PowerShell-Docs team is supporting Hacktoberfest contributions for several PowerShell
documentation repositories. We defined a set of cleanup tasks designed to be simple for first
time contributors. Full information can be found in the Hacktoberfest meta-issue      .

To be successful with these tasks, you should:

      Have a general understanding of PowerShell syntax
      Have an understanding of splatting
      Be able to read and follow the PowerShell-Docs style guide and Editorial checklist
      Have basic familiarity with Markdown

Before contributing should read the meta-issue. When you're ready to start, open a new
Hacktoberfest using one of the following links:

      MicrosoftDocs/PowerShell-Docs
      MicrosoftDocs/PowerShell-Docs-DSC
      MicrosoftDocs/PowerShell-Docs-Modules
      MicrosoftDocs/windows-powershell-docs
      MicrosoftDocs/azure-docs-powershell

Quality expectations

<!-- p.2993 -->

To have a successful contribution to an open source Microsoft Learn repository, create a
meaningful and impactful PR. The following examples from the official Hacktoberfest site are
considered low-quality contributions:

     PRs containing bulk automated changes
        Example: scripted PRs to remove whitespace, fix common spelling, or optimize images
        Submit an issue first describing the automated changes you want to make
     PRs deemed disruptive (for example, taking someone else's branch or commits and
     making a PR)
     PRs deemed a hindrance vs. helping
     PRs that are clearly an attempt to increment your PR count for October

Open a PR
A PR provides a convenient way for a contributor to propose a set of changes. Successful PRs
have these common characteristics:

     The PR adds value.
     The contributor is receptive to feedback.
     The intended changes are well articulated.
     The changes are related to an existing issue.

If you're proposing a PR without a corresponding issue, create an issue first. For more
information, see GitHub: About pull requests     .

See also
     Git and GitHub essentials for Microsoft Learn documentation
     Official Hacktoberfest site

<!-- p.2994 -->

How we manage issues
Article • 03/30/2025

This article documents how we manage issues in the PowerShell-Docs repository. This article is
designed to be a job aid for members of the PowerShell-Docs team. We publish this
information here to provide process transparency for our public contributors.

Sources of issues
      Community contributors
      Internal contributors
      Transcriptions of comments from social media channels
      Feedback via the Docs feedback form

Response time targets
80% of new issues are closed within 3 business days.

      Triaged - 1 business day
      Fix or change - 10 business days

Labeling & Milestones

Label Types
      Area - Identifies the part of PowerShell or the docs that the issue is discussing
      Issue - The type of issue: like bug, feedback, or idea
      Priority - The priority of the issue; value range 0-3 (high-low)
      Quality - The quality improvement effort the issue commits to resolving
      Status - The status of the work item or why it was closed
      Tag - Used to for additional classification like availability or doc-a-thons
      Waiting - Shows that we're waiting on some external person or event

For more information on specific labels, see Labeling.

Milestones
Issues and PRs should be tagged with the appropriate milestone. If the issue doesn't apply to a
specific version, then no milestone is used. PRs and related issues for changes that have yet to

<!-- p.2995 -->

be merged into the PowerShell code base should be assigned to the Future milestone. After
you merge the change, update the milestone to the appropriate version.

                                                                                      ﾉ   Expand table

 Milestone                 Description

 7.0.0                     Work items related to PowerShell 7.0

 7.2.0                     Work items related to PowerShell 7.2

 7.3.0                     Work items related to PowerShell 7.3

 Future                    Work items a future version of PowerShell

Triage process
PowerShell docs team members review the issues daily and triage new issues as they arrive.
The team meets weekly to discuss difficult issues need triage and prioritize the work.

Misplaced product feedback
         Enter a comment redirecting the customer to the correct feedback channel.

         Optional: Copy the issue to the appropriate product feedback location, add a link to the
         copied item, and close the issue.

         The default location for PowerShell issues is
         https://github.com/PowerShell/PowerShell/issues/new/choose         .

Support requests
         If the support question is simple, answer it politely and close the issue.

         If the question is more complicated, or the submitter replies with more questions, redirect
         them to forums and support channels. Suggested text for redirecting to forums:

           Markdown

           > This is not the right forum for these kinds of questions. Try posting your
           question in a
           > community support forum. For a list of community forums see:
           > https://learn.microsoft.com/powershell/scripting/community/community-
           support

<!-- p.2996 -->

Code of conduct violations
   Edit the issue to remove any offensive content, if necessary
   Enter a comment indicating the issue is spam, close the issue, and then lock it to prevent
   further comments
   Discuss each violation in the regular triage meeting to determine the need for further
   action

<!-- p.2997 -->

Managing pull requests
Article • 03/30/2025

This article documents how we manage pull requests in the PowerShell-Docs repository. This
article is designed to be a job aid for members of the PowerShell-Docs team. We publish this
information here to provide process transparency for our public contributors.

Best practices
      Request a review. The person submitting the PR shouldn't merge the PR without a peer
      review.
      Assign the peer reviewer when the PR is submitted. Early assignment allows the reviewer
      to respond sooner with editorial remarks.
      Use comments to describe the nature of the change being submitted. For example, if the
      change is minor, explain the change and that you don't need a full technical review. Be
      sure to @mention the reviewer.
      Use the comment suggestion feature to make it easier for the author to accept the
      suggested change. For more information, see Reviewing proposed changes in a pull
      request   .

PR Process steps
   1. Writer: Create PR

            Fill out the PR template
            Link any issues resolved by the PR
            Use GitHub's autoclose     feature to close the issue
            Work through and check off each item in the checklist

   2. Writer: Assign peer reviewer
   3. Reviewer: proofreads and comments (as necessary)
   4. Writer: Incorporate review feedback
   5. Both: Review preview rendering
   6. Both: Review validation report - fix warnings and errors
   7. Reviewer: Mark review "Approved"
   8. Repo Maintainer: Merge PR

Content Reviewer Checklist
See the editorial checklist for a more comprehensive list.

<!-- p.2998 -->

     Proofread for grammar, style, concision, technical accuracy
     Ensure examples still apply for the target version
     Check Preview rendering
     Check metadata - ms.date, remove ms.assetid, ensure required fields
     Validate markdown correctness
        See style guide for content-specific formatting rules
     Reorganize examples as follows:
        Intro paragraph
        Code and output
        Detailed explanation of code (as necessary)
     Check hyperlinks for accuracy
        Replace or remove TechNet/MSDN links
        Ensure minimum number of redirects to target
        Ensure HTTPS
        Correct link type
           File links for local files
           URL links for files outside of the docset
        Remove locales from URLs
        Simplify URLs pointing to learn.microsoft.com
     Verify versioned content is correct across all versions
        Review the versioned content change report

Branch Merge Process
The main branch is the only branch that should be merged into live . Merges from short-lived
(working) branches should be squashed before merging into main .

                                                                             ﾉ    Expand table

 Merge from/to                   release-branch                 main                live

 working-branch                squash and merge           squash and merge       Not allowed

 release-branch                          —                      merge            Not allowed

 main                                   rebase                   —                 merge

PR Merger checklist
     Content review complete
     Correct target branch for the change

<!-- p.2999 -->

     No merge conflicts
     All validation and build step pass
           Warnings and suggestions should be fixed (see Notes for exceptions)
           No broken links
           The Checklist action ran and passed
           If an Authorization check was triggered, it passed
     Merge according to table

Notes
The following warnings can be ignored:

  Can't find service name for `<version>/<modulepath>/About/About.md`

  Metadata with following name(s) are not allowed to be set in YAML header, or as
  file level
  metadata in docfx.json, or as global metadata in docfx.json: `locale`. They are
  generated by
  Docs platform, so the values set in these 3 places will be ignored. Please remove
  them from all
  3 places to resolve the warning.

When a PR is merged, the HEAD of the target branch is changed. Any open PRs that were
based on the previous HEAD are now outdated. A Maintainer has the right required to override
the merge warnings and merge the outdated PR in GitHub. Merging an outdated PR is safe if
the previously merged PRs didn't touch the same files.

To update the PR, select the Update Branch button. Choose Update with rebase option. For
more information, see Updating your pull request branch         .

Publishing to Live
Periodically, the changes accumulated in the main branch need to be published to the live
website.

     The main branch is merged to live each weekday at 3pm PST.
     The main branch should be merged to live after any significant change.
           Changes to 50 or more files
           After merging a release branch

<!-- p.3000 -->

Changes to repo or docset configurations (docfx.json, OPS configs, build scripts, etc.)
Changes to the redirection file
Changes to the TOC
After merging a "project" branch (content reorg, bulk update, etc.)
