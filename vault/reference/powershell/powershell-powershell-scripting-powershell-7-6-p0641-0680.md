---
title: "How to use this documentation — pages 641-680"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0641-0680
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0641-0680
family: powershell
documentKind: "doc"
abstract: "Fix checks for local user config file paths (#27432 ) Update PowerShell telemetry to respect the diagnostics and feedback setting on Windows (#27438 ) Enable usage in AppContainers (#27423 ) Delay update notification for one week to ensure all packages become available (#27220 )"
---

# How to use this documentation — pages 641-680

<!-- p.641 -->

Fix checks for local user config file paths (#27432   )
Update PowerShell telemetry to respect the diagnostics and feedback setting on Windows
(#27438      )
Enable usage in AppContainers (#27423      )
Delay update notification for one week to ensure all packages become available (#27220 )
Fix a regression in the API CompletionCompleters.CompleteFilename() that causes null
reference exception (#26487     )
Close pipe client handles after creating the child ssh process (#26564   )
Update the PSDiagnostics module to manage the PowerShellCore provider in PowerShell 7
(#25590      )
Allow opt-out of the named-pipe listener using the environment variable
POWERSHELL_DIAGNOSTICS_OPTOUT (#26086       )
Ensure that socket timeouts are set only during the token validation (#26066 )
Fix stderr output of console host to respect NO_COLOR (#24391 )
Update PSRP protocol to deprecate session key exchange between newer client and server
(#25774      )
Fix the ssh PATH check in SSHConnectionInfo when the default Runspace is not available
(#25780      ) (Thanks @jborean93!)
Adding hex format for native command exit codes (#21067 ) (Thanks @sba923!)
Fix infinite loop crash in variable type inference (#25696   ) (Thanks @MartinGC94!)
Add PSForEach and PSWhere as aliases for the PowerShell intrinsic methods Where and
Foreach (#25511      ) (Thanks @powercode!)
Added the AIShell module to telemetry collection list (#24747 )
Added helper in EnumSingleTypeConverter to get enum names as array (#17785 ) (Thanks
@fflaten!)
Update DnsNameList for X509Certificate2 to use
X509SubjectAlternativeNameExtension.EnumerateDnsNames() Method (#24714         ) (Thanks
@ArmaanMcleod!)
Stringify ErrorRecord with empty exception message to empty string (#24949       ) (Thanks
@MatejKafka!)
Add PipelineStopToken to Cmdlet which will be signaled when the pipeline is stopping
(#24620      ) (Thanks @jborean93!)
Fallback to AppLocker after WldpCanExecuteFile (#24912       )
Move .NET method invocation logging to after the needed type conversion is done for
method arguments (#25022 )
Fix infinite loop in variable type inference (#25206 ) (Thanks @MartinGC94!)
Remove the old fuzzy suggestion and fix the local script file name suggestion (#25177      )

<!-- p.642 -->

      Make SystemPolicy public APIs visible but non-op on Unix platforms so that they can be
      included in PowerShellStandard.Library (#25051 )
      Set standard handles explicitly when starting a process with -NoNewWindow (#25061 )
      Fix tooltip for variable expansion and include desc (#25112   ) (Thanks @jborean93!)
      Use script filepath when completing relative paths for using statements (#20017   ) (Thanks
      @MartinGC94!)
      Allow DSC parsing through OS architecture translation layers (#24852 ) (Thanks
      @bdeb1337!)

Experimental features
PowerShell 7.6 includes the following changes to experimental features.

The following features have been converted to mainstream features:

      PSFeedbackProvider
      PSNativeWindowsTildeExpansion
      PSRedirectToVariable
      PSSubsystemPluginModel

This release includes the following experimental features:

      PSSerializeJSONLongEnumAsNumber - ConvertTo-Json now treats large enums as numbers
      PSProfileDSCResource - Add DSC v3 resource for PowerShell Profiles

 Last updated on 07/15/2026

<!-- p.643 -->

What's New in PowerShell 7.5
PowerShell 7.5.8 includes the following features, updates, and breaking changes. PowerShell 7.5.8
is built on the .NET 9.0.17 runtime.

For a complete list of changes, see the CHANGELOG     in the GitHub repository. For more
information about .NET 9, see What's new in .NET 9.

Installer updates
The macOS PKG package is now notarized and signed by Microsoft. For more information, see
Install PowerShell 7 on macOS.

Breaking Changes
     Fix -OlderThan and -NewerThan parameters for Test-Path when using PathType and date
     range (#20942     ) (Thanks @ArmaanMcleod!)
        Previously -OlderThan would be ignored if specified together
     Change New-FileCatalog -CatalogVersion default to 2 (#20428       ) (Thanks @ThomasNieto!)
     Block getting help from network locations in restricted remoting sessions (#20593 )
     The Windows installer now remembers installation options used and uses them to initialize
     options for the next installation (#20420 ) (Thanks @reduckted!)
      ConvertTo-Json now serializes BigInteger as a number (#21000      ) (Thanks @jborean93!)

Updated modules
PowerShell 7.5.6 includes the following updated modules:

     Microsoft.PowerShell.PSResourceGet v1.1.1
     PSReadLine v2.3.6

Tab completion improvements
Many thanks to @ArmaanMcleod and others for all their work to improve tab completion.

     Fall back to type inference when hashtable key-value cannot be retrieved from safe
     expression (#21184     ) (Thanks @MartinGC94!)
     Fix the regression when doing type inference for $_ (#21223    ) (Thanks @MartinGC94!)

<!-- p.644 -->

  Expand ~ to $HOME on Windows with tab completion (#21529 )
  Don't complete when declaring parameter name and class member (#21182          ) (Thanks
  @MartinGC94!)
  Prevent fallback to file completion when tab completing type names (#20084 ) (Thanks
  @MartinGC94)
  Add argument completer to -Version for Set-StrictMode (#20554 ) (Thanks
  @ArmaanMcleod!)
  Add -Verb argument completer for Get-Verb / Get-Command and refactor Get-Verb
  (#20286   ) (Thanks @ArmaanMcleod)
  Add -Verb argument completer for Start-Process (#20415 ) (Thanks @ArmaanMcleod)
  Add -Scope argument completer for *-Variable , *-Alias & *-PSDrive commands
  (#20451   ) (Thanks @ArmaanMcleod)
  Add -Module completion for Save-Help / Update-Help commands (#20678          ) (Thanks
  @ArmaanMcleod)

New cmdlets
  Add ConvertTo-CliXml and ConvertFrom-CliXml cmdlets (#21063        ) (Thanks
  @ArmaanMcleod!)

Web cmdlets improvements
  Fix to allow -PassThru and -Outfile work together (#24086      )
  Add OutFile property in WebResponseObject (#24047      )
  Show filename in Invoke-WebRequest -OutFile -Verbose (#24041 )
  Fix WebCmdlets when -Body is specified but ContentType is not (#23952 ) (Thanks
  @CarloToso!)
  Fix Invoke-WebRequest to report correct size when -Resume is specified (#20207 ) (Thanks
  @LNKLEO!)
  Fix Web Cmdlets to allow WinForm apps to work correctly (#20606      )

Other cmdlet improvements
  Update MaxVisitCount and MaxHashtableKeyCount if VisitorSafeValueContext indicates
  SkipLimitCheck is true for Import-PowerShellDataFile

  Close pipe client handles after creating the child ssh process (#26822   )
  Fix the progress preference variable in script cmdlets (#26791 ) (Thanks @cmkb3!)

<!-- p.645 -->

Fix Out-GridView by replacing the use of obsolete BinaryFormatter with custom
implementation (#25559 )
Enable -NoRestart to work with Register-PSSessionConfiguration (#23891         )
Add IgnoreComments and AllowTrailingCommas options to Test-Json cmdlet (#23817 )
(Thanks @ArmaanMcleod!)
Get-Help may report parameters with ValueFromRemainingArguments attribute as pipeline-
able (#23871     )
Change type of LineNumber to ulong in Select-String (#24075 ) (Thanks @Snowman-25!)
Get-Process : Remove admin requirement for -IncludeUserName (#21302         ) (Thanks
@jborean93!)
Fix Test-Path -IsValid to check for invalid path and filename characters (#21358        )
Add RecommendedAction to ConciseView of the error reporting (#20826 ) (Thanks
@JustinGrote!)
Added progress bar for Remove-Item cmdlet (#20778         ) (Thanks @ArmaanMcleod!)
Fix Test-Connection due to .NET 8 changes (#20369     )
Fix Get-Service non-terminating error message to include category (#20276          )
Add -Empty and -InputObject parameters to New-Guid (#20014 ) (Thanks @CarloToso!)
Add the alias r to the parameter -Recurse for the Get-ChildItem command (#20100 )
(Thanks @kilasuit!)
Add LP to LiteralPath aliases for functions still missing it (#20820 )
Add implicit localization fallback to Import-LocalizedData (#19896     ) (Thanks @chrisdent-
de!)
Add Aliases to the properties shown up when formatting the help content of the
parameter returned by Get-Help (#20994     )
Add HelpUri to Remove-Service (#20476 )
Fix completion crash for the SCCM provider (#20815, #20919, #20915) (Thanks
@MartinGC94!)
Fix regression in Get-Content when -Tail 0 and -Wait are used together (#20734 )
(Thanks @CarloToso!)
Fix Start-Process -PassThru to make sure the ExitCode property is accessible for the
returned Process object (#20749 ) (Thanks @CodeCyclone!)
Fix Group-Object to use current culture for its output (#20608     )
Fix Group-Object output using interpolated strings (#20745       ) (Thanks @mawosoft!)
Fix rendering of DisplayRoot for network PSDrive (#20793       )
Fix Copy-Item progress to only show completed when all files are copied (#20517         )
Fix UNC path completion regression (#20419     ) (Thanks @MartinGC94!)
Report error if invalid -ExecutionPolicy is passed to pwsh (#20460 )

<!-- p.646 -->

  Add WinGetCommandNotFound and CompletionPredictor modules to track usage
  (#21040   )
  Add DateKind parameter to ConvertFrom-Json (#20925            ) (Thanks @jborean93!)
  Add DirectoryInfo to the OutputType for New-Item (#21126 ) (Thanks @MartinGC94!)
  Fix Get-Error serialization of array values (#21085       ) (Thanks @jborean93!)
  Fix Test-ModuleManifest so it can use a UNC path (#24115            )
  Fix Get-TypeData to write to the pipeline immediately instead of collecting data first
  (#24236   ) (Thanks @MartinGC94)
  Add -Force parameter to Resolve-Path and Convert-Path cmdlets to support wildcard
  hidden files #20981    (Thanks @ArmaanMcleod!)
  Set standard handles explicitly when starting a process with -NoNewWindow (#25324 )
  Make inherited protected internal instance members accessible in class scope. (#25547 )
  (Thanks @mawosoft!)
  Remove the old fuzzy suggestion and fix the local script file name suggestion (#25330         )
  Fix PSMethodInvocationConstraints.GetHashCode method (#25306 ) (Thanks @crazyjncsu!)

Engine improvements
  Fix checks for local user config file paths (#27479   )
  Update PowerShell telemetry to respect the diagnostics and feedback setting on Windows
  (#27472   )
  Fix the logic for finding the ssh executable in the PATH (#26165        ) (Thanks @jborean93!)
  Move .NET method invocation logging to after the needed type conversion is done for
  method arguments (#25357 )
  Fallback to AppLocker after WldpCanExecuteFile (#25305          )
  Explicitly start and stop ANSI Error Color (#24065    ) (Thanks @JustinGrote!)
  Improve .NET overload definition of generic methods (#21326 ) (Thanks @jborean93!)
  Optimize the += operation for a collection when it's an object array (#23901 ) (Thanks
  @jborean93!)
  Add telemetry to check for specific tags when importing a module (#20371            )
  Add PSAdapter and ConsoleGuiTools to module load telemetry allowlist (#20641             )
  Add WinGet module to track usage (#21040        )
  Ensure the filename is not null when logging WDAC ETW events (#20910              ) (Thanks
  @jborean93!)
  Fix four regressions introduced by the WDAC logging feature (#20913           )
  Leave the input, output, and error handles unset when they are not redirected (#20853 )
  Fix implicit remoting proxy cmdlets to act on common parameters (#20367             )

<!-- p.647 -->

        Include the module version in error messages when module is not found (#20144     )
        (Thanks @ArmaanMcleod!)
        Fix unixmode to handle setuid and sticky when file is not an executable (#20366   )
        Fix using assembly to use Path.Combine when constructing assembly paths (#21169 )
        Validate the value for using namespace during semantic checks to prevent declaring invalid
        namespaces (#21162     )
        Handle global tool specially when prepending $PSHOME to PATH (#24228     )
        Delay update notification for one week to ensure all packages become available (#27220 )

Experimental features
The following experimental features were converted to mainstream features in PowerShell 7.5-
rc.1:

        PSCommandNotFoundSuggestion
        PSCommandWithArgs
        PSModuleAutoLoadSkipOfflineFiles

The following experimental features are included in PowerShell 7.5-rc.1:

        PSRedirectToVariable - Allow redirecting to a variable (#20381   )
        PSNativeWindowsTildeExpansion - Add tilde expansion for Windows-native executables
        (#20402   ) (Thanks @domsleee!)
        PSSerializeJSONLongEnumAsNumber - ConvertTo-Json now treats large enums as numbers
        (#20999   ) (Thanks @jborean93!)

Performance improvements
PowerShell 7.5-rc.1 included PR#23901       from @jborean93 that improves the performance of the
+= operation for an array of objects.

The following example measures the performance for different methods of adding elements to
an array.

  PowerShell

  $tests = @{
      'Direct Assignment' = {
          param($count)

        $result = foreach($i in 1..$count) {
                $i

<!-- p.648 -->

          }
      }
      'List<T>.Add(T)' = {
          param($count)

          $result = [Collections.Generic.List[int]]::new()
          foreach($i in 1..$count) {
              $result.Add($i)
          }
      }
      'Array+= Operator' = {
          param($count)

          $result = @()
          foreach($i in 1..$count) {
              $result += $i
          }
      }
 }

 5kb, 10kb | ForEach-Object {
     $groupResult = foreach($test in $tests.GetEnumerator()) {
         $ms = (Measure-Command { & $test.Value -Count $_ }).TotalMilliseconds

          [pscustomobject]@{
              CollectionSize    = $_
              Test              = $test.Key
              TotalMilliseconds = [Math]::Round($ms, 2)
          }

          [GC]::Collect()
              [GC]::WaitForPendingFinalizers()
      }

     $groupResult = $groupResult | Sort-Object TotalMilliseconds
         $groupResult | Select-Object *, @{
             Name       = 'RelativeSpeed'
             Expression = {
                 $relativeSpeed = $_.TotalMilliseconds /
 $groupResult[0].TotalMilliseconds
                 $speed = [Math]::Round($relativeSpeed, 2).ToString() + 'x'
                 if ($speed -eq '1x') { $speed } else { $speed + ' slower' }
             }
         } | Format-Table -AutoSize
 }

When you run the script in PowerShell 7.4.6, you see that using the += operator is the slowest
method.

 Output

 CollectionSize Test                    TotalMilliseconds RelativeSpeed
 -------------- ----                    ----------------- -------------

<!-- p.649 -->

              5120 Direct Assignment                  4.17 1x
              5120 List<T>.Add(T)                    90.79 21.77x slower
              5120 Array+= Operator                 342.58 82.15x slower

 CollectionSize Test                    TotalMilliseconds RelativeSpeed
 -------------- ----                    ----------------- -------------
          10240 Direct Assignment                    0.64 1x
          10240 List<T>.Add(T)                     184.10 287.66x slower
          10240 Array+= Operator                  1668.13 2606.45x slower

When you run the script in PowerShell 7.5-rc.1, you see that using the += operator is much faster
than PowerShell 7.4.6. Now, it's also faster than using the List<T>.Add(T) method.

 Output

 CollectionSize Test                    TotalMilliseconds RelativeSpeed
 -------------- ----                    ----------------- -------------
           5120 Direct Assignment                    4.71 1x
           5120 Array+= Operator                    40.42 8.58x slower
           5120 List<T>.Add(T)                      92.17 19.57x slower

 CollectionSize Test                    TotalMilliseconds RelativeSpeed
 -------------- ----                    ----------------- -------------
          10240 Direct Assignment                    1.76 1x
          10240 Array+= Operator                   104.73 59.51x slower
          10240 List<T>.Add(T)                     173.00 98.3x slower

Last updated on 06/12/2026

<!-- p.650 -->

What's New in PowerShell 7.4
PowerShell 7.4.18 includes the following features, updates, and breaking changes. PowerShell
7.4.18 is built on the .NET 8.0.29 runtime.

For a complete list of changes, see the CHANGELOG      in the GitHub repository.

Breaking changes
     Nano server docker images aren't available for this release
     Added the ProgressAction parameter to the Common Parameters
     Update some PowerShell APIs to throw ArgumentException instead of
     ArgumentNullException when the argument is an empty string (#19215            ) (Thanks
     @xtqqczze!)
     Remove code related to #Requires -PSSnapin (#19320       )
      Test-Json now uses JsonSchema.NET instead of Newtonsoft.Json.Schema.

        With this change, Test-Json no longer supports the older Draft 4 schemas. (#18141      )
        (Thanks @gregsdennis!). For more information about JSON schemas, see JSON
        Schema     documentation. This also breaks Test-Json for JSON and JSONC files with
        comments.
         ConvertFrom-Json support still uses Newtonsoft.Json.Schema so it can convert JSON files

        with comments.
     Output from Test-Connection now includes more detailed information about TCP
     connection tests
     .NET introduced changes that affected Test-Connection . The cmdlet now returns an error
     about the need to use sudo on Linux platforms when using a custom buffer size (#20369         )
     Experimental feature PSNativeCommandPreserveBytePipe is now mainstream. PowerShell
     now preserves the byte-stream data when redirecting the stdout stream of a native
     command to a file or when piping byte-stream data to the stdin stream of a native
     command.
     Change how relative paths in Resolve-Path are handled when using the RelativeBasePath
     parameter (#19755      ) (Thanks @MartinGC94!)
     Remove unused PSv2 code - removes TabExpansion function (#18337 )

Installer updates

<!-- p.651 -->

The macOS PKG package is now notarized and signed by Microsoft. For more information, see
Install PowerShell 7 on macOS.

The Windows MSI package provides an option to disable PowerShell telemetry during
installation. For more information, see Install the msi package from the command line.

Updated versions of PSResourceGet and PSReadLine
PowerShell 7.4 includes Microsoft.PowerShell.PSResourceGet v1.1.1. This module is installed
side-by-side with PowerShellGet v2.2.5 and PackageManagement v1.4.8.1. For more information,
see the documentation for Microsoft.PowerShell.PSResourceGet.

PowerShell 7.4 now includes PSReadLine v2.3.6. For more information, see the documentation for
PSReadLine.

Tab completion improvements
Many thanks to @MartinGC94 and others for all their work to improve tab completion.

     Fix issue when completing the first command in a script with an empty array expression
     (#18355   )
     Fix positional argument completion (#17796    )
     Prioritize the default parameter set when completing positional arguments (#18755 )
     Improve pseudo binding for dynamic parameters (#18030 )
     Improve type inference of hashtable keys (#17907 )
     Fix type inference error for empty return statements (#18351 )
     Improve type inference for Get-Random (#18972         )
     Fix type inference for all scope variables (#18758 )
     Improve enumeration of inferred types in pipeline (#17799         )
     Add completion for values in comparisons when comparing Enums (#17654 )
     Add property assignment completion for enums (#19178          )
     Fix completion for PSCustomObject variable properties (#18682         )
     Fix member completion in attribute argument (#17902       )
     Exclude redundant parameter aliases from completion results (#19382 )
     Fix class member completion for classes with base types (#19179           )
     Add completion for the using keyword (#16514      )
     Fix TabExpansion2 variable leak when completing variables (#18763             )
     Enable completion of variables across ScriptBlock scopes (#19819          )
     Fix completion of the foreach statement variable (#19814 )

<!-- p.652 -->

     Fix variable type inference precedence (#18691 )
     Fix member completion for PowerShell Enum class (#19740 )
     Fix parsing for array literals in index expressions in method calls (#19224 )
     Improve path completion (#19489          )
     Fix an indexing out of bound error in CompleteInput for empty script input (#19501     )
     Improve variable completion performance (#19595       )
     Improve Hashtable key completion for type constrained variable assignments, nested
     Hashtables and more (#17660      )
     Infer external application output as strings (#19193 )
     Update parameter completion for enums to exclude values not allowed by ValidateRange
     attributes (#17750   ) (Thanks @fflaten!).
     Fix dynamic parameter completion (#19510      )
     Add completion for variables assigned by the data statement (#19831 )
     Fix expanding tilde ( ~ ) on Windows systems to $HOME to prevent breaking use cases with
     native commands (#21529 )

Web cmdlet improvements
Many thanks to @CarloToso and others for all the work on improving web cmdlets.

     Fix decompression in web cmdlets to include Brotli (#17955     ) (Thanks @iSazonov!)
     Webcmdlets add 308 to redirect codes and small cleanup (#18536          )
     Complete the progress bar rendering in Invoke-WebRequest when downloading is
     complete or cancelled (#18130        )
     Web cmdlets get Retry-After interval from response headers if the status code is 429
     (#18717   )
     Web cmdlets set default charset encoding to UTF8 (#18219 )
     Preserve WebSession.MaximumRedirection from changes (#19190 )
     WebCmdlets parse XML declaration to get encoding value, if present. (#18748     )
     Fix using xml -Body in webcmdlets without an encoding (#19281       )
     Adjust PUT method behavior to POST one for default content type in WebCmdlets
     (#19152   )
     Take into account ContentType from Headers in WebCmdlets (#19227            )
     Allow to preserve the original HTTP method by adding -PreserveHttpMethodOnRedirect to
     Web cmdlets (#18894     )
     Webcmdlets display an error on https to http redirect (#18595 )
     Add AllowInsecureRedirect switch to Web cmdlets (#18546 )
     Improve verbose message in web cmdlets when content length is unknown (#19252 )

<!-- p.653 -->

  Build the relative URI for links from the response in Invoke-WebRequest (#19092   )
  Fix redirection for -CustomMethod POST in WebCmdlets (#19111    )
  Dispose previous response in Webcmdlets (#19117      )
  Improve Invoke-WebRequest xml and json errors format (#18837 )
  Add ValidateNotNullOrEmpty to OutFile and InFile parameters of WebCmdlets (#19044 )
  HttpKnownHeaderNames update headers list (#18947 )
  Invoke-RestMethod -FollowRelLink fix links containing commas (#18829      )
  Fix bug with managing redirection and KeepAuthorization in Web cmdlets (#18902        )
  Add StatusCode to HttpResponseException (#18842          )
  Support HTTP persistent connections in Web Cmdlets (#19249 ) (Thanks @stevenebutler!)
  Small cleanup Invoke-RestMethod (#19490 )
  Improve the verbose message of WebCmdlets to show correct HTTP version (#19616 )
  Add FileNameStar to MultipartFileContent in WebCmdlets (#19467        )
  Fix HTTP status from 409 to 429 for WebCmdlets to get retry interval from Retry-After
  header. (#19622   ) (Thanks @mkht!)
  Change -TimeoutSec to -ConnectionTimeoutSeconds and add -OperationTimeoutSeconds to
  web cmdlets (#19558    ) (Thanks @stevenebutler!) Other cmdlets
  Support Ctrl+c when connection hangs while reading data in WebCmdlets (#19330 )
  (Thanks @stevenebutler!)
  Support Unix domain socket in WebCmdlets (#19343         )

Other cmdlet improvements
  Fix Out-GridView by replacing use of obsolete BinaryFormatter with custom implementation
  (#27426   )
  Update MaxVisitCount and MaxHashtableKeyCount if VisitorSafeValueContext indicates
  SkipLimitCheck is true for Import-PowerShellDataFile

  Test-Connection now returns error about the need to use sudo on Linux platforms when

  using a custom buffer size (#20369    )
  Add output types to Format commands (#18746       ) (Thanks @MartinGC94!)
  Add output type attributes for Get-WinEvent (#17948 ) (Thanks @MartinGC94!)
  Add Path and LiteralPath parameters to Test-Json cmdlet (#19042      ) (Thanks
  @ArmaanMcleod!)
  Add NoHeader parameter to ConvertTo-Csv and Export-Csv cmdlets (#19108 ) (Thanks
  @ArmaanMcleod!)
  Add Confirm and WhatIf parameters to Stop-Transcript (#18731        ) (Thanks
  @JohnLBevan!)

<!-- p.654 -->

    Add FuzzyMinimumDistance parameter to Get-Command (#18261              )
    Make Encoding parameter able to take ANSI encoding in PowerShell (#19298          ) (Thanks
    @CarloToso!)
    Add progress to Copy-Item (#18735       )
     Update-Help now reports an error when using implicit culture on non-US systems.

    (#17780   ) (Thanks @dkaszews!)
    Don't require activity when creating a completed progress record (#18474 ) (Thanks
    @MartinGC94!)
    Disallow negative values for Get-Content cmdlet parameters -Head and -Tail (#19715            )
    (Thanks @CarloToso!)
    Make Update-Help throw proper error when current culture isn't associated with a language
    (#19765   ) (Thanks @josea!)
    Allow combining of -Skip and -SkipLast parameters in Select-Object cmdlet. (#18849                )
    (Thanks @ArmaanMcleod!)
    Add Get-SecureRandom cmdlet (#19587 )
     Set-Clipboard -AsOSC52 for remote usage (#18222          ) (Thanks @dkaszews!)
    Speed up Resolve-Path relative path resolution (#19171         ) (Thanks @MartinGC94!)
    Added the [switch] parameter -CaseInsensitive to Select-Object and Get-Unique
    cmdlets (#19683       ) (Thanks @ArmaanMcleod!)
     Restart-Computer and Stop-Computer should fail with error when not running via sudo on

    Unix (#19824      )

Engine improvements
Updates to $PSStyle

    Adds Dim and DimOff properties (#18653        )
    Added static methods to the PSStyle class that map foreground and background
    ConsoleColor values to ANSI escape sequences (#17938           )
    Table headers for calculated fields are formatted in italics by default
    Add support of respecting $PSStyle.OutputRendering on the remote host (#19601            )
    Updated telemetry data to include use of CrescendoBuilt modules (#20371 )

Other Engine updates

    Fix checks for local user config file paths (#27454   )
    Update PowerShell telemetry to respect the diagnostics and feedback setting on Windows
    (#27430   )
    Delay update notification for one week to ensure all packages become available (#27229 )

<!-- p.655 -->

     Close pipe client handles after creating the child ssh process (#27139   )
     Move .NET method invocation logging to after the needed type conversion is done for
     method arguments (#25568 )
     Fallback to AppLocker after WldpCanExecuteFile (#25229       )
     Make PowerShell class not affiliate with Runspace when declaring the NoRunspaceAffinity
     attribute (#18138    )
     Add the ValidateNotNullOrWhiteSpace attribute (#17191        ) (Thanks @wmentha!)
     Add sqlcmd to the list for legacy argument passing (#18559 )
     Add the function cd~ (#18308 ) (Thanks @GigaScratch!)
     Fix array type parsing in generic types (#19205 ) (Thanks @MartinGC94!)
     Fix wildcard globbing in root of device paths (#19442 ) (Thanks @MartinGC94!)
     Add a public API for getting locations of PSModulePath elements (#19422      )
     Fix incorrect string to type conversion (#19560   ) (Thanks @MartinGC94!)
     Fix slow execution when many breakpoints are used (#14953        ) (Thanks @nohwnd!)
     Remove code related to #Requires -PSSnapin (#19320       )

Experimental Features
PowerShell 7.4 introduces the following experimental features:

     PSFeedbackProvider - Replaces the hard-coded suggestion framework with an extensible
     feedback provider.
        This feature also adds the FeedbackName, FeedbackText, and FeedbackAction
        properties to $PSStyle.Formatting that allow you to change the formatting of feedback
        messages.
     PSModuleAutoLoadSkipOfflineFiles - Module discovery now skips over files that are marked
     by cloud providers as not fully on disk.
     PSCommandWithArgs - Add support for passing arguments to commands as a single string

The following experimental features became mainstream:

     PSConstrainedAuditLogging
     PSCustomTableHeaderLabelDecoration
     PSNativeCommandErrorActionPreference
     PSNativeCommandPreserveBytePipe
     PSWindowsNativeCommandArgPassing

PowerShell 7.4 changed the following experimental features:

<!-- p.656 -->

     PSCommandNotFoundSuggestion - This feature now uses an extensible feedback provider
     rather than hard-coded suggestions (#18726    )

For more information about the Experimental Features, see Using Experimental Features.

Last updated on 07/20/2026

<!-- p.657 -->

What's New in PowerShell 7.3
PowerShell 7.3 is the next stable release, built on .NET 7.0.

PowerShell 7.3 includes the following features, updates, and breaking changes.

Breaking Changes and Improvements
     In this release, Windows APIs were updated or removed for compliance, which means that
     PowerShell 7.3 doesn't run on Windows 7. While Windows 7 is no longer supported,
     previous builds could run on Windows 7.
     PowerShell Direct for Hyper-V is only supported on Windows 10, version 1809 and higher.
      Test-Connection is broken due to an intentional breaking change      in .NET 7. It's tracked
     by #17018
     Add clean block to script block as a peer to begin , process , and end to allow easy
     resource cleanup (#15177 )
     Change default for $PSStyle.OutputRendering to Host
     Make Out-String and Out-File keep string input unchanged (#17455 )
     Move the type data definition of System.Security.AccessControl.ObjectSecurity to the
     Microsoft.PowerShell.Security module (#16355 ) (Thanks @iSazonov!)
        Before this change, a user doesn't need to explicitly import the
        Microsoft.PowerShell.Security module to use the code properties defined for an
        instance of System.Security.AccessControl.ObjectSecurity.
        After this change, a user needs to explicitly import Microsoft.PowerShell.Security
        module in order to use those code properties and code methods.

Tab completion improvements
     PowerShell 7.3 includes PSReadLine 2.2.6, which enables Predictive IntelliSense by default.
     For more information, see about_PSReadLine.
     Fix tab completion within the script block specified for the ValidateScriptAttribute .
     (#14550    ) (Thanks @MartinGC94!)
     Added tab completion for loop labels after break / continue (#16438     ) (Thanks
     @MartinGC94!)
     Improve Hashtable completion in multiple scenarios (#16498 ) (Thanks @MartinGC94!)
        Parameter splatting

<!-- p.658 -->

    Arguments parameter for Invoke-CimMethod
    FilterHashtable parameter for Get-WinEvent
    Property parameter for the CIM cmdlets
    Removes duplicates from member completion scenarios
  Support forward slashes in network share (UNC path) completion (#17111 ) (Thanks
  @sba923!)
  Improve member autocompletion (#16504 ) (Thanks @MartinGC94!)
  Prioritize ValidateSet completions over Enums for parameters (#15257 ) (Thanks
  @MartinGC94!)
  Add type inference support for generic methods with type parameters (#16951      )
  (Thanks @MartinGC94!)
  Improve type inference and completions (#16963     ) (Thanks @MartinGC94!)
    Allows methods to be shown in completion results for ForEach-Object -MemberName
    Prevents completion on expressions that return void like ([void](""))
    Allows non-default Class constructors to show up when class completion is based on
    the AST
  Improve type inference for $_ (#17716   ) (Thanks @MartinGC94!)
  Fix type inference for ICollection (#17752 ) (Thanks @MartinGC94!)
  Prevent braces from being removed when completing variables (#17751 ) (Thanks
  @MartinGC94!)
  Add completion for index expressions for dictionaries (#17619 ) (Thanks @MartinGC94!)
  Fix type completion for attribute tokens (#17484   ) (Thanks @MartinGC94!)
  Improve dynamic parameter tab completion (#17661 ) (Thanks @MartinGC94!)
  Avoid binding positional parameters when completing parameter in front of value
  (#17693   ) (Thanks @MartinGC94!)

Improved error handling
  Set $? correctly for command expression with redirections (#16046 )
  Fix a casting error when using $PSNativeCommandUseErrorActionPreference (#15993 )
  Make the native command error handling optionally honor ErrorActionPreference
  (#15897   )
  Specify the executable path as TargetObject for non-zero exit code ErrorRecord
  (#16108   ) (Thanks @rkeithhill!)

Session and remoting improvements

<!-- p.659 -->

     Add -Options to the PSRP over SSH commands to allow passing OpenSSH options
     directly (#12802       ) (Thanks @BrannenGH!)
     Add -ConfigurationFile parameter to pwsh to allow starting a new process with the
     session configuration defined in a .pssc file (#17447 )
     Add support for using New-PSSessionConfigurationFile on non-Windows platforms
     (#17447   )

Updated cmdlets
     Add -HttpVersion parameter to web cmdlets (#15853 ) (Thanks @hayhay27!)
     Add support to web cmdlets for open-ended input tags (#16193       ) (Thanks @farmerau!)
     Fix ConvertTo-Json -Depth to allow 100 at maximum (#16197       ) (Thanks @KevRitchie!)
     Improve variable handling when calling Invoke-Command with the $Using: expression
     (#16113   ) (Thanks @dwtaber!)
     Add -StrictMode to Invoke-Command to allow specifying strict mode when invoking
     command locally (#16545        ) (Thanks @Thomas-Yu!)
     Add clean block to script block as a peer to begin , process , and end to allow easy
     resource cleanup (#15177 )
     Add -Amended switch to Get-CimClass cmdlet (#17477 ) (Thanks @iSazonov)
     Changed ConvertFrom-Json -AsHashtable to use ordered hashtable (#17405 )
     Removed ANSI escape sequences in strings before sending to Out-GridView (#17664 )
     Added the Milliseconds parameter to New-TimeSpan (#17621 ) (Thanks @NoMoreFood!)
     Show optional parameters when displaying method definitions and overloads (#13799 )
     (Thanks @eugenesmlv!)
     Allow commands to still be executed even if the current working directory no longer
     exists (#17579     )
     Add support for HTTPS with Set-AuthenticodeSignature -TimeStampServer (#16134 )
     (Thanks @Ryan-Hutchison-USAF!)
     Render decimal numbers in a table using current culture (#17650 )
     Add type accelerator ordered for OrderedDictionary (#17804      ) (Thanks @fflaten!)
     Add find.exe to legacy argument binding behavior for Windows (#17715 )
     Add -NoProfileLoadTime switch to pwsh (#17535 ) (Thanks @rkeithhill!)

For a complete list of changes, see the Change Log    in the GitHub repository.

Experimental Features
In PowerShell 7.3, following experimental features became mainstream:

<!-- p.660 -->

     PSAnsiRenderingFileInfo - This feature adds the $PSStyle.FileInfo member and enables

     coloring of specific file types.

     PSCleanBlock - Adds clean block to script block as a peer to begin , process , and end to

     allow easy resource cleanup.

     PSAMSIMethodInvocationLogging - Extends the data sent to AMSI for inspection to include

     all invocations of .NET method members.

     PSNativeCommandArgumentPassing - PowerShell now uses the ArgumentList property
     of the StartProcessInfo object rather than the old mechanism of reconstructing a string
     when invoking a native executable.

     PowerShell 7.3.1 adds sqlcmd.exe to the list of native commands in Windows that use the
     Legacy style of argument passing.

     PSExec - Adds the new Switch-Process cmdlet (alias exec ) to provide exec compatibility

     for non-Windows systems.

     PowerShell 7.3.1 changed the exec alias to a function that wraps Switch-Process . The
     function allows you to pass parameters to the native command that might have
     erroneously bound to the WithCommand parameter.

PowerShell 7.3 introduces the following experimental features:

     PSNativeCommandErrorActionPreference - Adds the
     $PSNativeCommandUseErrorActionPreference variable to enable errors produced by native

     commands to be PowerShell errors.

PowerShell 7.3 removed the following experimental features:

     PSNativePSPathResolution experimental feature is no longer supported.

     PSStrictModeAssignment experimental feature is no longer supported.

For more information about the Experimental Features, see Using Experimental Features.

Last updated on 03/24/2025

<!-- p.661 -->

What's New in PowerShell 7.2
Article • 01/23/2025

PowerShell 7.2 is the next Long Term Servicing (LTS) release is built on .NET 6.0.

PowerShell 7.2 includes the following features, updates, and breaking changes.

      New universal installer packages for most supported Linux distributions
      Microsoft Update support on Windows
      2 new experimental features
         Improved native command argument passing support
         ANSI FileInfo color support
      Improved Tab Completions
      PSReadLine 2.1 with Predictive IntelliSense
      7 experimental features promoted to mainstream and 1 removed
      Separating DSC from PowerShell 7 to enable future improvements
      Several breaking changes to improve usability

For a complete list of changes, see the Change Log      in the GitHub repository.

Installation updates
Check the installation instructions for your preferred operating system:

      Windows
      macOS
      Linux

Additionally, PowerShell 7.2 supports ARM64 versions of Windows and macOS and
ARM32 and ARM64 versions of Debian and Ubuntu.

For up-to-date information about supported operating systems and support lifecycle,
see the PowerShell Support Lifecycle.

New universal install packages for Linux distributions
Previously, we created separate installer packages for each supported version of CentOS,
RHEL, Debian, and Ubuntu. The universal installer package combines eight different
packages into one, making installation on Linux simpler. The universal package installs
the necessary dependencies for the target distribution and creates the platform-specific
changes to make PowerShell work.

<!-- p.662 -->

Microsoft Update support for Windows
PowerShell 7.2 add support for Microsoft Update. When you enable this feature, you'll
get the latest PowerShell 7 updates in your traditional Windows Update (WU)
management flow, whether that's with Windows Update for Business, WSUS, SCCM, or
the interactive WU dialog in Settings.

The PowerShell 7.2 MSI package includes following command-line options:

     USE_MU - This property has two possible values:
        1 (default) - Opts into updating through Microsoft Update or WSUS

        0 - don't opt into updating through Microsoft Update or WSUS
     ENABLE_MU

        1 (default) - Opts into using Microsoft Update the Automatic Updates or

        Windows Update
        0 - don't opt into using Microsoft Update the Automatic Updates or Windows

        Update

Experimental Features
The following experimental features are now mainstream features in this release:

     Microsoft.PowerShell.Utility.PSImportPSDataFileSkipLimitCheck - see Import-

     PowerShellDataFile
     Microsoft.PowerShell.Utility.PSManageBreakpointsInRunspace
     PSAnsiRendering - see about_ANSI_Terminals

     PSAnsiProgress - see about_ANSI_Terminals
     PSCultureInvariantReplaceOperator

     PSNotApplyErrorActionToStderr

     PSUnixFileStat

The following experimental feature was added in this release:

     PSNativeCommandArgumentPassing - When this experimental feature is enabled
     PowerShell uses the ArgumentList property of the StartProcessInfo object rather
     than our current mechanism of reconstructing a string when invoking a native
     executable. This feature adds a new automatic variable
     $PSNativeCommandArgumentPassing that allows you to select the behavior at runtime.

     PSAnsiRenderingFileInfo - Allow ANSI color customization of file information.

<!-- p.663 -->

     PSLoadAssemblyFromNativeCode - Exposes an API to allow assembly loading from
     native code.

For more information about the Experimental Features, see Using Experimental Features.

Improved Tab Completions
PowerShell 7.2 includes several improvements to Tab Completion. These changes
include bugfixes and improve usability.

     Fix tab completion for unlocalized about* topics (#15265) (Thanks @MartinGC94)
     Fix splatting being treated as positional parameter in completions (#14623)
     (Thanks @MartinGC94)
     Add completions for comment-based help keywords (#15337) (Thanks
     @MartinGC94)
     Add completion for Requires statements (#14596) (Thanks @MartinGC94)
     Added tab completion for View parameter of Format-* cmdlets (#14513) (Thanks
     @iSazonov)

PSReadLine 2.1 Predictive IntelliSense
PSReadLine 2.1 introduced CommandPrediction APIs that establish a framework for
providing predictions for command-line completion. The API enables users to discover,
edit, and execute full commands based on matching predictions from the user's history.

Predictive IntelliSense is disabled by default. To enable predictions, run the following
command:

  PowerShell

  Set-PSReadLineOption -PredictionSource History

Separating DSC from PowerShell 7 to enable
future improvements
The PSDesiredStateConfiguration module was removed from the PowerShell 7.2
package and is now published to the PowerShell Gallery. This allows the
PSDesiredStateConfiguration module to be developed independently of PowerShell and
users can mix and match versions of PowerShell and PSDesiredStateConfiguration for

<!-- p.664 -->

their environment. To install PSDesiredStateConfiguration 2.0.5 from the PowerShell
Gallery:

  PowerShell

  Install-Module -Name PSDesiredStateConfiguration -Repository PSGallery -
  MaximumVersion 2.99

  ） Important

  Be sure to include the parameter MaximumVersion or you could install version 3 (or
  higher) of PSDesireStateConfiguration that contains significant differences.

Engine updates
     Add LoadAssemblyFromNativeMemory function to load assemblies in memory from a
     native PowerShell host by awakecoding · Pull Request #14652

Breaking Changes and Improvements
     The PSDesiredStateConfiguration was removed from the PowerShell 7.2 package
     Make PowerShell Linux deb and RPM packages universal (#15109)
     Experimental feature PSNativeCommandArgumentPassing : Use ArgumentList for native
     executable invocation (#14692)
     Ensure -PipelineVariable is set for all output from script cmdlets (#12766)
     Emit warning if ConvertTo-Json exceeds -Depth value (#13692)
     Remove alias D of -Directory switch CL-General #15171
     Improve detection of mutable value types (#12495)
     Restrict New-Object in NoLanguage mode under lock down (#14140)
     Enforce AppLocker Deny configuration before Execution Policy Bypass
     configuration (#15035)
     Change FileSystemInfo.Target from a CodeProperty to an AliasProperty that
     points to FileSystemInfo.LinkTarget (#16165)

<!-- p.665 -->

Migrating from Windows PowerShell 5.1 to
PowerShell 7
Designed for cloud, on-premises, and hybrid environments, PowerShell 7 is packed with
enhancements and new features.

     Installs and runs side-by-side with Windows PowerShell
     Improved compatibility with existing Windows PowerShell modules
     New language features, like ternary operators and ForEach-Object -Parallel
     Improved performance
     SSH-based remoting
     Cross-platform interoperability
     Support for Docker containers

PowerShell 7 works side-by-side with Windows PowerShell letting you easily test and compare
between editions before deployment. Migration is simple, quick, and safe.

PowerShell 7 is supported on the following Windows operating systems:

     Windows 10, and 11
     Windows Server 2016, 2019, and 2022

PowerShell 7 also runs on macOS and several Linux distributions. For a list of supported operating
systems and information about the support lifecycle, see the PowerShell Support Lifecycle.

Installing PowerShell 7
For flexibility and to support the needs of IT, DevOps engineers, and developers, there are several
options available to install PowerShell 7. In most cases, the installation options can be reduced to
the following methods:

     Deploy PowerShell using the MSI package
     Deploy PowerShell using the ZIP package

  ７ Note

  The MSI package can be deployed and updated with management products such as
  Microsoft Configuration Manager. Download the packages from GitHub Release page             .

<!-- p.666 -->

Deploying the MSI package requires Administrator permission. The ZIP package can be deployed
by any user. The ZIP package is the easiest way to install PowerShell 7 for testing, before
committing to a full installation.

You may also install PowerShell 7 via the Windows Store or winget . For more information about
both of these methods, see the detailed instructions in Installing PowerShell on Windows.

Using PowerShell 7 side-by-side with Windows
PowerShell 5.1
PowerShell 7 is designed to coexist with Windows PowerShell 5.1. The following features ensure
that your investment in PowerShell is protected and your migration to PowerShell 7 is simple.

     Separate installation path and executable name
     Separate PSModulePath
     Separate profiles for each version
     Improved module compatibility
     New remoting endpoints
     Group policy support
     Separate Event logs

Differences in .NET versions
PowerShell 7.4 is built on .NET 8.0. Windows PowerShell 5.1 is built on .NET Framework 4.x. The
differences between the .NET versions might affect the behavior of your scripts, especially if you
are calling .NET method directly. For more information, Differences between Windows PowerShell
5.1 and PowerShell 7.x.

Separate installation path and executable name
PowerShell 7 installs to a new directory, enabling side-by-side execution with Windows
PowerShell 5.1.

Install locations by version:

     Windows PowerShell 5.1: $Env:windir\System32\WindowsPowerShell\v1.0
     PowerShell 6.x: $Env:ProgramFiles\PowerShell\6
     PowerShell 7: $Env:ProgramFiles\PowerShell\7

The new location is added to your PATH allowing you to run both Windows PowerShell 5.1 and
PowerShell 7. If you're migrating from PowerShell 6.x to PowerShell 7, PowerShell 6 is removed

<!-- p.667 -->

and the PATH replaced.

In Windows PowerShell, the PowerShell executable is named powershell.exe . In version 6 and
above, the executable is named pwsh.exe . The new name makes it easy to support side-by-side
execution of both versions.

Separate PSModulePath
By default, Windows PowerShell and PowerShell 7 store modules in different locations. PowerShell
7 combines those locations in the $Env:PSModulePath environment variable. When importing a
module by name, PowerShell checks the location specified by $Env:PSModulePath . This allows
PowerShell 7 to load both Core and Desktop modules.

                                                                                           ﾉ   Expand table

 Install            Windows PowerShell 5.1                                PowerShell 7.0
 Scope

 PowerShell         $Env:windir\system32\WindowsPowerShell\v1.0\Modules   $Env:ProgramFiles\PowerShell\7\Modules
 modules

 User               $Env:ProgramFiles\WindowsPowerShell\Modules           $Env:ProgramFiles\PowerShell\Modules
 installed
 AllUsers
 scope

 User               $HOME\Documents\WindowsPowerShell\Modules             $HOME\Documents\PowerShell\Modules
 installed
 CurrentUser
 scope

The following examples show the default values of $Env:PSModulePath for each version.

        For Windows PowerShell 5.1:

           PowerShell

           $Env:PSModulePath -split (';')

           Output

           C:\Users\<user>\Documents\WindowsPowerShell\Modules
           C:\Program Files\WindowsPowerShell\Modules
           C:\WINDOWS\System32\WindowsPowerShell\v1.0\Modules

        For PowerShell 7:

<!-- p.668 -->

       PowerShell

       $Env:PSModulePath -split (';')

       Output

       C:\Users\<user>\Documents\PowerShell\Modules
       C:\Program Files\PowerShell\Modules
       C:\Program Files\PowerShell\7\Modules
       C:\Program Files\WindowsPowerShell\Modules
       C:\WINDOWS\System32\WindowsPowerShell\v1.0\Modules

Notice that PowerShell 7 includes the Windows PowerShell paths and the PowerShell 7 paths to
provide autoloading of modules.

  ７ Note

  Additional paths may exist if you have changed the PSModulePath environment variable or
  installed custom modules or applications.

For more information, see about_PSModulePath.

For more information about Modules, see about_Modules.

Separate profiles
A PowerShell profile is a script that executes when PowerShell starts. This script customizes your
environment by adding commands, aliases, functions, variables, modules, and PowerShell drives.
The profile script makes these customizations available in every session without having to
manually recreate them.

The path to the location of the profile has changed in PowerShell 7.

     In Windows PowerShell 5.1, the location of the profile is $HOME\Documents\WindowsPowerShell .
     In PowerShell 7, the location of the profile is $HOME\Documents\PowerShell .

The profile filenames have also changed:

 PowerShell

 $PROFILE | Select-Object *Host* | Format-List

 Output

<!-- p.669 -->

  AllUsersAllHosts       : C:\Program Files\PowerShell\7\profile.ps1
  AllUsersCurrentHost    : C:\Program
 Files\PowerShell\7\Microsoft.PowerShell_profile.ps1
  CurrentUserAllHosts    : C:\Users\<user>\Documents\PowerShell\profile.ps1
  CurrentUserCurrentHost : C:\Users\
 <user>\Documents\PowerShell\Microsoft.PowerShell_profile.ps1

For more information about_Profiles.

PowerShell 7 compatibility with Windows PowerShell 5.1
modules
Most of the modules you use in Windows PowerShell 5.1 already work with PowerShell 7,
including Azure PowerShell and Active Directory. We're continuing to work with other teams to
add native PowerShell 7 support for more modules including Microsoft Graph, Office 365, and
others. For the current list of supported modules, see PowerShell 7 module compatibility.

  ７ Note

  On Windows, we've also added a UseWindowsPowerShell switch to Import-Module to ease
  the transition to PowerShell 7 for those using incompatible modules. For more information
  on this functionality, see about_Windows_PowerShell_Compatibility.

PowerShell Remoting
PowerShell remoting lets you run any PowerShell command on one or more remote computers.
You can establish persistent connections, start interactive sessions, and run scripts on remote
computers.

WS-Management remoting
Windows PowerShell 5.1 and below use the WS-Management (WSMAN) protocol for connection
negotiation and data transport. Windows Remote Management (WinRM) uses the WSMAN
protocol. If WinRM has been enabled, PowerShell 7 uses the existing Windows PowerShell 5.1
endpoint named Microsoft.PowerShell for remoting connections. To update PowerShell 7 to
include its own endpoint, run the Enable-PSRemoting cmdlet. For information about connecting to
specific endpoints, see WS-Management Remoting in PowerShell

To use Windows PowerShell remoting, the remote computer must be configured for remote
management. For more information, including instructions, see About Remote Requirements.

<!-- p.670 -->

For more information about working with remoting, see About Remote

SSH-based remoting
SSH-based remoting was added in PowerShell 6.x to support other operating systems that can't
use Windows native components like WinRM. SSH remoting creates a PowerShell host process on
the target computer as an SSH subsystem. For details and examples on setting up SSH-based
remoting on Windows or Linux, see: PowerShell remoting over SSH.

  ７ Note

  The PowerShell Gallery (PSGallery) contains a module and cmdlet that automatically
  configures SSH-based remoting. Install the Microsoft.PowerShell.RemotingTools module
  from the PSGallery    and run the Enable-SSH cmdlet.

The New-PSSession , Enter-PSSession , and Invoke-Command cmdlets have new parameter sets to
support SSH connections.

 PowerShell

 [-HostName <string>]      [-UserName <string>]   [-KeyFilePath <string>]

To create a remote session, specify the target computer with the HostName parameter and
provide the user name with UserName. When running the cmdlets interactively, you're prompted
for a password.

 PowerShell

 Enter-PSSession -HostName <Computer> -UserName <Username>

Alternatively, when using the HostName parameter, provide the username information followed
by the at sign ( @ ), followed by the computer name.

 PowerShell

 Enter-PSSession -HostName <Username>@<Computer>

You may set up SSH key authentication using a private key file with the KeyFilePath parameter.
For more information, see OpenSSH Key Management.

Group Policy supported

<!-- p.671 -->

PowerShell includes Group Policy settings to help you define consistent option values for servers
in an enterprise environment. These settings include:

     Console session configuration: Sets a configuration endpoint in which PowerShell is run.
     Turn on Module Logging: Sets the LogPipelineExecutionDetails property of modules.
     Turn on PowerShell Script Block Logging: Enables detailed logging of all PowerShell scripts.
     Turn on Script Execution: Sets the PowerShell execution policy.
     Turn on PowerShell Transcription: enables capturing of input and output of PowerShell
     commands into text-based transcripts.
     Set the default source path for Update-Help: Sets the source for Updatable Help to a
     directory, not the Internet.

For more information, see about_Group_Policy_Settings.

PowerShell 7 includes Group Policy templates and an installation script in $PSHOME .

Group Policy tools use administrative template files ( .admx , .adml ) to populate policy settings in
the user interface. This allows administrators to manage registry-based policy settings. The
InstallPSCorePolicyDefinitions.ps1 script installs PowerShell Administrative Templates on the

local machine.

 PowerShell

 Get-ChildItem -Path $PSHOME -Filter *Core*Policy*

 Output

      Directory: C:\Program Files\PowerShell\7

 Mode                    LastWriteTime             Length Name
 ----                    -------------             ------ ----
 -a---              2/27/2020 12:38 AM              15861 InstallPSCorePolicyDefinitions.ps1
 -a---              2/27/2020 12:28 AM               9675 PowerShellCoreExecutionPolicy.adml
 -a---              2/27/2020 12:28 AM               6201 PowerShellCoreExecutionPolicy.admx

Separate Event Logs
Windows PowerShell and PowerShell 7 log events to separate event logs. Use the following
command to get a list of the PowerShell logs.

 PowerShell

 Get-WinEvent -ListLog *PowerShell*

<!-- p.672 -->

For more information, see about_Logging_Windows.

Improved editing experience with Visual Studio
Code
Visual Studio Code (VS Code)      with the PowerShell Extension    is the supported scripting
environment for PowerShell 7. The Windows PowerShell Integrated Scripting Environment (ISE)
only supports Windows PowerShell.

The updated PowerShell extension includes:

     New ISE compatibility mode
     PSReadLine in the Integrated Console, including syntax highlighting, multi-line editing, and
     back search
     Stability and performance improvements
     New CodeLens integration
     Improved path autocompletion

To make the transition to Visual Studio Code easier, use the Enable ISE Mode function available in
the Command Palette. This function switches VS Code into an ISE-style layout. The ISE-style
layout gives you all the new features and capabilities of PowerShell in a familiar user experience.

To switch to the new ISE layout, press Ctrl + Shift + P to open the Command Palette, type
PowerShell and select PowerShell: Enable ISE Mode.

To set the layout to the original layout, open the Command Palette, select PowerShell: Disable
ISE Mode (restore to defaults).

For details about customizing the VS Code layout to ISE, see How to Replicate the ISE Experience
in Visual Studio Code

  ７ Note

  There are no plans to update the ISE with new features. In the latest versions of Windows 10
  or Windows Server 2019 and higher, the ISE is now a user-uninstallable feature. There are no
  plans to permanently remove the ISE. The PowerShell Team and its partners are focused on
  improving the scripting experience in the PowerShell extension for Visual Studio Code.

Next Steps

<!-- p.673 -->

Armed with the knowledge to effectively migrate, install PowerShell 7 now!

Last updated on 04/16/2025

<!-- p.674 -->

Differences between Windows PowerShell
5.1 and PowerShell 7.x
Windows PowerShell 5.1 is built on top of the .NET Framework v4.5. With the release of
PowerShell 6.0, PowerShell became an open source project built on .NET Core 2.0. Moving from
the .NET Framework to .NET Core allowed PowerShell to become a cross-platform solution.
PowerShell runs on Windows, macOS, and Linux.

There are few differences in the PowerShell language between Windows PowerShell and
PowerShell. The most notable differences are in the availability and behavior of PowerShell
cmdlets between Windows and non-Windows platforms and the changes that stem from the
differences between the .NET Framework and .NET Core.

This article summarizes the significant differences and breaking changes between Windows
PowerShell and the current version of PowerShell. This summary doesn't include new features
or cmdlets that have been added. Nor does this article discuss what changed between versions.
The goal of this article is to present the current state of PowerShell and how that's different
from Windows PowerShell. For a detailed discussion of changes between versions and the
addition of new features, see the What's New articles for each version.

     What's new in PowerShell 7.5
     What's new in PowerShell 7.4
     What's new in PowerShell 7.3
     What's new in PowerShell 7.2
     What's new in PowerShell 7.1
     What's new in PowerShell 7.0
     What's new in PowerShell 6.x

.NET Framework vs .NET Core
PowerShell on Linux and macOS uses .NET core, which is a subset of the full .NET Framework
on Microsoft Windows. This is significant because PowerShell provides direct access to the
underlying framework types and methods. As a result, scripts that run on Windows may not run
on non-Windows platforms because of the differences in the frameworks. For more
information about changes in .NET Core, see Breaking changes for migration from .NET
Framework to .NET Core.

<!-- p.675 -->

Each new release of PowerShell is built on a newer version of .NET. There can be breaking
changes in .NET that affect PowerShell.

     PowerShell 7.6 - Built on .NET 10.0 (LTS)
     PowerShell 7.5 - Built on .NET 9.0
     PowerShell 7.4 - Built on .NET 8.0 (LTS)
     PowerShell 7.3 - Built on .NET 7.0
     PowerShell 7.2 - Built on .NET 6.0 (LTS)
     PowerShell 7.1 - Built on .NET 5.0
     PowerShell 7.0 - Built on .NET Core 3.1 (LTS)
     PowerShell 6.2 - Built on .NET Core 2.1
     PowerShell 6.1 - Built on .NET Core 2.1
     PowerShell 6.0 - Built on .NET Core 2.0

With the advent of .NET Standard 2.0      , PowerShell can load many traditional Windows
PowerShell modules without modification. Additionally, PowerShell 7 includes a Windows
PowerShell Compatibility feature that allows you to use Windows PowerShell modules that still
require the full framework.

For more information see:

     about_Windows_PowerShell_Compatibility
     PowerShell 7 module compatibility

Be aware of .NET method changes
While .NET method changes aren't specific to PowerShell, they can affect your scripts,
especially if you are calling .NET methods directly. Also, there might be new overloads for
constructors. This can have an impact on how you create objects using New-Object or the
[type]::new() method.

For example, .NET added overloads to the [System.String]::Split() method that aren't
available in .NET Framework 4.5. The following list shows the overloads for the Split()
method available in Windows PowerShell 5.1:

 PowerShell

 PS> "".Split

 OverloadDefinitions
 -------------------
 string[] Split(Params char[] separator)

<!-- p.676 -->

 string[] Split(char[] separator, int count)
 string[] Split(char[] separator, System.StringSplitOptions options)
 string[] Split(char[] separator, int count, System.StringSplitOptions options)
 string[] Split(string[] separator, System.StringSplitOptions options)
 string[] Split(string[] separator, int count, System.StringSplitOptions options)

The following list shows the overloads for the Split() method available in PowerShell 7:

 PowerShell

 "".Split

 OverloadDefinitions
 -------------------
 string[] Split(char separator, System.StringSplitOptions options)
 string[] Split(char separator, int count, System.StringSplitOptions options)
 string[] Split(Params char[] separator)
 string[] Split(char[] separator, int count)
 string[] Split(char[] separator, System.StringSplitOptions options)
 string[] Split(char[] separator, int count, System.StringSplitOptions options)
 string[] Split(string separator, System.StringSplitOptions options)
 string[] Split(string separator, int count, System.StringSplitOptions options)
 string[] Split(string[] separator, System.StringSplitOptions options)
 string[] Split(string[] separator, int count, System.StringSplitOptions options)

In Windows PowerShell 5.1, you could pass a character array ( char[] ) to the Split() method
as a string . The method splits the target string at any occurrence of a character in the array.
The following command splits the target string in Windows PowerShell 5.1, but not in
PowerShell 7:

 PowerShell

 # PowerShell 7 example
 "1111p2222q3333".Split('pq')

 Output

 1111p2222q3333

To bind to the correct overload, you must typecast the string to a character array:

 PowerShell

 # PowerShell 7 example
 "1111p2222q3333".Split([char[]]'pq')

<!-- p.677 -->

  Output

  1111
  2222
  3333

Modules no longer shipped with PowerShell
For various compatibility reasons, the following modules are no longer included in PowerShell.

      ISE
      Microsoft.PowerShell.LocalAccounts
      Microsoft.PowerShell.ODataUtils
      Microsoft.PowerShell.Operation.Validation
      PSScheduledJob
      PSWorkflow
      PSWorkflowUtility

PowerShell Workflow
PowerShell Workflow is a feature in Windows PowerShell that builds on top of Windows
Workflow Foundation (WF) that enables the creation of robust runbooks for long-running or
parallelized tasks.

Due to the lack of support for Windows Workflow Foundation in .NET Core, we removed
PowerShell Workflow from PowerShell.

In the future, we would like to enable native parallelism/concurrency in the PowerShell
language without the need for PowerShell Workflow.

If there is a need to use checkpoints to resume a script after the OS restarts, we recommend
using Task Scheduler to run a script on OS startup, but the script would need to maintain its
own state (like persisting it to a file).

Cmdlets removed from PowerShell
For the modules that are included in PowerShell, the following cmdlets were removed from
PowerShell for various compatibility reasons or the use of unsupported APIs.

CimCmdlets

      Export-BinaryMiLog

<!-- p.678 -->

Microsoft.PowerShell.Core

     Add-PSSnapin

     Export-Console

     Get-PSSnapin

     Remove-PSSnapin

     Resume-Job

     Suspend-Job

Microsoft.PowerShell.Diagnostics

     Export-Counter

     Import-Counter

Microsoft.PowerShell.Management

     Add-Computer

     Checkpoint-Computer

     Clear-EventLog

     Complete-Transaction

     Disable-ComputerRestore

     Enable-ComputerRestore

     Get-ComputerRestorePoint

     Get-ControlPanelItem

     Get-EventLog

     Get-Transaction

     Get-WmiObject

     Invoke-WmiMethod

     Limit-EventLog

     New-EventLog

     New-WebServiceProxy

     Register-WmiEvent

     Remove-Computer

     Remove-EventLog

     Remove-WmiObject

     Reset-ComputerMachinePassword

     Restore-Computer

     Set-WmiInstance

     Show-ControlPanelItem

<!-- p.679 -->

     Show-EventLog

     Start-Transaction

     Test-ComputerSecureChannel

     Undo-Transaction

     Use-Transaction

     Write-EventLog

Microsoft.PowerShell.Utility

     Convert-String

     ConvertFrom-String

PSDesiredStateConfiguration

     Disable-DscDebug

     Enable-DscDebug

     Get-DscConfiguration

     Get-DscConfigurationStatus

     Get-DscLocalConfigurationManager

     Publish-DscConfiguration

     Remove-DscConfigurationDocument

     Restore-DscConfiguration

     Set-DscLocalConfigurationManager

     Start-DscConfiguration

     Stop-DscConfiguration

     Test-DscConfiguration

     Update-DscConfiguration

WMI v1 cmdlets
The following WMI v1 cmdlets were removed from PowerShell:

     Register-WmiEvent

     Set-WmiInstance

     Invoke-WmiMethod

     Get-WmiObject

     Remove-WmiObject

The CimCmdlets module (aka WMI v2) cmdlets perform the same function and provide new
functionality and a redesigned syntax.

<!-- p.680 -->

New-WebServiceProxy cmdlet removed

.NET Core doesn't support the Windows Communication Framework, which provides services
for using the SOAP protocol. This cmdlet was removed because it requires SOAP.

*-Transaction cmdlets removed

These cmdlets had very limited usage. The decision was made to discontinue support for them.

     Complete-Transaction

     Get-Transaction

     Start-Transaction

     Undo-Transaction

     Use-Transaction

*-EventLog cmdlets

Due to the use of unsupported APIs, the *-EventLog cmdlets have been removed from
PowerShell. Get-WinEvent and New-WinEvent are available to get and create events on
Windows.

Cmdlets that use the Windows Presentation Framework (WPF)
.NET Core 3.1 added support for WPF, so the release of PowerShell 7.0 restored the following
Windows-specific features:

     The Show-Command cmdlet
     The Out-GridView cmdlet
     The ShowWindow parameter of Get-Help

PowerShell Desired State Configuration (DSC) changes
Invoke-DscResource was restored as an experimental feature in PowerShell 7.0.

Beginning with PowerShell 7.2, the PSDesiredStateConfiguration module has been removed
from PowerShell and has been published to the PowerShell Gallery. For more information, see
the announcement       in the PowerShell Team blog.

PowerShell executable changes
