# План задачи TASK-2026-0001: kimi-adaptation

## Этап 1: Инфраструктура (switch.py, .gitignore)
- [x] Добавить `'kimi': '.kimi/skills'` в PLATFORMS
- [x] Добавить Kimi в interactive_mode()
- [x] Убрать PowerShell как опцию для kimi (только python)
- [x] Добавить `.kimi/skills/` в .gitignore
- [x] Добавить `.kimi/skills/` в README.md таблицу платформ

## Этап 2: Удаление PowerShell-скриптов
- [x] Найти все `.ps1` файлы в `.claude/skills/`
- [x] Удалить все `.ps1` файлы
- [x] Обновить SKILL.md: удалить ссылки на `.ps1`, оставить только `.py`

## Этап 3: Адаптация SKILL.md
- [x] Убрать `argument-hint` и `allowed-tools` из frontmatter (лишние для Kimi)
- [x] Заменить слеш-команды `/name` → `/skill:name` в заголовках и примерах
- [x] Заменить пути `.claude/skills/` на `.kimi/skills/` (или относительные)
- [x] Убрать `AskUserQuestion` из 10 навыков (db-*, web-*)
- [x] Обновить примеры вызова скриптов: `python3 scripts/...` вместо `powershell.exe ...`

## Этап 4: Документация
- [x] Обновить README.md: добавить Kimi CLI в быстрый старт
- [x] Обновить docs/ если есть упоминания платформ
- [x] Добавить раздел про Kimi CLI в README

## Этап 5: Проверка
- [ ] Запустить `python -m py_compile scripts/switch.py`
- [ ] Проверить отсутствие .ps1: `find .claude/skills -name "*.ps1" | wc -l`
- [ ] Проверить синтаксис SKILL.md
- [x] Коммит + push

## Риски
- Удаление .ps1 может сломать Claude Code пользователей (но это наш форк, ориентирован на Kimi)
- Некоторые навыки зависят от Windows/1С платформы — их Python-скрипты остаются, но функциональность ограничена
