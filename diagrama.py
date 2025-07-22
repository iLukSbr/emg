from graphviz import Digraph

# Criar um novo grafo direcionado (fluxograma)
dot = Digraph(comment='Fluxograma de Processamento de Sinal EMG', format='pdf')

# Definir atributos do grafo para melhor legibilidade e ajuste ao tamanho A4 (landscape)
dot.attr(
    rankdir='LR',
    size='11.7,8.3!',
    ratio='fill',
    margin='0.4',
    bgcolor='#f8fafc'
)

# Adicionar título com nome, disciplina e nome do circuito
dot.attr(
    label='Fluxograma do Circuito EMG\nDisciplina: Eletrônica 3: Amplificadores\nAluno: Lucas Yukio Fukuda Matsumoto\n27/05/2025',
    labelloc='t',
    fontsize='18',
    fontname='Helvetica Bold',
    fontcolor='#1a202c'
)

# Adicionar nós com estilos aprimorados
dot.node('A', 'Conectar eletrodos ao paciente', shape='oval', style='filled,setlinewidth(2),shadow', fillcolor='#e0f2fe', fontname='Helvetica', fontsize='13', color='#0284c7')
dot.node('B', 'Adquirir sinal\n(Amplificador Diferencial)', shape='box', style='rounded,filled,setlinewidth(2),shadow', fillcolor='#f1f5f9', fontname='Helvetica', fontsize='13', color='#0ea5e9')
dot.node('C', 'Aplicar Filtro\nPassa-Alta', shape='box', style='rounded,filled,setlinewidth(2),shadow', fillcolor='#f1f5f9', fontname='Helvetica', fontsize='13', color='#0ea5e9')
dot.node('D', 'Aplicar Filtro\nPassa-Baixa', shape='box', style='rounded,filled,setlinewidth(2),shadow', fillcolor='#f1f5f9', fontname='Helvetica', fontsize='13', color='#0ea5e9')
dot.node('E', 'Ajustar Ganho\n(Amplificador Ajustável)', shape='box', style='rounded,filled,setlinewidth(2),shadow', fillcolor='#f1f5f9', fontname='Helvetica', fontsize='13', color='#0ea5e9')
dot.node('I', 'Saída de Sinal\npara MCU', shape='parallelogram', style='filled,setlinewidth(2),shadow', fillcolor='#dbeafe', fontname='Helvetica', fontsize='13', color='#2563eb')
dot.node('K', 'Ler Sinal\nAnalógico', shape='parallelogram', style='filled,setlinewidth(2),shadow', fillcolor='#dbeafe', fontname='Helvetica', fontsize='13', color='#2563eb')
dot.node('N', 'Processar Dados\nRecebidos do MCU\n(Filtragem, Normalização, etc.)', shape='box', style='rounded,filled,setlinewidth(2),shadow', fillcolor='#fef9c3', fontname='Helvetica', fontsize='13', color='#eab308')
dot.node('L', 'Visualizar Gráfico\nno PC', shape='box', style='rounded,filled,setlinewidth(2),shadow', fillcolor='#f1f5f9', fontname='Helvetica', fontsize='13', color='#0ea5e9')
dot.node('M', 'Fim', shape='oval', style='filled,setlinewidth(2),shadow', fillcolor='#e0f2fe', fontname='Helvetica', fontsize='13', color='#0284c7')

# Adicionar arestas com cor e espessura
edge_style = {'color': '#64748b', 'penwidth': '2'}
dot.edge('A', 'B', **edge_style)
dot.edge('B', 'C', **edge_style)
dot.edge('C', 'D', **edge_style)
dot.edge('D', 'E', **edge_style)
dot.edge('E', 'I', **edge_style)
dot.edge('I', 'K', **edge_style)
dot.edge('K', 'N', **edge_style)
dot.edge('N', 'L', **edge_style)
dot.edge('L', 'M', **edge_style)

# Agrupar nós para melhor organização
with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('B')
    s.node('C')
    s.node('D')

with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('E')
    s.node('I')

with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('N')
    s.node('L')

# Renderizar o fluxograma em um arquivo PDF (A4)
dot.render('fluxograma_emg', view=True)

print("Fluxograma gerado como 'fluxograma_emg.pdf'")
