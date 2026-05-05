# План: TASK-2026-0006 — Удаление PowerShell 5.1 и Windows legacy

## Этап 1: Удаление устаревших файлов
- [x] Удалить `scripts/switch-to-powershell.py`
- [x] Удалить `scripts/switch-to-python.py`
- [x] Удалить `docs/python-porting-guide.md`

## Этап 2: Переработка `scripts/switch.py`
- [x] Удалить `RX_PS` и `RX_PY` regex
- [x] Удалить `classify_skill_runtime()`
- [x] Удалить `check_missing_files()`
- [x] Удалить `collect_runtime_messages()`
- [x] Удалить `print_runtime_messages()`
- [x] Удалить `switch_runtime_content()`
- [x] Удалить `cmd_switch_runtime()`
- [x] Удалить `--runtime` из argparse
- [x] Упростить `cmd_install()` — всегда Python, без runtime-конверсии
- [x] Упростить `interactive_mode()` — убрать выбор рантайма
- [x] Обновить docstring и комментарии

## Этап 3: Обновление документации проекта
- [x] README.md — убрать PowerShell из требований и раздел "Переключение рантайма"
- [x] AGENTS.md — уточнить, что рантайм только Python 3
- [x] CHANGELOG.md — добавить запись об удалении PowerShell

## Этап 4: Обновление гайдов и спецификаций
- [x] docs/epf-guide.md — убрать упоминание PowerShell-скриптов
- [x] docs/cf-guide.md — заменить `powershell` на `bash` в блоках кода (это примеры CLI, не PS)
- [x] docs/meta-guide.md — заменить `powershell` на `bash` в блоках кода
- [x] docs/subsystem-guide.md — заменить `powershell` на `bash` в блоках кода

## Этап 5: Обновление кода навыков
- [x] meta-edit/json-dsl.md — заменить `powershell.exe` на `python`
- [x] skd-compile.py — переименовать комментарий "match PS1 output"
- [x] mxl-compile.py — переименовать комментарии "like PS1"
- [x] verify-snapshots.mjs — убрать `--runtime powershell|python` из заголовка и логики
- [x] runner.mjs — убрать `--runtime` из CLI, отчётов и вызовов функций

## Этап 6: Проверка
- [x] Проверить отсутствие `.ps1` файлов
- [x] Проверить `grep -ri powershell` (исключая исторические задачи)
- [x] Проверить работу `switch.py --help`
- [x] Проверить `switch.py` на тестовой установке
