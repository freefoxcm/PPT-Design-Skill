"""Standalone P5 prototype: BCA strata and clinical comparison axis."""
from pathlib import Path
from pptx_designer import Presentation
from pptx_designer.renderer.theme import ThemeComposer
from pptx_designer.tools.layout import page_number
from pptx_designer.tools.shapes import arrow, oval, rect
from pptx_designer.tools.text import multiline, text

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples/new_examplex/car_t_single_cell_paper"
OUT = CASE / "output/car_t_single_cell_p05_persistence_axis.pptx"
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
def panel(s,x,y,w,h,accent="line"): rect(s,x,y,w,h,fill=C["paper"],line=C[accent],C=C)
def build():
    theme=ThemeComposer().compose(query="light biotech research editorial",seed=3109)
    prs=Presentation(theme=theme,strict_theme=True)
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.74,.46,2.8,.14,"04 / PERSISTENCE AXIS",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"orange")
    tx(s,.74,1.00,11.8,.48,"BCA strata define the clinical comparison axis",22,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.4,.2,"The groups are ordered by reported B-cell aplasia duration; they are not a fitted continuous curve.",10,"muted")

    # Left: duration bars.
    tx(s,.82,2.12,4.55,.16,"REPORTED DURATION / MONTHS",8.8,"orange",True,"Consolas"); line(s,.82,2.44,4.55,.025,"orange")
    groups=[("BCA-L","101","n=5","orange"),("BCA-O","61","n=11","blue"),("BCA3","18","n=11","cyan"),("BCA2","4","n=38","blue"),("BCA1","1","n=17","green")]
    base_y=4.95; xs=[1.0,1.78,2.56,3.34,4.12]; heights=[2.12,1.62,.98,.60,.40]
    line(s,.95,base_y,3.95,.03,"line")
    for i,(g,val,n,col) in enumerate(groups):
        x=xs[i]; h=heights[i]; rect(s,x,base_y-h,.50,h,fill=C[col],C=C); tx(s,x-.18,base_y-h-.34,.86,.22,val,15,col,True,"Aptos Display","center"); tx(s,x-.26,base_y+.18,1.02,.16,g,8.5,col,True,"Consolas","center"); tx(s,x-.26,base_y+.44,1.02,.15,n,8.2,"muted",False,"Consolas","center")
    tx(s,.82,5.98,4.4,.20,"BCA-L: no relapse  |  BCA1: relapse",12,"navy",True)

    # Right: editable evidence matrix.
    tx(s,5.55,2.12,6.1,.16,"COHORT FACTS USED IN LATER COMPARISONS",8.8,"cyan",True,"Consolas"); line(s,5.55,2.44,6.05,.025,"cyan")
    panel(s,5.55,2.78,6.05,2.72,"line")
    cols=[7.05,8.00,8.95,9.90,10.85]; heads=["BCA-L","BCA-O","BCA3","BCA2","BCA1"]
    tx(s,5.78,3.05,1.25,.16,"GROUP",8.2,"muted",True,"Consolas");
    for x,h,col in zip(cols,heads,["orange","blue","cyan","blue","green"]): tx(s,x,3.05,.90,.16,h,8.0,col,True,"Consolas","center")
    line(s,5.78,3.38,5.48,.015,"line")
    rows=[("Median duration","101 mo","61 mo","18 mo","4 mo","1 mo"),("Cohort size","n=5","n=11","n=11","n=38","n=17"),("Relapse observed","No","No","Yes","Yes","Yes")]
    for r,(labv,*vals) in enumerate(rows):
        y=3.72+r*.48; tx(s,5.78,y,1.25,.18,labv,8.0,"muted",True,"Consolas")
        for x,val in zip(cols,vals): tx(s,x,y,.90,.18,val,8.8,"navy",True,"Aptos","center")
    line(s,5.78,5.18,5.48,.015,"line")
    tx(s,5.78,5.32,1.10,.16,"ROLE",8.1,"cyan",True,"Consolas"); tx(s,6.98,5.30,4.15,.20,"stratify before molecular comparison",9.8,"navy",True)

    # Bottom bridge to P6.
    line(s,.82,6.70,10.8,.025,"cyan"); tx(s,.82,6.90,1.45,.15,"NEXT QUESTION",8.3,"cyan",True,"Consolas"); tx(s,2.32,6.86,8.8,.2,"What molecular program distinguishes the longest-remission state?",11.5,"navy",True)
    tx(s,.82,7.18,10.4,.18,"Source: Bai et al., Fig. 1c. Values are reported months; strata are associative.",12,"muted",False,"Consolas")
    page_number(s,5,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
