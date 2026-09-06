"""CAR-T paper case v2: figure-led research editorial baseline."""
from pathlib import Path
from PIL import Image
from pptx_designer import Presentation
from pptx_designer.renderer.theme import ThemeComposer
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.layout import page_number
from pptx_designer.tools.shapes import arrow, oval, rect
from pptx_designer.tools.text import multiline, text

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples/new_examplex/car_t_single_cell_paper"
ASSET = CASE / "assets"
CROP_DIR = ASSET / "crops_v2"
OUT = CASE / "output/car_t_single_cell_atlas_research_baseline_v4.pptx"
C = {"bg":"#F5F8FA","paper":"#FFFFFF","navy":"#0D3557","ink":"#193E59","muted":"#667F91","line":"#BFD5E0","blue":"#1476B8","cyan":"#08A8B8","orange":"#D28327","green":"#5C8F45","white":"#FFFFFF"}

def tx(s,x,y,w,h,v,size=12,color="ink",bold=False,font="Aptos",align=None):
    kw=dict(font_size=size,color=color,bold=bold,font_name=font,C=C)
    if align is not None: kw["align"]=align
    return text(s,x,y,w,h,v,**kw)
def ml(s,x,y,w,h,vals,size=11,color="muted",spacing=1.1,align=None):
    kw=dict(font_size=size,color=color,C=C,line_spacing=spacing)
    if align is not None: kw["align"]=align
    return multiline(s,x,y,w,h,vals,**kw)
def line(s,x,y,w,h=.018,color="line"): rect(s,x,y,w,h,fill=C[color],C=C)
def rule(s,x,y,w,color="cyan"): line(s,x,y,w,.025,color)
def dot(s,x,y,d,color): oval(s,x,y,d,d,fill=C[color],C=C)
def crop(n,key,box):
    CROP_DIR.mkdir(exist_ok=True)
    src=ASSET/f"41586_2024_7762_Fig{n}_HTML.png"; out=CROP_DIR/f"fig{n}_{key}.png"
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime: Image.open(src).crop(box).save(out)
    return out
def fig(s,path,x,y,w,h,label):
    rect(s,x-.04,y-.04,w+.08,h+.08,fill=C["paper"],line=C["line"],C=C)
    cover_image(s,x,y,w,h,str(path)); tx(s,x,y+h+.06,w,.13,label,7.6,"muted",False,"Consolas")
def ffull(s,n,x,y,w,h,label): fig(s,ASSET/f"41586_2024_7762_Fig{n}_HTML.png",x,y,w,h,label)
def fcase(s,n,key,box,x,y,w,h,label): fig(s,crop(n,key,box),x,y,w,h,label)
def label(s,x,y,w,v,color="blue"): tx(s,x,y,w,.15,v,8.4,color,True,"Consolas")
def base(prs,n,section,title,sub,accent="cyan"):
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.74,.46,2.5,.14,section,8.5,"navy",True,"Consolas")
    rule(s,.74,.74,1.1,accent); tx(s,.74,1.00,11.85,.48,title,23,"navy",True,"Aptos Display")
    tx(s,.76,1.58,11.6,.2,sub,10,"muted")
    page_number(s,n,12,C=C); tx(s,11.55,.50,1.0,.14,"PAPER / 03",8,"muted",False,"Consolas","right")
    return s
def foot(s,v): tx(s,.76,7.10,11.8,.13,v,7.2,"muted",False,"Consolas")
def pill(s,x,y,w,v,color="blue"):
    rect(s,x,y,w,.28,fill=C[color],C=C); tx(s,x,y+.065,w,.12,v,8,"white",True,"Consolas","center")
def stat(s,x,y,w,num,lab,color="blue"):
    tx(s,x,y,w,.34,num,28,color,True,"Aptos Display"); tx(s,x,y+.40,w,.14,lab,8.2,"muted",True,"Consolas")

