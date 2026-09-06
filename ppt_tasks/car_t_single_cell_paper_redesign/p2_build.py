"""Standalone P2 prototype: clinical signal and persistence."""
from pathlib import Path
from pptx_designer import Presentation
from pptx_designer.renderer.theme import ThemeComposer
from pptx_designer.tools.layout import page_number
from pptx_designer.tools.shapes import arrow, oval, rect
from pptx_designer.tools.text import multiline, text

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples/new_examplex/car_t_single_cell_paper"
OUT = CASE / "output/car_t_single_cell_p02_clinical_signal.pptx"
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
def stat(s,x,y,w,num,lab,color="blue"):
    tx(s,x,y,w,.38,num,28,color,True,"Aptos Display"); tx(s,x,y+.45,w,.15,lab,8.4,"muted",True,"Consolas")
def build():
    theme=ThemeComposer().compose(query="light biotech research editorial",seed=3109)
    prs=Presentation(theme=theme,strict_theme=True)
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.74,.46,2.8,.14,"01 / CLINICAL SIGNAL",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"orange")
    tx(s,.74,1.00,11.8,.48,"The clinical question is persistence—not merely response",22,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.4,.2,"Before asking what the cell is, establish how long its clinical phenotype remains visible.",10,"muted")

    # Left: context and endpoint definition.
    tx(s,.82,2.16,3.65,.16,"CLINICAL CONTEXT",8.8,"orange",True,"Consolas"); line(s,.82,2.48,3.65,.025,"orange")
    tx(s,.82,2.82,3.0,.40,"≈50%",30,"orange",True,"Aptos Display"); tx(s,.82,3.28,3.25,.18,"relapse within the first year",11,"navy",True)
    ml(s,.82,3.68,3.5,.62,["Durable remission is the exception that", "the atlas tries to explain."],11.5,"ink",1.15)
    tx(s,.82,4.62,3.65,.16,"WHAT IS MEASURED",8.8,"cyan",True,"Consolas"); line(s,.82,4.94,3.65,.025,"cyan")
    ml(s,.82,5.24,3.55,.85,["B-cell aplasia (BCA) duration", "→ clinical persistence axis", "→ BCA-L = longest-remission group"],11,"navy",1.18)

    # Center: reported time axis.
    tx(s,4.72,2.16,5.75,.16,"REPORTED BCA STRATA / MONTHS AFTER INFUSION",8.8,"orange",True,"Consolas"); line(s,4.72,2.48,5.75,.025,"orange")
    line(s,4.86,3.35,5.30,.035,"orange")
    points=[(4.98,"0","infusion","blue"),(5.86,"1","BCA1","green"),(6.74,"4","BCA2","blue"),(7.62,"18","BCA3","cyan"),(8.50,"61","BCA-O","blue"),(9.58,"101","BCA-L","orange")]
    for x,month,group,col in points:
        dot(s,x,3.19,.30,col); tx(s,x-.28,3.70,.62,.22,month,14,"navy",True,"Aptos Display","center"); tx(s,x-.55,4.08,1.10,.17,group,12,col,True,"Consolas","center")
    tx(s,4.86,4.64,5.30,.18,"The duration axis is ordered, not a fitted continuous curve.",9.2,"muted",False,"Consolas")
    line(s,4.86,5.14,5.30,.02,"line")
    tx(s,4.86,5.40,1.22,.16,"OBSERVATION",8.5,"orange",True,"Consolas"); tx(s,6.15,5.36,3.8,.24,"long B-cell aplasia",14,"navy",True)
    arrow(s,7.90,5.48,.62,0,C["cyan"],C=C); tx(s,8.68,5.40,1.65,.16,"NEXT QUESTION",8.5,"cyan",True,"Consolas"); tx(s,8.68,5.74,1.65,.24,"what sustains it?",13,"navy",True)

    # Right: hero metric and cohort anchor.
    rect(s,10.78,2.16,1.76,3.08,fill=C["paper"],line=C["orange"],C=C)
    tx(s,11.02,2.48,1.30,.16,"BCA-L",9,"orange",True,"Consolas"); tx(s,11.02,3.00,1.40,.52,"8.4",38,"orange",True,"Aptos Display"); tx(s,11.02,3.58,1.3,.20,"years",14,"orange",True)
    line(s,11.02,4.02,1.28,.025,"orange"); tx(s,11.02,4.28,1.35,.18,"median duration",9,"navy",True); tx(s,11.02,4.62,1.25,.18,"n = 5",10,"muted",False,"Consolas")

    # Bottom: paper evidence source and bridge.
    line(s,.82,6.38,11.72,.025,"cyan")
    tx(s,.82,6.62,1.5,.16,"READING RULE",8.5,"cyan",True,"Consolas"); tx(s,2.38,6.58,7.2,.22,"Clinical persistence is the entry point, not the mechanism.",12,"navy",True)
    tx(s,.82,7.10,10.8,.12,"Source: Bai et al., Nature 634, 702–711 (2024), Fig. 1c; background relapse context from the paper abstract.",7.2,"muted",False,"Consolas")
    page_number(s,2,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
