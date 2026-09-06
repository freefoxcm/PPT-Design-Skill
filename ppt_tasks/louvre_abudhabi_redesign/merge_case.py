"""Merge the reviewed Louvre P1-P10 prototypes into a new complete deck."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import re


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
BASE = CASE / "output" / "louvre_abudhabi_complete.pptx"
OUT = CASE / "output" / "louvre_abudhabi_visual_baseline_final.pptx"
REDESIGN = ROOT / "ppt_tasks" / "louvre_abudhabi_redesign"
SOURCES = {index: REDESIGN / f"louvre_abudhabi_p{index:02d}_visual_baseline.pptx" for index in range(1, 11)}


def merge():
    with ZipFile(BASE, "r") as base_zip:
        entries = {name: base_zip.read(name) for name in base_zip.namelist()}
    for slide_no, source in SOURCES.items():
        with ZipFile(source, "r") as src_zip:
            slide_xml = src_zip.read("ppt/slides/slide1.xml")
            rels_xml = src_zip.read("ppt/slides/_rels/slide1.xml.rels")
            for match in re.finditer(rb'Target="\.\./media/([^\"]+)"', rels_xml):
                old_name = match.group(1).decode("utf-8")
                new_name = f"louvre_merged_slide{slide_no}_{old_name}"
                entries[f"ppt/media/{new_name}"] = src_zip.read(f"ppt/media/{old_name}")
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
