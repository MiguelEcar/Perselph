# Perselph

**Perselph** é um conselheiro de reflexão sobre os impactos humanos da adoção de assistentes de IA no trabalho. Seu princípio: **a pessoa para além do papel**.

Este repositório é a própria skill: o `SKILL.md` na raiz é a fonte normativa, e os arquivos complementares oferecem referências operacionais, exemplos e cenários de avaliação.

## Estrutura

```text
Perselph/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
│   ├── guia-de-facilitacao.md
│   ├── lentes-e-limites.md
│   └── fontes-e-rastreabilidade.md
├── examples/
│   ├── daily.md
│   ├── one-on-one.md
│   ├── retrospectiva.md
│   └── lideranca.md
├── evals/
│   ├── casos.json
│   └── rubrica.md
└── scripts/
    └── validate_skill.py
```

## Instalação no Claude Code

Clone o repositório direto no diretório de skills, com o nome `perselph`:

- **No usuário:** `git clone https://github.com/MiguelEcar/Perselph.git ~/.claude/skills/perselph`
- **Por projeto:** `git clone https://github.com/MiguelEcar/Perselph.git <seu-repositorio>/.claude/skills/perselph`

O arquivo de entrada deve ficar em `.claude/skills/perselph/SKILL.md`. Em outros ambientes compatíveis com o formato `SKILL.md`, instale o repositório inteiro como a pasta da skill.

## Uso

Peça, por exemplo: “Use Perselph para preparar um 1:1 com um desenvolvedor que sente que a IA está fazendo tudo”. O agente segue o `SKILL.md` e consulta `references/` e `examples/` quando forem úteis.

## Verificação local

```bash
python scripts/validate_skill.py
```

O validador verifica a estrutura, o frontmatter e a integridade dos cenários de avaliação; **não** realiza avaliação semântica automatizada das respostas geradas.

## Origem e responsabilidade

`SKILL.md` deriva do arquivo `Perselph_SKILL.md` original; apenas a `description` do frontmatter foi encurtada, e o corpo foi preservado. Os demais arquivos foram criados para empacotamento e operacionalização. Não foram incluídos textos integrais das obras de Jung nem do artigo-base.
