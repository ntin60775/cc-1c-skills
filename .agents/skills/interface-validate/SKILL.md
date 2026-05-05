---
name: interface-validate
description: 1C interface - validate subsystem command interface after edits.
---

# $interface-validate — валидация CommandInterface.xml

Проверяет XML командного интерфейса на структурные ошибки: корневой элемент, допустимые секции, порядок, формат ссылок на команды, дубликаты.

## Параметры

| Параметр  | Обяз. | Умолч. | Описание                                |
|-----------|:-----:|---------|-----------------------------------------|
| CIPath    | да    | —       | Путь к CommandInterface.xml             |
| Detailed  | нет   | —       | Подробный вывод (все проверки, включая успешные) |
| MaxErrors | нет   | 30      | Остановиться после N ошибок              |
| OutFile   | нет   | —       | Записать результат в файл (UTF-8 BOM)   |

## Команда

```bash
python ".agents/skills/interface-validate/scripts/interface-validate.py" -CIPath "Subsystems/Продажи"
python ".agents/skills/interface-validate/scripts/interface-validate.py" -CIPath "Subsystems/Продажи/Ext/CommandInterface.xml"
```
