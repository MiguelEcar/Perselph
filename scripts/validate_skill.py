#!/usr/bin/env python3
"""Validação estrutural simples; não executa um modelo nem mede qualidade semântica."""
from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parent.parent
skill = root / 'perselph' / 'SKILL.md'
required = [
    skill,
    root / 'README.md',
    root / 'perselph' / 'references' / 'guia-de-facilitacao.md',
    root / 'perselph' / 'references' / 'lentes-e-limites.md',
    root / 'perselph' / 'references' / 'fontes-e-rastreabilidade.md',
    root / 'perselph' / 'evals' / 'casos.json',
    root / 'perselph' / 'evals' / 'rubrica.md',
]
errors = [f'Arquivo ausente: {p.relative_to(root)}' for p in required if not p.is_file()]
if skill.is_file():
    content = skill.read_text(encoding='utf-8')
    if not content.startswith('---\n'):
        errors.append('SKILL.md deve começar com frontmatter YAML')
    else:
        front = content.split('---', 2)[1]
        for key in ('name:', 'description:'):
            if key not in front:
                errors.append(f'Frontmatter sem {key}')
    for needle in ('pessoa ≠ papel ≠ tarefa ≠ contribuição', 'Perselph não deve:', 'Jung afirma'):
        if needle not in content:
            errors.append(f'SKILL.md não contém: {needle}')
try:
    data = json.loads((root / 'perselph' / 'evals' / 'casos.json').read_text(encoding='utf-8'))
    assert isinstance(data['cases'], list) and len(data['cases']) >= 5
    assert all({'id', 'input', 'expect'} <= set(c) for c in data['cases'])
except (OSError, ValueError, KeyError, AssertionError) as exc:
    errors.append(f'Cenários de teste inválidos: {exc}')
if errors:
    print('FALHA:')
    for error in errors: print(' -', error)
    sys.exit(1)
print('OK: estrutura, entrada SKILL.md e cenários de avaliação validados.')
