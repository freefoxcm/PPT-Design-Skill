"""Standalone P3 prototype: cohort, sample processing, readouts, and analysis."""
from pathlib import Path
from PIL import Image
from pptx_designer import Presentation
from pptx_designer.renderer.theme import ThemeComposer
from pptx_designer.tools.layout import page_number
from pptx_designer.tools.shapes import arrow, oval, rect
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.text import multiline, text

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples/new_examplex/car_t_single_cell_paper"
ASSET = CASE / "assets"
OUT = CASE / "output/car_t_single_cell_p03_study_design.pptx"
C = {"bg":"#F5F8FA","paper":"#FFFFFF","navy":"#0D3557","ink":"#193E59","muted":"#667F91","line":"#BFD5E0","blue":"#1476B8","cyan":"#08A8B8","orange":"#D28327","green":"#5C8F45","white":"#FFFFFF"}

def tx(s,x,y,w,h,v,size=12,color="ink",bold=False,font="Aptos",align=None):
    size=max(size,12)
    kw=dict(font_size=size,color=color,bold=bold,font_name=font,C=C)
    if align is not None: kw["align"]=align
    return text(s,x,y,w,h,v,**kw)
def ml(s,x,y,w,h,vals,size=11,color="muted",spacing=1.1,align=None):
    size=max(size,12)
    kw=dict(font_size=size,color=color,C=C,line_spacing=spacing)
    if align is not None: kw["align"]=align
    return multiline(s,x,y,w,h,vals,**kw)
def line(s,x,y,w,h=.02,color="line"): rect(s,x,y,w,h,fill=C[color],C=C)
def dot(s,x,y,d,color): oval(s,x,y,d,d,fill=C[color],C=C)
def panel(s,x,y,w,h,accent="line"):
    rect(s,x,y,w,h,fill=C["paper"],line=C[accent],C=C)
def build():
    theme=ThemeComposer().compose(query="light biotech research editorial",seed=3109)
    prs=Presentation(theme=theme,strict_theme=True)
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.74,.46,2.8,.14,"02 / STUDY DESIGN",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"cyan")
    tx(s,.74,1.00,11.8,.48,"The paper turns a clinical phenotype into a measurable cell-state system",21.5,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.4,.2,"The workflow matters: each readout answers a different part of the persistence question.",10,"muted")

    # Stage 1 — cohort and product.
    tx(s,.82,2.12,2.05,.16,"01  /  COHORT",8.8,"orange",True,"Consolas"); line(s,.82,2.42,2.45,.025,"orange")
    panel(s,.82,2.72,2.45,2.12,"orange"); tx(s,1.05,3.00,1.8,.30,"82",27,"orange",True,"Aptos Display"); tx(s,1.05,3.40,1.8,.18,"ALL patients",12,"navy",True); line(s,1.05,3.78,1.8,.02,"line"); tx(s,1.05,4.08,1.8,.24,"+ 6 healthy donors",12,"navy",True); tx(s,1.05,4.48,1.8,.15,"BCA groups",12,"muted",False,"Consolas")
    arrow(s,3.42,3.65,.55,0,C["cyan"],C=C)
    tx(s,4.10,2.12,2.05,.16,"02  /  PRODUCT",8.8,"blue",True,"Consolas"); line(s,4.10,2.42,2.45,.025,"blue")
    panel(s,4.10,2.72,2.45,2.12,"blue"); tx(s,4.34,3.00,1.9,.22,"CAR T",18,"blue",True,"Aptos Display"); tx(s,4.34,3.38,1.9,.18,"product",12,"navy",True); line(s,4.34,3.78,1.9,.02,"line"); ml(s,4.34,4.08,1.9,.48,["pre-infusion cells", "linked to BCA strata"],12,"navy",1.15)
    arrow(s,6.70,3.65,.55,0,C["cyan"],C=C)

    # Stage 3 — sample processing and readouts.
    tx(s,7.36,2.12,2.65,.16,"03  /  SAMPLE → READOUT",8.8,"cyan",True,"Consolas"); line(s,7.36,2.42,4.95,.025,"cyan")
    panel(s,7.36,2.72,4.95,2.12,"cyan")
    steps=[("SINGLE-CELL","10x 3′ assay\n>10⁶ cells","cyan"),("FUNCTION","flow cytometry\nsecretome","blue"),("CHROMATIN","ATAC\nGATA3 / STAT6","orange")]
    for i,(head,body,col) in enumerate(steps):
        x=7.62+i*1.55; dot(s,x,3.02,.30,col); tx(s,x-.18,3.48,1.05,.16,head,8.2,col,True,"Consolas","center"); ml(s,x-.35,3.84,1.4,.48,body.split("\n"),9.2,"navy",1.08,"center")
        if i<2: arrow(s,x+.42,3.15,.82,0,C["cyan"],C=C)
    tx(s,7.62,4.48,4.2,.15,"orthogonal readouts",12,"muted",False,"Consolas")

    # Stage 4 — analysis and clinical link.
    tx(s,.82,5.20,2.7,.16,"04  /  ANALYSIS",8.8,"blue",True,"Consolas"); line(s,.82,5.50,5.55,.025,"blue")
    panel(s,.82,5.78,5.55,.82,"blue"); tx(s,1.05,6.02,1.7,.18,"UNSUPERVISED",8.3,"blue",True,"Consolas"); tx(s,2.82,5.98,3.1,.22,"clustering → differential expression → pathway analysis",10.2,"navy",True)
    arrow(s,6.62,6.17,.62,0,C["cyan"],C=C)
    tx(s,7.46,5.20,2.65,.16,"05  /  OUTPUT",8.8,"orange",True,"Consolas"); line(s,7.46,5.50,4.85,.025,"orange")
    panel(s,7.46,5.78,4.85,.82,"orange"); tx(s,7.70,6.02,1.65,.18,"CLINICAL LINK",8.3,"orange",True,"Consolas"); tx(s,9.42,5.98,2.5,.22,"17 cell states · 5 BCA strata",10.2,"navy",True)

    tx(s,.82,6.82,5.6,.18,"Source: Bai et al., Fig. 1a. Pipeline is editorially redrawn; assay facts remain paper-tied.",12,"muted",False,"Consolas")
    tx(s,7.46,6.82,4.8,.18,"Outcome: clinical duration becomes a comparable cell-state space.",12,"muted",True,"Consolas")
    page_number(s,3,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
