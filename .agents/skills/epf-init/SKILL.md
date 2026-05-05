---
name: epf-init
description: 1C EPF - create empty XML scaffold for external processor.
---

# /skill:epf-init — Создание новой обработки

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

```powershell
python .agents/skills/epf-init/scripts/init.py -Name "<Name>" [-Synonym "<Synonym>"] [-SrcDir "<SrcDir>"]
```

## Дальнейшие шаги

- Добавить форму: `/skill:form-add`
- Добавить макет: `/skill:template-add`
- Добавить справку: `/skill:help-add`
- Собрать EPF: `/skill:epf-build`
