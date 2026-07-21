"""
Example: OT Asset Discovery using Claude Agent Pattern
This demonstrates how the same workflow would work with Claude agents
instead of direct orchestration. Use this as a learning reference.

Key difference: Claude decides WHAT to do and in WHAT ORDER.
You provide tools; Claude calls them autonomously.
"""

import json
import fitz
from pathlib import Path
from anthropic import Anthropic
import Schema


# =============================================================================
# DEFINE TOOLS (What Claude can call)
# =============================================================================

tools = [
    {
        "name": "extract_machines_from_pdf",
        "description": "Extract machine and line metadata from PDF documentation using Claude's structured extraction capabilities.",
        "input_schema": {
            "type": "object",
            "properties": {
                "pdf_text": {
                    "type": "string",
                    "description": "The extracted text from the PDF (first 15 pages)"
                },
                "site": {
                    "type": "string",
                    "description": "Site name (e.g., Ballina, Kaunas)"
                },
                "area": {
                    "type": "string",
                    "description": "Area name (Ostomy or Continence)"
                },
                "line": {
                    "type": "string",
                    "description": "Line ID (e.g., PS1)"
                }
            },
            "required": ["pdf_text", "site", "area", "line"]
        }
    },
    {
        "name": "extract_stations_for_machine",
        "description": "Extract station details from documentation for a specific machine.",
        "input_schema": {
            "type": "object",
            "properties": {
                "machine_text": {
                    "type": "string",
                    "description": "The relevant text sections describing this machine"
                },
                "machine_name": {
                    "type": "string",
                    "description": "Name of the machine (e.g., Post Puncher)"
                },
                "machine_id": {
                    "type": "string",
                    "description": "Machine ID (e.g., MC001)"
                }
            },
            "required": ["machine_text", "machine_name", "machine_id"]
        }
    },
    {
        "name": "map_stations_to_tags",
        "description": "Match discovered stations against the tags.json file to create tag mappings.",
        "input_schema": {
            "type": "object",
            "properties": {
                "stations_json": {
                    "type": "string",
                    "description": "JSON string of discovered stations"
                },
                "tags_json_path": {
                    "type": "string",
                    "description": "Path to the tags.json file"
                }
            },
            "required": ["stations_json", "tags_json_path"]
        }
    },
    {
        "name": "write_to_excel",
        "description": "Write extracted machines and stations to the Excel workbook.",
        "input_schema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "string",
                    "description": "JSON string containing lines, machines, and stations to write"
                },
                "excel_path": {
                    "type": "string",
                    "description": "Path to the Excel file"
                }
            },
            "required": ["data", "excel_path"]
        }
    }
]


# =============================================================================
# IMPLEMENT TOOLS (The actual functions Claude calls)
# =============================================================================

def extract_machines_from_pdf(pdf_text: str, site: str, area: str, line: str) -> dict:
    """
    Call Claude with extraction prompt to get machines.
    In a real implementation, this would return structured discovery data.
    """
    client = Anthropic()

    prompt = f"""
    You are a specialized Operational Technology (OT) asset discovery engine.
    Extract the line metadata and machines from this documentation.

    Site: {site}
    Area: {area}
    Line: {line}

    Return JSON with:
    - line_metadata: {{Description, OEM_Manufacturer, Install_Date}}
    - machines: [{{MachineName, Equipment_Type, Serial_Number, Position_In_Line, OEM_Contact, PLC_Make, start_page, end_page}}]
    """

    response = client.messages.create(
        model="claude-opus-4-1",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\nDocumentation:\n{pdf_text[:5000]}"
            }
        ]
    )

    # Parse response
    result = response.content[0].text
    return {"status": "success", "machines": result}


