# 📚 EditaVertical - Transforme seu edital em plano de estudos

## ✨ O que é este projeto?

Uma das coisas mais importantes na prepação para uma prova de concurso é organizar um plano de estudos eficiente. Uma das formas que eu mais gosto é criando um edital verticalizado, que nada mais é do que dispor as disciplinas em um formato de tabela, que acaba sendo mais adequado para monitorar o progresso. Nesse sentido criei o **EditaVerticalF**, um app simples em Python + Streamlit que transforma tópicos de um edital de concurso em um plano de estudos estruturado, pronto para acompanhamento.

O usuário cola os tópicos do edital, informa o nome da disciplina e o app gera um **DataFrame** com campos como:

| Disciplina | Item | Estudo 1 | Estudo 2 | Revisado | Questões Feitas | % Acerto |
|---|---|---|---|---|---|---|


---


## 🚀 Funcionalidades principais:

✅ Conversão automática de tópicos numerados (ex: `1.`, `1.1`, `2.1`)  
✅ Possibilidade de adicionar várias disciplinas antes de exportar  
✅ Exportação final para **Excel (.xlsx)**  
✅ Interface web simples via Streamlit (acessa direto pelo navegador)

---


## 🛠️ Como rodar localmente:

**Pré-requisitos:**

- Python 3.7+
- Pip

**Passos:**

```bash
# Clone o repositório
git clone https://github.com/seuusuario/edital2df.git
cd edital2df

# Crie e ative um ambiente virtual (opcional mas recomendado)
python -m venv venv
venv\Scripts\activate  # No Windows
# ou
source venv/bin/activate  # No Linux/Mac



# Instale as dependências
pip install -r requirements.txt

# Rode o app
streamlit run app.py
