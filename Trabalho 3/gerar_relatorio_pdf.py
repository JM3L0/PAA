"""
Gerador de Relatório PDF - Problema das N-Rainhas
Análise Comparativa: Backtracking vs Guloso Simples vs Guloso com Restart
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
import pandas as pd
from datetime import datetime
import os

def criar_relatorio_pdf():
    # Configurações
    pdf_file = "Relatorio_N_Rainhas.pdf"
    
    # Criar documento
    doc = SimpleDocTemplate(pdf_file, pagesize=A4,
                           topMargin=2*cm, bottomMargin=2*cm,
                           leftMargin=2*cm, rightMargin=2*cm)
    
    elementos = []
    estilos = getSampleStyleSheet()
    
    # Estilos personalizados
    estilo_titulo = ParagraphStyle(
        'TituloCustom',
        parent=estilos['Title'],
        fontSize=24,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    estilo_subtitulo = ParagraphStyle(
        'SubtituloCustom',
        parent=estilos['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    estilo_secao = ParagraphStyle(
        'SecaoCustom',
        parent=estilos['Heading2'],
        fontSize=13,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    )
    
    estilo_corpo = ParagraphStyle(
        'CorpoCustom',
        parent=estilos['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        leading=14
    )
    
    estilo_codigo = ParagraphStyle(
        'CodigoCustom',
        parent=estilos['Code'],
        fontSize=9,
        leftIndent=20,
        spaceAfter=10,
        fontName='Courier'
    )
    
    # PÁGINA 1: Capa
    elementos.append(Spacer(1, 3*cm))
    elementos.append(Paragraph("RELATÓRIO TÉCNICO", estilo_titulo))
    elementos.append(Spacer(1, 0.5*cm))
    elementos.append(Paragraph("Problema das N-Rainhas", estilo_subtitulo))
    elementos.append(Paragraph("Análise Comparativa de Algoritmos", estilo_subtitulo))
    elementos.append(Spacer(1, 2*cm))
    
    info_capa = [
        ["<b>Algoritmos Implementados:</b>"],
        ["• Backtracking (Busca Completa)"],
        ["• Guloso Simples (Heurística Determinística)"],
        ["• Guloso com Restart (Heurística Randomizada)"],
        [""],
        [f"<b>Data:</b> {datetime.now().strftime('%d/%m/%Y')}"],
        ["<b>Linguagem:</b> Python 3.12"],
        ["<b>Métricas:</b> Tempo, Memória, Taxa de Sucesso"]
    ]
    
    tabela_info = Table(info_capa, colWidths=[15*cm])
    tabela_info.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 11),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2c3e50')),
    ]))
    elementos.append(tabela_info)
    
    elementos.append(PageBreak())
    
    # PÁGINA 2: Resumo Executivo
    elementos.append(Paragraph("1. RESUMO EXECUTIVO", estilo_subtitulo))
    
    elementos.append(Paragraph(
        "Este relatório apresenta uma análise comparativa de três abordagens algorítmicas "
        "para resolver o Problema das N-Rainhas: Backtracking, Guloso Simples e Guloso com Restart. "
        "Os experimentos foram conduzidos para valores de N entre 4 e 14, medindo tempo de execução, "
        "consumo de memória e taxa de sucesso.",
        estilo_corpo
    ))
    
    elementos.append(Paragraph("1.1 Principais Resultados", estilo_secao))
    
    resultados_principais = [
        ["<b>Algoritmo</b>", "<b>Complexidade</b>", "<b>Taxa Sucesso</b>", "<b>Tempo N=12</b>"],
        ["Backtracking", "O(N!)", "100%", "28.34s"],
        ["Guloso Simples", "O(N²)", "7% (1/14)", "0.0006s"],
        ["Guloso Restart", "O(N²)", "100%", "0.011s"],
    ]
    
    tabela_resultados = Table(resultados_principais, colWidths=[4*cm, 3.5*cm, 3.5*cm, 3.5*cm])
    tabela_resultados.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
    ]))
    elementos.append(tabela_resultados)
    elementos.append(Spacer(1, 0.5*cm))
    
    elementos.append(Paragraph(
        "<b>Conclusão Principal:</b> Guloso com Restart combina eficiência (2.580x mais rápido que Backtracking) "
        "com confiabilidade (100% de sucesso), sendo a melhor escolha para N grande.",
        estilo_corpo
    ))
    
    elementos.append(PageBreak())
    
    # PÁGINA 3: Descrição dos Algoritmos
    elementos.append(Paragraph("2. ALGORITMOS IMPLEMENTADOS", estilo_subtitulo))
    
    elementos.append(Paragraph("2.1 Backtracking", estilo_secao))
    elementos.append(Paragraph(
        "Algoritmo de busca completa que explora todas as possibilidades através de recursão. "
        "Garante encontrar todas as soluções válidas mas com complexidade exponencial O(N!).",
        estilo_corpo
    ))
    
    elementos.append(Paragraph("Características:", estilo_corpo))
    caracteristicas_bt = [
        ["✓ Solução garantida", "✓ Encontra todas as soluções"],
        ["✗ Tempo exponencial", "✗ Alto consumo de memória"],
    ]
    tab_bt = Table(caracteristicas_bt, colWidths=[7*cm, 7*cm])
    tab_bt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#ecf0f1')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    elementos.append(tab_bt)
    elementos.append(Spacer(1, 0.3*cm))
    
    elementos.append(Paragraph("2.2 Guloso Simples", estilo_secao))
    elementos.append(Paragraph(
        "Heurística determinística que escolhe a posição com menor número de conflitos a cada linha. "
        "Rápido mas frequentemente falha em encontrar solução válida.",
        estilo_corpo
    ))
    
    caracteristicas_gs = [
        ["✓ Muito rápido O(N²)", "✓ Baixo consumo de memória"],
        ["✗ Taxa de falha 93%", "✗ Determinístico (sempre falha nos mesmos casos)"],
    ]
    tab_gs = Table(caracteristicas_gs, colWidths=[7*cm, 7*cm])
    tab_gs.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#ecf0f1')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    elementos.append(tab_gs)
    elementos.append(Spacer(1, 0.3*cm))
    
    elementos.append(Paragraph("2.3 Guloso com Restart", estilo_secao))
    elementos.append(Paragraph(
        "Versão randomizada do guloso que usa aleatoriedade na escolha entre posições empatadas. "
        "Permite até 100 tentativas, garantindo alta taxa de sucesso mantendo eficiência.",
        estilo_corpo
    ))
    
    caracteristicas_gr = [
        ["✓ Rápido O(N²)", "✓ Taxa de sucesso 100%"],
        ["✓ Escalável para N grande", "✓ Memória constante"],
    ]
    tab_gr = Table(caracteristicas_gr, colWidths=[7*cm, 7*cm])
    tab_gr.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#ecf0f1')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    elementos.append(tab_gr)
    
    elementos.append(PageBreak())
    
    # PÁGINA 4: Resultados Experimentais
    elementos.append(Paragraph("3. RESULTADOS EXPERIMENTAIS", estilo_subtitulo))
    
    elementos.append(Paragraph("3.1 Configuração dos Experimentos", estilo_secao))
    config_exp = [
        ["<b>Parâmetro</b>", "<b>Valor</b>"],
        ["Linguagem", "Python 3.12"],
        ["Sistema Operacional", "Windows"],
        ["Valores de N testados", "4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14"],
        ["Medição de tempo", "time.perf_counter()"],
        ["Medição de memória", "tracemalloc"],
        ["Tentativas (Guloso Restart)", "Máximo 100"],
    ]
    
    tab_config = Table(config_exp, colWidths=[6*cm, 8*cm])
    tab_config.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#ecf0f1')),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ]))
    elementos.append(tab_config)
    
    elementos.append(Spacer(1, 0.5*cm))
    elementos.append(Paragraph("3.2 Dados Completos", estilo_secao))
    
    # Carregar dados do CSV
    df = pd.read_csv('resultados/tabela_resultados_n_rainhas.csv')
    
    # Tabela de resultados - Tempo
    elementos.append(Paragraph("<b>Tabela 1: Tempo de Execução (segundos)</b>", estilo_corpo))
    
    dados_tempo = [["<b>N</b>", "<b>BT</b>", "<b>G. Simples</b>", "<b>G. Restart</b>", "<b>Speedup<br/>GR vs BT</b>"]]
    for _, row in df.iterrows():
        n = int(row['N'])
        tempo_bt = row['Tempo BT (s)']
        tempo_gs = row['Tempo Guloso Simples (s)']
        tempo_gr = row['Tempo Guloso Restart (s)']
        speedup = tempo_bt / tempo_gr if tempo_gr > 0 else 0
        
        dados_tempo.append([
            str(n),
            f"{tempo_bt:.6f}" if tempo_bt < 1 else f"{tempo_bt:.2f}",
            f"{tempo_gs:.6f}",
            f"{tempo_gr:.6f}" if tempo_gr < 1 else f"{tempo_gr:.3f}",
            f"{speedup:.0f}x"
        ])
    
    tab_tempo = Table(dados_tempo, colWidths=[2*cm, 3*cm, 3*cm, 3*cm, 2.5*cm])
    tab_tempo.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#ecf0f1')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 1), (-1, -1), 'Courier'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
    ]))
    elementos.append(tab_tempo)
    
    elementos.append(PageBreak())
    
    # Continuação - Memória
    elementos.append(Paragraph("<b>Tabela 2: Consumo de Memória (MB)</b>", estilo_corpo))
    
    dados_mem = [["<b>N</b>", "<b>BT</b>", "<b>G. Simples</b>", "<b>G. Restart</b>", "<b>Razão<br/>BT/GR</b>"]]
    for _, row in df.iterrows():
        n = int(row['N'])
        mem_bt = row['Mem BT (MB)']
        mem_gs = row['Mem Guloso Simples (MB)']
        mem_gr = row['Mem Guloso Restart (MB)']
        razao = mem_bt / mem_gr if mem_gr > 0 else 0
        
        dados_mem.append([
            str(n),
            f"{mem_bt:.6f}" if mem_bt < 1 else f"{mem_bt:.2f}",
            f"{mem_gs:.6f}",
            f"{mem_gr:.6f}",
            f"{razao:.0f}x"
        ])
    
    tab_mem = Table(dados_mem, colWidths=[2*cm, 3*cm, 3*cm, 3*cm, 2.5*cm])
    tab_mem.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e74c3c')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#ecf0f1')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 1), (-1, -1), 'Courier'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
    ]))
    elementos.append(tab_mem)
    
    elementos.append(Spacer(1, 0.5*cm))
    
    # Taxa de Sucesso
    elementos.append(Paragraph("<b>Tabela 3: Taxa de Sucesso</b>", estilo_corpo))
    
    dados_sucesso = [["<b>N</b>", "<b>BT</b>", "<b>G. Simples</b>", "<b>G. Restart</b>", "<b>Soluções<br/>Totais</b>"]]
    for _, row in df.iterrows():
        n = int(row['N'])
        num_sol = int(row['Num Solucoes BT'])
        valid_gs = "✓" if row['Guloso Simples Valido'] else "✗"
        valid_gr = "✓" if row['Guloso Restart Valido'] else "✗"
        
        dados_sucesso.append([
            str(n),
            "✓",
            valid_gs,
            valid_gr,
            str(num_sol)
        ])
    
    tab_sucesso = Table(dados_sucesso, colWidths=[2*cm, 2.5*cm, 2.5*cm, 2.5*cm, 2.5*cm])
    tab_sucesso.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#ecf0f1')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
    ]))
    elementos.append(tab_sucesso)
    
    elementos.append(PageBreak())
    
    # PÁGINA 5: Análise e Conclusões
    elementos.append(Paragraph("4. ANÁLISE DOS RESULTADOS", estilo_subtitulo))
    
    elementos.append(Paragraph("4.1 Crescimento de Complexidade", estilo_secao))
    elementos.append(Paragraph(
        "O Backtracking apresenta crescimento exponencial claro: de N=12 para N=13, o tempo "
        "aumenta 6.6x (28s → 188s), e para N=14, mais 7.6x (188s → 1.425s = 23min). "
        "Isso confirma a complexidade O(N!) teórica.",
        estilo_corpo
    ))
    
    crescimento_dados = [
        ["<b>Transição</b>", "<b>Tempo BT</b>", "<b>Fator</b>", "<b>Tempo GR</b>", "<b>Fator</b>"],
        ["N=11 → 12", "3.9s → 28.3s", "7.2x", "6.6ms → 11.0ms", "1.7x"],
        ["N=12 → 13", "28.3s → 187.7s", "6.6x", "11.0ms → 4.0ms", "0.4x"],
        ["N=13 → 14", "187.7s → 1425s", "7.6x", "4.0ms → 19.7ms", "4.9x"],
    ]
    
    tab_cresc = Table(crescimento_dados, colWidths=[3*cm, 3*cm, 2*cm, 3*cm, 2*cm])
    tab_cresc.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#95a5a6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecf0f1')]),
    ]))
    elementos.append(tab_cresc)
    elementos.append(Spacer(1, 0.3*cm))
    
    elementos.append(Paragraph(
        "Guloso Restart mantém crescimento suave, com variação devido à aleatoriedade nas tentativas.",
        estilo_corpo
    ))
    
    elementos.append(Paragraph("4.2 Eficiência Comparativa", estilo_secao))
    
    eficiencia_dados = [
        ["<b>N</b>", "<b>Speedup (GR vs BT)</b>", "<b>Economia de Memória</b>", "<b>Trade-off</b>"],
        ["8", "26x mais rápido", "21x menos memória", "Vantagem clara GR"],
        ["10", "1.515x mais rápido", "160x menos memória", "Vantagem clara GR"],
        ["12", "2.580x mais rápido", "3.394x menos memória", "Vantagem clara GR"],
        ["14", "72.488x mais rápido", "93.532x menos memória", "Vantagem MASSIVA GR"],
    ]
    
    tab_efic = Table(eficiencia_dados, colWidths=[2*cm, 4*cm, 4*cm, 4*cm])
    tab_efic.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#16a085')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#d5f4e6')]),
    ]))
    elementos.append(tab_efic)
    
    elementos.append(Spacer(1, 0.5*cm))
    elementos.append(Paragraph("4.3 Por que Guloso Simples Falha?", estilo_secao))
    elementos.append(Paragraph(
        "O Guloso Simples é determinístico: sempre escolhe a primeira posição com mínimo de conflitos. "
        "Isso o prende em mínimos locais - configurações onde todas as próximas escolhas aumentam conflitos, "
        "mas não são a solução ótima global. Taxa de falha: 93% (13 de 14 casos testados).",
        estilo_corpo
    ))
    
    elementos.append(Paragraph("4.4 Como Guloso Restart Resolve?", estilo_secao))
    elementos.append(Paragraph(
        "A randomização permite escolher aleatoriamente entre posições empatadas. Cada tentativa "
        "explora um caminho diferente. Com até 100 tentativas, a probabilidade de encontrar "
        "uma solução válida é extremamente alta. Nos testes: 100% de sucesso (14/14 casos).",
        estilo_corpo
    ))
    
    elementos.append(PageBreak())
    
    # PÁGINA 6: Conclusões e Recomendações
    elementos.append(Paragraph("5. CONCLUSÕES", estilo_subtitulo))
    
    elementos.append(Paragraph("5.1 Resumo das Descobertas", estilo_secao))
    
    conclusoes = [
        "<b>1. Backtracking:</b> Solução completa e garantida, mas inviável para N>14 (tempo proibitivo).",
        "<b>2. Guloso Simples:</b> Extremamente rápido mas não confiável (93% de falha).",
        "<b>3. Guloso com Restart:</b> MELHOR ESCOLHA - combina rapidez com confiabilidade total.",
    ]
    
    for conclusao in conclusoes:
        elementos.append(Paragraph(conclusao, estilo_corpo))
    
    elementos.append(Spacer(1, 0.5*cm))
    elementos.append(Paragraph("5.2 Recomendações de Uso", estilo_secao))
    
    recomendacoes = [
        ["<b>Cenário</b>", "<b>Algoritmo Recomendado</b>", "<b>Justificativa</b>"],
        ["N ≤ 10", "Backtracking", "Rápido o suficiente e encontra todas soluções"],
        ["N entre 11-20", "Guloso Restart", "Backtracking muito lento, Restart confiável"],
        ["N > 20", "Guloso Restart", "Única opção viável"],
        ["Precisa TODAS soluções", "Backtracking", "Gulosos encontram apenas uma"],
        ["Aplicação crítica", "Guloso Restart", "100% sucesso vs 7% do Simples"],
        ["Pesquisa acadêmica", "Ambos", "Comparação didática"],
    ]
    
    tab_rec = Table(recomendacoes, colWidths=[4*cm, 5*cm, 5*cm])
    tab_rec.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8e44ad')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f4ecf7')]),
    ]))
    elementos.append(tab_rec)
    
    elementos.append(Spacer(1, 0.5*cm))
    elementos.append(Paragraph("5.3 Trabalhos Futuros", estilo_secao))
    
    futuros = [
        "• Implementar algoritmos genéticos para comparação",
        "• Testar paralelização do Backtracking",
        "• Otimizar Guloso Restart com heurísticas adaptativas",
        "• Estender testes para N > 20",
        "• Estudar distribuição de soluções no espaço de busca"
    ]
    
    for futuro in futuros:
        elementos.append(Paragraph(futuro, estilo_corpo))
    
    elementos.append(Spacer(1, 1*cm))
    elementos.append(Paragraph("5.4 Considerações Finais", estilo_secao))
    elementos.append(Paragraph(
        "Este estudo demonstra que a escolha do algoritmo correto é crucial para problemas "
        "combinatoriais. O Guloso com Restart prova que heurísticas simples, quando combinadas "
        "com aleatoriedade, podem superar algoritmos completos em termos práticos, oferecendo "
        "uma solução 72.000x mais rápida para N=14 sem sacrificar confiabilidade.",
        estilo_corpo
    ))
    
    elementos.append(PageBreak())
    
    # PÁGINA 7: Gráficos (se existirem)
    elementos.append(Paragraph("6. VISUALIZAÇÕES", estilo_subtitulo))
    
    # Verificar se gráficos existem
    graficos_dir = "resul_salvos/graficos"
    if os.path.exists(graficos_dir):
        elementos.append(Paragraph(
            "Os gráficos a seguir ilustram visualmente os resultados apresentados. "
            "Foram gerados automaticamente a partir dos dados coletados.",
            estilo_corpo
        ))
        elementos.append(Spacer(1, 0.3*cm))
        
        # Lista de gráficos esperados
        graficos_esperados = [
            ("comparacao_tempo.png", "Comparação de Tempo de Execução"),
            ("comparacao_memoria.png", "Comparação de Consumo de Memória"),
            ("tempo_log.png", "Tempo em Escala Logarítmica"),
            ("tabela_resultados.png", "Tabela Resumida de Resultados"),
        ]
        
        for arquivo, titulo in graficos_esperados:
            caminho = os.path.join(graficos_dir, arquivo)
            if os.path.exists(caminho):
                elementos.append(Paragraph(f"<b>{titulo}</b>", estilo_secao))
                try:
                    img = Image(caminho, width=14*cm, height=10*cm)
                    elementos.append(img)
                    elementos.append(Spacer(1, 0.5*cm))
                except:
                    elementos.append(Paragraph(f"[Erro ao carregar: {arquivo}]", estilo_corpo))
    else:
        elementos.append(Paragraph(
            "Os gráficos podem ser gerados executando o script 'resul_salvos/plotar_graficos.py'. "
            "Isso criará visualizações detalhadas dos dados apresentados neste relatório.",
            estilo_corpo
        ))
    
    # Rodapé final
    elementos.append(PageBreak())
    elementos.append(Spacer(1, 10*cm))
    elementos.append(Paragraph("=" * 80, estilo_corpo))
    elementos.append(Paragraph("FIM DO RELATÓRIO", estilo_titulo))
    elementos.append(Paragraph(f"Gerado em {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}", estilo_corpo))
    
    # Gerar PDF
    doc.build(elementos)
    print(f"\n✓ Relatório PDF gerado com sucesso: {pdf_file}")
    print(f"✓ Total de páginas: 7+")
    print(f"✓ Tabelas incluídas: 8")
    print(f"✓ Gráficos: Verificar pasta resul_salvos/graficos/")

if __name__ == "__main__":
    criar_relatorio_pdf()
