# Changelog

## 0.3.0

- Удалены 13 навыков, функциональность которых перекрыта v8-runner CLI:
  `db-create`, `db-load-cf`, `db-load-xml`, `db-load-git`, `db-dump-cf`, `db-dump-xml`,
  `db-update`, `db-run`, `cf-validate`, `epf-build`, `erf-build`, `epf-dump`, `erf-dump`.
- Обновлён `SKILL.md`: добавлена ссылка на `skills-1c-project-v8runner`.
- Обновлён `skill.json`: версия 0.3.0, описание.

## 0.2.0

- Полностью удалена поддержка PowerShell 5.1-рантайма.
- Удалены скрипты `switch-to-powershell.py` и `switch-to-python.py`.
- Удалено руководство `docs/python-porting-guide.md`.
- `scripts/switch.py` упрощён: удалён аргумент `--runtime`, Python 3 — единственный рантайм.
- Обновлена документация: убраны все упоминания PowerShell из README, AGENTS.md и гайдов.

## 0.1.0

- Агрегатор оформлен как навык `skills-1c-system` с ролью `devtools`.
- Рантайм единообразно переведён на Python 3.
- Убраны устаревшие ссылки на PowerShell-рантайм.
- Добавлено поле `install_source` для flatten-установки через `skills-1c-system`.
