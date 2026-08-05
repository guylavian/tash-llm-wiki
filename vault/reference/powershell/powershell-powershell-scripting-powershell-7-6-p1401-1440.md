---
title: "How to use this documentation — pages 1401-1440"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1401-1440
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1401-1440
family: powershell
documentKind: "doc"
abstract: "dash lt dash match dash ne dash notcontains dash notin dash notlike dash notmatch dash replace dash shl* dash shr dash split format-operator: dash f B.2 Syntactic grammar B.2.1 Basic concepts Syntax script-file: script-block module-file: script-block interactive-input: script-bl"
---

# How to use this documentation — pages 1401-1440

<!-- p.1401 -->

     dash lt            dash match         dash ne
     dash notcontains   dash notin        dash notlike
     dash notmatch      dash replace      dash shl*
     dash shr           dash split

 format-operator:
     dash f

B.2 Syntactic grammar
B.2.1 Basic concepts

 Syntax

 script-file:
     script-block

 module-file:
     script-block

 interactive-input:
     script-block

 data-file:
     statement-list

B.2.2 Statements

 Syntax

 script-block:
     param-block~opt~ statement-terminators~opt~ script-block-body~opt~

 param-block:
     new-lines~opt~ attribute-list~opt~ new-lines~opt~ param new-lines~opt~
         ( parameter-list~opt~ new-lines~opt~ )

 parameter-list:
     script-parameter
     parameter-list new-lines~opt~ , script-parameter

 script-parameter:
     new-lines~opt~ attribute-list~opt~ new-lines~opt~ variable script-parameter-
 default~opt~

 script-parameter-default:
     new-lines~opt~ = new-lines~opt~ expression

 script-block-body:
     named-block-list

<!-- p.1402 -->

    statement-list

named-block-list:
    named-block
    named-block-list named-block

named-block:
    block-name statement-block statement-terminators~opt~

block-name: one of
    dynamicparam begin process end

statement-block:
    new-lines~opt~ { statement-list~opt~ new-lines~opt~ }

statement-list:
    statement
    statement-list statement

statement:
    if-statement
    label~opt~ labeled-statement
    function-statement
    flow-control-statement statement-terminator
    trap-statement
    try-statement
    data-statement
    inlinescript-statement
    parallel-statement
    sequence-statement
    pipeline statement-terminator

statement-terminator:
    ;
    new-line-character

statement-terminators:
    statement-terminator
    statement-terminators statement-terminator

if-statement:
    if new-lines~opt~ ( new-lines~opt~ pipeline new-lines~opt~ ) statement-block
        elseif-clauses~opt~ else-clause~opt~

elseif-clauses:
    elseif-clause
    elseif-clauses elseif-clause

elseif-clause:
    new-lines~opt~ elseif new-lines~opt~ ( new-lines~opt~ pipeline new-lines~opt~ )
statement-block

else-clause:
    new-lines~opt~ else statement-block

<!-- p.1403 -->

labeled-statement:
    switch-statement
    foreach-statement
    for-statement
    while-statement
    do-statement

switch-statement:
    switch new-lines~opt~ switch-parameters~opt~ switch-condition switch-body

switch-parameters:
    switch-parameter
    switch-parameters switch-parameter

switch-parameter:
    -Regex
    -Wildcard
    -Exact
    -CaseSensitive
    -Parallel

switch-condition:
    ( new-lines~opt~ pipeline new-lines~opt~ )
    -file new-lines~opt~ switch-filename

switch-filename:
    command-argument
    primary-expression

switch-body:
    new-lines~opt~ { new-lines~opt~ switch-clauses }

switch-clauses:
    switch-clause
    switch-clauses switch-clause

switch-clause:
    switch-clause-condition statement-block statement-terimators~opt~

switch-clause-condition:
    command-argument
    primary-expression

foreach-statement:
    foreach new-lines~opt~ foreach-parameter~opt~ new-lines~opt~
        ( new-lines~opt~ variable new-lines~opt~ in new-lines~opt~ pipeline
        new-lines~opt~ ) statement-block

foreach-parameter:
    -parallel

for-statement:
    for new-lines~opt~ (
        new-lines~opt~ for-initializer~opt~ statement-terminator
        new-lines~opt~ for-condition~opt~ statement-terminator

<!-- p.1404 -->

        new-lines~opt~ for-iterator~opt~
        new-lines~opt~ ) statement-block
    for new-lines~opt~ (
        new-lines~opt~ for-initializer~opt~ statement-terminator
        new-lines~opt~ for-condition~opt~
        new-lines~opt~ ) statement-block
    for new-lines~opt~ (
        new-lines~opt~ for-initializer~opt~
        new-lines~opt~ ) statement-block

for-initializer:
    pipeline

for-condition:
    pipeline

for-iterator:
    pipeline

while-statement:
    while new-lines~opt~ ( new-lines~opt~ while-condition new-lines~opt~ )
statement-block

do-statement:
    do statement-block new-lines~opt~ while new-lines~opt~ ( while-condition new-
lines~opt~ )
    do statement-block new-lines~opt~ until new-lines~opt~ ( while-condition new-
lines~opt~ )

while-condition:
    new-lines~opt~ pipeline

function-statement:
    function new-lines~opt~ function-name function-parameter-declaration~opt~ {
script-block }
    filter new-lines~opt~ function-name function-parameter-declaration~opt~ {
script-block }
    workflow new-lines~opt~ function-name function-parameter-declaration~opt~ {
script-block }

function-name:
    command-argument

function-parameter-declaration:
    new-lines~opt~ ( parameter-list new-lines~opt~ )

flow-control-statement:
    break label-expression~opt~
    continue label-expression~opt~
    throw pipeline~opt~
    return pipeline~opt~
    exit pipeline~opt~

label-expression:
    simple-name

<!-- p.1405 -->

    unary-expression

trap-statement:
    trap new-lines~opt~ type-literal~opt~ new-lines~opt~ statement-block

try-statement:
    try statement-block catch-clauses
    try statement-block finally-clause
    try statement-block catch-clauses finally-clause

catch-clauses:
    catch-clause
    catch-clauses catch-clause

catch-clause:
    new-lines~opt~ catch catch-type-list~opt~ statement-block

catch-type-list:
    new-lines~opt~ type-literal
    catch-type-list new-lines~opt~ , new-lines~opt~ type-literal

finally-clause:
    new-lines~opt~ finally statement-block

data-statement:
    data new-lines~opt~ data-name data-commands-allowed~opt~
    statement-block

data-name:
    simple-name

data-commands-allowed:
    new-lines~opt~ -SupportedCommand data-commands-list

data-commands-list:
    new-lines~opt~ data-command
    data-commands-list , new-lines~opt~ data-command

data-command:
    command-name-expr

inlinescript-statement:
    inlinescript statement-block