def build():
    resolved_theme = ThemeComposer().compose(query="light biotech research editorial, figure-led academic paper presentation", seed=3109)
    prs=Presentation(theme=resolved_theme, strict_theme=True)
    # 1 — cover: question first, visual second.
    s=prs.slides.add_slide(prs.slide_layouts[6]); cover_image(s,0,0,13.333,7.5,str(ASSET/"cart_hero_blue.png"))
    tx(s,.82,.78,4.7,.15,"PAPER CASE 03  /  NATURE 2024",9,"cyan",True,"Consolas")
    tx(s,.82,1.45,4.95,1.18,"""When does a
CAR T cell stay fit?""",30,"white",True,"Aptos Display")
    tx(s,.84,3.10,4.65,.62,"A single-cell atlas of an 8-year remission.",15,"cyan",True)
    rule(s,.84,4.18,2.0,"orange")
    ml(s,.84,4.52,4.7,.84,["Bai et al. · Nature 634 · 702–711 · 2024","82 patients · 695,819 analyzed cells","CONCEPTUAL COVER VISUAL"],10.5,"white",1.25)
    pill(s,.84,6.18,2.6,"CLINICAL → CELLULAR → TESTED","cyan"); tx(s,.84,6.82,5.0,.12,"DOI 10.1038/s41586-024-07762-w",7.2,"white",False,"Consolas")

    # 2 — clinical timeline; no paper screenshot.
    s=base(prs,2,"01 / CLINICAL SIGNAL","The phenotype stays visible for years","The paper begins with a durable clinical readout: B-cell aplasia after CAR T infusion.","orange")
    label(s,.82,2.12,2.4,"CLINICAL TIME AXIS","orange"); rule(s,.82,2.48,10.7,"orange")
    for x,labv,sub in [(1.0,"0","CAR T infusion"),(3.2,"1 mo","BCA1"),(5.4,"4 mo","BCA2"),(7.6,"18 mo","BCA3"),(9.8,"61 mo","BCA-O"),(10.95,"101 mo","BCA-L")]:
        dot(s,x,2.35,.26,"orange"); tx(s,x-.52,2.88,1.04,.18,labv,13,"navy",True,"Aptos Display","center"); tx(s,x-.60,3.22,1.2,.18,sub,8.3,"muted",True,"Consolas","center")
    tx(s,1.0,3.70,4.5,.16,"BCA = B-cell aplasia  ·  BCA-L = longest-remission stratum",8.8,"muted",False,"Consolas")
    tx(s,1.0,4.15,5.0,.36,"8.4 years",31,"orange",True,"Aptos Display"); tx(s,1.0,4.63,3.6,.18,"median BCA-L duration",11,"navy",True)
    ml(s,6.15,4.12,5.2,.72,["This is not a single endpoint.","It is a clinical trace that motivates the atlas."],15,"navy",1.18)
    rule(s,1.0,5.62,10.2,"cyan"); tx(s,1.0,5.92,2.0,.18,"OBSERVED",8,"orange",True,"Consolas"); tx(s,3.0,5.88,3.2,.24,"long B-cell aplasia",14,"navy",True); arrow(s,6.5,5.96,1.0,0,C["cyan"],C=C); tx(s,8.0,5.88,3.0,.24,"what sustains it?",14,"navy",True)
    foot(s,"Source: Bai et al., Fig. 1c and reported BCA-L duration. Clinical association only.")

    # 3 — study design as vertical pathway.
    s=base(prs,3,"02 / STUDY DESIGN","The study turns persistence into a measurable system","Five linked layers connect patients, products, cell states, function, and clinical correlation.")
    xs=[1.0,3.25,5.5,7.75,10.0]; nodes=[("01","PATIENTS","82 ALL + 6 healthy","orange"),("02","CAR T PRODUCT","manufactured cells","blue"),("03","MULTI-OMICS","10x 3′ · >10⁶ cells","cyan"),("04","FUNCTION","flow · ATAC · secretion","blue"),("05","CORRELATION","17 states · 5 strata","orange")]
    rule(s,1.25,3.05,9.7,"cyan")
    for i,(num,head,body,col) in enumerate(nodes):
        dot(s,xs[i],2.76,.58,col); tx(s,xs[i],2.98,.58,.12,num,8,"white",True,"Consolas","center"); tx(s,xs[i]-.4,3.55,1.4,.18,head,10,col,True,"Consolas","center"); ml(s,xs[i]-.56,3.94,1.72,.48,body.split(" · "),10,"navy",1.08,"center")
        if i<4: arrow(s,xs[i]+.72,3.03,1.15,0,C["cyan"],C=C)
    tx(s,.86,4.58,1.8,.16,"METHOD LOGIC",8.8,"cyan",True,"Consolas"); tx(s,2.72,4.55,8.9,.20,"sample → molecular profile → functional readout → unsupervised states → clinical correlation",10.5,"navy",True)
    fcase(s,1,"design",(0,0,2122,420),.86,5.10,6.7,.78,"Source: Fig. 1a · editorial redraw of study pipeline")
    stat(s,8.2,5.05,1.8,"695,819","analyzed cells","blue"); stat(s,10.15,5.05,1.8,"17","cell states","orange")
    tx(s,8.2,6.05,3.8,.18,"READOUT LAYERS",8.8,"cyan",True,"Consolas"); tx(s,8.2,6.33,4.0,.34,"transcriptome · flow cytometry · secretome · ATAC",9.5,"navy",True)
    foot(s,"Cohort and assay facts remain tied to Fig. 1a and the paper methods.")

    # 4 — atlas map: large crop and direct legend.
    s=base(prs,4,"03 / CELL ATLAS","A field of 695,819 cells resolves into 17 states","This map is the paper’s transition from clinical phenotype to cellular state.")
    fcase(s,1,"atlas2",(0,300,880,1044),.82,2.12,7.0,4.08,"Source: Fig. 1b · UMAP and cluster annotation")
    tx(s,8.38,2.22,3.8,.18,"FOUR STATE FAMILIES",9,"cyan",True,"Consolas"); rule(s,8.38,2.58,3.65,"cyan")
    for y,head,col,body in [(3.02,"NAIVE","blue","memory / early state"),(3.78,"CYTOTOXIC","orange","effector program"),(4.54,"REGULATORY","cyan","signalling program"),(5.30,"PROLIFERATIVE","green","expansion program")]:
        dot(s,8.42,y+.02,.18,col); tx(s,8.72,y,1.8,.18,head,11,"navy",True); tx(s,8.72,y+.28,2.5,.15,body,8.6,"muted")
    tx(s,8.42,5.86,3.7,.16,"WHAT THE MAP ENABLES",8.8,"cyan",True,"Consolas"); tx(s,8.42,6.10,3.7,.34,"state composition → function → clinical strata",9.8,"navy",True)
    stat(s,8.42,6.52,1.65,"17","cell states","orange"); stat(s,10.42,6.52,1.65,"695,819","cells","blue")
    foot(s,"Original cluster colors are preserved inside the source figure; family labels are editorial grouping, not new clusters.")

    # 5 — ordered strata, not a fake continuous chart.
    s=base(prs,5,"04 / PERSISTENCE AXIS","BCA strata create the clinical gradient","The groups are ordered by reported duration; the slide does not imply a continuous fitted curve.","orange")
    fcase(s,1,"followup",(1050,210,2122,1044),.82,2.06,4.8,2.78,"Source: Fig. 1c · demographics and follow-up")
    tx(s,6.15,2.12,5.7,.18,"REPORTED DURATION / MONTHS",9,"orange",True,"Consolas"); rule(s,6.15,2.48,5.55,"orange")
    groups=[("BCA-L","101","n=5","orange"),("BCA-O","61","n=11","blue"),("BCA3","18","n=11","cyan"),("BCA2","4","n=38","blue"),("BCA1","1","n=17","green")]
    for i,(g,val,n,col) in enumerate(groups):
        x=6.22+i*1.12; rect(s,x,3.04,.82,2.1,fill=C["paper"],line=C[col],C=C); tx(s,x,3.30,.82,.32,val,23,col,True,"Aptos Display","center"); tx(s,x,3.82,.82,.18,g,8.8,col,True,"Consolas","center"); tx(s,x,4.28,.82,.18,n,8.6,"muted",False,"Consolas","center")
    rule(s,.88,5.52,10.95,"cyan"); tx(s,.88,5.84,1.8,.18,"READING RULE",8,"cyan",True,"Consolas"); tx(s,2.7,5.80,8.8,.24,"BCA-L is the extreme anchor; later pages ask what distinguishes that state.",13,"navy",True)
    foot(s,"Reported values shown in months. The clinical axis is associative; it is not itself a mechanistic explanation.")

    # 6 — type 2 convergence: one dominant figure, three claims.
    s=base(prs,6,"05 / TYPE 2 STATE","Long-remission cells show a type 2-like program","Three molecular readouts converge on the same state; the title stays associative.","orange")
    fcase(s,2,"type2",(0,0,1200,1100),.82,2.08,5.25,3.95,"Source: Fig. 2a–d · type 2 score and validation")
    tx(s,6.55,2.14,4.8,.18,"CONVERGENT READOUTS",9,"cyan",True,"Consolas"); rule(s,6.55,2.50,4.85,"cyan")
    for y,head,body,col in [(2.94,"TRANSCRIPTOME","IL4 · IL5 · IL13", "orange"),(3.86,"SECRETION","type 2 cytokines", "cyan"),(4.78,"CHROMATIN","GATA3 / STAT6", "blue")]:
        tx(s,6.58,y,1.7,.17,head,8.6,col,True,"Consolas"); tx(s,8.45,y-.04,2.9,.24,body,13,"navy",True)
    rule(s,6.55,5.74,4.85,"orange"); tx(s,6.55,6.04,4.8,.24,"one coherent type 2 state",15,"orange",True,"Aptos Display")
    tx(s,6.55,6.43,4.8,.16,"Functional context: repeat stimulation → tumour-cell lysis",8.8,"muted",False,"Consolas")
    tx(s,.84,6.66,5.3,.16,"METHOD LOGIC: BCA-stratified cells → type 2 score → secretion → ATAC / transcription factors",8.4,"muted",False,"Consolas")
    foot(s,"Source: Fig. 2. Type 2 enrichment is a cellular association; GATA3/STAT6 perturbation supplies functional context.")

    # 7 — mechanism network with a visible boundary.
    s=base(prs,7,"06 / CANDIDATE MECHANISM","Cluster 2 emerges as a candidate regulatory hub","The paper proposes a network relationship; this page does not turn it into complete causal proof.","blue")
    fcase(s,3,"network",(0,0,1420,820),.82,2.10,5.25,3.2,"Source: Fig. 3a–b · ligand–receptor network")
    fcase(s,3,"cluster2",(1180,0,2125,900),6.45,2.10,3.45,3.2,"Source: Fig. 3c–d · cluster 2 and DEGs")
    stat(s,10.35,2.22,1.3,"13.9%","cluster 2","orange")
    rule(s,.92,5.92,10.8,"cyan"); tx(s,.94,6.22,1.4,.16,"BOUNDARY",8,"orange",True,"Consolas"); tx(s,2.45,6.18,8.9,.25,"candidate network → hypothesis for dysfunctional-subpopulation regulation",13,"navy",True)
    tx(s,2.45,6.58,8.9,.16,"Analysis layers: ligand–receptor links · mTOR signalling · cluster-2 differential expression",8.8,"muted",False,"Consolas")
    foot(s,"Source: Fig. 3. Network and cluster-2 evidence are reproduced; mechanism remains proposed.")

    # 8 — longitudinal serum: large panels and explicit sample window.
    s=base(prs,8,"07 / LONGITUDINAL SERUM","The type 2 signal survives time, not just a snapshot","Serial serum measurements extend the cellular observation into a longitudinal readout.")
    fcase(s,4,"series",(0,0,2124,650),.82,2.08,6.95,2.55,"Source: Fig. 4a–b · collection timeline and time series")
    fcase(s,4,"heat",(0,520,2124,1283),.82,5.10,6.95,1.16,"Source: Fig. 4c–e · cytokine windows and heatmap")
    stat(s,8.45,2.20,1.45,"345","measurements","cyan"); stat(s,10.20,2.20,1.45,"30","cytokines","blue"); stat(s,11.95,2.20,1.0,"33","patients","orange")
    tx(s,8.45,3.42,3.25,.18,"TYPE 2 WINDOW",9,"orange",True,"Consolas"); rule(s,8.45,3.76,3.2,"orange"); ml(s,8.45,4.10,3.2,.92,["IL-4 · IL-5 · IL-13","days 1–63","discovery 33 · validation 8"],11.5,"navy",1.18)
    tx(s,8.45,5.02,3.2,.16,"METHOD LOGIC",8.6,"cyan",True,"Consolas"); ml(s,8.45,5.24,3.2,.46,["serum collection → 30-plex panel","time windows → validation"],9.3,"navy",1.10)
    foot(s,"Source: Fig. 4. Longitudinal serum evidence supports persistence of the biology; it does not replace the cell-state analysis.")

    # 9 — preclinical sequence + selected panels.
    s=base(prs,9,"08 / PRECLINICAL TEST","The state is tested as function in a recall model","The mouse experiment tests expansion, tumour control, and response after rechallenge.","green")
    fcase(s,5,"growth",(0,0,1066,520),.82,2.08,4.05,2.05,"Source: Fig. 5b–c · expansion and tumour flux")
    fcase(s,5,"survival",(0,500,1066,897),.82,4.78,4.05,1.45,"Source: Fig. 5d · survival after rechallenge")
    tx(s,5.55,2.12,5.8,.18,"EXPERIMENTAL SEQUENCE",9,"green",True,"Consolas"); rule(s,5.55,2.46,5.7,"green")
    rule(s,5.85,3.35,4.9,"green")
    for x,day,labv in [(5.92,"−7","Nalm6"),(7.45,"0","CAR T"),(9.0,"17","rechallenge"),(10.65,"24–28","imaging")]:
        dot(s,x,3.22,.23,"green"); tx(s,x-.25,3.68,.7,.18,day,11,"navy",True,"Aptos Display","center"); tx(s,x-.48,4.02,1.0,.16,labv,8.5,"muted",True,"Consolas","center")
    tx(s,5.55,4.72,5.7,.18,"READOUT",9,"cyan",True,"Consolas"); rule(s,5.55,5.06,5.7,"cyan"); ml(s,5.55,5.40,5.7,.62,["Type 2-high cells expand more and show stronger recall in the reported model.","Selected readouts: n=5 mice."],12,"navy",1.15)
    tx(s,5.55,6.22,5.7,.16,"Comparison: type 2-low versus type 2-high CAR T cells",8.8,"muted",False,"Consolas")
    tx(s,5.55,6.48,5.7,.16,"METHOD LOGIC: NSG + Nalm6 → CAR T infusion → tumour rechallenge → imaging / flow",8.4,"muted",False,"Consolas")
    foot(s,"Source: Fig. 5. Preclinical function is demonstrated in the reported model; clinical efficacy is not established.")

    # 10 — engineering workflow.
    s=base(prs,10,"09 / ENGINEERING DIRECTION","IL-4 provides a preclinical manufacturing direction","The final figure asks whether a type 2-like program can be introduced or primed experimentally.","orange")
    fcase(s,6,"workflow",(0,0,1100,1000),.82,2.08,4.55,3.15,"Source: Fig. 6a · priming and ET2-L/H strategies")
    tx(s,5.85,2.12,5.8,.18,"EXPOSURE → PRODUCT → TEST",9,"orange",True,"Consolas"); rule(s,5.85,2.46,5.7,"orange")
    for i,(head,body,col) in enumerate([("PRIME","10 ng ml⁻¹ / 12 h","cyan"),("MANUFACTURE","ET2-L 10 · ET2-H 50","blue"),("TEST","expansion + survival","green")]):
        x=5.9+i*2.0; dot(s,x,3.12,.38,col); tx(s,x-.22,3.78,1.2,.18,head,8.4,col,True,"Consolas","center"); ml(s,x-.42,4.12,1.6,.54,body.split(" · "),10,"navy",1.08,"center");
        if i<2: arrow(s,x+.5,3.27,.9,0,C["cyan"],C=C)
    tx(s,5.9,4.82,5.8,.16,"Culture context: IL-7 + IL-15; dose labels remain paper-specific",8.8,"muted",False,"Consolas")
    tx(s,5.9,5.10,5.8,.16,"METHOD LOGIC: type 2-low donor cells → IL-4 priming / enhanced culture → CAR T expansion → mouse test",8.4,"muted",False,"Consolas")
    fcase(s,6,"result",(0,850,1250,1523),.82,5.36,4.55,1.02,"Source: Fig. 6c–d · expansion and survival")
    tx(s,8.35,5.40,3.25,.18,"BOUNDARY",9,"orange",True,"Consolas"); rule(s,8.35,5.74,3.2,"orange"); tx(s,8.35,6.08,3.35,.24,"promising lever, still preclinical",13,"navy",True)
    foot(s,"Source: Fig. 6. Concentrations and ET2-L/H labels remain tied to the paper; engineering framing is editorial.")

    # 11 — evidence ladder.
    s=base(prs,11,"10 / EVIDENCE LADDER","The argument is strongest when evidence types stay separate","A disciplined reading keeps association, state definition, mechanism, and intervention distinct.")
    levels=[("01","OBSERVED","8.4-year persistence","BCA-L 101 months · Fig. 1c / 4","clinical","orange"),("02","RESOLVED","type 2-like state","IL4 · IL5 · IL13 · GATA3 · Fig. 2","cellular","cyan"),("03","PROPOSED","cluster 2 network","ligand–receptor links · DEGs · Fig. 3","mechanism","blue"),("04","TESTED","recall + IL-4","mouse expansion · rechallenge · Fig. 5 / 6","preclinical","green")]
    for i,(num,kind,claim,evidence,domain,col) in enumerate(levels):
        x=.92+i*2.95; h=1.15+i*.55; y=5.92-h; rect(s,x,y,2.25,h,fill=C["paper"],line=C[col],C=C); tx(s,x+.18,y+.18,1.9,.15,num+"  /  "+kind,8,col,True,"Consolas"); tx(s,x+.18,y+.52,1.9,.23,claim,12,"navy",True); tx(s,x+.18,y+.86,1.9,.15,domain,8.5,"muted",False,"Consolas"); tx(s,x+.18,y+1.05,1.9,.28,evidence,7.2,"muted",False,"Consolas")
        if i<3: arrow(s,x+2.32,5.52,0.45,0,C["cyan"],C=C)
    rule(s,.92,6.26,11.1,"cyan"); tx(s,.92,6.48,10.9,.18,"association → state definition → candidate explanation → functional test / engineering lever",9.4,"muted",False,"Consolas")
    foot(s,"Figure refs: Fig. 1/4 → Fig. 2 → Fig. 3 → Fig. 5/6. The ladder is an editorial summary, not a new result.")

    # 12 — close: contribution, limit, figure index.
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["bg"],C=C)
    tx(s,.84,.86,3,.16,"THE BOUNDED TAKEAWAY",9,"orange",True,"Consolas"); tx(s,.84,1.38,5.25,1.0,"""Type 2 function
may sustain fitness.""",28,"navy",True,"Aptos Display")
    ml(s,.86,2.86,4.8,1.28,["A durable clinical phenotype", "becomes a recognizable cell state,", "a candidate circuit, and a preclinical lever."],14,"muted",1.18)
    rule(s,.86,4.65,4.1,"cyan"); tx(s,.86,5.02,4.6,.25,"Contribution",11,"blue",True); tx(s,.86,5.38,4.65,.56,"connects persistence to cell state and function",13,"navy",True)
    tx(s,6.42,.98,5.3,.18,"EVIDENCE MAP",9,"cyan",True,"Consolas"); rule(s,6.42,1.32,5.35,"cyan")
    fcase(s,2,"close2",(0,0,900,950),6.42,1.64,2.55,2.15,"Fig. 2 · cellular state")
    fcase(s,3,"close3",(0,0,1100,900),9.30,1.64,2.55,2.15,"Fig. 3 · candidate network")
    fcase(s,6,"close6",(0,0,1250,1523),6.42,4.30,5.43,1.92,"Fig. 6 · engineering direction")
    tx(s,6.42,6.52,5.4,.16,"LIMITS",8.8,"orange",True,"Consolas"); ml(s,6.42,6.76,5.5,.34,["Optimal clinical type-2 level remains to be established; preclinical models do not establish efficacy."],9.4,"navy",1.08)
    tx(s,.86,6.86,5.4,.12,"Bai et al. · Nature 634 · 702–711 · 2024",7.2,"muted",False,"Consolas")
    prs.save(OUT); print(OUT)

if __name__ == "__main__": build()
