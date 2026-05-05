---
name: mxl-decompile
description: 1C MXL layout - decompile tabular document to JSON.
---

# $mxl-decompile — Декомпилятор макета в DSL

Принимает Template.xml табличного документа 1С и генерирует компактное JSON-определение (DSL). Обратная операция к `$mxl-compile`.

## Использование

```
$mxl-decompile <TemplatePath> [OutputPath]
```

## Параметры

| Параметр     | Обязательный | Описание                                |
|--------------|:------------:|-----------------------------------------|
| TemplatePath | да           | Путь к Template.xml                     |
| OutputPath   | нет          | Путь для JSON (если не указан — stdout) |

## Команда

```bash
python .agents/skills/mxl-decompile/scripts/mxl-decompile.py -TemplatePath "<путь>/Template.xml" [-OutputPath "<путь>.json"]
```

## Рабочий процесс

Декомпиляция существующего макета для анализа или доработки:

1. Агент вызывает `$mxl-decompile` для получения JSON из Template.xml
2. Агент анализирует или модифицирует JSON (добавляет области, меняет стили)
3. Агент вызывает `$mxl-compile` для генерации нового Template.xml
4. Агент вызывает `$mxl-validate` для проверки

## JSON-схема DSL

Полная спецификация формата: **`docs/mxl-dsl-spec.md`** (прочитать через Read tool).

## Генерация имён

Скрипт автоматически генерирует осмысленные имена:

- **Шрифты**: `default`, `bold`, `header`, `small`, `italic` — или описательные имена по свойствам
- **Стили**: `bordered`, `bordered-center`, `bold-right`, `border-top` и т.д. — по комбинации свойств

## Детектирование `rowStyle`

Если в строке есть пустые ячейки (без параметров/текста) и все они имеют одинаковый формат — этот формат распознаётся как `rowStyle`, а пустые ячейки исключаются из вывода.