parallel-statement:
    parallel statement-block

sequence-statement:
    sequence statement-block

pipeline:
    assignment-expression
    expression redirections~opt~ pipeline-tail~opt~
    command verbatim-command-argument~opt~ pipeline-tail~opt~

<!-- p.1406 -->

assignment-expression:
    expression assignment-operator statement

pipeline-tail:
    | new-lines~opt~ command
    | new-lines~opt~ command pipeline-tail

command:
    command-name command-elements~opt~
    command-invocation-operator command-module~opt~ command-name-expr command-
elements~opt~

command-invocation-operator: one of
    &   .

command-module:
    primary-expression

command-name:
    generic-token
    generic-token-with-subexpr

generic-token-with-subexpr:
    No whitespace is allowed between ) and command-name.
    generic-token-with-subexpr-start statement-list~opt~ ) command-name

command-name-expr:
    command-name
    primary-expression

command-elements:
    command-element
    command-elements command-element

command-element:
    command-parameter
    command-argument
    redirection

command-argument:
    command-name-expr

verbatim-command-argument:
    --% verbatim-command-argument-chars

redirections:
    redirection
    redirections redirection

redirection:
    merging-redirection-operator
    file-redirection-operator redirected-file-name

redirected-file-name:

<!-- p.1407 -->

     command-argument
     primary-expression

B.2.3 Expressions

 Syntax

 expression:
     logical-expression

 logical-expression:
     bitwise-expression
     logical-expression -and new-lines~opt~ bitwise-expression
     logical-expression -or new-lines~opt~ bitwise-expression
     logical-expression -xor new-lines~opt~ bitwise-expression

 bitwise-expression:
     comparison-expression
     bitwise-expression -band new-lines~opt~ comparison-expression
     bitwise-expression -bor new-lines~opt~ comparison-expression
     bitwise-expression -bxor new-lines~opt~ comparison-expression

 comparison-expression:
     additive-expression
     comparison-expression comparison-operator new-lines~opt~
     additive-expression

 additive-expression:
     multiplicative-expression
     additive-expression + new-lines~opt~ multiplicative-expression
     additive-expression dash new-lines~opt~ multiplicative-expression

 multiplicative-expression:
     format-expression
     multiplicative-expression \ new-lines~opt~ format-expression
     multiplicative-expression / new-lines~opt~ format-expression
     multiplicative-expression % new-lines~opt~ format-expression

 format-expression:
     range-expression
     format-expression format-operator new-lines~opt~ range-expression

 range-expression:
     array-literal-expression
     range-expression .. new-lines~opt~ array-literal-expression

 array-literal-expression:
     unary-expression
     unary-expression , new-lines~opt~ array-literal-expression

 unary-expression:
     primary-expression
     expression-with-unary-operator

<!-- p.1408 -->

expression-with-unary-operator:
    , new-lines~opt~ unary-expression
    -not new-lines~opt~ unary-expression
    ! new-lines~opt~ unary-expression
    -bnot new-lines~opt~ unary-expression
    + new-lines~opt~ unary-expression
    dash new-lines~opt~ unary-expression
    pre-increment-expression
    pre-decrement-expression
    cast-expression
    -split new-lines~opt~ unary-expression
    -join new-lines~opt~ unary-expression

pre-increment-expression:
    ++ new-lines~opt~ unary-expression

pre-decrement-expression:
    dashdash new-lines~opt~ unary-expression

cast-expression:
    type-literal unary-expression

attributed-expression:
    type-literal variable

primary-expression:
    value
    member-access
    element-access
    invocation-expression
    post-increment-expression
    post-decrement-expression

value:
    parenthesized-expression
    sub-expression
    array-expression
    script-block-expression
    hash-literal-expression
    literal
    type-literal
    variable

parenthesized-expression:
    ( new-lines~opt~ pipeline new-lines~opt~ )

sub-expression:
    $( new-lines~opt~ statement-list~opt~ new-lines~opt~ )

array-expression:
    @( new-lines~opt~ statement-list~opt~ new-lines~opt~ )

script-block-expression:
    { new-lines~opt~ script-block new-lines~opt~ }

<!-- p.1409 -->

hash-literal-expression:
    @{ new-lines~opt~ hash-literal-body~opt~ new-lines~opt~ }

hash-literal-body:
    hash-entry
    hash-literal-body statement-terminators hash-entry

hash-entry:
    key-expression = new-lines~opt~ statement

key-expression:
    simple-name
    unary-expression

post-increment-expression:
    primary-expression ++

post-decrement-expression:
    primary-expression dashdash

member-access: Note no whitespace is allowed after
    primary-expression.
    primary-expression . member-name
    primary-expression :: member-name

element-access: Note no whitespace is allowed between primary-expression and [.
    primary-expression [ new-lines~opt~ expression new-lines~opt~ ]

invocation-expression: Note no whitespace is allowed after
    primary-expression.
    primary-expression . member-name argument-list
    primary-expression :: member-name argument-list

argument-list:
    ( argument-expression-list~opt~ new-lines~opt~ )

argument-expression-list:
    argument-expression
    argument-expression new-lines~opt~ , argument-expression-list

argument-expression:
    new-lines~opt~ logical-argument-expression

logical-argument-expression:
    bitwise-argument-expression
    logical-argument-expression -and new-lines~opt~ bitwise-argument-expression
    logical-argument-expression -or new-lines~opt~ bitwise-argument-expression
    logical-argument-expression -xor new-lines~opt~ bitwise-argument-expression

bitwise-argument-expression:
    comparison-argument-expression
    bitwise-argument-expression -band new-lines~opt~ comparison-argument-expression
    bitwise-argument-expression -bor new-lines~opt~ comparison-argument-expression
    bitwise-argument-expression -bxor new-lines~opt~ comparison-argument-expression

<!-- p.1410 -->

comparison-argument-expression:
    additive-argument-expression
    comparison-argument-expression comparison-operator
        new-lines~opt~ additive-argument-expression

additive-argument-expression:
    multiplicative-argument-expression
    additive-argument-expression +     new-lines~opt~ multiplicative-argument-
expression
    additive-argument-expression dash new-lines~opt~ multiplicative-argument-
expression

multiplicative-argument-expression:
    format-argument-expression
    multiplicative-argument-expression \ new-lines~opt~ format-argument-expression
    multiplicative-argument-expression / new-lines~opt~ format-argument-expression
    multiplicative-argument-expression % new-lines~opt~ format-argument-expression

format-argument-expression:
    range-argument-expression
    format-argument-expression format-operator new-lines~opt~ range-argument-
expression

range-argument-expression:
    unary-expression
    range-expression .. new-lines~opt~ unary-expression

member-name:
    simple-name
    string-literal
    string-literal-with-subexpression
    expression-with-unary-operator
    value

string-literal-with-subexpression:
    expandable-string-literal-with-subexpr
    expandable-here-string-literal-with-subexpr

expandable-string-literal-with-subexpr:
    expandable-string-with-subexpr-start statement-list~opt~ )
        expandable-string-with-subexpr-characters expandable-string-with-subexpr-
