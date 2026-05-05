# TASK-2026-0006: Удаление PowerShell 5.1 и Windows legacy из проекта

## Ветка
main

## Краткое имя
remove-powershell

## Человекочитаемое описание
Полностью вырезать из проекта `skills-1c-project-devtools` остатки PowerShell 5.1-рантайма, Windows legacy-логики и всю связанную документацию. Python 3 становится единственным рантаймом.

## Контекст
В рамках TASK-2026-0001 все `.ps1` файлы были удалены из `.agents/skills/`. Однако в репозитории остались:
- Скрипты переключения рантайма (`switch-to-powershell.py`, `switch-to-python.py`)
- Поддержка `--runtime powershell` в `switch.py`
- Руководство по портированию PS→PY (`docs/python-porting-guide.md`)
- Упоминания PowerShell в README, AGENTS.md, CHANGELOG.md, гайдах
- `powershell.exe` в примерах вызовов (`meta-edit/json-dsl.md`)
- Комментарии "match PS1 output" / "like PS1" в Python-скриптах

## Цель
Сделать Python 3 единственным и очевидным рантаймом. Убрать любую путаницу для пользователей и разработчиков.

## Границы
- Удаление файлов: `scripts/switch-to-powershell.py`, `scripts/switch-to-python.py`, `docs/python-porting-guide.md`
- Переработка `scripts/switch.py` — упрощение, удаление PowerShell-логики
- Обновление документации — README, AGENTS.md, CHANGELOG.md, гайды
- Обновление комментариев и примеров в коде навыков
- Не затрагивается функциональность Python-скриптов (только комментарии)

## Риски
- Сломать `switch.py` для пользователей, которые используют его для установки навыков
- Mitigation: `switch.py` продолжает работать, но только с Python-рантаймом

## Проверки
- [x] `find . -name "*.ps1" | wc -l` → 0
- [x] `grep -ri "powershell" --include="*.py" --include="*.md" --include="*.mjs" .` → только в `knowledge/tasks/TASK-2026-0001*` (исторические задачи)
- [x] `python scripts/switch.py --help` работает и не содержит `--runtime powershell`
- [ ] `python scripts/switch.py kimi --project-dir /tmp/test-install` успешно устанавливает навыки
