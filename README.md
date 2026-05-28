# 📄 PDF Merger Pro

> Uma ferramenta web leve e eficiente, desenvolvida em Python com Streamlit, projetada para mesclar múltiplos arquivos PDF em um único documento de forma simples, rápida e segura.

## Fluxo de Trabalho

O processo é intuitivo e direto:

```
[ Upload de PDFs ] → [ Visualizar lista ] → [ Mesclar ] → [ Download ]
```

---

## Funcionalidades

- Upload múltiplo — selecione vários PDFs de uma só vez
- Pré-visualização — lista os arquivos carregados para conferência antes de mesclar
- Nome personalizado — defina o nome do arquivo de saída
- Barra de progresso — feedback visual em tempo real durante o processamento
- Download direto — o PDF gerado é disponibilizado para download sem sair da página
- Processamento em memória — nenhum arquivo é salvo no servidor

---

## Tecnologias Utilizadas

| Tecnologia - Função 
|---|---|
| [Python] - Linguagem base do projeto 
| [Streamlit] - Framework para a interface web 
| [pypdf] - Leitura e mesclagem dos arquivos PDF 

---

## Como Executar Localmente

### Pré-requisitos

- Python 3.8 ou superior
- pip

### Instalação

1. **Clone o repositório:**
   
   git clone https://github.com/Gui-prog/pdf-merger-pro.git
   cd pdf-merger-pro
   

2. **Instale as dependências:**

   pip install streamlit pypdf
   

3. **Execute a aplicação:**
   
   streamlit run app.py
   

4. Acesse `http://localhost:8501` no seu navegador.

---

##  Estrutura do Projeto

```
pdf-merger-pro/
│
├── app.py          # Código principal da aplicação
└── README.md       # Documentação do projeto
```

---

## ⚠️ Observações

- Arquivos PDF **protegidos por senha** não são suportados.
- O processamento ocorre inteiramente em memória — nenhum dado é persistido.
- A ordem de mesclagem segue a ordem em que os arquivos foram selecionados no upload.

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">Desenvolvido com Python 🐍</p>