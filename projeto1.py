import streamlit as st
import pypdf
import io

# 1. Configuração da Interface (Aparência)
st.set_page_config(
    page_title="Mesclador de PDF Profissional", 
    page_icon="📄", 
    layout="centered"
)

# Estilização básica com Markdown
st.title("📄 PDF Merger Pro")
st.subheader("Transforme múltiplos arquivos em um único documento")
st.markdown("---")

# 2. Área de Upload
# O parâmetro accept_multiple_files permite selecionar vários PDFs de uma vez
arquivos_pdf = st.file_uploader(
    "Arraste seus arquivos PDF ou clique para selecionar", 
    type="pdf", 
    accept_multiple_files=True
)

# 3. Lógica Principal
if arquivos_pdf:
    st.success(f"✅ {len(arquivos_pdf)} arquivos carregados.")
    
    # Lista os nomes dos arquivos para o usuário conferir a ordem
    with st.expander("Ver lista de arquivos selecionados"):
        for arquivo in arquivos_pdf:
            st.write(f"- {arquivo.name}")

    # Campo para o usuário dar nome ao arquivo final
    nome_saida = st.text_input("Nome do arquivo de saída:", "documento_final")

    # Botão que dispara a ação de mesclagem
    if st.button("Mesclar e Gerar Download", type="primary"):
        # Criamos o objeto que vai escrever o novo PDF
        # Na versão atual da pypdf, PdfWriter faz todo o trabalho
        escritor = pypdf.PdfWriter()
        
        try:
            # Barra de progresso para dar feedback visual (UX)
            progresso = st.progress(0)
            
            for i, pdf in enumerate(arquivos_pdf):
                escritor.append(pdf)
                # Atualiza a barra de progresso proporcionalmente
                progresso.progress((i + 1) / len(arquivos_pdf))
            
            # Criamos um arquivo virtual em memória para salvar o PDF gerado
            output_buffer = io.BytesIO()
            escritor.write(output_buffer)
            escritor.close()
            
            st.markdown("---")
            
            # 4. Botão de Download
            st.download_button(
                label="⬇️ Baixar PDF Mesclado",
                data=output_buffer.getvalue(),
                file_name=f"{nome_saida}.pdf",
                mime="application/pdf"
            )
            
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")
            st.info("Dica: Verifique se os arquivos não estão protegidos por senha.")

else:
    # Mensagem de espera caso não haja arquivos
    st.info("Aguardando o upload de arquivos para começar...")

# Rodapé informativo para o Portfólio
st.markdown("---")
st.caption("Desenvolvimento de uma Automação em Python.")