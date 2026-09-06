"""Standalone P7 prototype: candidate mechanism and evidence boundary."""
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
CROP_DIR = ASSET / "crops_p7"
OUT = CASE / "output/car_t_single_cell_p07_candidate_mechanism.pptx"
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
def crop_fig(key,box):
    CROP_DIR.mkdir(exist_ok=True)
    src=ASSET/"41586_2024_7762_Fig3_HTML.png"
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
    tx(s,.74,.46,3.5,.14,"06 / CANDIDATE MECHANISM",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"blue")
    tx(s,.74,1.00,11.8,.48,"Cluster 2 emerges as a candidate regulatory hub",22,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.4,.2,"The network suggests a regulatory relationship; it does not by itself establish complete causal mechanism.",10,"muted")

    # Dominant evidence: ligand–receptor network as the focal visual.
    fig(s,crop_fig("network_ab_top2",(0,0,1250,520)),.82,2.10,6.70,2.95,"Source: Bai et al., Fig. 3a–b · ligand–receptor network")
    fig(s,crop_fig("cluster2_cd_top2",(1300,0,2125,520)),7.82,2.10,4.55,2.95,"Source: Bai et al., Fig. 3c–d · cluster 2")

    # Evidence synthesis beneath the figures.
    line(s,.82,5.92,11.55,.025,"cyan")
    tx(s,.82,6.18,1.35,.16,"EVIDENCE CHAIN",8.5,"cyan",True,"Consolas")
    steps=[("L–R links","orange"),("cluster 2","blue"),("DEGs","cyan"),("hub hypothesis","green")]
    for i,(labv,col) in enumerate(steps):
        x=2.42+i*2.18; dot(s,x,6.13,.22,col); tx(s,x-.58,6.47,1.16,.18,labv,12,"navy",True,"Consolas","center")
        if i<3: arrow(s,x+.31,6.24,1.32,0,C["cyan"],C=C)
    tx(s,10.86,6.02,1.35,.28,"13.9%",22,"orange",True,"Aptos Display","center"); tx(s,10.84,6.38,1.38,.18,"cluster 2",12,"muted",True,"Consolas","center")

    tx(s,.82,6.92,1.15,.16,"BOUNDARY",8.5,"orange",True,"Consolas")
    tx(s,2.12,6.88,8.9,.20,"candidate network → hypothesis for dysfunctional-subpopulation regulation",12,"navy",True)
    tx(s,.82,7.18,10.8,.18,"Source: Bai et al., Fig. 3. Network and cluster-2 evidence are reproduced; mechanism remains proposed.",12,"muted",False,"Consolas")
    page_number(s,7,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
