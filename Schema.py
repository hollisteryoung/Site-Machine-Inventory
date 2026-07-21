from pydantic import BaseModel, Field
from typing import List, Optional

# ==============================================================================
# 1. DATABASE ROW TARGET SCHEMAS (For writing rows to Excel)
# ==============================================================================

class StationRow(BaseModel):
    StationID: str = Field(description="The unique identifier, e.g., ST1015 based on the station number.")
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
    Min_Threshold: Optional[float] = Field(default=None, description="Minimum acceptable threshold for this parameter.")
    Max_Threshold: Optional[float] = Field(default=None, description="Maximum acceptable threshold for this parameter.")
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
            "The unique identifier extracted from the documentation (e.g., 'St1015', '1001', 'Turret1'). "
            "Extract the station number or identifier as it appears in control logic, PLC programming, "
            "electrical schematics, or operation manuals. NOT all stations have a clean numeric or "
            "alphanumeric PLC-style code — some are only ever referred to by a descriptive/module name "
            "(e.g., 'Module A', 'Infeed Turret Assembly'). In that case, use the descriptive name itself "
            "as the StationID rather than inventing a numeric code that isn't documented."
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
    Data_Type: str = Field(default="", description="Inferred data type (Float, Integer, Boolean, String), blank if not inferable.")
    Confidence: float = Field(default=1.0, description="Confidence 0.0-1.0 that this tag genuinely belongs to the station.")

class ParameterMatchPayload(BaseModel):
    matches: List[MatchedParameter]