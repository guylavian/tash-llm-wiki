---
title: "How to use this documentation — pages 2361-2400"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2361-2400
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2361-2400
family: powershell
documentKind: "doc"
abstract: "Child Elements ﾉ Expand table Element Description CustomControl Element Optional element. Defines a control that is used by this control. CustomControlName Element for ExpressionBinding for Optional element. Controls for Configuration Specifies the name of a common control or a"
---

# How to use this documentation — pages 2361-2400

<!-- p.2361 -->

Child Elements

                                                                                       ﾉ    Expand table

Element                                                  Description

CustomControl Element                                    Optional element.

                                                         Defines a control that is used by this control.

CustomControlName Element for ExpressionBinding for      Optional element.
Controls for Configuration
                                                         Specifies the name of a common control or a
                                                         view control.

EnumerateCollection Element for ExpressionBinding for    Optional element.
Controls for Configuration
                                                         Specified that the elements of collections are
                                                         displayed by the control.

ItemSelectionCondition Element for ExpressionBinding     Optional element.
for Controls for Configuration
                                                         Defines the condition that must exist for this
                                                         common control to be used.

PropertyName Element for ExpressionBinding for           Optional element.
Controls for Configuration
                                                         Specifies the .NET property whose value is
                                                         displayed by the common control.

ScriptBlock Element for ExpressionBinding for Controls   Optional element.
for Configuration
                                                         Specifies the script whose value is displayed by
                                                         the common control.

Parent Elements

                                                                                       ﾉ    Expand table

Element                                          Description

CustomItem Element for CustomEntry for           Defines what data is displayed by the custom control
Controls for Configuration                       view and how it is displayed.

Remarks
See Also

<!-- p.2362 -->

CustomItem Element for CustomEntry for Controls for Configuration

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2363 -->

CustomControlName Element for
ExpressionBinding for Controls for
Configuration
Specifies the name of a common control. This element is used when defining a common
control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     CustomControlName Element

Syntax
 XML

 <CustomControlName>NameofCustomControl</CustomControlName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomControlName element.

Attributes
None.

Child Elements

<!-- p.2364 -->

None.

Parent Elements

                                                                                    ﾉ   Expand table

 Element                                                     Description

 ExpressionBinding Element for CustomItem for Controls for   Defines the data that is displayed by the
 Configuration                                               control.

Text Value
Specify the name of the control.

Remarks
You can create common controls that can be used by all the views of a formatting file, and you
can create view controls that can be used by a specific view. The following elements specify the
names of these controls:

      Name Element for Control for Controls for Configuration

      Name Element for Control for Controls for View

See Also
Name Element for Control for Controls for Configuration

Name Element for Control for Controls for View

ExpressionBinding Element for CustomItem for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2365 -->

EnumerateCollection Element for
ExpressionBinding for Controls for
Configuration
Specified that the elements of collections are displayed by the control. This element is used
when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     EnumerateCollection Element

Syntax
 XML

 <EnumerateCollection/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
EnumerateCollection element.

Attributes
None.

Child Elements

<!-- p.2366 -->

None.

Parent Elements

                                                                                    ﾉ   Expand table

 Element                                                     Description

 ExpressionBinding Element for CustomItem for Controls for   Defines the data that is displayed by the
 Configuration                                               control.

Remarks

See Also
ExpressionBinding Element for CustomItem for Controls for Configuration

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2367 -->

ItemSelectionCondition Element for
ExpressionBinding for Controls for
Configuration
Defines the condition that must exist for this control to be used. This element is used when
defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     ItemSelectionCondition Element

Syntax
 XML

 <ItemSelectionCondition>
   <PropertyName>.NetTypeProperty</PropertyName>
   <ScriptBlock>ScriptToEvaluate</ScriptBlock>
 </ItemSelectionCondition>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ItemSelectionCondition element.

Attributes
None.

<!-- p.2368 -->

Child Elements

                                                                                       ﾉ    Expand table

 Element                                                       Description

 PropertyName Element for ItemSelectionCondition for           Optional element.
 Controls for Configuration
                                                               Specifies the .NET property that triggers
                                                               the condition.

 ScriptBlock Element for ItemSelectionCondition for Controls   Optional element.
 for Configuration
                                                               Specifies the script that triggers the
                                                               condition.

Parent Elements

                                                                                       ﾉ    Expand table

 Element                                                       Description

 ExpressionBinding Element for CustomItem for Controls for     Defines the data that is displayed by the
 Configuration                                                 control.

Remarks
You can specify one property name or a script for this condition but cannot specify both.

