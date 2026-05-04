# План задачи TASK-2026-0001: kimi-adaptation

## Этап 1: Инфраструктура (switch.py, .gitignore)
- [ ] Добавить `'kimi': '.kimi/skills'` в PLATFORMS
- [ ] Добавить Kimi в interactive_mode()
- [ ] Убрать PowerShell как опцию для kimi (только python)
- [ ] Добавить `.kimi/skills/` в .gitignore
- [ ] Добавить `.kimi/skills/` в README.md таблицу платформ

## Этап 2: Удаление PowerShell-скриптов
- [ ] Найти все `.ps1` файлы в `.claude/skills/`
- [ ] Удалить все `.ps1` файлы
- [ ] Обновить SKILL.md: удалить ссылки на `.ps1`, оставить только `.py`

## Этап 3: Адаптация SKILL.md
- [ ] Убрать `argument-hint` и `allowed-tools` из frontmatter (лишние для Kimi)
- [ ] Заменить слеш-команды `/name` → `/skill:name` в заголовках и примерах
- [ ] Заменить пути `.claude/skills/` на `.kimi/skills/` (или относительные)
- [ ] Убрать `AskUserQuestion` из 10 навыков (db-*, web-*)
- [ ] Обновить примеры вызова скриптов: `python3 scripts/...` вместо `powershell.exe ...`

## Этап 4: Документация
- [ ] Обновить README.md: добавить Kimi CLI в быстрый старт
- [ ] Обновить docs/ если есть упоминания платформ
- [ ] Добавить раздел про Kimi CLI в README

## Этап 5: Проверка
- [ ] Запустить `python -m py_compile scripts/switch.py`
- [ ] Проверить отсутствие .ps1: `find .claude/skills -name "*.ps1" | wc -l`
- [ ] Проверить синтаксис SKILL.md
- [ ] Коммит + push

## Риски
- Удаление .ps1 может сломать Claude Code пользователей (но это наш форк, ориентирован на Kimi)
- Некоторые навыки зависят от Windows/1С платформы — их Python-скрипты остаются, но функциональность ограничена
