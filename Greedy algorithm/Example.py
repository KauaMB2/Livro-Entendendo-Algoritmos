estados_abranger=set(['mt','wa','or','id','nv','ut','ca','az'])#Estados que podem ser abrangidos
estacoes={}
estacoes['kum']=set(['id','nv','ut'])
estacoes['kdois']=set(['wa','id','mt'])
estacoes['ktres']=set(['or','nv','ca'])
estacoes['kquatro']=set(['nv','ut'])
estacoes['kcinco']=set(['ca','az'])
estacoes_final=set()
while estados_abranger:#Enquanto o estado abranger não está vazio...
    melhor_estacao=None
    estados_cobertos=set()
    for estacao, estados_por_estacao in estacoes.items():
        cobertos=estados_abranger & estados_por_estacao#Intersecção
        if len(cobertos) > len(estados_cobertos):#Se a quantidade de estados cobertos pela estação atual for maior que a quantidade de estados pela cobertos pela última melhor estação verificada...
            melhor_estacao=estacao#Define-se que a melhor estação será a que está sendo verificada atualmente
            estados_cobertos=cobertos#Define-se que os estados cobertos são os estados da estação atual
    estados_abranger-=estados_cobertos#Retira os estados que serão abrangidos do conjunto de todos os estados
    estacoes_final.add(melhor_estacao)
print(estacoes_final)


