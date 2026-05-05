---
name: erf-init
description: 1C ERF - create empty report XML scaffold.
---

# /skill:erf-init — Создание нового отчёта

Генерирует минимальный набор XML-исходников для внешнего отчёта 1С: корневой файл метаданных и каталог отчёта.

## Usage

```
/erf-init <Name> [Synonym] [SrcDir] [--with-skd]
```

| Параметр  | Обязательный | По умолчанию | Описание                              |
|-----------|:------------:|--------------|---------------------------------------|
| Name      | да           | —            | Имя отчёта (латиница/кириллица)       |
| Synonym   | нет          | = Name       | Синоним (отображаемое имя)            |
| SrcDir    | нет          | `src`        | Каталог исходников относительно CWD   |
| --WithSKD | нет          | —            | Создать пустую СКД и привязать к MainDataCompositionSchema |

## Команда

```powershell
python .agents/skills/epf-init/scripts/init.py -Name "<Name>" [-Synonym "<Synonym>"] [-SrcDir "<SrcDir>"] [-WithSKD]
```

## Дальнейшие шаги

- Добавить форму: `/skill:form-add`
- Добавить макет: `/skill:template-add`
- Добавить справку: `/skill:help-add`
- Собрать ERF: `/skill:erf-build`
