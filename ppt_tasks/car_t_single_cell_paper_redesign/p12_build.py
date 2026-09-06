"""Standalone P12 prototype: bounded conclusion and evidence map."""
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
CROP_DIR = ASSET / "crops_p12"
OUT = CASE / "output/car_t_single_cell_p12_bounded_conclusion.pptx"
C = {"bg":"#F5F8FA","paper":"#FFFFFF","navy":"#0D3557","ink":"#193E59","muted":"#667F91","line":"#BFD5E0","blue":"#1476B8","cyan":"#08A8B8","orange":"#D28327","green":"#5C8F45","white":"#FFFFFF"}

def tx(s,x,y,w,h,v,size=12,color="ink",bold=False,font="Aptos",align=None):
    size=max(size,12); kw=dict(font_size=size,color=color,bold=bold,font_name=font,C=C)
    if align is not None: kw["align"]=align
    return text(s,x,y,w,h,v,**kw)
def ml(s,x,y,w,h,vals,size=11,color="muted",spacing=1.1,align=None):
    size=max(size,12); kw=dict(font_size=size,color=color,C=C,line_spacing=spacing)
    if align is not None: kw["align"]=align
    return multiline(s,x,y,w,h,vals,**kw)
def line(s,x,y,w,h=.02,color="line"): rect(s,x,y,w,h,fill=C[color],C=C)
def crop_fig(key,src_name,box):
    CROP_DIR.mkdir(exist_ok=True); src=ASSET/src_name; out=CROP_DIR/f"{key}.png"
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime: Image.open(src).crop(box).save(out)
    return out
def evidence_row(s,path,y,label,claim,detail,col):
    rect(s,6.35,y,1.72,1.20,fill=C["paper"],line=C[col],C=C); cover_image(s,6.39,y+.04,1.64,1.12,str(path))
    tx(s,8.35,y+.04,3.55,.18,label,12,col,True,"Consolas")
    tx(s,8.35,y+.36,3.55,.24,claim,15,"navy",True,"Aptos Display")
    tx(s,8.35,y+.78,3.55,.18,detail,12,"muted",False,"Aptos")
def build():
    theme=ThemeComposer().compose(query="light biotech research editorial",seed=3109); prs=Presentation(theme=theme,strict_theme=True)
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.74,.46,3.2,.14,"11 / BOUNDED TAKEAWAY",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"orange")
    tx(s,.74,1.00,11.8,.48,"Type 2 function may sustain fitness",22,"navy",True,"Aptos Display")
    tx(s,.76,1.58,5.25,.2,"The paper connects persistence to cell state, candidate circuitry, and preclinical function.",10,"muted")

    tx(s,.82,2.18,1.65,.16,"CONTRIBUTION",8.5,"blue",True,"Consolas"); line(s,.82,2.48,4.75,.025,"cyan")
    ml(s,.82,2.78,4.85,1.00,["A durable clinical phenotype","becomes a recognizable cell state,","a candidate circuit, and a preclinical lever."],16,"navy",1.16)
    line(s,.82,4.25,4.75,.025,"orange")
    tx(s,.82,4.52,1.05,.16,"LIMITS",8.5,"orange",True,"Consolas")
    ml(s,.82,4.86,4.85,1.22,["Optimal clinical type 2 level remains unknown.","Preclinical models do not establish efficacy.","Mechanism remains proposed, not complete causal proof."],12,"navy",1.15)
    line(s,.82,6.42,4.75,.025,"cyan")
    tx(s,.82,6.70,1.40,.16,"READING RULE",8.5,"cyan",True,"Consolas")
    tx(s,2.40,6.66,3.1,.20,"keep evidence levels separate",12,"navy",True)

    tx(s,6.35,2.18,2.0,.16,"EVIDENCE MAP",8.5,"cyan",True,"Consolas"); line(s,6.35,2.48,5.55,.025,"cyan")
    evidence_row(s,crop_fig("state", "41586_2024_7762_Fig2_HTML.png", (0,0,900,950)),2.72,"CELLULAR STATE","type 2-like program","Fig. 2 · resolved cellular association","cyan")
    evidence_row(s,crop_fig("network", "41586_2024_7762_Fig3_HTML.png", (0,0,1100,900)),4.12,"CANDIDATE NETWORK","cluster 2 hypothesis","Fig. 3 · proposed mechanism","blue")
    evidence_row(s,crop_fig("lever", "41586_2024_7762_Fig6_HTML.png", (0,0,1250,900)),5.52,"PRECLINICAL LEVER","IL-4 / ET2-L/H direction","Fig. 6 · engineering experiment","orange")
    tx(s,6.35,7.10,5.5,.18,"Bai et al. · Nature 634 · 702–711 · 2024",12,"muted",False,"Consolas")
    page_number(s,12,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
