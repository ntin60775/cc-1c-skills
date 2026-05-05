---
name: meta-validate
description: 1C metadata - validate config object after create/edit.
---

# /skill:meta-validate — валидация объекта метаданных 1С

Проверяет XML объекта метаданных из выгрузки конфигурации на структурные ошибки.

## Параметры

| Параметр   | Обяз. | Умолч. | Описание                                      |
|------------|:-----:|---------|-------------------------------------------------|
| ObjectPath | да    | —       | Путь к XML-файлу или каталогу. Через `\|` для batch |
| Detailed   | нет   | —       | Подробный вывод (все проверки, включая успешные) |
| MaxErrors  | нет   | 30      | Остановиться после N ошибок (per object)        |
| OutFile    | нет   | —       | Записать результат в файл (UTF-8 BOM)           |

## Команда

```powershell
python .agents/skills/epf-init/scripts/init.py -ObjectPath "Catalogs/Номенклатура/Номенклатура.xml"
python .agents/skills/epf-init/scripts/init.py -ObjectPath "Catalogs/Банки|Documents/Заказ"
```
