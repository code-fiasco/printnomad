# PrintNomad

PrintNomad converts a 3MF project made for one printer (usually a Bambu Lab printer on MakerWorld) into a project for the user's own printer and slicer, keeping the designer's changes.

## Projects and models

**Project**:
A 3MF file, either the one being converted (source project) or the one produced (converted project).
_Avoid_: model, file (when the 3MF is meant)

**Model**:
A listing on MakerWorld: its page, designer and print profiles.
_Avoid_: project, the model's values

**Meshes**:
The geometry inside a project.
_Avoid_: model

**Plate**:
One arrangement sheet in a project, with its objects and its assignment.
_Avoid_: bed, build plate

**Designer change**:
A process or filament setting the project marks as changed and whose value differs from the preset the designer started from; when that preset is unavailable, the mark alone counts.
_Avoid_: model's values, designer settings, overrides

**Leftover**:
A value in the source project only because the designer's preset set it, not because the designer changed it; it is removed so the slicer's own defaults apply.
_Avoid_: factory value, default

**Object override**:
A setting attached to one object or part of a project, taking precedence over the plate's settings.
_Avoid_: override (alone)

**Source slicer**:
The slicer that saved the source project: Bambu Studio or an Orca-based slicer, or PrusaSlicer, whose projects mark no changes, so a fixed set of its process settings counts as designer changes.

## Printers

**Printer**:
An entry in *My printers*: a machine preset, the slicer it is converted for, and its build plate.
_Avoid_: machine, device

**Target**:
The printer a given conversion or review is for.
_Avoid_: destination

**Target slicer**:
The slicer a printer is converted for: the brand's own slicer when it has one, otherwise OrcaSlicer, unless the user picks another.

**Printer setting**:
A process setting that describes the machine rather than the print (accelerations, calibration, arc fitting, G-code file name, cooling); it comes from the target unless the user opts to keep the designer's.
_Avoid_: machine setting, hardware setting

**Chip**:
The button for one of the user's printers that PrintNomad adds next to MakerWorld's own printers on a model page.

**Build plate**:
The bed surface type chosen for a printer, such as Cool Plate or SuperTack.
_Avoid_: plate, bed type

**Bed**:
The printer's physical bed: its size and shape.
_Avoid_: plate

**Extruder**:
One print head or nozzle path of a printer.
_Avoid_: tool, slot, head

## Filaments

**Filament**:
One filament entry in a project, with a colour, a type and a preset.
_Avoid_: colour, slot

**Assignment**:
Which extruder prints each filament, per plate.
_Avoid_: map, mapping

**Assignment mode**:
*Compatible* (the slicer chooses extruders automatically), *Exact* (the planned assignment is enforced manually), or *By slicer* (Exact when the target slicer accepts it, otherwise Compatible).
_Avoid_: map mode, Auto/Manual, slicer decides

## Presets and profiles

**Preset**:
One named set of slicer settings of one kind: machine, process or filament.
_Avoid_: profile (for a single preset)

**Machine preset**:
The preset that describes a printer's hardware.
_Avoid_: printer profile, machine profile

**Profiles**:
All of one vendor's presets from one slicer release.
_Avoid_: presets (for the whole set)

**Profile bundle**:
The packaged form of a vendor's profiles that the extension uses.

**Catalog**:
The set of profile bundles CI builds every week from the slicers' latest releases and publishes online.

**Shipped copy**:
The profile bundles included in the extension itself.

## Outcomes

**Conversion**:
Turning a source project into a project for the target.
_Avoid_: export, port

**Review**:
Checking a project that already targets the user's printer and fixing only what would stop it slicing.
_Avoid_: repair, fix

**Report**:
The record of every value a conversion or review replaced, kept, removed or warned about, in text and JSON.
_Avoid_: log, summary

**Error code**:
A stable `PNxxx` code naming what failed, at which stage, and what the user can try.
_Avoid_: issue