See Also
PropertyName Element for ItemSelectionCondition for Controls for Configuration

ScriptBlock Element for ItemSelectionCondition for Controls for Configuration

ExpressionBinding Element for CustomItem for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2369 -->

PropertyName Element for
ItemSelectionCondition for Controls for
Configuration
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the control is used. This element is used when
defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     ItemSelectionCondition Element
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

<!-- p.2370 -->

Child Elements
None.

Parent Elements

                                                                                     ﾉ    Expand table

 Element                                                    Description

 ItemSelectionCondition Element for ExpressionBinding for   Defines the condition that must exist for
 Controls for Configuration                                 this control to be used.

Text Value
Specify the name of the .NET property that triggers the condition.

Remarks
If this element is used, you cannot specify the ScriptBlock element when defining the selection
condition.

See Also
ScriptBlock Element for ItemSelectionCondition for Controls for Configuration

ItemSelectionCondition Element for ExpressionBinding for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2371 -->

ScriptBlock Element for
ItemSelectionCondition for Controls for
Configuration
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the control is used. This element is used when defining a common
control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     ItemSelectionCondition Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

<!-- p.2372 -->

Child Elements
None.

Parent Elements

                                                                                     ﾉ    Expand table

 Element                                                    Description

 ItemSelectionCondition Element for ExpressionBinding for   Defines the condition that must exist for
 Controls for Configuration                                 this control to be used.

Text Value
Specify the script that is evaluated.

Remarks
If this element is used, you cannot specify the PropertyName element when defining the
selection condition.

See Also
PropertyName Element for ItemSelectionCondition for Controls for Configuration

ItemSelectionCondition Element for ExpressionBinding for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2373 -->

PropertyName Element for
ExpressionBinding for Controls for
Configuration
Specifies the .NET property whose value is displayed by the common control. This element is
used when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

Child Elements

<!-- p.2374 -->

None.

Parent Elements

                                                                                    ﾉ   Expand table

 Element                                                     Description

 ExpressionBinding Element for CustomItem for Controls for   Defines the data that is displayed by the
 Configuration                                               control.

Text Value
Specify the name of the .NET property whose value is displayed by the control.

Remarks
See Also
ExpressionBinding Element for CustomItem for Controls for Configuration

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2375 -->

ScriptBlock Element for ExpressionBinding
for Controls for Configuration
Specifies the script whose value is displayed by the common control. This element is used
when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

Child Elements
None.

<!-- p.2376 -->

Parent Elements

                                                                                     ﾉ   Expand table

 Element                                                 Description

 ExpressionBinding Element for CustomItem for Controls   Defines the data that is displayed by the
 for Configuration                                       common control.

Text Value
Specify the script whose value is displayed by the control.

Remarks
See Also
ExpressionBinding Element for CustomItem for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2377 -->

Frame Element for CustomItem for
Controls for Configuration
Defines how the data is displayed, such as shifting the data to the left or right. This element is
used when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element

Syntax
 XML

 <Frame>
   <LeftIndent>NumberOfCharactersToShift</LeftIndent>
   <RightIndent>NumberOfCharactersToShift</RightIndent>
   <FirstLineHanging>NumberOfCharactersToShift</FirstLineHanging>
   <FirstLineIndent>NumberOfCharactersToShift</FirstLineIndent>
   <CustomItem>...</CustomItem>
 </Frame>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the Frame
element.

Attributes
None.

<!-- p.2378 -->

Child Elements

                                                                                         ﾉ   Expand table

 Element                                           Description

 CustomItem Element                                Required Element

 FirstLineHanging Element for Frame for Controls   Optional element.
 for Configuration
                                                   Specifies how many characters the first line of data is
                                                   shifted to the left.

 FirstLineIndent Element for Frame for Controls    Optional element.
 for Configuration
                                                   Specifies how many characters the first line of data is
                                                   shifted to the right.

 LeftIndent Element for Frame for Controls for     Optional element.
 Configuration
                                                   Specifies how many characters the data is shifted
                                                   away from the left margin.

 RightIndent Element for Frame for Controls for    Optional element.
 Configuration
                                                   Specifies how many characters the data is shifted
                                                   away from the right margin.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                                              Description

 CustomItem Element for CustomEntry for Controls      Defines what data is displayed by the control and
 for Configuration                                    how it is displayed.

Remarks
You cannot specify the FirstLineHanging and the FirstLineIndent elements in the same Frame
element.

See Also
FirstLineHanging Element for Frame for Controls for Configuration

<!-- p.2379 -->

FirstLineIndent Element for Frame for Controls for Configuration

