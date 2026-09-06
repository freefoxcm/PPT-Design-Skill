"""Standalone P6 prototype: type 2 state, readouts, and perturbation."""
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
CROP_DIR = ASSET / "crops_p6"
OUT = CASE / "output/car_t_single_cell_p06_type2_state.pptx"
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
    CROP_DIR.mkdir(exist_ok=True); src=ASSET/"41586_2024_7762_Fig2_HTML.png"; out=CROP_DIR/f"{key}.png"
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime: Image.open(src).crop(box).save(out)
    return out
def fig(s,path,x,y,w,h,label):
    rect(s,x-.04,y-.04,w+.08,h+.08,fill=C["paper"],line=C["line"],C=C); cover_image(s,x,y,w,h,str(path)); tx(s,x,y+h+.06,w,.13,label,7.5,"muted",False,"Consolas")
def build():
    theme=ThemeComposer().compose(query="light biotech research editorial",seed=3109)
    prs=Presentation(theme=theme,strict_theme=True)
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.74,.46,2.8,.14,"05 / TYPE 2 STATE",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"orange")
    tx(s,.74,1.00,11.8,.48,"Long-remission cells show a convergent type 2-like program",22,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.4,.2,"The state is not assigned from one marker: transcriptome, secretion, chromatin, and perturbation point in the same direction.",10,"muted")

    # Evidence figures: two readable selections rather than a full tiny Fig. 2.
    fig(s,crop_fig("type2_score",(0,0,1700,1000)),.82,2.10,5.65,2.70,"Source: Fig. 2a–d · type 2 score and validation")
    fig(s,crop_fig("type2_function",(0,980,1700,1959)),.82,5.02,5.65,1.12,"Source: Fig. 2e–j · cytokines, secretion, ATAC, GATA3")

    # Right: method and result hierarchy.
    tx(s,6.88,2.10,5.05,.16,"METHOD / FOUR ORTHOGONAL READOUTS",8.8,"cyan",True,"Consolas"); line(s,6.88,2.42,5.15,.025,"cyan")
    reads=[("01","TYPE 2 SCORE","cell-state enrichment","orange"),("02","FLOW CYTOKINES","IL-3 · IL-4 · IL-5 · IL-13","blue"),("03","SECRETOME","IL-4 / type 2 secretion","cyan"),("04","ATAC + TF","GATA3 / STAT6 context","green")]
    for i,(num,head,body,col) in enumerate(reads):
        y=2.76+i*.56; dot(s,6.92,y+.03,.20,col); tx(s,7.25,y,1.65,.16,num+"  "+head,8.3,col,True,"Consolas"); tx(s,9.15,y,2.7,.16,body,9.3,"navy",True)
    tx(s,6.88,4.92,5.05,.13,"Comparison axis: BCA-L vs BCA-O / BCA3 / BCA2 / BCA1",8.0,"muted",False,"Consolas")
    line(s,6.88,5.12,5.15,.025,"orange"); tx(s,6.88,5.38,2.2,.16,"RESULT / CONVERGENCE",8.8,"orange",True,"Consolas")
    tx(s,6.88,5.76,5.05,.27,"one coherent type 2 state",16,"orange",True,"Aptos Display")
    ml(s,6.88,6.14,5.05,.34,["Enriched in long-remission cells; functional context follows through repeat stimulation."],9.8,"navy",1.08)

    # Process bridge.
    line(s,.82,6.55,11.15,.025,"cyan"); tx(s,.82,6.78,1.35,.15,"EXPERIMENT LOGIC",8.3,"cyan",True,"Consolas")
    steps=[("BCA","orange"),("score","blue"),("cytokines","cyan"),("ATAC + TF","green"),("re-stim.","orange")]
    for i,(labv,col) in enumerate(steps):
        x=2.36+i*2.0; dot(s,x,6.72,.20,col); tx(s,x-.55,7.00,1.10,.18,labv,12,"navy",True,"Consolas","center")
        if i<4: arrow(s,x+.28,6.82,1.18,0,C["cyan"],C=C)
    page_number(s,6,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
