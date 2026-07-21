# Slide Script: OT Machine Tagging → Enterprise Data Model
*Audience: Global IT (no factory-floor context). Purpose: build the case for scale and the pipeline's value, and quietly surface the access dependency without asking for it outright on-slide.*
*Paste this into Claude (or your slide tool of choice) as source material for slide design.*

---

## Slide 1 — Title
**Headline:** Building the Data Foundation for [Enterprise Data Model Initiative Name]
**Subhead:** Turning factory floor equipment documentation into structured, machine-readable data

**Script:** This work is the groundwork for the larger enterprise data model — specifically, the layer that connects physical equipment on the factory floor to the tag data our historian systems already collect. I want to walk through the scale of that problem, the approach we're taking, and where things stand.

---

## Slide 2 — Why This Matters Beyond the Factory Floor
**Headline:** This is the source-data layer for the enterprise data model
**Content bullets:**
- The enterprise data model needs a reliable way to know what a tag *is* — what machine, what station, what parameter it belongs to
- That mapping doesn't exist today in any structured, centralized form
- This project builds that layer once, so every downstream analytics/reporting effort can build on it rather than re-deriving it
- Get this foundation right, and it's reusable across every site — not a one-off for a single line

**Script:** Global IT doesn't need to care about factory floor logistics for its own sake — but the data model absolutely depends on having this layer solved. Right now that layer is missing, which is the gap this work closes.

---

## Slide 3 — A Quick Translation Layer
**Headline:** Factory floor terms, in IT terms you already know
**Content bullets:**
- **Site** → think data center (a physical facility)
- **Line** → a rack — a group of related equipment working together
- **Machine** → a physical server — a discrete piece of equipment
- **Station** → a component within that machine (a specific process step)
- **Tag** → a monitored metric, like CPU temp or memory usage — a single data point collected continuously by our historian system (Ignition)

**Script:** Since most of this audience has never been on a production floor, it's worth a quick translation: a tag is conceptually the same as any telemetry metric you already monitor — it just happens to be attached to a piece of manufacturing equipment instead of a server.

---

## Slide 4 — The Scale
**Headline:** This isn't a handful of machines — it's an enterprise-wide structure
**Content bullets:**
- [4+] sites currently in scope (Ballina, Bawal, Kaunas, Stuarts Draft), more to follow
- [48] production lines across those sites
- Each line has multiple machines, each machine multiple stations, each station multiple monitored parameters
- Every parameter maps to one or more historian tags — easily thousands of tags enterprise-wide
- Source documentation: 30+ equipment manuals per site, none in a standardized format

**Script:** The reason this needs to be solved with a pipeline rather than a spreadsheet is scale. Multiply sites by lines by machines by stations by parameters, and you get an enterprise-wide dataset that no team can maintain by hand — and that number only grows as more sites come online.

---

## Slide 5 — The Problem With Today's State
**Headline:** Tag data and equipment data don't speak to each other
**Content bullets:**
- Historian tag exports are flat lists — a tag ID with no equipment context
- Equipment context lives only in unstructured PDF manuals, scattered per line
- Connecting the two today means a person manually opening manuals and cross-referencing tag IDs
- Not standardized, not repeatable, doesn't scale past a handful of lines — and breaks the moment a new site is added

**Script:** Today, if someone wants to know what physical equipment a given tag belongs to, there's no shortcut — someone has to go find the manual and read it. That's fine for one line. It falls apart completely at enterprise scale.

---

## Slide 6 — The Solution: A Repeatable Extraction Pipeline
**Headline:** One pipeline, built once, scales to every site
**Content bullets:**
- Automated pipeline reads equipment manuals and extracts the machine → station → parameter hierarchy
- Cross-references that structure against real historian tag exports
- Populates a standardized data model (Lines / Machines / Stations / Parameters)
- Same logic applies to every site — this is infrastructure, not a one-time cleanup effort

**Script:** The design goal here wasn't to solve this for one line — it was to build something that solves it permanently, for every site, going forward. That's what makes this a data-model asset rather than a one-off project.

---

## Slide 7 — Proof of Feasibility
**Headline:** The hard technical problems are already solved
**Content bullets:**
- ~40% of source manuals were scanned images with no extractable text — solved with an OCR fallback integrated directly into the pipeline
- Built and deployed on a standard managed workstation, no elevated access required
- [X] of 48 lines already validated end-to-end against real historian data
- Cost to run is measured and predictable, not speculative

**Script:** This isn't a proposal — it's a pipeline that already works against real data, including the messy cases like scanned documentation. The remaining work is scaling it up, not proving it's possible.

---

## Slide 8 — Where This Stands Today
**Headline:** Current phase: data gathering and validation
**Content bullets:**
- Consolidating equipment manuals and historian tag exports across all in-scope sites
- Extraction logic validated on the lines with readable documentation
- Standardized output model built and ready to receive full-site data
- Next phase: run the pipeline at full scale across all sites

**Script:** We're at the stage of making sure every site's source data is gathered and consistent before running this at full volume — that groundwork determines how clean the resulting data model is.

---

## Slide 9 — What Moves This to the Next Phase
**Headline:** Dependencies to move from validation to full-scale pilot
**Content bullets:**
- Confirmation of the right access pathway for automated, high-volume model usage — this workload is programmatic/batch, distinct from interactive chat tools
- Data governance alignment for automated processing of equipment documentation
- Continued IT support for lightweight tooling (OCR) on managed endpoints

**Script:** *(Say this part live — keep it factual and low-key rather than a direct ask.)* To move from validating on individual lines to running this across the full site network, a few things need to line up — chief among them, making sure the model-access pathway matches how this workload actually runs: continuous, automated, batch processing rather than a person typing into a chat window. That's an infrastructure/procurement question more than a research one at this point, and I'd welcome guidance on the right way to route it.

---

## Slide 10 — Takeaways
**Headline:** A one-time investment that scales enterprise-wide
**Content bullets:**
- The mapping between physical equipment and tag data doesn't exist today — this project builds it
- Built to scale across every site, not just the lines currently in scope
- Core technical risks (bad scans, tooling constraints) already resolved
- This becomes the foundation the broader data model initiative builds on

**Script:** The headline is simple: this is infrastructure. Once built, it doesn't need to be rebuilt per site — every new line or site that comes online benefits from the same pipeline, and the enterprise data model gets a reliable foundation it doesn't have today.

---

### Notes for you (not slide content)
- **On the API key ask:** I deliberately kept Slide 9 factual and structural ("access pathway for automated/batch usage") rather than personal ("I need my own key on my own billing"). Don't put the billing/personal-ownership framing on the slide at all — if IT asks a follow-up question live (e.g. "so what do you need from us specifically"), that's your opening to say the pipeline needs API-level (Console) access provisioned for this workload, and ask who owns that decision. Let them ask "what does that look like" rather than you volunteering "put it on my card."
- Replace bracketed placeholders (`[4+]`, `[48]`, `[X] of 48`, initiative name) with current numbers before presenting — verify against your latest run counts.
- Slide 3 (translation layer) is the one most worth spending live time on — if this audience doesn't grasp what a "tag" is in the first two minutes, the scale argument in Slide 4 won't land.
- Consider a live demo or screenshot of the output Excel model (Lines/Machines/Stations/Parameters) after Slide 6 — a concrete artifact will do more for IT credibility than any bullet list.