end
    expandable-here-string-with-subexpr-start statement-list~opt~ )
        expandable-here-string-with-subexpr-characters
        expandable-here-string-with-subexpr-end

expandable-string-with-subexpr-characters:
    expandable-string-with-subexpr-part
    expandable-string-with-subexpr-characters expandable-string-with-subexpr-part

expandable-string-with-subexpr-part:
    sub-expression
    expandable-string-part

<!-- p.1411 -->

 expandable-here-string-with-subexpr-characters:
     expandable-here-string-with-subexpr-part
     expandable-here-string-with-subexpr-characters expandable-here-string-with-
 subexpr-part

 expandable-here-string-with-subexpr-part:
     sub-expression
     expandable-here-string-part

 type-literal:
     [ type-spec ]

 type-spec:
     array-type-name new-lines~opt~ dimension~opt~ ]
     generic-type-name new-lines~opt~ generic-type-arguments ]
     type-name

 dimension:
     ,
     dimension ,

 generic-type-arguments:
     type-spec new-lines~opt~
     generic-type-arguments , new-lines~opt~ type-spec

B.2.4 Attributes

 Syntax

 attribute-list:
     attribute
     attribute-list new-lines~opt~ attribute

 attribute:
     [ new-lines~opt~ attribute-name ( attribute-arguments new-lines~opt~ ) new-
 lines~opt~ ]
     type-literal

 attribute-name:
     type-spec

 attribute-arguments:
     attribute-argument
     attribute-argument new-lines~opt~ , attribute-arguments

 attribute-argument:
     new-lines~opt~ expression
     new-lines~opt~ simple-name
     new-lines~opt~ simple-name = new-lines~opt~ expression

<!-- p.1412 -->

Last updated on 03/24/2025

<!-- p.1413 -->

C. References
Article • 01/08/2025

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December
  2012 and is based on Windows PowerShell 3.0. This specification does not reflect
  the current state of PowerShell. There is no plan to update this documentation to
  reflect the current state. This documentation is presented here for historical
  reference.

  The specification document is available as a Microsoft Word document from the
  Microsoft Download Center at:
  https://www.microsoft.com/download/details.aspx?id=36389            That Word
  document has been converted for presentation here on Microsoft Learn. During
  conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

ANSI/IEEE 754−2008, Binary floating-point arithmetic for microprocessor systems.

ECMA-334, C# Language Specification, 4th edition (June 2006), https://www.ecma-
international.org/publications-and-standards/standards/ecma-334/ . [This Ecma
publication is also approved as ISO/IEC 23270:2006.]

The Open Group Base Specifications: Pattern Matching, IEEE Std 1003.1, 2004 Edition.
http://www.opengroup.org/onlinepubs/000095399/utilities/xcu_chap02.html#tag_02_13
_01

The Open Group Base Specifications: Regular Expressions, IEEE Std 1003.1, 2004 Edition.
http://www.opengroup.org/onlinepubs/000095399/basedefs/xbd_chap09.html             .

Ecma Technical Report TR/84, Common Language Infrastructure (CLI) - Information
Derived from Partition IV XML File, 4th edition (June 2006), https://www.ecma-
international.org/publications-and-standards/technical-reports/ecma-tr-84/ . This TR
was also published as ISO/IEC TR 23272:2006.

ISO 639-1, Codes for the representation of names of languages - Part 1: Alpha-2 code.

<!-- p.1414 -->

ISO 3166-1, Codes for the representation of names of countries and their subdivisions -
Part 1: Country codes.

ISO/IEC 10646-1/AMD1:1996, Amendment 1 to ISO/IEC 10646-1:1993, Transformation
Format for 16 planes of group 00 (UTF-16).

The Unicode Standard, Edition 5.2. The Unicode Consortium,
http://www.unicode.org/standard/standard.html      .

<!-- p.1415 -->

Windows PowerShell
Updated: July 8, 2013

Windows PowerShell® is a task-based command-line shell and scripting language designed
especially for system administration. Built on the .NET Framework, Windows PowerShell® helps
IT professionals and power users control and automate the administration of the Windows
operating system and applications that run on Windows.

The documents published here are written primarily for cmdlet, provider, and host application
developers who require reference information about the APIs provided by Windows
PowerShell. However, system administrators might also find the information provided by these
documents useful.

For the basic information needed to start using Windows PowerShell, see Getting Started with
Windows PowerShell .

Windows PowerShell Documents
     Installing the Windows PowerShell SDK Provides information about how to install the
     Windows PowerShell SDK.

     Writing a Windows PowerShell Module Provides information for administrators, script
     developers, and cmdlet developers who need to package and distribute their Windows
     PowerShell solutions.

     Writing a Windows PowerShell Cmdlet Provides information for designing and
     implementing cmdlets.

     Writing a Windows PowerShell Provider Provides information for designing and
     implementing Windows PowerShell providers. It will help you understand how Windows
     PowerShell providers work, and it provides sample code that you can use to start
     designing or writing your own providers.

     Writing a Windows PowerShell Host Application Provides information that can be used by
     program managers who are designing host applications and by developers who are
     implementing them. The host application can, define the runspace where commands are
     run, open sessions on a local or remote computer, and invoke the commands either
     synchronously or asynchronously based on the needs of the application.

<!-- p.1416 -->

     Writing a PowerShell Formatting File Provides information for the authoring of formatting
     files, which control the display format for the objects that are returned by commands
     (cmdlets, functions, and scripts).

     Windows PowerShell Reference Provides reference content for the APIs used in writing
     cmdlets, providers, and host applications, as well as other supporting APIs.

Last updated on 05/20/2025

<!-- p.1417 -->

Installing the Windows PowerShell SDK
Applies To: Windows PowerShell 2.0, Windows PowerShell 3.0

The following topic describes how to install the PowerShell SDK on different versions of
Windows.

Installing Windows PowerShell 3.0 SDK for
Windows 8 and Windows Server 2012
Windows PowerShell 3.0 is automatically installed with Windows 8 and Windows Server 2012.
In addition, you can download and install the reference assemblies for Windows PowerShell 3.0
as part of the Windows 8 SDK. These assemblies allow you to write cmdlets, providers, and host
programs for Windows PowerShell 3.0. When you install the Windows SDK for Windows 8, the
Windows PowerShell assemblies are automatically installed in the reference assembly folder, in
\Program Files (x86)\Reference Assemblies\Microsoft\WindowsPowerShell\3.0 . For more

