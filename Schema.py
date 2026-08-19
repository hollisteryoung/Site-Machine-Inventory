from pydantic import BaseModel, Field
from typing import Dict, List, Optional

# ==============================================================================
# 1. DATABASE ROW TARGET SCHEMAS (For writing rows to Excel)
# ==============================================================================

class StationRow(BaseModel):
    StationID: str = Field(description=(
        "Globally unique storage key, formatted '<MachineID>-<raw station code or descriptive name>' "
        "(e.g., 'MC002-MainDial'). The MachineID prefix is required because raw station identifiers "
        "(numeric PLC codes or descriptive names alike) are not guaranteed unique across machines - "
        "cloned/replicated machine models (e.g. multiple lines running the same equipment model) "
        "commonly reuse the same internal station numbering or naming convention. Composed by the "
        "pipeline in LineProcess.py, not by the discovery model - see DiscoveredStation.StationID."
    ))
    StationName: str = Field(description="The official name of the station assembly, e.g., Eye Punching.")
    MachineID: str = Field(description="The Foreign Key identifying which physical machine framework this station belongs to.")
    Station_Type: str = Field(description="The functional/operational type of the station (e.g., Turret, Vision Inspection, Sealing, Transfer, Funnel, Cooling, Pressure Gauge).")
    ISA95_Level: str = Field(default="L2", description="ISA95 control layer level, defaults to 'L2'.")
    Status: str = Field(default="Active", description="Operational status, defaults to 'Active'.")

class StationInventory(BaseModel):
    stations: List[StationRow]


class ParameterRow(BaseModel):
    ParameterID: str = Field(description="Unique identifier for this parameter (e.g., PR0001).")
    ParameterName: str = Field(description="The name of the parameter (e.g., Cap Torque, Vision Reject Count).")
    StationID: str = Field(description="Foreign Key linking to the station this parameter belongs to.")
    Unit_of_Measure: str = Field(default="", description="Unit of measurement (e.g., Nm, bar, °C, %).")
    Data_Type: str = Field(default="", description="Data type (e.g., Float, Integer, Boolean).")
    Min_Threshold: Optional[str] = Field(default=None, description="Historian_Tag path of the tag that holds this parameter's live low-limit value, if one exists (e.g., NGP2/LN001/MC001/ST002/CapTorque_LoLimit). Not a literal number - the limit is operator/PLC-adjustable, so only a pointer to the live tag stays accurate.")
    Max_Threshold: Optional[str] = Field(default=None, description="Historian_Tag path of the tag that holds this parameter's live high-limit value, if one exists. See Min_Threshold.")
    Target_Threshold: Optional[str] = Field(default=None, description="Historian_Tag path of the tag that holds this parameter's live target/setpoint value, if one exists. See Min_Threshold.")
    Historian_Tag: str = Field(default="", description="The OT system tag path (e.g., NGP2/LN001/MC001/ST002/CapTorque).")

class ParameterInventory(BaseModel):
    parameters: List[ParameterRow]


class MachineRow(BaseModel):
    MachineID: str = Field(description="The unique identifier tracking sequence, e.g., MC002.")
    MachineName: str = Field(description="The official name of the physical machine unit, e.g., Post Puncher, Tooling Sleever.")
    LineID: str = Field(description="The Foreign Key matching the stable LineID this machine belongs to (e.g., PS1).")
    Equipment_Type: str = Field(description="The technical classification or role of the machine unit (e.g., Puncher, Sleever, Feeder, Vision Inspection System, Conveyor).")
    Serial_Number: str = Field(default="Unknown", description="Serial number of the physical machine framework.")
    Position_In_Line: str = Field(default="0", description="The sequential position the machine occupies in the production line flow (e.g., '1', '2', '3'). Use '0' if position cannot be determined from documentation. Note: some lines may contain only a single machine.")
    OEM_Contact: str = Field(default="Unknown", description="Vendor support line or specialist contact information.")
    PLC_Make: str = Field(default="Unknown", description="The hardware controller vendor responsible for the PLC (e.g., Siemens, Allen-Bradley).")
    PLC_Credentials_Status: str = Field(default="", description="Backup credentials audit flag; defaults to blank.")

class MachineInventory(BaseModel):
    machines: List[MachineRow]    


