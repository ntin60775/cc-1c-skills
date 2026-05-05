---
name: mxl-validate
description: 1C MXL layout - validate tabular document after create/edit.
---

# $mxl-validate — валидация макета табличного документа (MXL)

Проверяет Template.xml на структурные ошибки: индексы, ссылки на палитры, диапазоны именованных областей и объединений.

## Параметры

| Параметр      | Обяз. | Умолч. | Описание                                 |
|---------------|:-----:|---------|--------------------------------------------|
| TemplatePath  | да    | —       | Путь к макету (директория или Template.xml) |
| Detailed      | нет   | —       | Подробный вывод (все проверки, включая успешные) |
| MaxErrors     | нет   | 20      | Остановиться после N ошибок                |

## Команда

```bash
python .agents/skills/mxl-validate/scripts/mxl-validate.py -TemplatePath "Catalogs/Номенклатура/Templates/Макет"
python .agents/skills/mxl-validate/scripts/mxl-validate.py -TemplatePath "src/МояОбработка/Templates/ПечатнаяФорма"
```

