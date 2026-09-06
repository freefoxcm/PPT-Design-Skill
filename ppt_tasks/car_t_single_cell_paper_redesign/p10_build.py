"""Standalone P10 prototype: IL-4 priming and engineering direction."""
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
CROP_DIR = ASSET / "crops_p10"
OUT = CASE / "output/car_t_single_cell_p10_engineering_direction.pptx"
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
def dot(s,x,y,d,color): oval(s,x,y,d,d,fill=C[color],C=C)
def crop_fig(key,box):
    CROP_DIR.mkdir(exist_ok=True); src=ASSET/"41586_2024_7762_Fig6_HTML.png"; out=CROP_DIR/f"{key}.png"
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime: Image.open(src).crop(box).save(out)
    return out
def fig(s,path,x,y,w,h,label):
    rect(s,x-.04,y-.04,w+.08,h+.08,fill=C["paper"],line=C["line"],C=C); cover_image(s,x,y,w,h,str(path)); tx(s,x,y+h+.06,w,.13,label,7.5,"muted",False,"Consolas")
def build():
    theme=ThemeComposer().compose(query="light biotech research editorial",seed=3109); prs=Presentation(theme=theme,strict_theme=True)
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.74,.46,3.6,.14,"09 / ENGINEERING DIRECTION",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"orange")
    tx(s,.74,1.00,11.8,.48,"IL-4 provides a preclinical manufacturing direction",22,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.4,.2,"The final figure asks whether a type 2-like program can be primed experimentally and tested in vivo.",10,"muted")

    fig(s,crop_fig("workflow_a3",(0,0,720,700)),.82,2.10,4.80,3.50,"Source: Bai et al., Fig. 6a · priming and ET2-L/H strategies")
    tx(s,6.35,2.10,5.55,.16,"EXPOSURE → PRODUCT → TEST",8.5,"orange",True,"Consolas"); line(s,6.35,2.42,5.65,.025,"orange")
    steps=[("PRIME","10 ng ml⁻¹ IL-4\n12 h","cyan"),("CULTURE","IL-7 + IL-15\nET2-L 10 / ET2-H 50","blue"),("TEST","expansion +\nsurvival","green")]
    for i,(head,body,col) in enumerate(steps):
        x=6.48+i*1.95; dot(s,x,3.05,.30,col); tx(s,x-.42,3.50,1.30,.18,head,12,col,True,"Consolas","center"); ml(s,x-.56,3.84,1.60,.62,body.split("\n"),12,"navy",1.08,"center")
        if i<2: arrow(s,x+.40,3.17,.95,0,C["cyan"],C=C)
    tx(s,6.35,4.78,5.55,.16,"DOSE COMPARISON",8.5,"cyan",True,"Consolas"); line(s,6.35,5.08,5.65,.025,"cyan")
    ml(s,6.35,5.34,5.55,.72,["Primed: 10 ng ml⁻¹ IL-4 for 12 h","ET2-L: 10 ng ml⁻¹ · ET2-H: 50 ng ml⁻¹","same culture context: IL-7 + IL-15"],12,"navy",1.10)

    fig(s,crop_fig("result_cd",(0,800,1050,1523)),.82,5.82,5.15,.72,"Fig. 6c–d · expansion and survival")
    line(s,6.35,6.62,5.65,.025,"orange"); tx(s,6.35,6.84,1.05,.16,"BOUNDARY",8.5,"orange",True,"Consolas"); tx(s,7.55,6.80,4.35,.20,"promising lever, still preclinical",12,"navy",True)
    tx(s,.82,7.10,10.9,.18,"Source: Bai et al., Fig. 6 · doses tied to paper; engineering framing is editorial.",12,"muted",False,"Consolas")
    page_number(s,10,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