LeftIndent Element for Frame for Controls for Configuration

RightIndent Element for Frame for Controls for Configuration

CustomItem Element for CustomEntry for Controls for Configuration

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2380 -->

FirstLineHanging Element for Frame for
Controls for Configuration
Specifies how many characters the first line of data is shifted to the left. This element is used
when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element
     FirstLineHanging Element

Syntax
 XML

 <FirstLineHanging>NumberOfCharactersToShift</FirstLineHanging>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
FirstLineHanging element.

Attributes
None.

Child Elements
None.

<!-- p.2381 -->

Parent Elements

                                                                                      ﾉ   Expand table

 Element                                      Description

 Frame Element for CustomItem for Controls    Defines how the data is displayed, such as shifting the
 for Configuration                            data to the left or right.

Text Value
Specify the number of characters that you want to shift the first line of the data.

Remarks
If this element is specified, you cannot specify the FirstLineIndent element.

See Also
Frame Element for CustomItem for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2382 -->

FirstLineIndent Element for Frame for
Controls for Configuration
Specifies how many characters the first line of data is shifted to the right. This element is used
when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element
     FirstLineIndent Element

Syntax
 XML

 <FirstLineIndent>NumberOfCharactersToShift</FirstLineIndent>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
FirstLineIndent element.

Attributes
None.

Child Elements
None.

<!-- p.2383 -->

Parent Elements

                                                                                      ﾉ   Expand table

 Element                                      Description

 Frame Element for CustomItem for Controls    Defines how the data is displayed, such as shifting the
 for Configuration                            data to the left or right.

Text Value
Specify the number of characters that you want to shift the first line of the data.

Remarks
If this element is specified, you cannot specify the FirstLineHanging element.

See Also
FirstLineHanging Element for Frame for Controls for Configuration

Frame Element for CustomItem for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2384 -->

LeftIndent Element for Frame for Controls
for Configuration
Specifies how many characters the data is shifted away from the left margin. This element is
used when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element
     LeftIndent Element

Syntax
 XML

 <LeftIndent>CharactersToShift</LeftIndent>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
LeftIndent element.

Attributes
None.

Child Elements
None.

<!-- p.2385 -->

Parent Elements

                                                                                     ﾉ   Expand table

 Element                                     Description

 Frame Element for CustomItem for Controls   Defines how the data is displayed, such as shifting the
 for Configuration                           data to the left or right.

Text Value
Specify the number of characters that you want to shift the data to the left.

Remarks
See Also
Frame Element for CustomItem for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2386 -->

RightIndent Element for Frame for Controls
for Configuration
Specifies how many characters the data is shifted away from the right margin. This element is
used when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element
     RightIndent Element

Syntax
 XML

 <RightIndent>CharactersToShift</RightIndent>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
RightIndent element.

Attributes
None.

Child Elements
None.

<!-- p.2387 -->

Parent Elements

                                                                                     ﾉ   Expand table

 Element                                     Description

 Frame Element for CustomItem for Controls   Defines how the data is displayed, such as shifting the
 for Configuration                           data to the left or right.

Text Value
Specify the number of characters that you want to shift the data to the right.

Remarks
See Also
Frame Element for CustomItem for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2388 -->

NewLine Element for CustomItem for
Controls for Configuration
Adds a blank line to the display of the control. This element is used when defining a common
control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     NewLine Element

Syntax
 XML

 <NewLine/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
NewLine element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2389 -->

                                                                              ﾉ   Expand table

 Element                                               Description

 CustomItem Element for CustomEntry for Controls for   Defines a control for the custom control
 Configuration                                         view.

Remarks
See Also
CustomItem Element for CustomEntry for Controls for Configuration

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2390 -->

Text Element for CustomItem for Controls
for Configuration
Specifies text that is added to the data that is displayed by the control, such as a label, brackets
to enclose the data, and spaces to indent the data. This element is used when defining a
common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Text Element

Syntax
 XML

 <Text>TextToDisplay</Text>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the Text
element.

Attributes
None.

Child Elements
None.

<!-- p.2391 -->

Parent Elements

                                                                                    ﾉ   Expand table

 Element                                           Description

 CustomItem Element for CustomEntry for Controls   Defines what data is displayed by the control and
 for Configuration                                 how it is displayed.

Text Value
Specify the text of a control for data that you want to display.

Remarks
See Also
CustomItem Element for CustomEntry for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2392 -->

EntrySelectedBy Element for CustomEntry
for Controls
Defines the .NET types that use the definition of the common control or the condition that
must exist for this control to be used. This element is used when defining a common control
that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element