class LineRow(BaseModel):
    LineID: str = Field(description="The unique system identifier, e.g., HU3, PS1 parsed from folder structures.")
    LineName: str = Field(description="The full descriptive identifying name of the production line, e.g., 'HU3 Assembly Line'.")
    Site: str = Field(description="The geographic manufacturing plant location parsed from tagpaths (e.g., 'Ballina', 'Kaunas').")
    Area: str = Field(description="The functional product manufacturing department. Must strictly map to 'Ostomy' or 'Continence'.")
    Description: str = Field(default="", description="A brief summary describing the overall workflow or purpose of the production line.")
    OEM_Manufacturer: str = Field(description="The primary engineering vendor or system integrator responsible for building the line cell.")
    Install_Date: str = Field(default="", description="The original physical installation or site validation release date.")    

class LineInventory(BaseModel):
    lines: List[LineRow]    


# ==============================================================================
# 2. LLM EXTRACTION LAYER SCHEMAS (For Unified Pydantic Discovery Outputs)
# ==============================================================================

class LineMetadata(BaseModel):
    Description: Optional[str] = Field(description="Short description of the overall line purpose.")
    OEM_Manufacturer: Optional[str] = Field(description="The vendor/integrator responsible for the line.")
    Install_Date: Optional[str] = Field(description="The installation or manual release date if found.")

class DiscoveredMachine(BaseModel):
    MachineName: str = Field(
        description=(
            "The macro-level official name of the entire machine unit system (e.g., 'Post Puncher'). "
            "CRITICAL: Do NOT create separate machine entries for internal sub-stations, modular zones, "
            "or station sequences (e.g., do NOT extract 'Station 1001 - Rotary Turret' as a machine)."
        )
    )
    Equipment_Type: str = Field(description="The technical classification or role (e.g., Puncher, Sleever, Feeder, Vision Inspection System, Conveyor).")
    Serial_Number: str = Field(default="Unknown", description="Serial number of the macro machine unit.")
    Position_In_Line: str = Field(
        default="0",
        description=(
            "The sequential position this machine occupies on the production line (e.g., '1' for first, '2' for downstream, etc.). "
            "Analyze the operational sequence text, material transport descriptions, and references to "
            "'upstream', 'downstream', 'infeed', and 'outfeed' to establish the chronological equipment order. "
            "Use '0' if position cannot be determined."
        )
    ),
    start_page: Optional[int] = Field(
        default=None,
        description=(
            "The GLOBAL_PAGE number (not the per-document page number) where this machine's "
            "documentation begins, as marked by the '===== DOCUMENT: ... | GLOBAL_PAGE n =====' "
            "headers in the source text, since a single line may be documented across multiple PDFs."
        )
    )
    end_page: Optional[int] = Field(
        default=None,
        description="The GLOBAL_PAGE number where this machine's documentation ends (see start_page)."
    )
    OEM_Contact: str = Field(default="Unknown", description="Manufacturer support contact details.")
    PLC_Make: str = Field(default="Unknown", description="The master PLC vendor controlling the entire unit.")

class DiscoveredStation(BaseModel):
    StationID: str = Field(
        description=(
            "The raw identifier as it appears in the documentation for THIS machine only (e.g., 'St1015', "
            "'1001', 'Turret1'). Extract the station number or identifier as it appears in control logic, "
            "PLC programming, electrical schematics, or operation manuals. NOT all stations have a clean "
            "numeric or alphanumeric PLC-style code — some are only ever referred to by a descriptive/module "
            "name (e.g., 'Module A', 'Infeed Turret Assembly'). In that case, use the descriptive name itself "
            "as the StationID rather than inventing a numeric code that isn't documented. Do not worry about "
            "uniqueness across other machines or lines - this value only needs to be unique within this "
            "machine's own set of stations; the pipeline namespaces it with the MachineID before storage "
            "(see StationRow.StationID) since equipment models are frequently cloned across multiple lines "
            "with identical internal station numbering/naming."
        )
    )
    StationName: str = Field(
        description=(
            "The official name of the station assembly as documented (e.g., 'Eye Punching', 'Rotary Turret', "
            "'Vision Inspection', 'Long Seal', 'Position Verification'). "
            "Extract the exact designation used in the equipment documentation."
        )
    )
    Station_Type: str = Field(
        description=(
            "The functional/operational classification inferred from the station's role in the process. "
            "Examples: 'Turret' (rotary positioning station), 'Vision Inspection' (quality/detection station), "
            "'Sealing' (thermal/pressure sealing operation), 'Transfer' (material movement/conveyor), "
            "'Funnel' (feeding/infeed mechanism), 'Cooling' (thermal regulation), 'Pressure Gauge' (measurement). "
            "Do NOT use generic defaults like 'Process'—infer the specific operational function from the documentation."
        )
    )
    ISA95_Level: str = Field(
        default="L2",
        description="ISA95 automation hierarchy level (e.g., 'L2' for Equipment Control, 'L3' for Area Supervision). Default to 'L2' if not determinable."
    )
    Status: str = Field(
        default="Active",
        description="Operational status (e.g., 'Active', 'Maintenance', 'Decommissioned'). Default to 'Active' if not specified."
    )
    start_page: Optional[int] = Field(
        default=None,
        description="The start page in the documentation where this station is described."
    )
    end_page: Optional[int] = Field(
        default=None,
        description="The end page in the documentation where this station is described."
    )

