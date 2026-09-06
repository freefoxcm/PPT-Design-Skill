"""Standalone P8 prototype: longitudinal serum evidence."""
from pathlib import Path
from PIL import Image
from pptx_designer import Presentation
from pptx_designer.renderer.theme import ThemeComposer
from pptx_designer.tools.layout import page_number
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.text import multiline, text

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples/new_examplex/car_t_single_cell_paper"
ASSET = CASE / "assets"
CROP_DIR = ASSET / "crops_p8"
OUT = CASE / "output/car_t_single_cell_p08_longitudinal_serum.pptx"
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
def crop_fig(key,box):
    CROP_DIR.mkdir(exist_ok=True)
    src=ASSET/"41586_2024_7762_Fig4_HTML.png"
    out=CROP_DIR/f"{key}.png"
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime:
        Image.open(src).crop(box).save(out)
    return out
def fig(s,path,x,y,w,h,label):
    rect(s,x-.04,y-.04,w+.08,h+.08,fill=C["paper"],line=C["line"],C=C)
    cover_image(s,x,y,w,h,str(path))
    tx(s,x,y+h+.06,w,.13,label,7.5,"muted",False,"Consolas")
def build():
    theme=ThemeComposer().compose(query="light biotech research editorial",seed=3109)
    prs=Presentation(theme=theme,strict_theme=True)
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.74,.46,3.5,.14,"07 / LONGITUDINAL SERUM",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"cyan")
    tx(s,.74,1.00,11.8,.48,"The type 2 signal survives time, not just a snapshot",22,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.4,.2,"Serial serum measurements extend the cellular observation into a longitudinal readout.",10,"muted")

    # Two complementary longitudinal views: discovery and validation.
    fig(s,crop_fig("discovery_series",(0,0,1320,650)),.82,2.10,7.15,2.78,"Fig. 4a–b · discovery serum series")
    fig(s,crop_fig("validation_series",(1300,0,2124,650)),8.22,2.10,4.15,2.78,"Fig. 4a–b · validation")

    # Quantitative frame and assay logic.
    line(s,.82,5.24,11.55,.025,"cyan")
    tx(s,.82,5.46,1.55,.16,"LONGITUDINAL",8.5,"cyan",True,"Consolas")
    stat_x=[2.42,3.85,5.28]
    for x,val,lab,col in zip(stat_x,["345","30","33"],["measurements","cytokines","patients"],["cyan","blue","orange"]):
        tx(s,x,5.38,1.35,.28,val,21,col,True,"Aptos Display","center"); tx(s,x,5.76,1.35,.16,lab,12,"muted",True,"Consolas","center")
    tx(s,6.88,5.46,2.05,.16,"TYPE 2 WINDOW",8.5,"orange",True,"Consolas"); line(s,6.88,5.76,2.05,.02,"orange")
    ml(s,6.88,5.94,2.15,.52,["IL-4 · IL-5 · IL-13","days 1–63"],12,"navy",1.12)
    tx(s,9.35,5.46,2.3,.16,"METHOD LOGIC",8.5,"cyan",True,"Consolas"); line(s,9.35,5.76,2.55,.02,"cyan")
    ml(s,9.35,5.94,2.7,.52,["30-plex serum panel","discovery → validation"],12,"navy",1.12)

    line(s,.82,6.58,11.55,.025,"orange")
    tx(s,.82,6.82,1.05,.16,"BOUNDARY",8.5,"orange",True,"Consolas")
    tx(s,2.02,6.78,9.55,.20,"longitudinal serum evidence supports persistence of the biology; it does not replace cell-state analysis",12,"navy",True)
    tx(s,.82,7.18,10.9,.18,"Source: Bai et al., Fig. 4. Discovery uses 33 patients; validation uses 8 patients and selected cytokines.",12,"muted",False,"Consolas")
    page_number(s,8,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
