---
title: "How to use this documentation — pages 2481-2520"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2481-2520
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2481-2520
family: powershell
documentKind: "doc"
abstract: "None. Child Elements ﾉ Expand table Element Description CustomControl Element Optional element. Defines a control that is used by this control. CustomControlName Element for ExpressionBinding for Optional element. Controls for View Specifies the name of a common control or a vie"
---

# How to use this documentation — pages 2481-2520

<!-- p.2481 -->

None.

Child Elements

                                                                                           ﾉ   Expand table

 Element                                                    Description

 CustomControl Element                                      Optional element.

                                                            Defines a control that is used by this control.

 CustomControlName Element for ExpressionBinding for        Optional element.
 Controls for View
                                                            Specifies the name of a common control or a
                                                            view control.

 EnumerateCollection Element for ExpressionBinding for      Optional element.
 Controls for View
                                                            Specifies that the elements of collections are
                                                            displayed.

 ItemSelectionCondition Element of ExpressionBinding        Optional element.
 for Controls for View
                                                            Defines the condition that must exist for this
                                                            control to be used.

 PropertyName Element for ExpressionBinding for             Optional element.
 Controls for View
                                                            Specifies the .NET property whose value is
                                                            displayed by the control.

 ScriptBlock Element for ExpressionBinding for Controls     Optional element.
 for View
                                                            Specifies the script whose value is displayed by
                                                            the control.

Parent Elements

                                                                                           ﾉ   Expand table

 Element                                           Description

 CustomItem Element for CustomEntry for            Defines what data is displayed by the control and how
 Controls for View                                 it is displayed.

Remarks

<!-- p.2482 -->

See Also
CustomItem Element for CustomEntry for Controls for View

CustomControlName Element for ExpressionBinding for Controls for View

EnumerateCollection Element for ExpressionBinding for Controls for View

ItemSelectionCondition Element of ExpressionBinding for Controls for View

PropertyName Element for ExpressionBinding for Controls for View

ScriptBlock Element for ExpressionBinding for Controls for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2483 -->

CustomControlName Element for
ExpressionBinding for Controls for View
Specifies the name of a common control or a view control. This element is used when defining
controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2484 -->

None.

Parent Elements

                                                                                       ﾉ    Expand table

 Element                                                     Description

 ExpressionBinding Element for CustomItem for Controls for   Defines the data that is displayed by the
 View                                                        control.

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

ExpressionBinding Element for CustomItem for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2485 -->

EnumerateCollection Element for
ExpressionBinding for Controls for View
Specified that the elements of collections are displayed. This element is used when defining
controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2486 -->

None.

Parent Elements

                                                                                       ﾉ    Expand table

 Element                                                     Description

 ExpressionBinding Element for CustomItem for Controls for   Defines the data that is displayed by the
 View                                                        control.

Remarks

See Also
ExpressionBinding Element for CustomItem for Controls for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2487 -->

ItemSelectionCondition Element for
ExpressionBinding for Controls for View
Defines the condition that must exist for this control to be used. This element is used when
defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2488 -->

Child Elements

                                                                                        ﾉ    Expand table

 Element                                                     Description

 PropertyName Element for ItemSelectionCondition for         Optional element.
 Controls for View
                                                             Specifies the .NET property that triggers
                                                             the condition.

 ScriptBlock Element for ItemSelectionCondition for          Optional element.
 Controls for View
                                                             Specifies the script that triggers the
                                                             condition.

Parent Elements

                                                                                        ﾉ    Expand table

 Element                                                     Description

 ExpressionBinding Element for CustomItem for Controls for   Defines the data that is displayed by the
 View                                                        control.

Remarks
You can specify one property name or a script for this condition but cannot specify both.

See Also
PropertyName Element for ItemSelectionCondition for Controls for View

ScriptBlock Element for ItemSelectionCondition for Controls for View

ExpressionBinding Element for CustomItem for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2489 -->

PropertyName Element for
ItemSelectionCondition for Controls for
View
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the control is used. This element is used when
defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2490 -->

None.

Child Elements
None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                                   Description

 ItemSelectionCondition Element of ExpressionBinding for   Defines the condition that must exist for this
 Controls for View                                         control to be used.

Text Value
Specify the name of the .NET property that triggers the condition.

Remarks
If this element is used, you cannot specify the ScriptBlock element when defining the selection
condition.

See Also
ScriptBlock Element for ItemSelectionCondition for Controls for View

ItemSelectionCondition Element of ExpressionBinding for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2491 -->

ScriptBlock Element for
ItemSelectionCondition for Controls for
View
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the control is used. This element is used when defining controls that can
be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2492 -->

None.

Child Elements
None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                                   Description

 ItemSelectionCondition Element of ExpressionBinding for   Defines the condition that must exist for this
 Controls for View                                         control to be used.

Text Value
Specify the script that is evaluated.

