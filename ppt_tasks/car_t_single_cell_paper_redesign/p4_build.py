"""Standalone P4 prototype: atlas map, state families, and analysis logic."""
from pathlib import Path
from PIL import Image
from pptx_designer import Presentation
from pptx_designer.renderer.theme import ThemeComposer
from pptx_designer.tools.layout import page_number
from pptx_designer.tools.shapes import arrow, oval, rect
from pptx_designer.tools.text import multiline, text

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples/new_examplex/car_t_single_cell_paper"
ASSET = CASE / "assets"
CROP_DIR = ASSET / "crops_p4"
OUT = CASE / "output/car_t_single_cell_p04_cell_atlas.pptx"
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
def crop_map():
    CROP_DIR.mkdir(exist_ok=True); src=ASSET/"41586_2024_7762_Fig1_HTML.png"; out=CROP_DIR/"umap2.png"
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime: Image.open(src).crop((0,300,780,1044)).save(out)
    return out
def fig(s,path,x,y,w,h,label):
    rect(s,x-.04,y-.04,w+.08,h+.08,fill=C["paper"],line=C["line"],C=C); from pptx_designer.tools.images import cover_image; cover_image(s,x,y,w,h,str(path)); tx(s,x,y+h+.06,w,.13,label,7.6,"muted",False,"Consolas")
def build():
    theme=ThemeComposer().compose(query="light biotech research editorial",seed=3109)
    prs=Presentation(theme=theme,strict_theme=True)
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.74,.46,2.8,.14,"03 / CELL ATLAS",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"cyan")
    tx(s,.74,1.00,11.8,.48,"The atlas resolves one cohort into 17 measurable cell states",22,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.4,.2,"The UMAP is not the conclusion; it is the map used by every later comparison.",10,"muted")

    # Dominant map.
    fig(s,crop_map(),.82,2.12,7.15,3.92,"Source: Bai et al., Fig. 1b · selected UMAP / cluster annotation")
    tx(s,8.45,2.12,3.2,.16,"HOW TO READ THE MAP",8.8,"cyan",True,"Consolas"); line(s,8.45,2.44,3.65,.025,"cyan")
    ml(s,8.45,2.78,3.65,.72,["Each numbered region is a cell state.","Spatial proximity suggests a state landscape—not a causal pathway."],10.5,"navy",1.16)
    tx(s,8.45,3.78,3.2,.16,"FOUR STATE FAMILIES",8.8,"orange",True,"Consolas"); line(s,8.45,4.10,3.65,.025,"orange")
    families=[("NAIVE","memory / early","blue"),("CYTOTOXIC","effector program","orange"),("REGULATORY","signalling program","cyan"),("PROLIFERATIVE","expansion program","green")]
    for i,(head,desc,col) in enumerate(families):
        y=4.40+i*.38; dot(s,8.48,y+.01,.16,col); tx(s,8.78,y,1.55,.16,head,9.5,"navy",True); tx(s,10.32,y,1.75,.16,desc,8.1,"muted")

    # Analysis logic at bottom.
    line(s,.82,6.38,11.35,.025,"cyan"); tx(s,.82,6.62,1.55,.16,"ANALYSIS LOGIC",8.5,"cyan",True,"Consolas")
    steps=[("map","blue"),("cluster","cyan"),("states","orange"),("BCA","green")]
    for i,(labv,col) in enumerate(steps):
        x=2.55+i*2.22; dot(s,x,6.54,.22,col); tx(s,x-.58,6.86,1.18,.18,labv,12,"navy",True,"Consolas","center")
        if i<3: arrow(s,x+.32,6.65,1.38,0,C["cyan"],C=C)
    tx(s,10.95,6.60,1.2,.25,"17",24,"orange",True,"Aptos Display","center"); tx(s,10.88,6.90,1.35,.13,"cell states",7.8,"muted",True,"Consolas","center")
    # The readable source caption directly under the figure carries the citation;
    # no duplicate micro-footnote is used at the bottom edge.
    page_number(s,4,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
