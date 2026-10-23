from pathlib import Path
from Bio import SeqIO, Align
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import Phylo
import csv,io,json
ROOT=Path(__file__).resolve().parent
names=['Homo sapiens','Pan troglodytes','Gorilla gorilla','Pongo pygmaeus','Hylobates lar']
ids=['NC_012920.1','NC_001643.1','NC_001645.1','NC_001646.1','NC_002082.1']
seqs={};validation=[]
for name,acc in zip(names,ids):
 p=ROOT/'genbank'/f'sequence_{acc}.gb';r=SeqIO.read(p,'genbank')
 assert r.id==acc and r.annotations['organism']==name
 fs=[f for f in r.features if f.type=='CDS' and f.qualifiers.get('gene',[''])[0].upper() in ('COX1','COI','MT-CO1')]
 assert len(fs)==1
 f=fs[0];s=str(f.extract(r.seq)).upper();assert set(s)<=set('ACGT')
 assert len(s)%3==0
 translation=str(Seq(s).translate(table=2)); internal=translation[:-1].count('*')
 assert internal==0
 seqs[name]=s
 validation.append([name,acc,str(f.location),len(s),s.count('N'),f.qualifiers.get('transl_table',[''])[0],internal])
with (ROOT/'validacion-cox1.csv').open('w',newline='') as h:
 w=csv.writer(h);w.writerow(['organismo','accesion','coordenadas_0_based','longitud_nt','N','codigo_genetico','paradas_internas']);w.writerows(validation)
SeqIO.write([SeqRecord(Seq(seqs[n]),id=n.replace(' ','_'),description=acc) for n,acc in zip(names,ids)],ROOT/'secuencias-cox1.fasta','fasta')
# Progressive reference-anchored multiple alignment. Each sequence globally aligned to human,
# then insertions in the human reference are merged into shared columns.
ref=seqs[names[0]]
a=Align.PairwiseAligner(mode='global',match_score=2,mismatch_score=-1,open_gap_score=-6,extend_gap_score=-0.5)
def align_to_ref(other):
 al=a.align(ref,other)[0];ar,ao=al[0],al[1]; ins={i:'' for i in range(len(ref)+1)};base={};pos=0
 for x,y in zip(ar,ao):
  if x=='-':ins[pos]+=y
  else:
   base[pos]=y;pos+=1
 assert pos==len(ref)
 return ins,base
aligned={n:align_to_ref(seqs[n]) for n in names}
maxins={i:max(len(aligned[n][0][i]) for n in names) for i in range(len(ref)+1)}
msa={}
for n in names:
 ins,base=aligned[n];parts=[]
 for i in range(len(ref)+1):
  parts.append(ins[i].ljust(maxins[i],'-'))
  if i<len(ref):parts.append(base[i])
 msa[n]=''.join(parts)
assert len(set(map(len,msa.values())))==1
assert all(msa[n].replace('-','')==seqs[n] for n in names)
SeqIO.write([SeqRecord(Seq(msa[n]),id=n.replace(' ','_'),description='reference anchored global alignment') for n in names],ROOT/'alineamiento-cox1.fasta','fasta')
L=len(next(iter(msa.values())));dist={};counts={}
for i in range(len(names)):
 for j in range(i):
  x,y=msa[names[i]],msa[names[j]];valid=[(u,v) for u,v in zip(x,y) if u in 'ACGT' and v in 'ACGT'];c=sum(u!=v for u,v in valid);d=c/len(valid)
  dist[frozenset([names[i],names[j]])]=d;counts[frozenset([names[i],names[j]])]=(c,len(valid))
with (ROOT/'distancias.csv').open('w',newline='') as h:
 w=csv.writer(h);w.writerow(['especie']+names)
 for x in names:w.writerow([x]+[f'{dist.get(frozenset([x,y]),0):.9f}' for y in names])
with (ROOT/'diferencias.csv').open('w',newline='') as h:
 w=csv.writer(h);w.writerow(['especie_1','especie_2','diferencias','posiciones_comparables','distancia_p'])
 for i in range(len(names)):
  for j in range(i):
   c,k=counts[frozenset([names[i],names[j]])];w.writerow([names[i],names[j],c,k,f'{c/k:.9f}'])
clusters={n:{'members':[n],'height':0.,'newick':n.replace(' ','_')} for n in names};dists=dist.copy();steps=[];snapshots=[]
while len(clusters)>1:
 order=sorted(clusters)
 snapshots.append({'clusters':order,'matrix':[[0 if x==y else dists[frozenset([x,y])] for y in order] for x in order]})
 key=min(dists,key=lambda k:(dists[k],tuple(sorted(k))));x,y=sorted(key);d=dists[key];h=d/2;cx,cy=clusters[x],clusters[y];new=f'G{len(steps)+1}'
 nd={z:(len(cx['members'])*dists[frozenset([x,z])]+len(cy['members'])*dists[frozenset([y,z])])/(len(cx['members'])+len(cy['members'])) for z in clusters if z not in (x,y)}
 steps.append({'step':len(steps)+1,'a':x,'b':y,'distance':d,'height':h,'members_a':cx['members'],'members_b':cy['members'],'new':new,'updated':nd})
 nw=f"({cx['newick']}:{h-cx['height']:.9f},{cy['newick']}:{h-cy['height']:.9f})"
 dists={k:v for k,v in dists.items() if x not in k and y not in k};del clusters[x];del clusters[y]
 clusters[new]={'members':cx['members']+cy['members'],'height':h,'newick':nw}
 for z,v in nd.items():dists[frozenset([new,z])]=v
newick=next(iter(clusters.values()))['newick']+';';(ROOT/'arbol-upgma.nwk').write_text(newick+'\n')
with (ROOT/'iteraciones-upgma.csv').open('w',newline='') as h:
 w=csv.writer(h);w.writerow(['paso','grupo_A','grupo_B','distancia','altura','miembros_A','miembros_B','nuevo_grupo','nuevas_distancias'])
 for s in steps:w.writerow([s['step'],s['a'],s['b'],s['distance'],s['height'],';'.join(s['members_a']),';'.join(s['members_b']),s['new'],str(s['updated'])])
tree=Phylo.read(io.StringIO(newick),'newick');heights=list(tree.depths().values());leafdepths=[tree.depths()[t] for t in tree.get_terminals()];assert max(leafdepths)-min(leafdepths)<1e-7
(ROOT/'resultados.json').write_text(json.dumps({'names':names,'ids':ids,'validation':validation,'alignment_length':L,'msa':msa,'snapshots':snapshots,'steps':steps,'newick':newick,'matrix':snapshots[0]['matrix']},ensure_ascii=False,indent=2))
print('length',L,'steps',steps,'newick',newick)