Remarks
If this element is used, you cannot specify the PropertyName element when defining the
selection condition.

See Also
PropertyName Element for ItemSelectionCondition for Controls for View

ItemSelectionCondition Element of ExpressionBinding for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2493 -->

PropertyName Element for
ExpressionBinding for Controls for View
Specifies the .NET property whose value is displayed by the control. This element is used when
defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2494 -->

None.

Parent Elements

                                                                                       ﾉ    Expand table

 Element                                                     Description

 ExpressionBinding Element for CustomItem for Controls for   Defines the data that is displayed by the
 View                                                        control.

Text Value
Specify the name of the .NET property whose value is displayed by the control.

Remarks
See Also
ExpressionBinding Element for CustomItem for Controls for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2495 -->

ScriptBlock Element for ExpressionBinding
for Controls for View
Specifies the script whose value is displayed by the control. This element is used when defining
controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2496 -->

None.

Parent Elements

                                                                                       ﾉ    Expand table

 Element                                                     Description

 ExpressionBinding Element for CustomItem for Controls for   Defines the data that is displayed by the
 View                                                        control.

Text Value
Specify the script whose value is displayed by the control.

Remarks
See Also
ExpressionBinding Element for CustomItem for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2497 -->

Frame Element for CustomItem for
Controls for View
Defines how the data is displayed, such as shifting the data to the left or right. This element is
used when defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2498 -->

None.

Child Elements

                                                                                         ﾉ   Expand table

 Element                                      Description

 CustomItem Element                           Required Element

 FirstLineHanging Element of Frame of         Optional element.
 Controls of View
                                              Specifies how many characters the first line is shifted to the
                                              left.

 FirstLineIndent Element of Frame of          Optional element.
 Controls of View
                                              Specifies how many characters the first line is shifted to the
                                              right.

 LeftIndent Element of Frame of Controls of   Optional element.
 View
                                              Specifies how many characters the data is shifted away
                                              from the left margin.

 RightIndent Element of Frame of Controls     Optional element.
 of View
                                              Specifies how many characters the data is shifted away
                                              from the right margin.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                                          Description

 CustomItem Element for CustomEntry for           Defines what data is displayed by the control and how
 Controls for View                                it is displayed.

Remarks
You cannot specify the FirstLineHanging and the FirstLineIndent elements in the same Frame
element.

See Also

<!-- p.2499 -->

FirstLineHanging Element of Frame of Controls of View

FirstLineIndent Element of Frame of Controls of View

LeftIndent Element of Frame of Controls of View

RightIndent Element of Frame of Controls of View

CustomItem Element for CustomEntry for Controls for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2500 -->

FirstLineHanging Element for Frame for
Controls for View
Specifies how many characters the first line of data is shifted to the left. This element is used
when defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2501 -->

None.

Parent Elements

                                                                                      ﾉ   Expand table

 Element                                  Description

 Frame Element for CustomItem for         Defines how the data is displayed, such as shifting the data
 Controls for View                        to the left or right.

Text Value
Specify the number of characters that you want to shift the first line of the data.

Remarks
If this element is specified, you cannot specify the FirstLineIndent element.

See Also
FirstLineIndent Element for Frame for Controls for View

Frame Element for CustomItem for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2502 -->

FirstLineIndent Element for Frame for
Controls for View
Specifies how many characters the first line of data is shifted to the right. This element is used
when defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2503 -->

None.

Parent Elements

                                                                                      ﾉ   Expand table

 Element                                  Description

 Frame Element for CustomItem for         Defines how the data is displayed, such as shifting the data
 Controls for View                        to the left or right.

Text Value
Specify the number of characters that you want to shift the first line of the data.

Remarks
If this element is specified, you cannot specify the FirstLineHanging element.

See Also
FirstLineHanging Element for Frame for Controls for View

Frame Element for CustomItem for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2504 -->

LeftIndent Element for Frame for Controls
for View
Specifies how many characters the data is shifted away from the left margin. This element is
used when defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2505 -->

None.

Parent Elements

                                                                                     ﾉ   Expand table

 Element                                 Description

 Frame Element for CustomItem for        Defines how the data is displayed, such as shifting the data
 Controls for View                       to the left or right.

Text Value
Specify the number of characters that you want to shift the data to the left.

Remarks
See Also
Frame Element for CustomItem for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2506 -->

RightIndent Element for Frame for Controls
for View
Specifies how many characters the data is shifted away from the right margin. This element is
used when defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2507 -->

None.

Parent Elements

                                                                                     ﾉ   Expand table

 Element                                 Description

 Frame Element for CustomItem for        Defines how the data is displayed, such as shifting the data
 Controls for View                       to the left or right.

Text Value
Specify the number of characters that you want to shift the data to the right.

Remarks
See Also
Frame Element for CustomItem for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2508 -->

NewLine Element for CustomItem for
Controls for View
Adds a blank line to the display of the control. This element is used when defining controls that
can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2509 -->

