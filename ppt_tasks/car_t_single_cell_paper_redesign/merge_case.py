"""Merge the approved P1 cover with the reviewed standalone P2-P12 pages."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import re

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples/new_examplex/car_t_single_cell_paper"
OUT = CASE / "output/car_t_single_cell_atlas_research_baseline_final.pptx"
BASE = CASE / "output/car_t_single_cell_atlas_research_baseline_v3.pptx"

SOURCES = {
    2: CASE / "output/car_t_single_cell_p02_clinical_signal.pptx",
    3: CASE / "output/car_t_single_cell_p03_study_design.pptx",
    4: CASE / "output/car_t_single_cell_p04_cell_atlas.pptx",
    5: CASE / "output/car_t_single_cell_p05_persistence_axis.pptx",
    6: CASE / "output/car_t_single_cell_p06_type2_state.pptx",
    7: CASE / "output/car_t_single_cell_p07_candidate_mechanism.pptx",
    8: CASE / "output/car_t_single_cell_p08_longitudinal_serum.pptx",
    9: CASE / "output/car_t_single_cell_p09_preclinical_test.pptx",
    10: CASE / "output/car_t_single_cell_p10_engineering_direction.pptx",
    11: CASE / "output/car_t_single_cell_p11_evidence_ladder.pptx",
    12: CASE / "output/car_t_single_cell_p12_bounded_conclusion.pptx",
}

def merge():
    with ZipFile(BASE, "r") as base_zip:
        entries = {name: base_zip.read(name) for name in base_zip.namelist()}
    for slide_no, source in SOURCES.items():
        with ZipFile(source, "r") as src_zip:
            slide_xml = src_zip.read("ppt/slides/slide1.xml")
            rels_name = "ppt/slides/_rels/slide1.xml.rels"
            rels_xml = src_zip.read(rels_name)
            for match in re.finditer(rb'Target="\.\./media/([^\"]+)"', rels_xml):
                old_name = match.group(1).decode("utf-8")
                new_name = f"merged_slide{slide_no}_{old_name}"
                old_part = f"ppt/media/{old_name}"
                new_part = f"ppt/media/{new_name}"
                entries[new_part] = src_zip.read(old_part)
                rels_xml = rels_xml.replace(
                    f"../media/{old_name}".encode("utf-8"),
                    f"../media/{new_name}".encode("utf-8"),
                )
            entries[f"ppt/slides/slide{slide_no}.xml"] = slide_xml
            entries[f"ppt/slides/_rels/slide{slide_no}.xml.rels"] = rels_xml
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(OUT, "w", ZIP_DEFLATED) as out_zip:
        for name, data in entries.items():
            out_zip.writestr(name, data)
    print(OUT)

if __name__ == "__main__":
    merge()
