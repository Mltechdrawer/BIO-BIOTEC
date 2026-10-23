from pathlib import Path
import json, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
from Bio import Phylo
ROOT=Path(__file__).resolve().parent;R=json.loads((ROOT/'resultados.json').read_text());out=ROOT/'imagenes';out.mkdir(exist_ok=True)
short={'Homo sapiens':'Human','Pan troglodytes':'Chimpanzee','Gorilla gorilla':'Gorilla','Pongo pygmaeus':'Orangutan','Hylobates lar':'Gibbon'}
frames=[]
def base(title,subtitle):
 fig=plt.figure(figsize=(12,6.75),facecolor='#f9fbfd');fig.text(.06,.93,title,fontsize=23,fontweight='bold',color='#18324b');fig.text(.06,.875,subtitle,fontsize=12,color='#4d6479');return fig
def save(fig,repeat=2):
 fig.canvas.draw();im=Image.frombytes('RGB',fig.canvas.get_width_height(),fig.canvas.tostring_rgb()) if hasattr(fig.canvas,'tostring_rgb') else Image.frombuffer('RGBA',fig.canvas.get_width_height(),fig.canvas.buffer_rgba()).convert('RGB');frames.extend([im.copy()]*repeat);plt.close(fig)
fig=base('From DNA sequences to a phylogenetic tree','Five primates · mitochondrial COX1 · real GenBank records')
for i,(n,acc) in enumerate(zip(R['names'],R['ids'])):fig.text(.12,.75-i*.12,f'{short[n]:<13}    {acc}    {len(R["msa"][n].replace("-",""))} nt',fontfamily='monospace',fontsize=15,color='#244a66')
fig.text(.12,.1,'1  Select and validate homologous sequences',fontsize=15,color='#167a7c');save(fig,4)
fig=base('Multiple sequence alignment','Reference-anchored global alignment · 1,560 columns · selected window')
start=75;end=120
for i,n in enumerate(R['names']):
 fig.text(.08,.75-i*.125,short[n],fontsize=14,color='#18324b');fig.text(.30,.75-i*.125,R['msa'][n][start:end],fontfamily='monospace',fontsize=13,color='#235b79')
fig.text(.08,.1,'2  Compare homologous positions before measuring differences',fontsize=14,color='#167a7c');save(fig,4)
fig=base('Genetic distance matrix','p-distance = nucleotide differences / comparable sites')
ax=fig.add_axes([.17,.15,.55,.64]);m=np.array(R['matrix']);ax.imshow(m,cmap='Blues',vmin=0,vmax=.17)
ax.set_xticks(range(5),[short[n] for n in R['names']],rotation=30,ha='right');ax.set_yticks(range(5),[short[n] for n in R['names']]);
for i in range(5):
 for j in range(5):ax.text(j,i,f'{m[i,j]:.3f}',ha='center',va='center',color='white' if m[i,j]>.1 else '#18324b',fontsize=12)
fig.text(.77,.50,'3  Calculate the ten\npairwise distances',fontsize=14,color='#167a7c');save(fig,5)
for s in R['steps']:
 fig=base(f'UPGMA · merge {s["step"]} of 4',f'Merge {s["a"]} + {s["b"]} · distance {s["distance"]:.5f} · node height {s["height"]:.5f}')
 snap=R['snapshots'][s['step']-1]; labels=snap['clusters'];mat=np.array(snap['matrix']);n=len(labels)
 ax=fig.add_axes([.08,.21,.56,.59]);ax.imshow(mat,cmap='Blues',vmin=0,vmax=.17);ax.set_xticks(range(n),[short.get(k,k) for k in labels],rotation=28,ha='right');ax.set_yticks(range(n),[short.get(k,k) for k in labels]);
 for i in range(n):
  for j in range(n):
   ax.text(j,i,f'{mat[i,j]:.3f}',ha='center',va='center',fontsize=12,color='white' if mat[i,j]>.1 else '#18324b')
 ax.add_patch(plt.Rectangle((labels.index(s['a'])-.48,labels.index(s['b'])-.48),.96,.96,fill=False,edgecolor='#d66b2d',linewidth=3))
 ax.add_patch(plt.Rectangle((labels.index(s['b'])-.48,labels.index(s['a'])-.48),.96,.96,fill=False,edgecolor='#d66b2d',linewidth=3))
 fig.text(.68,.67,'Closest clusters',fontsize=17,fontweight='bold',color='#18324b');fig.text(.68,.56,f'{s["a"]} + {s["b"]}',fontsize=13,color='#167a7c');fig.text(.68,.40,'Updated distances:',fontsize=13,color='#18324b')
 for k,(name,val) in enumerate(s['updated'].items()):fig.text(.68,.33-.07*k,f'{name}: {val:.5f}',fontsize=12,color='#235b79')
 save(fig,5)
fig=base('Final UPGMA tree','Branch lengths represent p-distance units · UPGMA assumes a molecular clock')
ax=fig.add_axes([.1,.15,.78,.67]);tree=Phylo.read(str(ROOT/'arbol-upgma.nwk'),'newick');Phylo.draw(tree,axes=ax,do_show=False,label_func=lambda c: short.get(c.name.replace('_',' '),c.name) if c.is_terminal() else None,show_confidence=False)
ax.set_xlabel('p-distance');ax.set_ylabel('');save(fig,7)
frames[0].save(out/'construccion-upgma.gif',save_all=True,append_images=frames[1:],duration=1100,loop=0,optimize=True)
fig=base('Final UPGMA tree','Mitochondrial COX1 · five primates');ax=fig.add_axes([.1,.15,.78,.67]);Phylo.draw(tree,axes=ax,do_show=False,label_func=lambda c:short.get(c.name.replace('_',' '),c.name) if c.is_terminal() else None);ax.set_xlabel('p-distance');fig.savefig(out/'arbol-upgma.png',dpi=170);plt.close(fig)
print('GIF',out/'construccion-upgma.gif')