class UnifiedDiscoveryPayload(BaseModel):
    line_metadata: LineMetadata
    machines: List[DiscoveredMachine]

class StationDiscoveryPayload(BaseModel):
    stations: List[DiscoveredStation]


class MatchedParameter(BaseModel):
    ParameterName: str = Field(description="Descriptive name of the parameter derived from the tag name.")
    Historian_Tag: str = Field(description="The OPC/historian tag path this parameter reads from.")
    Unit_of_Measure: str = Field(default="", description="Inferred unit of measure, blank if not inferable.")
    Unit_Verified: bool = Field(
        default=False,
        description=(
            "True ONLY if this unit is explicitly stated somewhere in the source documentation or tag "
            "data itself (e.g. a literal '°C', 'PSI', 'bar' string in a tag comment or manual). False if "
            "it was inferred from the tag/parameter name's naming convention or general engineering "
            "plausibility - which is the common case, since most historian exports don't state units "
            "explicitly. Default to False when unsure; do not mark True on a guess just because it seems "
            "plausible. IMPORTANT: if the same physical measurement appears under more than one tag (e.g. "
            "a raw/internal '_REAL' representation and a separate '_DISPLAY' representation of the same "
            "signal), assume they share the same real-world unit and give them the SAME Unit_of_Measure - "
            "do not invent a different guessed unit for each one, since a control loop's internal value "
            "and its HMI display for the same signal are essentially always the same physical unit unless "
            "the documentation explicitly shows a scaling/conversion between them."
        ),
    )
    Data_Type: str = Field(default="", description="Inferred data type (Float, Integer, Boolean, String), blank if not inferable.")
    Min_Threshold: Optional[str] = Field(
        default=None,
        description=(
            "Historian_Tag path of another candidate in THIS SAME candidate list that is a naming-convention "
            "low-limit companion to this parameter (e.g. this parameter is 'CapTorque' and a candidate named "
            "'CapTorque_Min'/'CapTorque_LoLimit'/'CapTorque_LL' exists). When set, that companion tag must NOT "
            "also be returned as its own separate match entry - it is folded in here instead. Leave null if no "
            "such companion tag exists in the candidate list."
        ),
    )
    Max_Threshold: Optional[str] = Field(
        default=None,
        description="Historian_Tag path of a naming-convention high-limit companion candidate (e.g. '_Max'/'_HiLimit'/'_HH'). See Min_Threshold - same folding rule applies.",
    )
    Target_Threshold: Optional[str] = Field(
        default=None,
        description="Historian_Tag path of a naming-convention target/setpoint companion candidate (e.g. '_Target'/'_SP'). See Min_Threshold - same folding rule applies.",
    )
    Confidence: float = Field(default=1.0, description="Confidence 0.0-1.0 that this tag genuinely belongs to the station.")

class ParameterMatchPayload(BaseModel):
    matches: List[MatchedParameter]