Syntax
 XML

 <EntrySelectedBy>
   <TypeName>Nameof.NetType</TypeName>
   <SelectionSetName>SelectionSet</SelectionSetName>
   <SelectionCondition>...</SelectionCondition>
 </EntrySelectedBy>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
EntrySelectedBy element.

Attributes
None.

Child Elements

<!-- p.2393 -->

                                                                                          ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Optional element.
 Controls for Configuration
                                                      Defines the condition that must exist for the
                                                      common control definition to be used.

 SelectionSetName Element for EntrySelectedBy for     Optional element.
 Controls for Configuration
                                                      Specifies a set of .NET types that use this definition
                                                      of the common control.

 TypeName Element for EntrySelectedBy for             Optional element.
 Controls for Configuration
                                                      Specifies a .NET type that uses this definition of the
                                                      common control.

Parent Elements

                                                                                          ﾉ   Expand table

 Element                                                          Description

 CustomEntry Element for CustomControl for Controls for           Provides a definition of the common
 Configuration                                                    control.

Remarks
At a minimum, each definition must have at least one .NET type, selection set, or selection
condition specified. There is no maximum limit to the number of types, selection sets, or
selection conditions that you can specify.

See Also
SelectionCondition Element for EntrySelectedBy for Controls for Configuration

SelectionSetName Element for EntrySelectedBy for Controls for Configuration

CustomEntry Element for CustomControl for Controls for Configuration

TypeName Element for EntrySelectedBy for Controls for Configuration

Writing a PowerShell Formatting File

<!-- p.2394 -->

Last updated on 05/20/2025

<!-- p.2395 -->

SelectionCondition Element for
EntrySelectedBy for Controls for
Configuration
Defines a condition that must exist for a common control definition to be used. This element is
used when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element
     SelectionCondition Element

Syntax
 XML

 <SelectionCondition>
   <TypeName>Nameof.NetType</TypeName>
   <SelectionSetName>NameofSelectionSet</SelectionSetName>
   <PropertyName>.NetTypeProperty</PropertyName>
   <ScriptBlock>ScriptToEvaluate</ScriptBlock>
 </SelectionCondition>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionCondition element.

Attributes
None.

<!-- p.2396 -->

Child Elements

                                                                                          ﾉ    Expand table

 Element                                                        Description

 PropertyName Element for SelectionCondition for Controls       Optional element.
 for Configuration
                                                                Specifies a .NET property that triggers the
                                                                condition.

 ScriptBlock Element for SelectionCondition for Controls for    Optional element.
 Configuration
                                                                Specifies the script that triggers the
                                                                condition.

 SelectionSetName Element for SelectionCondition for            Optional element.
 Controls for Configuration
                                                                Specifies the set of .NET types that
                                                                triggers the condition.

 TypeName Element for SelectionCondition for Controls for       Optional element.
 Configuration
                                                                Specifies a .NET type that triggers the
                                                                condition.

Parent Elements

                                                                                          ﾉ    Expand table

 Element                                               Description

 EntrySelectedBy Element for CustomEntry for           Defines the .NET types that use this entry of the
 Controls for Configuration                            common control definition.

Remarks
The following guidelines must be followed when defining a selection condition:

     The selection condition must specify a least one property name or a script block, but
     cannot specify both.
     The selection condition can specify any number of .NET types or selection sets, but
     cannot specify both.

<!-- p.2397 -->

For more information about how selection conditions can be used, see Defining Conditions for
when Data is Displayed.

See Also
PropertyName Element for SelectionCondition for Controls for Configuration

ScriptBlock Element for SelectionCondition for Controls for Configuration

SelectionSetName Element for SelectionCondition for Controls for Configuration

TypeName Element for SelectionCondition for Controls for Configuration

EntrySelectedBy Element for CustomEntry for Controls for Configuration

Writing a Windows PowerShell Formatting and Types File

Last updated on 05/20/2025

<!-- p.2398 -->

PropertyName Element for
SelectionCondition for Controls for
Configuration
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the entry is used. This element is used when
defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

Child Elements

<!-- p.2399 -->

None.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for a common
 Controls for Configuration                           control definition to be used.

Text Value
Specify the .NET property name.

Remarks
The selection condition must specify a least one property name or a script, but cannot specify
both. For more information about how selection conditions can be used, see Defining
Conditions for Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for Controls for Configuration

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2400 -->

ScriptBlock Element for SelectionCondition
for Controls for Configuration
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the definition is used. This element is used when defining a common
control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

Child Elements
None.
