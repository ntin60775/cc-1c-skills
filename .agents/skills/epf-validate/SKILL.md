---
name: epf-validate
description: 1C EPF - validate XML sources after create/edit.
---

# $epf-validate — валидация внешней обработки (EPF)

Проверяет структурную корректность XML-исходников внешней обработки: корневую структуру, InternalInfo, свойства, ChildObjects, реквизиты, табличные части, уникальность имён, наличие файлов форм и макетов. Также работает для внешних отчётов (ERF).

## Параметры

| Параметр   | Обяз. | Умолч. | Описание                                      |
|------------|:-----:|---------|-------------------------------------------------|
| ObjectPath | да    | —       | Путь к корневому XML или каталогу обработки     |
| Detailed   | нет   | —       | Подробный вывод (все проверки, включая успешные) |
| MaxErrors  | нет   | 30      | Остановиться после N ошибок                     |
| OutFile    | нет   | —       | Записать результат в файл (UTF-8 BOM)           |

## Команда

```bash
python .agents/skills/epf-validate/scripts/epf-validate.py -ObjectPath "src/МояОбработка"
python .agents/skills/epf-validate/scripts/epf-validate.py -ObjectPath "src/МояОбработка/МояОбработка.xml"
```