information, see the Windows 8 SDK download site. Windows PowerShell code samples are
also available in the powershell-sdk-samples    repository.

Reference assemblies
Reference assemblies are installed in the following location by default: C:\Program
Files\Reference Assemblies\Microsoft\WindowsPowerShell\V1.0 .

  ７ Note

  Code that is compiled against the Windows PowerShell 2.0 assemblies cannot be loaded
  into Windows PowerShell 1.0 installations. However, code that is compiled against the
  Windows PowerShell 1.0 assemblies can be loaded into Windows PowerShell 2.0
  installations.

Samples
Code samples are installed in the following location by default: C:\Program Files\Microsoft
SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\ . The following sections provide a brief

description of what each sample does.

<!-- p.1418 -->

Cmdlet samples

   GetProcessSample01 - Shows how to write a simple cmdlet that gets all the processes on
   the local computer.
   GetProcessSample02 - Shows how to add parameters to the cmdlet. The cmdlet takes
   one or more process names and returns the matching processes.
   GetProcessSample03 - Shows how to add parameters that accept input from the pipeline.
   GetProcessSample04 - Shows how to handle non-terminating errors.
   GetProcessSample05 - Shows how to display a list of specified processes.
   SelectObject - Shows how to write a filter to select only certain objects.
   SelectString - Shows how to search files for specified patterns.
   StopProcessSample01 - Shows how to implement a PassThru parameter, and how to
   request user feedback by calls to the ShouldProcess and ShouldContinue methods. Users
   specify the PassThru parameter when they want to force the cmdlet to return an object,
   StopProcessSample02 - Shows how to stop a specific process.
   StopProcessSample03 - Shows how to declare aliases for parameters and how to support
   wildcards.
   StopProcessSample04 - Shows how to declare parameter sets, the object that the cmdlet
   takes as input, and how to specify the default parameter set to use.

Remoting samples

   RemoteRunspace01 - Shows how to create a remote runspace that is used to establish a
   remote connection.
   RemoteRunspacePool01 - Shows how to construct a remote runspace pool and how to
   run multiple commands concurrently by using this pool.
   Serialization01 - Shows how to look at an existing .NET class and make sure that
   information from selected public properties of this class is preserved across
   serialization/deserialization.
   Serialization02 - Shows how to look at an existing .NET class and make sure that
   information from instance of this class is preserved across serialization/deserialization
   when the information is not available in public properties of the class.
   Serialization03 - Shows how to look at an existing .NET class and make sure that instances
   of this class and of derived classes are deserialized (rehydrated) into live .NET objects.

Event samples

   Event01 - Shows how to create a cmdlet for event registration by deriving from
   ObjectEventRegistrationBase.

<!-- p.1419 -->

   Event02 - Shows how to shows how to receive notifications of Windows PowerShell
   events that are generated on remote computers. It uses the PSEventReceived event
   exposed through the Runspace class.

Hosting application samples

   Runspace01 - Shows how to use the PowerShell class to run the Get-Process cmdlet
   synchronously. The Get-Process cmdlet returns Process objects for each process running
   on the local computer.
   Runspace02 - Shows how to use the PowerShell class to run the Get-Process and Sort-
   Object cmdlets synchronously. The Get-Process cmdlet returns Process objects for each

   process running on the local computer, and the Sort-Object sorts the objects based on
   their Id property. The results of these commands is displayed by using a DataGridView
   control.
   Runspace03 - Shows how to use the PowerShell class to run a script synchronously, and
   how to handle non-terminating errors. The script receives a list of process names and
   then retrieves those processes. The results of the script, including any non-terminating
   errors that were generated when running the script, are displayed in a console window.
   Runspace04 - Shows how to use the PowerShell class to run commands, and how to catch
   terminating errors that are thrown when running the commands. Two commands are run,
   and the last command is passed a parameter argument that is not valid. As a result, no
   objects are returned and a terminating error is thrown.
   Runspace05 - Shows how to add a snap-in to an InitialSessionState object so that the
   cmdlet of the snap-in is available when the runspace is opened. The snap-in provides a
   Get-Proc cmdlet (defined by the GetProcessSample01 Sample) that is run synchronously
   using a PowerShell object.
   Runspace06 - Shows how to add a module to an InitialSessionState object so that the
   module is loaded when the runspace is opened. The module provides a Get-Proc cmdlet
   (defined by the GetProcessSample02 Sample) that is run synchronously using a
   PowerShell object.
   Runspace07 - Shows how to create a runspace, and then use that runspace to run two
   cmdlets synchronously using a PowerShell object.
   Runspace08 - Shows how to add commands and arguments to the pipeline of a
   PowerShell object and how to run the commands synchronously.
   Runspace09 - Shows how to add a script to the pipeline of a PowerShell object and how
   to run the script asynchronously. Events are used to handle the output of the script.
   Runspace10 - Shows how to create a default initial session state, how to add a cmdlet to
   the InitialSessionState, how to create a runspace that uses the initial session state, and

<!-- p.1420 -->

   how to run the command using a PowerShell object.
   Runspace11 - Shows how to use the ProxyCommand class to create a proxy command
   that calls an existing cmdlet, but restricts the set of available parameters. The proxy
   command is then added to an initial session state that is used to create a constrained
   runspace. This means that the user can access the functionality of the cmdlet only
   through the proxy command.
   PowerShell01 - Shows how to create a constrained runspace using an InitialSessionState
   object.
   PowerShell02 - Shows how to use a runspace pool to run multiple commands
   concurrently.

Host samples

   Host01 - Shows how to implement a host application that uses a custom host. In this
   sample a runspace is created that uses the custom host, and then the PowerShell API is
   used to run a script that calls exit . The host application then looks at the output of the
   script and prints out the results.
   Host02 - Shows how to write a host application that uses the Windows PowerShell
   runtime along with a custom host implementation. The host application sets the host
   culture to German, runs the Get-Process cmdlet and displays the results as you would see
   them by using pwrsh.exe, and then prints out the current data and time in German.
   Host03 - Shows how to build an interactive console-based host application that reads
   commands from the command line, executes the commands, and then displays the
   results to the console.
   Host04 - Shows how to build an interactive console-based host application that reads
   commands from the command line, executes the commands, and then displays the
   results to the console. This host application also supports displaying prompts that allow
   the user to specify multiple choices.
   Host05 - Shows how to build an interactive console-based host application that reads
   commands from the command line, executes the commands, and then displays the
   results to the console. This host application also supports calls to remote computers by
   using the Enter-PSSession and Exit-PSSession cmdlets.
   Host06 - Shows how to build an interactive console-based host application that reads
   commands from the command line, executes the commands, and then displays the
   results to the console. In addition, this sample uses the Tokenizer APIs to specify the color
   of the text that is entered by the user.

Provider samples

