---
name: form-info
description: Форма 1С — анализ Form.xml, элементов, реквизитов, команд и событий.
argument-hint: <FormPath>
allowed-tools:
  - Bash
  - Read
  - Glob
---

# /form-info — Компактная сводка формы

Читает Form.xml и выводит дерево элементов, реквизиты с типами, команды, события. Заменяет чтение тысяч строк XML.

## Команда

```powershell
powershell.exe -NoProfile -File .claude/skills/form-info/scripts/form-info.ps1 -FormPath "<путь к Form.xml>"
```

## Параметры

| Параметр | Обязательный | Описание |
|----------|:------------:|----------|
| FormPath | да | Путь к файлу Form.xml |
| Expand   | нет | Раскрыть свёрнутую секцию по имени или title, `*` — все |
| Limit    | нет | Макс. строк (по умолчанию 150) |
| Offset   | нет | Пропустить N строк (пагинация) |

Вывод самодокументирован. `[Group:AH]`/`[Group:AV]` = AlwaysHorizontal/AlwaysVertical.
