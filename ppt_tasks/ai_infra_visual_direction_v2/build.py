from pathlib import Path
from pptx_designer import Presentation
from pptx_designer.tools.shapes import rect, rrect, arrow
from pptx_designer.tools.text import text, multiline

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output" / "ai_infra_visual_direction_v2.pptx"
C = {"ink":"#182338","ink2":"#E9E1D4","paper":"#F5F0E8","paper2":"#E9E1D4","muted":"#6B7280","rule":"#C9C0B2","cyan":"#245BDB","red":"#C6473B","lime":"#6B8E5A","green":"#6B8E5A","white":"#FFFFFF"}

def t(s,x,y,w,h,v,size=14,color="ink",bold=False,font="Aptos",align=None):
    kw=dict(font_size=size,color=C[color],bold=bold,font_name=font,C=C)
    if align is not None: kw["align"]=align
    return text(s,x,y,w,h,v,**kw)
def m(s,x,y,w,h,lines,size=12,color="muted",spacing=1.1):
    return multiline(s,x,y,w,h,lines,font_size=size,color=C[color],C=C,line_spacing=spacing)
def line(s,x,y,w,h=0.02,color="rule"): rect(s,x,y,w,h,fill=C[color],C=C)
def base(prs,num,section,title,subtitle=None):
    s=prs.slides.add_slide(prs.slide_layouts[6]); rect(s,0,0,13.333,7.5,fill=C["paper"],C=C)
    line(s,0.62,0.55,0.04,6.35,"rule")
    for x in (2.15,5.0,7.85,10.7): line(s,x,0.55,0.012,6.35,"rule")
    t(s,0.82,0.48,2.4,0.2,section,9,"cyan",True,"Consolas")
    t(s,11.65,0.48,0.85,0.2,f"02 / {num:02d}",9,"muted",False,"Consolas","right")
    if title: t(s,0.82,0.92,11.3,0.58,title,24,"ink",True)
    if subtitle: t(s,0.84,1.53,10.8,0.25,subtitle,11,"muted")
    t(s,0.84,7.04,5.5,0.16,"AI INFRASTRUCTURE ECONOMICS / VISUAL DIRECTION V2",8,"muted",False,"Consolas")
    t(s,11.72,7.04,0.7,0.16,f"{num:02d} / 03",8,"muted",False,"Consolas","right")
    return s
def main():
    prs=Presentation()
    s=base(prs,1,"INFRASTRUCTURE LEDGER / PROTOTYPE","AI infrastructure is a physical system.","Capital moves first. Constraints decide what ships.")
    t(s,0.84,2.2,4.6,1.1,"The margin pool can move upward.\nThe bottleneck stays physical.",20,"lime",True)
    line(s,0.84,3.78,1.65,0.06,"red"); m(s,0.84,4.14,3.9,0.8,["A visual baseline for capacity,","compute, energy, and operating choice."],13,"ink")
    t(s,7.15,1.72,3.6,0.22,"THE VALUE CHAIN IS PHYSICAL",9,"muted",True,"Consolas")
    for y,w,label,accent in [(2.15,4.8,"APPLICATIONS","green"),(2.85,4.25,"PLATFORM","cyan"),(3.55,3.7,"COMPUTE","red"),(4.25,3.15,"POWER + PLACE","ink")]:
        x=8.0-(w-3.15)/2; rrect(s,x,y,w,0.55,fill=C["ink2"],line=C[accent],C=C); t(s,x+0.2,y+0.17,w-0.4,0.16,label,10,accent,True,"Consolas","center")
    t(s,7.38,5.1,4.45,0.5,"PHYSICAL\nBEFORE DIGITAL",27,"ink",True,"Consolas")
    s=base(prs,2,"04 / BOTTLENECK","Capacity only ships when the slowest layer arrives.","Land, energy, networking, and servers arrive on different clocks.")
    t(s,0.84,2.22,2.0,0.18,"ARRIVAL ORDER",10,"cyan",True,"Consolas")
    stages=[(1,"LAND","permitted + buildable","red"),(3.85,"ENERGY","predictable supply","red"),(6.7,"NETWORK","fabric + interconnect","cyan"),(9.55,"SERVERS","GPU + components","cyan")]
    for i,(x,label,body,accent) in enumerate(stages,1):
        t(s,x,2.78,0.45,0.2,f"0{i}",11,accent,True,"Consolas"); line(s,x,3.2,2.15,0.07,accent); t(s,x,3.55,2.2,0.26,label,18,"ink",True,"Consolas"); m(s,x,4.0,2.2,0.55,[body,"lead time ≠ demand"],11,"muted")
        if i<4: arrow(s,x+2.3,3.18,0.33,0.18,fill=C["rule"],C=C)
    line(s,1.0,5.42,10.7,0.04,"red"); t(s,1.0,5.72,9.9,0.32,"THE SLOWEST LAYER SETS THE CLOCK.",19,"red",True,"Consolas"); t(s,10.3,5.7,1.5,0.3,"CONSTRAINT",10,"lime",True,"Consolas","right")
    s=base(prs,3,"08 / RISK","The dangerous asset is capacity you cannot use.","Risk appears when long lead time meets low utilization.")
    t(s,0.84,2.15,3.1,0.2,"LEAD TIME  ↑",10,"red",True,"Consolas"); t(s,5.25,6.3,2.5,0.2,"UTILIZATION  →",10,"cyan",True,"Consolas","center")
    rect(s,1.1,2.75,3.1,1.35,fill="#F0D8D1",C=C); rect(s,4.25,2.75,3.1,1.35,fill="#E6DDE8",C=C); rect(s,1.1,4.15,3.1,1.35,fill="#DCE7D3",C=C); rect(s,4.25,4.15,3.1,1.35,fill="#DDE7FF",C=C)
    line(s,1.1,4.1,6.25,0.03,"paper"); line(s,4.2,2.75,0.03,2.75,"paper")
    for x,y,label,body,accent in [(1.35,3.0,"STRANDED","fixed cost · no flexibility","red"),(4.5,3.0,"BOTTLENECK","demand exists · supply lags","lime"),(1.35,4.4,"UNDERUSE","capacity exists · demand is soft","green"),(4.5,4.4,"HEALTHY","matched load · optionality","cyan")]:
        t(s,x,y,2.5,0.2,label,14,accent,True,"Consolas"); t(s,x,y+0.42,2.5,0.18,body,10,"ink")
    line(s,8.75,2.6,0.06,3.2,"red"); t(s,9.15,2.65,2.5,0.18,"WATCH ITEM",10,"red",True,"Consolas"); t(s,9.15,3.15,3.0,1.0,"Lead time\ncan outlive\ndemand.",24,"ink",True); m(s,9.15,4.55,2.6,0.65,["Hold capacity as an option.","Prove demand before ownership."],10,"muted")
    prs.save(str(OUT)); print(f"Saved: {OUT}")
if __name__=="__main__": main()