<!-- p.1421 -->

     AccessDBProviderSample01 - Shows how to declare a provider class that derives directly
     from the CmdletProvider class. It is included here only for completeness.

     AccessDBProviderSample02 - Shows how to overwrite the NewDrive and RemoveDrive
     methods to support calls to the New-PSDrive and Remove-PSDrive cmdlets. The provider
     class in this sample derives from the DriveCmdletProvider class.

     AccessDBProviderSample03 - Shows how to overwrite the GetItem and SetItem methods
     to support calls to the Get-Item and Set-Item cmdlets. The provider class in this sample
     derives from the ItemCmdletProvider class.

     AccessDBProviderSample04 - Shows how to overwrite container methods to support calls
     to the Copy-Item , Get-ChildItem , New-Item , and Remove-Item cmdlets. These methods
     should be implemented when the data store contains items that are containers. A
     container is a group of child items under a common parent item. The provider class in this
     sample derives from the ItemCmdletProvider class.

     AccessDBProviderSample05 - Shows how to overwrite container methods to support calls
     to the Move-Item and Join-Path cmdlets. These methods should be implemented when
     the user needs to move items within a container and if the data store contains nested
     containers. The provider class in this sample derives from the NavigationCmdletProvider
     class.

     AccessDBProviderSample06 - Shows how to overwrite content methods to support calls
     to the Clear-Content , Get-Content , and Set-Content cmdlets. These methods should be
     implemented when the user needs to manage the content of the items in the data store.
     The provider class in this sample derives from the NavigationCmdletProvider class, and it
     implements the IContentCmdletProvider interface.

Last updated on 05/20/2025

<!-- p.1422 -->

Windows PowerShell Reference
Windows PowerShell is a Microsoft .NET Framework-connected environment designed for
administrative automation. Windows PowerShell provides a new approach to building
commands, composing solutions, and creating graphical user interface-based management
tools.

Windows PowerShell enables a system administrator to automate the administration of system
resources by the execution of commands either directly or through scripts.

Developer Audience
The Windows PowerShell Software Development Kit (SDK) is written for command developers
who require reference information about the APIs provided by Windows PowerShell. Command
developers use Windows PowerShell to create both commands and providers that extend the
tasks that can be performed by Windows PowerShell.

Windows PowerShell Resources
In addition to the Windows PowerShell SDK, the following resources provide more information.

Getting Started with Windows PowerShell Provides an introduction to Windows PowerShell: the
language, the cmdlets, the providers, and the use of objects.

Writing a Windows PowerShell Module Provides information and examples for administrators,
script developers, and cmdlet developers who need to package and distribute their Windows
PowerShell solutions using Windows PowerShell modules.

Writing a Windows PowerShell Cmdlet Provides information and code examples for program
managers who are designing cmdlets and for developers who are implementing cmdlet code.

Windows PowerShell Team Blog        The best resource for learning from and collaborating with
other Windows PowerShell users. Read the Windows PowerShell Team blog, and then join the
Windows PowerShell User Forum (microsoft.public.windows.powershell). Use Windows Live
Search to find other Windows PowerShell blogs and resources. Then, as you develop your
expertise, freely contribute your ideas.

PowerShell module browser Provides the latest versions of the command-line Help topics.

<!-- p.1423 -->

Class Libraries
System.Management.Automation This namespace is the root namespace for Windows
PowerShell. It contains the classes, enumerations, and interfaces required to implement custom
cmdlets. In particular, the System.Management.Automation.Cmdlet class is the base class from
which all cmdlet classes must be derived. For more information about cmdlets, see.

System.Management.Automation.Provider This namespace contains the classes, enumerations,
and interfaces required to implement a Windows PowerShell provider. In particular, the
System.Management.Automation.Provider.CmdletProvider class is the base class from which all
Windows PowerShell provider classes must be derived.

Microsoft.PowerShell.Commands This namespace contains the classes for the cmdlets and
providers implemented by Windows PowerShell. Similarly, it is recommended that you create a
YourName.Commands namespace for those cmdlets that you implement.

System.Management.Automation.Host This namespace contains the classes, enumerations, and
interfaces that the cmdlet uses to define the interaction between the user and Windows
PowerShell.

System.Management.Automation.Internal This namespace contains the base classes used by
other namespace classes. For example, the
System.Management.Automation.Internal.CmdletMetadataAttribute class is the base class for
the System.Management.Automation.CmdletAttribute class.

System.Management.Automation.Runspaces This namespace contains the classes,
enumerations, and interfaces used to create a Windows PowerShell runspace. In this context,
the Windows PowerShell runspace is the context in which one or more Windows PowerShell
pipelines invoke cmdlets. That is, cmdlets work within the context of a Windows PowerShell
runspace. For more information aboutWindows PowerShell runspaces, see Windows PowerShell
Runspaces.

Last updated on 05/20/2025

<!-- p.1424 -->

What's New
Windows PowerShell 2.0 provides the following new features for use when writing cmdlets,
providers, and host applications.

Modules
You can now package and distribute Windows PowerShell solutions by using modules. Modules
allow you to partition, organize, and abstract your Windows PowerShell code into self-
contained, reusable units. For more information about modules, see Writing a Windows
PowerShell Module.

The PowerShell class
The PowerShell class provides a simpler solution for creating applications, referred to as host
applications, that programmatically run commands. This class allows you to create a pipeline of
commands, specify the runspace that is used to run the commands, and specify invoking the
commands synchronously or asynchronously.

The RunspacePool class
Runspace pools allow you to create multiple runspaces by using a single call. The
CreateRunspacePool method provides several overloads that can be used to create runspaces
that have the same features, such as the same host, initial session state, and connection
information.

The InitialSessionState class
The InitialSessionState class allows you to create a session state configuration that is used
when a runspace is opened. You can create a custom configuration, a default configuration that
includes the commands provided by mshshort, and a configuration whose commands are
restricted based on the capabilities of the session.

Remote runspaces
You can now create runspaces that can be opened on remote computers, allowing you to run
commands on the remote machine and collect the results locally. To create a remote runspace,

<!-- p.1425 -->

you must specify information about the remote connection when creating the runspace. See
the CreateRunspace and CreateRunspacePool methods for examples. The connection
information is defined by the RunspaceConnectionInfo class.

Private runspace elements
You can now create runspaces whose elements are public or private. This allows you to create
runspaces whose elements are available to the runspace, but are not available to the user. See
the ConstrainedSessionStateEntry class to find out which elements of the runspace can be
made private.

Runspace threading modes and apartment state
You can now specify how threads are created and used when running commands in a runspace.
See the System.Management.Automation.Runspaces.Runspace.ThreadOptions and
System.Management.Automation.Runspaces.RunspacePool.ThreadOptions properties.

