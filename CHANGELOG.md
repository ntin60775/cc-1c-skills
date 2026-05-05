# Changelog

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