Parent Elements

                                                                               ﾉ   Expand table

 Element                                   Description

 CustomItem Element for CustomEntry for    Defines what data is displayed by the control and how
 Controls for View                         it is displayed.

Remarks

See Also
CustomItem Element for CustomEntry for Controls for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2510 -->

Text Element for CustomItem for Controls
for View
Specifies text that is added to the data that is displayed by the control, such as a label, brackets
to enclose the data, and spaces to indent the data. This element is used when defining controls
that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element

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

<!-- p.2511 -->

Parent Elements

                                                                                   ﾉ   Expand table

 Element                                       Description

 CustomItem Element for CustomEntry for        Defines what data is displayed by the control and how
 Controls for View                             it is displayed.

Text Value
Specify the text of a control for data that you want to display.

Remarks
See Also
CustomItem Element for CustomEntry for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2512 -->

EntrySelectedBy Element for CustomEntry
for Controls for View
Defines the .NET types that use this control definition or the condition that must exist for this
definition to be used. This element is used when defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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
   <SelectionSetName>NameofSelectionSet</SelectionSetName>
   <SelectionCondition>...</SelectionCondition>
 </EntrySelectedBy>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
EntrySelectedBy element. You must specify at least one type, selection set, or selection

condition for a definition. There is no maximum limit to the number of child elements that you
can use.

Attributes

<!-- p.2513 -->

None.

Child Elements

                                                                                           ﾉ   Expand table

 Element                                               Description

 SelectionCondition Element for EntrySelectedBy for    Optional element.
 Controls for View
                                                       Defines the condition that must exist for this
                                                       definition to be used.

 SelectionSetName Element for EntrySelectedBy for      Optional element.
 Controls for View
                                                       Specifies a set of .NET types that use this
                                                       definition of the control.

 TypeName Element for EntrySelectedBy for Controls     Optional element.
 for View
                                                       Specifies a .NET type that uses this definition of
                                                       the control.

Parent Elements

                                                                                           ﾉ   Expand table

 Element                                                              Description

 CustomEntry Element for CustomEntries for Controls for View          Provides a definition of the control.

Remarks
Selection conditions are used to define a condition that must exist for the definition to be
used, such as when an object has a specific property or when a specific property value or script
evaluates to true . For more information about selection conditions, see Defining Conditions
for when a View Entry or Item is Used.

See Also
CustomEntry Element for CustomEntries for Controls for View

Writing a PowerShell Formatting File

<!-- p.2514 -->

Last updated on 05/20/2025

<!-- p.2515 -->

SelectionCondition Element for
EntrySelectedBy for Controls for View
Defines a condition that must exist for the control definition to be used. This element is used
when defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2516 -->

Child Elements

                                                                                          ﾉ    Expand table

 Element                                                     Description

 PropertyName Element for SelectionCondition for             Optional element.
 Controls for View
                                                             Specifies a .NET property that triggers the
                                                             condition.

 ScriptBlock Element for SelectionCondition for Controls     Optional element.
 for View
                                                             Specifies the script that triggers the
                                                             condition.

 SelectionSetName Element for SelectionCondition for         Optional element.
 Controls for View
                                                             Specifies the set of .NET types that triggers
                                                             the condition.

 TypeName Element for SelectionCondition for Controls        Optional element.
 for View
                                                             Specifies a .NET type that triggers the
                                                             condition.

Parent Elements

                                                                                          ﾉ    Expand table

 Element                                  Description

 EntrySelectedBy Element for              Defines the .NET types that use this control definition or the
 CustomEntry for Controls for View        condition that must exist for this definition to be used.

Remarks
When you are defining a selection condition, the following requirements apply:

     The selection condition must specify a least one property name or a script block, but
     cannot specify both.
     The selection condition can specify any number of .NET types or selection sets, but
     cannot specify both.

<!-- p.2517 -->

For more information about how to use selection conditions, see Defining Conditions for when
Data is Displayed.

See Also
PropertyName Element for SelectionCondition for Controls for View

ScriptBlock Element for SelectionCondition for Controls for View

SelectionSetName Element for SelectionCondition for Controls for View

TypeName Element for SelectionCondition for Controls for View

EntrySelectedBy Element for CustomEntry for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2518 -->

PropertyName Element for
SelectionCondition for CustomControl for
View
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the definition is used. This element is used when
defining a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
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

<!-- p.2519 -->

Child Elements
None.

Parent Elements

                                                                                      ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the
 CustomControl for View                               control definition to be used.

Text Value
Specify the .NET property name.

Remarks
The selection condition must specify a least one property name or a script, but cannot specify
both. For more information about how selection conditions can be used, see Defining
Conditions for Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for CustomControl for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2520 -->

ScriptBlock Element for SelectionCondition
for CustomControl for View
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the definition is used. This element is used when defining a custom
control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
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