You can now get the apartment state of the threads that are used to run commands in a
runspace. See the System.Management.Automation.Runspaces.Runspace.ApartmentState and
System.Management.Automation.Runspaces.RunspacePool.ApartmentState properties.

Transaction cmdlets
You can now create cmdlets that can be used within a transaction. When a cmdlet is used in a
transaction, its actions are temporary, and they can be accepted or rejected by the transaction
cmdlets provided by Windows PowerShell.

For more information about transactions, see How to Support Transactions.

Transaction provider
You can now create providers that can be used within a transaction. Similar to cmdlets, when a
provider is used in a transaction, its actions are temporary, and they can be accepted or
rejected by the transaction cmdlets provided by Windows PowerShell.

For more information about specifying support for transaction within a provider class, see the
System.Management.Automation.Provider.CmdletProviderAttribute.ProviderCapabilities
property.

<!-- p.1426 -->

Job cmdlets
You can now write cmdlets that can perform their action as a job. These jobs are run in the
background without interacting with the current session. For more information about how
Windows PowerShell supports jobs, see Background Jobs.

Cmdlet output types
You can now specify the .NET Framework types that are returned by your cmdlets by declaring
the OutputType attribute when writing your cmdlets. This will allow others to determine what
type of objects are returned by a cmdlet by looking at the OutputType property of the cmdlet.

Event support
You can now write cmdlets that add and consume events. See the PSEvent class.

Proxy commands
You can now write proxy commands that can be used to run another command. A proxy
command allows you to control what functionality of the source cmdlet is available to the user.
For example, you can create a proxy command that removes a parameter that is supplied by
the source command. See the ProxyCommand class.

Multiple choice prompts
You can now write applications that can provide prompts that allow the user to select multiple
choices. See the IHostUISupportsMultipleChoiceSelection interface

Interactive sessions
You can now write applications that can start and stop an interactive session on a remote
computer. See the IHostSupportsInteractiveSession interface.

Custom Cmdlet Help for Providers
You can now create customized Help topics for the provider cmdlets. Custom cmdlet help
topics can explain how the cmdlet works in the provider path and document special features,
including the dynamic parameters that the provider adds to the cmdlet.

<!-- p.1427 -->

Last updated on 05/20/2025

<!-- p.1428 -->

Cmdlet Overview
Commands native to PowerShell are known as cmdlets (pronounced command-lets). A cmdlet is
implemented in a .NET class that's compiled into a .NET assembly. The PowerShell runtime
invokes these cmdlets within the context of automation scripts that are provided at the command
line. The PowerShell runtime also invokes them programmatically through PowerShell APIs.

