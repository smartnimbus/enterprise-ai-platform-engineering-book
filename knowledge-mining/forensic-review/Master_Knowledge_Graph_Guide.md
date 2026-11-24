# Master Knowledge Graph — how to read and use it

The source-derived register contains **86 curated concepts**, distributed across eight distinct project identifiers plus one intentionally duplicated Estate Pulse package. The graph contains **255 nodes and 1,009 directed edges**; these are relationships for editorial traceability, not evidence that historical diagrams themselves were implemented.

## Graph schema

```text
Project (source family)
  └─contains→ Concept (IA-###)
       └─instantiates→ Pattern (controlled thematic label)
            └─informs→ Decision (existing D-01..D-30)
                 └─governed_area→ Architecture (frozen 4L or 8P)
                      └─context_for→ Chapter (frozen 1..58)
                           └─cross_references→ AtlasPage (existing D-###)
```

Additional `Pattern → Chapter`, `Pattern → Architecture`, and `Decision → Chapter` links preserve direct mappings. `Decision → AtlasPage` is one-to-one and does not create a decision or alter its default. Every `Concept` source, line and SHA-256 is in the Intellectual Asset Register; direct source links were not copied as graph nodes to keep the GraphML manageable.

## Three important traversals

**Security enforcement lineage:** `AEGIS → Interceptable cognition → pre-action-governance → D-10 / D-18 → Eight Control Planes → Chapter 16 → D-10/D-18 AtlasPage`. Similar paths exist from UAF GovernanceGuard, Kollab hooks and workshop identity ADR.

**Context and memory lineage:** `MemOS → Bitemporal persistent memory → temporal-memory-provenance → D-12/D-14 → Four Structural Layers → Chapter 13 → D-12/D-14 AtlasPage`, complemented by AEGIS persistent disagreement, Estate Pulse source provenance, and Kollab memory boundaries.

**Decision evidence lineage:** `Reference architecture complete-v2 → Weighted platform selection method → weighted-option-appraisal → D-02/D-03 → Eight Control Planes → Chapter 5/23/54`; separately, workshop quality gates and UAF implementation audit point to D-22/D-23/D-24.

## Data boundaries

- The graph supports **historical evidence discovery**; it does not supersede the binding book architecture.
- A `supports` edge means an editor found a topical connection, not that the decision quotes or depends upon the prior source.
- The 86 concepts map to **43 frozen chapters** and **29 distinct frozen decisions**. Other book chapters/decisions remain authoritative and are simply not mapped by the selected historical source material.
- The complete-v2 and final-V2 snapshots are separate project IDs to preserve variant history. Estate Pulse duplicate package is preserved in original custody, with concepts counted only once under EP.

## Graph files

- `Master_Knowledge_Graph.graphml` for Gephi/NetworkX/yEd-compatible import.
- `Knowledge_Graph_Nodes.csv` and `Knowledge_Graph_Edges.csv` for spreadsheet/SQL ingestion.
- `Book_Relevance_Matrix.csv` expands 86 concept records into source→chapter→Decision combinations.
- `Cross_Project_Patterns.csv` lists repeated controlled patterns across multiple project families.

**Before using any graph edge in a manuscript:** open the source file shown in the Intellectual Asset Register and verify wording, applicability, rights, date and claim status.