# ==============================================================================
# 3. TAG SOURCE PROFILE (discovery of the tag export's own conventions)
# ==============================================================================
# Historian/PLC tag exports differ not just in FILE FORMAT (which a reader handles)
# but in NAMING CONVENTION - and the convention is what actually decides whether a
# tag can be attributed to a station. Observed across this site alone:
#   - K9/K10 (WinCC):    station code sits literally in the tag name ('DB_02UWS_...')
#   - NGP2 (Ignition):   station number is TRUNCATED in the tag ('2057' -> 'St057'),
#                        and every path shares a structural root ('Application')
#   - HF11 (WinCC):      tags carry only opaque module codes ('AG03', 'SIKO') with no
#                        descriptive text anywhere, needing an external legend
#   - 1AC3 (RSLogix):    tag names are opaque ('DRV02', 'MAN01', 'R2') but a populated
#                        DESCRIPTION column names the station in plain English, AND a
#                        code->description legend is derivable from the file itself
# Hardcoding each of those as its own branch is what this profile replaces: discover
# the convention once per line, then let ONE matcher be parameterized by it.
class TagSourceProfile(BaseModel):
    station_identity_fields: List[str] = Field(
        default_factory=lambda: ["tag_path", "name", "description"],
        description=(
            "Which normalized TagRecord fields actually carry station identity for THIS export, "
            "most reliable first. Valid values: 'tag_path', 'name', 'description', 'context'. "
            "E.g. an RSLogix export whose tag names are opaque drive codes but whose DESCRIPTION "
            "column names the station would rank 'description' first."
        ),
    )
    station_code_style: str = Field(
        default="mixed",
        description=(
            "How station identity is encoded: 'descriptive_words' (station's real name/abbreviation "
            "appears as text), 'numeric_coded' (a numeric station code appears, e.g. St1015), "
            "'opaque_module_code' (only an internal code like AG03/DRV02 with no descriptive text), "
            "'mixed', or 'absent' (no station attribution is recoverable from this export at all)."
        ),
    )
    numeric_tag_pattern: Optional[str] = Field(
        default=None,
        description=(
            "Regex with exactly ONE capture group that extracts a numeric station code from a tag, "
            r"e.g. 'st(\\d+)'. Matched case-insensitively. Null if this export uses no numeric codes."
        ),
    )
    numeric_truncated_digits: int = Field(
        default=0,
        description=(
            "How many leading digits the export drops from the documented station number. 0 = the tag "
            "carries the full number. 1 = station '2057' appears as 'St057' (seen on NGP2). Used to "
            "allow a right-aligned suffix match at exactly the documented width minus this value, "
            "rather than a loose 'endswith' that collides across station ranges."
        ),
    )
    segment_delimiters: List[str] = Field(
        default_factory=lambda: ["_", ".", ":"],
        description="Characters that separate meaningful segments in a tag name for this export.",
    )
    structural_tokens: List[str] = Field(
        default_factory=list,
        description=(
            "Lowercase words that are part of the export's own scaffolding rather than any station's "
            "identity - PLC program/folder roots, HMI screen-group names, array wrappers (e.g. "
            "'application', 'tmphmic5', 'var', 'data'). Never keyword-matched on, because they appear "
            "in most or all tags and would flood any station whose name happens to share the word."
        ),
    )
    description_populated: bool = Field(
        default=False,
        description="True if a meaningful share of tags carry descriptive text worth matching against.",
    )
    inline_code_legend: Dict[str, str] = Field(
        default_factory=dict,
        description=(
            "Opaque code -> plain-English description, DERIVED FROM THIS EXPORT ITSELF where the file "
            "makes it recoverable (e.g. RSLogix module tag 'DRV02' whose DESCRIPTION reads 'BARRIER "
            "INFEED MAGAZINE SERVO'). Serves the same role as an external Tag_Code_Legend.csv but "
            "without needing an engineer to supply it. Merged with any external legend at match time."
        ),
    )
    hmi_exposure_marker: Optional[str] = Field(
        default=None,
        description=(
            "Regex identifying tags that are already wired to an operator HMI screen, if the export "
            "distinguishes them (e.g. RSLogix ALIAS rows / 'HMI PUSH BUTTON'|'HMI ANIMATION' description "
            "prefixes). Lets the report separate 'already monitored on the HMI' from 'exists in the PLC "
            "but is not displayed anywhere' - the latter being what this pipeline adds over reading an HMI."
        ),
    )
    coverage_note: str = Field(
        default="",
        description=(
            "Plain-English note on what this export does and does not cover, for the match report - e.g. "
            "'controller export for the 1-piece bag configuration only; insert/drumhead stations are not "
            "present in this file at all'. Prevents a genuine scope limit being misread as a match failure."
        ),
    )


class TagSourceProfilePayload(BaseModel):
    profile: TagSourceProfile