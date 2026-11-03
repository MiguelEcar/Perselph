# Perselph — projeto completo de skill

**Perselph** é um conselheiro de reflexão sobre os impactos humanos da adoção de assistentes de IA no trabalho. Seu princípio: **a pessoa para além do papel**.

Esta distribuição mantém o `SKILL.md` fornecido como **fonte normativa**, sem alterar seus conceitos, limites ou processo. Os arquivos complementares oferecem referências operacionais, exemplos, testes e formas de instalação.

## Estrutura

```text
perselph_skill_project/
├── README.md
├── CHANGELOG.md
├── perselph/
│   ├── SKILL.md
│   ├── references/
│   │   ├── guia-de-facilitacao.md
│   │   ├── lentes-e-limites.md
│   │   └── fontes-e-rastreabilidade.md
│   ├── examples/
│   │   ├── daily.md
│   │   ├── one-on-one.md
│   │   ├── retrospectiva.md
│   │   └── lideranca.md
│   └── evals/
│       ├── casos.json
│       └── rubrica.md
└── scripts/
    └── validate_skill.py
```

## Instalação no Claude Code

Copie a pasta **`perselph`** (não apenas o conteúdo do arquivo) para um dos destinos:

- **Por projeto:** `<seu-repositorio>/.claude/skills/perselph/`
- **No usuário:** `~/.claude/skills/perselph/`

O arquivo de entrada deve ficar em `.claude/skills/perselph/SKILL.md`. Em ambientes com suporte a skills compatíveis com o formato `SKILL.md`, a pasta `perselph/` pode ser instalada no diretório de skills correspondente.

## Uso

Peça, por exemplo: “Use Perselph para preparar um 1:1 com um desenvolvedor que sente que a IA está fazendo tudo”. O agente deve seguir `SKILL.md` e consultar os materiais complementares quando forem úteis.

## Verificação local

```bash
python scripts/validate_skill.py
```

O validador verifica a estrutura, o frontmatter e a integridade de cenários de avaliação; **não** realiza avaliação semântica automatizada das respostas geradas.

## Origem e responsabilidade

`perselph/SKILL.md` é uma cópia integral do arquivo `Perselph_SKILL.md` fornecido pelo usuário. Os demais arquivos foram criados para empacotamento e operacionalização. Não foram incluídos textos integrais das obras de Jung nem do artigo-base, pois esses materiais não acompanharam o arquivo recebido.
