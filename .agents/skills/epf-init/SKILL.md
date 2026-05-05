---
name: epf-init
description: 1C EPF - create empty XML scaffold for external processor.
---

# $epf-init — Создание новой обработки

Генерирует минимальный набор XML-исходников для внешней обработки 1С: корневой файл метаданных и каталог обработки.

## Usage

```
/epf-init <Name> [Synonym] [SrcDir]
```

| Параметр  | Обязательный | По умолчанию | Описание                            |
|-----------|:------------:|--------------|-------------------------------------|
| Name      | да           | —            | Имя обработки (латиница/кириллица)  |
| Synonym   | нет          | = Name       | Синоним (отображаемое имя)          |
| SrcDir    | нет          | `src`        | Каталог исходников относительно CWD |

## Команда

```bash
python .agents/skills/epf-init/scripts/init.py -Name "<Name>" [-Synonym "<Synonym>"] [-SrcDir "<SrcDir>"]
```

## Дальнейшие шаги

- Добавить форму: `$form-add`
- Добавить макет: `$template-add`
- Добавить справку: `$help-add`
- Собрать EPF: `$epf-build`
