
import streamlit as st
import pandas as pd

st.title('Ana Alice Ramos')

st.write("   Maracatiara, Curitiba-PR")
st.write("✆ +551899686.4358")
st.write("✉ anah.ramos@outlook.com")


with st.expander("                 "):
    local = pd.DataFrame({
        'latitude': [ -25.42 ],
        'longitude': [ -49.27 ]
    })
    
    st.map(local)

st.button("Formação")
col1, col2 = st.columns(2)

with col1:
    st.write("- Puc Campinas -                            "
             "Bacharelado em Administração              "
             "02/2019 - 12/2022")
    
    st.write("- USP Esalq -                     "
             "MBA em Data Science & Analytics                 "
             "08/2024 - A Cursar")
    
    st.write("- Harve -                                                           "
             "Programação em Python                                               "
             
             "                             03/2025 - A Cursar")

with col2:
     
    st.write("- Conceitos e características dos projetos - FGV")
    st.write("- Gestão de projetos e fundamentos de  métodos ágeis (Kanban, Scrum e Lean) - Santander")
             

st.button("Experiências Profissionais")
with st.expander("-----------"):
    st.write("Analista de Compras")

    st.write("Progen - 01/2024 - Atual")

    st.write("Category Management e homologação de fornecedores;Desenvolvimento de estratégias de negociação (TCO, Should Cost)"
    "Gestão de contratos, aditivos e compliance; Gestão de processos e KPIs(Cost Savings, Lead Time, SLA) Data-Driven"
    "Procurement: Criação de dashboards e relatórios; Risk Assessment e mitigação de riscos na cadeia de suprimentos.")

    st.write("                ")
    st.write("Desenvolvedora de Negócios")

    st.write("Smile Startup Argentina - 06/2023 - 12/2023")

    st.write("Market Intelligence e Análise de Concorrência; B2B Sales & Lead Generation (Inside Sales, CRM, SDR); Estratégias de" 
                "Growth Marketing e Automação; Customer Insights & NPS Analytics (CSAT, CES); Data-Driven Decision Making e análise de Big Data.")

    st.write("                ")
    st.write("Analista de Compras")

    st.write("Imerys do Brasil - 07/2021 - 06/2023")

    st.write("trategic Sourcing e Gestão de Fornecedores; Negociação de  contratos e propostas OPEX & CAPEX; Gestão de processos e  KPIs" 
                "(Cost Savings, Lead Time, SLA); Supply Chain Optimization e análise de consumo; Procurement Analytics e  automação de processos;"
                "Data-Driven Procurement: Criação de dashboards e relatórios.")

opcao = st.radio(" ",["Hard Skills", "Soft Skills"])
if opcao =="Hard Skills":
     st.write("Power BI, Looker Studio, Python"
        "SAP ECC, SAP HANA, TOTVS, Nimbi, SRM"
        "Salesforce, HubSpot, Adobe Sign")
else:
    st.write("Procurement & Strategic Sourcing, Gestão de Fornecedores e Contratos, Negociação & Redução de Custos" 
        "Análise de Dados & Business Intelligence, KPI Monitoring & Performance Metrics, Supply Chain Management & Compliance"
        "Resolução de Problemas & Tomada de Decisão")



st.button("Idiomas")
st.write("Português: Nativo")
st.write("Inglês: Intermediário")
st.write("Espanhol: Avançado")

with st.expander("                "):
    st.write("Linkedin: https://www.linkedin.com/in/ana-alice-ramos-0008a5149/")
    st.write("Github: https://github.com/anasantos2897/AnaR_Repository_289.git")


