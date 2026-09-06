"""Standalone P9 prototype: preclinical recall model."""
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
CROP_DIR = ASSET / "crops_p9"
OUT = CASE / "output/car_t_single_cell_p09_preclinical_test.pptx"
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
    src=ASSET/"41586_2024_7762_Fig5_HTML.png"
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
    tx(s,.74,.46,3.4,.14,"08 / PRECLINICAL TEST",8.5,"navy",True,"Consolas"); line(s,.74,.74,1.1,.025,"green")
    tx(s,.74,1.00,11.8,.48,"The state is tested as function in a recall model",22,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.4,.2,"The mouse experiment tests expansion, tumour control, and response after rechallenge.",10,"muted")

    fig(s,crop_fig("upper_results",(0,0,1066,610)),.82,2.10,6.55,2.95,"Fig. 5a–c · model + flux")
    fig(s,crop_fig("survival_result7",(0,600,700,897)),.82,5.18,3.30,1.40,"")
    tx(s,4.38,5.18,2.52,.16,"FUNCTIONAL READOUT",8.5,"cyan",True,"Consolas"); line(s,4.38,5.48,2.52,.02,"cyan")
    ml(s,4.38,5.72,2.62,.64,["expansion · tumour flux","survival after rechallenge","type 2-high > type 2-low"],12,"navy",1.10)

    # Editable experimental sequence.
    tx(s,7.78,2.10,4.35,.16,"EXPERIMENTAL SEQUENCE",8.5,"green",True,"Consolas"); line(s,7.78,2.42,4.55,.025,"green")
    line(s,8.05,3.40,4.05,.025,"green")
    events=[("−7","Nalm6","1 × 10⁶", "blue"),("0","CAR T","2 × 10⁶ · low / high","orange"),("17","rechallenge","Nalm6 · 1 × 10⁶","green"),("24–28","imaging","weekly", "cyan")]
    for i,(day,head,body,col) in enumerate(events):
        x=8.12+i*1.23; dot(s,x,3.29,.22,col); tx(s,x-.32,3.62,.64,.18,day,12,"navy",True,"Aptos Display","center"); tx(s,x-.60,3.96,1.20,.18,head,12,"navy",True,"Consolas","center"); tx(s,x-.60,4.25,1.20,.42,body,12,"muted",False,"Aptos","center")

    tx(s,7.78,4.92,4.35,.16,"READOUTS",8.5,"cyan",True,"Consolas"); line(s,7.78,5.22,4.55,.025,"cyan")
    ml(s,7.78,5.48,4.45,.66,["expansion · tumour flux · survival","type 2-low versus type 2-high CAR T","reported model: n = 5 mice"],12,"navy",1.10)
    line(s,.82,6.84,11.55,.025,"orange")
    tx(s,.82,7.02,1.05,.16,"BOUNDARY",8.5,"orange",True,"Consolas")
    tx(s,2.02,6.98,9.55,.20,"preclinical function is demonstrated in the reported model; clinical efficacy is not established",12,"navy",True)
    tx(s,.82,7.18,10.9,.18,"Source: Bai et al., Fig. 5. NSG + Nalm6 model; type 2-high cells show stronger recall in the reported experiment.",12,"muted",False,"Consolas")
    page_number(s,9,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER 03",12,"muted",False,"Consolas","right")
    prs.save(OUT); print(OUT)
if __name__ == "__main__": build()