def extract_stations_for_machine(machine_text: str, machine_name: str, machine_id: str) -> dict:
    """
    Extract stations for a specific machine.
    """
    client = Anthropic()

    prompt = f"""
    Extract all stations/sub-assemblies from this {machine_name} documentation.

    Return JSON array with:
    - StationID: unique identifier
    - StationName: official name
    - Station_Type: functional type (Turret, Vision Inspection, Sealing, Transfer, etc.)
    - ISA95_Level: control level
    - Status: operational status
    - start_page, end_page: where documented
    """

    response = client.messages.create(
        model="claude-opus-4-1",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\nDocumentation:\n{machine_text}"
            }
        ]
    )

    result = response.content[0].text
    return {"status": "success", "stations": result, "machine_id": machine_id}


def map_stations_to_tags(stations_json: str, tags_json_path: str) -> dict:
    """
    Match extracted stations to tags.json entries.
    """
    try:
        with open(tags_json_path, 'r') as f:
            tags = json.load(f)

        # In real implementation, use fuzzy matching or Claude to map stations to tags
        return {"status": "success", "mappings": "mapping logic here"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def write_to_excel(data: str, excel_path: str) -> dict:
    """
    Write results to Excel.
    """
    # In real implementation, use openpyxl to write to Excel
    return {"status": "success", "message": f"Would write to {excel_path}"}


# =============================================================================
# AGENT LOOP (Claude autonomously calls tools)
# =============================================================================

def run_agent(pdf_path: str, site: str, area: str, line: str):
    """
    Main agent loop. Claude reasons about what to do and calls tools.
    """
    client = Anthropic()

    # Extract PDF text
    with fitz.open(pdf_path) as doc:
        pdf_text = ""
        for page in doc[:15]:
            pdf_text += page.get_text()

    # Initial message to agent
    messages = [
        {
            "role": "user",
            "content": f"""
            Process this production line documentation and extract the complete asset inventory.

            PDF: {pdf_path}
            Site: {site}
            Area: {area}
            Line: {line}

            Steps:
            1. Extract machines and line metadata
            2. For each machine found, extract its stations
            3. Map stations to tags.json
            4. Write results to Excel
            5. Report what you found
            """
        }
    ]

    # Agentic loop
    while True:
        # Claude decides what to do next
        response = client.messages.create(
            model="claude-opus-4-1",
            max_tokens=4096,
            tools=tools,
            messages=messages
        )

        # Check if Claude is done
        if response.stop_reason == "end_turn":
            # Extract final response
            final_text = [block.text for block in response.content if hasattr(block, 'text')]
            print("Agent completed:", final_text)
            return

        # Claude called tools—execute them
        if response.stop_reason == "tool_use":
            # Collect tool results
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input

                    print(f"🔧 Agent calling: {tool_name}")

                    # Execute the right tool
                    if tool_name == "extract_machines_from_pdf":
                        result = extract_machines_from_pdf(**tool_input)
                    elif tool_name == "extract_stations_for_machine":
                        result = extract_stations_for_machine(**tool_input)
                    elif tool_name == "map_stations_to_tags":
                        result = map_stations_to_tags(**tool_input)
                    elif tool_name == "write_to_excel":
                        result = write_to_excel(**tool_input)
                    else:
                        result = {"error": f"Unknown tool: {tool_name}"}

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result)
                    })

            # Feed tool results back to Claude
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == '__main__':
    # Example: process a production line
    pdf_path = "Ballina/Continence/PS1/some_manual.pdf"

    if Path(pdf_path).exists():
        run_agent(
            pdf_path=pdf_path,
            site="Ballina",
            area="Continence",
            line="PS1"
        )
    else:
        print("Example PDF not found. This demonstrates the agent pattern.")
        print("\nKey concepts:")
        print("1. You define TOOLS (what Claude can do)")
        print("2. You set a GOAL (what Claude should accomplish)")
        print("3. Claude REASONS about the goal and decides which tools to call")
        print("4. You EXECUTE the tools and feed results back")
        print("5. Claude continues until the goal is achieved")
        print("\nBenefits over direct scripting:")
        print("- Claude can handle multi-step workflows autonomously")
        print("- Claude can parallelize (e.g., extract stations for all machines)")
        print("- Claude can retry/adapt if extraction confidence is low")
        print("- Less orchestration code you have to write")
