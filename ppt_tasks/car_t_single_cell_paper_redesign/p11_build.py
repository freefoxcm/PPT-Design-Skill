"""Standalone P11 prototype: evidence ladder and boundaries."""
from pathlib import Path
from pptx_designer import Presentation
from pptx_designer.renderer.theme import ThemeComposer
from pptx_designer.tools.layout import page_number
from pptx_designer.tools.shapes import arrow, oval, rect
from pptx_designer.tools.text import multiline, text

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples/new_examplex/car_t_single_cell_paper"
OUT = CASE / "output/car_t_single_cell_p11_evidence_ladder.pptx"
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
def build():
    theme=ThemeComposer().compose(query="light biotech research editorial",seed=3109); prs=Presentation(theme=theme,strict_theme=True)
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.74,.46,3.3,.14,"10 / EVIDENCE LADDER",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"cyan")
    tx(s,.74,1.00,11.8,.48,"The argument is strongest when evidence types stay separate",22,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.4,.2,"A disciplined reading keeps association, state definition, mechanism, and intervention distinct.",10,"muted")

    # One rising ladder: the vertical rise signals increasing intervention, not certainty.
    levels=[
        ("01 / OBSERVED","8.4-year persistence","BCA-L 101 months","clinical phenotype","Fig. 1c / 4","orange"),
        ("02 / RESOLVED","type 2-like state","IL-4 · IL-5 · IL-13 · GATA3","cellular state","Fig. 2","cyan"),
        ("03 / PROPOSED","cluster 2 network","ligand–receptor links · DEGs","candidate mechanism","Fig. 3","blue"),
        ("04 / TESTED","recall + IL-4","mouse expansion · rechallenge","preclinical lever","Fig. 5 / 6","green"),
    ]
    xs=[.82,3.82,6.82,9.82]; ys=[4.12,3.55,2.98,2.41]
    line(s,1.08,5.80,10.25,.035,"line")
    for i,(head,claim,evidence,domain,ref,col) in enumerate(levels):
        x=xs[i]; y=ys[i]
        rect(s,x,y,2.45,2.02,fill=C["paper"],line=C[col],C=C)
        tx(s,x+.18,y+.18,2.05,.18,head,12,col,True,"Consolas")
        tx(s,x+.18,y+.60,2.05,.24,claim,15,"navy",True,"Aptos Display")
        ml(s,x+.18,y+.99,2.05,.50,[evidence,domain],12,"navy",1.10)
        tx(s,x+.18,y+1.68,2.05,.18,ref,12,"muted",False,"Consolas")
        if i<3: arrow(s,x+2.52,y+1.05,.36,0,C["cyan"],C=C)
    # Explicit semantic boundary below the ladder.
    line(s,.82,6.30,11.45,.025,"orange")
    tx(s,.82,6.52,1.40,.16,"READING RULE",8.5,"orange",True,"Consolas")
    tx(s,2.40,6.48,9.35,.20,"association → state definition → candidate explanation → functional test / engineering lever",12,"navy",True)
    tx(s,.82,6.86,11.0,.18,"The ladder is an editorial summary, not a new result; clinical type-2 optimum remains unresolved.",12,"muted",False,"Consolas")
    tx(s,.82,7.18,10.9,.18,"Source: Bai et al., Figs. 1–6. Evidence levels are intentionally kept distinct.",12,"muted",False,"Consolas")
    page_number(s,11,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
