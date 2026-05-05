---
name: skd-validate
description: 1C SKD/DCS - validate data composition schema after create/edit.
---

# $skd-validate — валидация СКД (DataCompositionSchema)

Проверяет структурную корректность Template.xml схемы компоновки данных. Выявляет ошибки формата, битые ссылки, дубликаты имён.

## Параметры

| Параметр     | Обяз. | Умолч. | Описание                                              |
|--------------|:-----:|---------|---------------------------------------------------------|
| TemplatePath | да    | —       | Путь к Template.xml или каталогу макета                 |
| Detailed     | нет   | —       | Подробный вывод (все проверки, включая успешные)         |
| MaxErrors    | нет   | 20      | Остановиться после N ошибок                             |
| OutFile      | нет   | —       | Записать результат в файл                               |

## Команда

```bash
python .agents/skills/epf-init/scripts/init.py -TemplatePath "src/МойОтчёт/Templates/ОсновнаяСхема"
python .agents/skills/epf-init/scripts/init.py -TemplatePath "Catalogs/Номенклатура/Templates/СКД/Ext/Template.xml"
```