Cmdlets
Cmdlets perform an action and typically return a .NET object to the next command in the
pipeline. A cmdlet is a single command that participates in the pipeline semantics of PowerShell.
This includes binary (C#) cmdlets, advanced script functions, and CDXML commands.

This SDK documentation describes how to create binary cmdlets written in C#. For information
about script-based cmdlets, see:

     about_Functions_Advanced
     about_Functions_CmdletBindingAttribute
     about_Functions_Advanced_Methods

To create a binary cmdlet, you must implement a cmdlet class that derives from one of two
specialized cmdlet base classes. The derived class must:

     Declare an attribute that identifies the derived class as a cmdlet.
     Define public properties that are decorated with attributes that identify the public
     properties as cmdlet parameters.
     Override one or more of the input processing methods to process records.

You can load the assembly that contains the class directly by using the Import-Module cmdlet, or
you can create a host application that loads the assembly by using the
System.Management.Automation.Runspaces.InitialSessionState API. Both methods provide
programmatic and command-line access to the functionality of the cmdlet.

Cmdlet Terms
The following terms are used frequently in the PowerShell cmdlet documentation:

Cmdlet attribute

<!-- p.1429 -->

A .NET attribute that's used to declare a cmdlet class as a cmdlet. Although PowerShell uses
several other attributes that are optional, the Cmdlet attribute is required. For more information
about this attribute, see Cmdlet Attribute Declaration.

Cmdlet parameter
The public properties that define the parameters that are available to the user or to the
application that's running the cmdlet. Cmdlets can have required, named, positional, and
[switch] parameters. [switch] parameters allow you to define parameters that are evaluated

only if the parameters are specified in the call. For more information about the different types of
parameters, see Cmdlet Parameters.

Parameter set
A group of parameters that can be used in the same command to perform a specific action. A
cmdlet can have multiple parameter sets, but each parameter set must have at least one
parameter that's unique. Good cmdlet design strongly suggests that the unique parameter also
be a required parameter. For more information about parameter sets, see Cmdlet Parameter Sets.

Dynamic parameter
A parameter that's added to the cmdlet at runtime. Typically, the dynamic parameters are added
to the cmdlet when another parameter is set to a specific value. For more information about
dynamic parameters, see Cmdlet Dynamic Parameters.

Input processing methods
The System.Management.Automation.Cmdlet class provides the following virtual methods that
are used to process records. All the derived cmdlet classes must override one or more of the first
three methods:

     System.Management.Automation.Cmdlet.BeginProcessing: Used to provide optional one-
     time, pre-processing functionality for the cmdlet.
     System.Management.Automation.Cmdlet.ProcessRecord: Used to provide record-by-record
     processing functionality for the cmdlet. The
     System.Management.Automation.Cmdlet.ProcessRecord method might be called any
     number of times, or not at all, depending on the input of the cmdlet.
     System.Management.Automation.Cmdlet.EndProcessing: Used to provide optional one-
     time, post-processing functionality for the cmdlet.

<!-- p.1430 -->

     System.Management.Automation.Cmdlet.StopProcessing: Used to stop processing when the
     user stops the cmdlet asynchronously (for example, by pressing CTRL + C ).

For more information about these methods, see Cmdlet Input Processing Methods.

When you implement a cmdlet, you must override at least one of these input processing
methods. Typically, the ProcessRecord() is the method that you override because it's called for
every record that the cmdlet processes. In contrast, the BeginProcessing() method and the
EndProcessing() method are called one time to perform pre-processing or post-processing of
the records. For more information about these methods, see Input Processing Methods.

ShouldProcess feature
PowerShell allows you to create cmdlets that prompt the user for feedback before the cmdlet
makes a change to the system. To use this feature, the cmdlet must declare that it supports the
ShouldProcess feature when you declare the Cmdlet attribute, and the cmdlet must call the

System.Management.Automation.Cmdlet.ShouldProcess and
System.Management.Automation.Cmdlet.ShouldContinue methods from within an input
processing method. For more information about how to support the ShouldProcess functionality,
see Requesting Confirmation.

Transaction
A logical group of commands that are treated as a single task. The task automatically fails if any
command in the group fails, and the user has the choice to accept or reject the actions
performed within the transaction. To participate in a transaction, the cmdlet must declare that it
supports transactions when the Cmdlet attribute is declared. Support for transactions was
introduced in Windows PowerShell 2.0. For more information about transactions, see How to
Support Transactions.

How Cmdlets Differ from Commands
Cmdlets differ from commands in other command-shell environments in the following ways:

     Cmdlets are instances of .NET classes; they aren't stand-alone executables.
     Cmdlets can be created from as few as a dozen lines of code.
     Cmdlets don't generally do their own parsing, error presentation, or output formatting.
     Parsing, error presentation, and output formatting are handled by the PowerShell runtime.
     Cmdlets process input objects from the pipeline rather than from streams of text, and
     cmdlets typically deliver objects as output to the pipeline.

<!-- p.1431 -->

     Cmdlets are record-oriented because they process a single object at a time.

Cmdlet Base Classes
Windows PowerShell supports cmdlets that are derived from the following two base classes.

     Most cmdlets are based on .NET classes that derive from the
     System.Management.Automation.Cmdlet base class. Deriving from this class allows a cmdlet
     to use the minimum set of dependencies on the Windows PowerShell runtime. This has two
     benefits. The first benefit is that the cmdlet objects are smaller, and you are less likely to be
     affected by changes to the PowerShell runtime. The second benefit is that, if you have to,
     you can directly create an instance of the cmdlet object and then invoke it directly instead
     of invoking it through the PowerShell runtime.

     The more-complex cmdlets are based on .NET classes that derive from the
     System.Management.Automation.PSCmdlet base class. Deriving from this class gives you
     much more access to the PowerShell runtime. This access allows your cmdlet to call scripts,
     to access providers, and to access the current session state. (To access the current session
     state, you get and set session variables and preferences.) However, deriving from this class
     increases the size of the cmdlet object, and it means that your cmdlet is more tightly
     coupled to the current version of the PowerShell runtime.

In general, unless you need the extended access to the PowerShell runtime, you should derive
from the System.Management.Automation.Cmdlet class. However, the PowerShell runtime has
extensive logging capabilities for the execution of cmdlets. If your auditing model depends on
this logging, you can prevent the execution of your cmdlet from within another cmdlet by
deriving from the System.Management.Automation.PSCmdlet class.

Cmdlet Attributes
PowerShell defines several .NET attributes that are used to manage cmdlets and to specify
common functionality that's provided by PowerShell and that might be required by the cmdlet.
For example, attributes are used to designate a class as a cmdlet, to specify the parameters of the
cmdlet, and to request the validation of input so that cmdlet developers don't have to implement
that functionality in their cmdlet code. For more information about attributes, see PowerShell
Attributes.

Cmdlet Names

<!-- p.1432 -->

PowerShell uses a verb-and-noun name pair to name cmdlets. For example, the Get-Command
cmdlet included in PowerShell is used to get all the cmdlets that are registered in the command
shell. The verb identifies the action that the cmdlet performs, and the noun identifies the resource
on which the cmdlet performs its action.

These names are specified when the .NET class is declared as a cmdlet. For more information
about how to declare a .NET class as a cmdlet, see Cmdlet Attribute Declaration.

Writing Cmdlet Code
This document provides two ways to discover how cmdlet code is written. If you prefer to see the
code without much explanation, see Examples of Cmdlet Code. If you prefer more explanation
about the code, see the GetProc Tutorial, StopProc Tutorial, or SelectStr Tutorial topics.

For more information about the guidelines for writing cmdlets, see Cmdlet Development
Guidelines.

See Also
      PowerShell Cmdlet Concepts
      Writing a PowerShell Cmdlet
      PowerShell SDK

 Last updated on 07/13/2026

<!-- p.1433 -->

Windows PowerShell Cmdlet Concepts
This section describes how cmdlets work.

In This Section
This section includes the following topics.

Cmdlet Development Guidelines This topic provides development guidelines that can be used
to produce well-formed cmdlets.

Cmdlet Class Declaration This topic describes cmdlet class declaration.

Approved Verbs for Windows PowerShell Commands This topic lists the predefined cmdlet
verbs that you can use when you declare a cmdlet class.

Cmdlet Input Processing Methods This topic describes the methods that allow a cmdlet to
perform preprocessing operations, input processing operations, and post processing
operations.

Cmdlet Parameters This section describes the different types of parameters that you can add to
cmdlets.

Cmdlet Attributes This section describes the attributes that are used to declare .NET Framework
classes as cmdlets, to declare fields as cmdlet parameters, and to declare input validation rules
for parameters.

Cmdlet Aliases This topic describes cmdlet aliases.

Cmdlet Output This section describes the type of output that cmdlets can return and how to
define and display the objects that are returned by cmdlets.

Registering Cmdlets This section describes how to register cmdlets by using modules and
snap-ins.

Requesting Confirmation This section describes how cmdlets request confirmation from a user
before they make a change to the system.

Windows PowerShell Error Reporting This section describes how cmdlets report terminating
errors and non-terminating errors, and it describes how to interpret error records.

<!-- p.1434 -->

Background Jobs This topic describes how cmdlets can perform their work within background
jobs that do not interfere with the commands that are executing in the current session.

Invoking Cmdlets and Scripts Within a Cmdlet This topic describes how cmdlets can invoke
other cmdlets and scripts from within their input processing methods.

Cmdlet Sets This topic describes using base classes to create sets of cmdlets.

Windows PowerShell Session State This topic describes Windows PowerShell session state.

 Last updated on 05/20/2025

<!-- p.1435 -->

Cmdlet Development Guidelines
The topics in this section provide development guidelines that you can use to produce well-
formed cmdlets. By leveraging the common functionality provided by the Windows PowerShell
runtime and by following these guidelines, you can develop robust cmdlets with minimal effort
and provide the user with a consistent experience. Additionally, you will reduce the test burden
because common functionality does not require retesting.

In This Section
      Required Development Guidelines

      Strongly Encouraged Development Guidelines

      Advisory Development Guidelines

See Also
Writing a Windows PowerShell Cmdlet

Windows PowerShell SDK

 Last updated on 05/20/2025

<!-- p.1436 -->

Required Development Guidelines
The following guidelines must be followed when you write your cmdlets. They're separated into
guidelines for designing cmdlets and guidelines for writing your cmdlet code. If you don't follow
these guidelines, your cmdlets could fail, and your users might have a poor experience when they
use your cmdlets.

In this Topic
Design Guidelines
     Use only approved verbs (RD01)
     Cmdlet names: characters that can't be used (RD02)
     Parameter names that can't be used (RD03)
     Support confirmation requests (RD04)
     Support force parameter for interactive sessions (RD05)
     Document output objects (RD06)

Code Guidelines
     Derive from the Cmdlet or PSCmdlet classes (RC01)
     Specify the Cmdlet attribute (RC02)
     Override an input processing method (RC03)
     Specify the OutputType attribute (RC04)
     Don't retain handles to output objects (RC05)
     Handle errors robustly (RC06)
     Use a Windows PowerShell module to deploy your cmdlets (RC07)

Design Guidelines
The following guidelines must be followed when designing cmdlets to ensure a consistent user
experience between using your cmdlets and other cmdlets. When you find a Design guideline
that applies to your situation, be sure to look at the Code guidelines for similar guidelines.

Use Only Approved Verbs (RD01)

<!-- p.1437 -->

The verb specified in the Cmdlet attribute must come from the recognized set of verbs provided
by Windows PowerShell. It must not be one of the prohibited synonyms. Use the constant strings
that are defined by the following enumerations to specify cmdlet verbs:

        System.Management.Automation.VerbsCommon
        System.Management.Automation.VerbsCommunications
        System.Management.Automation.VerbsData
        System.Management.Automation.VerbsDiagnostic
        System.Management.Automation.VerbsLifecycle
        System.Management.Automation.VerbsSecurity
        System.Management.Automation.VerbsOther

For more information about the approved verb names, see Cmdlet Verbs.

Users need a set of discoverable and expected cmdlet names. Use the appropriate verb so that
the user can make a quick assessment of what a cmdlet does and to easily discover the
capabilities of the system. For example, the following command-line command gets a list of all
the commands on the system whose names begin with "Start": Get-Command Start-* . Use the
nouns in your cmdlets to differentiate your cmdlets from other cmdlets. The noun indicates the
resource on which the operation will be performed. The operation itself is represented by the
verb.

Cmdlet Names: Characters that can't be Used (RD02)
When you name cmdlets, don't use any of the following special characters.

                                                                                ﾉ   Expand table

             Character           Name

                 #               number sign

                 ,               comma

                ( )              parentheses

                { }              braces

                [ ]              brackets

                 &               ampersand

                 -               hyphen

<!-- p.1438 -->

            Character             Name

                /                 slash mark

                \                 backslash

                $                 dollar sign

                ^                 caret

                ;                 semicolon

                :                 colon

                "                 double quotation mark

                '                 single quotation mark

               < >                angle brackets

                |                 vertical bar

                ?                 question mark

                @                 at sign

                `                 back tick (grave accent)

                *                 asterisk

                %                 percent sign

                +                 plus sign

                =                 equals sign

                ~                 tilde

Parameter names that can't be used (RD03)
Windows PowerShell provides a common set of parameters to all cmdlets plus additional
parameters that are added in specific situations. When designing your own cmdlets you can't use
the following names: Confirm , Debug , ErrorAction , ErrorVariable , OutBuffer , OutVariable ,
WarningAction , WarningVariable , WhatIf , UseTransaction , and Verbose . For more information

about these parameters, see Common Parameter Names.

Support confirmation requests (RD04)

<!-- p.1439 -->

For cmdlets that perform an operation that modifies the system, they should call the
System.Management.Automation.Cmdlet.ShouldProcess* method to request confirmation, and in
special cases call the System.Management.Automation.Cmdlet.ShouldContinue* method. (The
System.Management.Automation.Cmdlet.ShouldContinue* method should be called only after
the System.Management.Automation.Cmdlet.ShouldProcess* method is called.)

To make these calls the cmdlet must specify that it supports confirmation requests by setting the
SupportsShouldProcess keyword of the Cmdlet attribute. For more information about setting this

attribute, see Cmdlet Attribute Declaration.

  ７ Note

  If the Cmdlet attribute of the cmdlet class indicates that the cmdlet supports calls to the
  System.Management.Automation.Cmdlet.ShouldProcess* method, and the cmdlet fails to
  make the call to the System.Management.Automation.Cmdlet.ShouldProcess* method, the
  user could modify the system unexpectedly.

Use the System.Management.Automation.Cmdlet.ShouldProcess* method for any system
modification. A user preference and the WhatIf parameter control the
System.Management.Automation.Cmdlet.ShouldProcess* method. In contrast, the
System.Management.Automation.Cmdlet.ShouldContinue* call performs an additional check for
potentially dangerous modifications. This method isn't controlled by any user preference or the
WhatIf parameter. If your cmdlet calls the

System.Management.Automation.Cmdlet.ShouldContinue* method, it should have a Force
parameter that bypasses the calls to these two methods and that proceeds with the operation.
This is important because it allows your cmdlet to be used in non-interactive scripts and hosts.

If your cmdlets support these calls, the user can determine whether the action should actually be
performed. For example, the Stop-Process cmdlet calls the
System.Management.Automation.Cmdlet.ShouldContinue* method before it stops a set of critical
processes, including the System, Winlogon, and Spoolsv processes.

For more information about supporting these methods, see Requesting Confirmation.

Support Force parameter for interactive sessions (RD05)
If your cmdlet is used interactively, always provide a Force parameter to override the interactive
actions, such as prompts or reading lines of input. This is important because it allows your cmdlet

<!-- p.1440 -->

to be used in non-interactive scripts and hosts. The following methods can be implemented by
an interactive host.

     System.Management.Automation.Host.PSHostUserInterface.Prompt*
     System.Management.Automation.Host.PSHostUserInterface.PromptForChoice
     System.Management.Automation.Host.IHostUISupportsMultipleChoiceSelection.PromptForC
     hoice
     System.Management.Automation.Host.PSHostUserInterface.PromptForCredential*
     System.Management.Automation.Host.PSHostUserInterface.ReadLine*
     System.Management.Automation.Host.PSHostUserInterface.ReadLineAsSecureString*

Document output objects (RD06)
Windows PowerShell uses the objects that are written to the pipeline. In order for users to take
advantage of the objects that are returned by each cmdlet, you must document the objects that
are returned, and you must document what the members of those returned objects are used for.

Code guidelines
The following guidelines must be followed when writing cmdlet code. When you find a Code
guideline that applies to your situation, be sure to look at the Design guidelines for similar
guidelines.

Derive from the Cmdlet or PSCmdlet classes (RC01)
A cmdlet must derive from either the System.Management.Automation.Cmdlet or
System.Management.Automation.PSCmdlet base class. Cmdlets that derive from the
System.Management.Automation.Cmdlet class don't depend on the Windows PowerShell
runtime. They can be called directly from any Microsoft .NET Framework language. Cmdlets that
derive from the System.Management.Automation.PSCmdlet class depend on the Windows
PowerShell runtime. Therefore, they execute within a runspace.

All cmdlet classes that you implement must be public classes. For more information about these
cmdlet classes, see Cmdlet Overview.

Specify the Cmdlet attribute (RC02)
For a cmdlet to be recognized by Windows PowerShell, its .NET Framework class must be
decorated with the Cmdlet attribute. This attribute specifies the following features of the cmdlet.
