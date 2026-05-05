---
name: erf-validate
description: 1C ERF - validate XML sources after create/edit.
---

# $erf-validate — валидация внешнего отчёта (ERF)

Проверяет структурную корректность XML-исходников внешнего отчёта: корневую структуру, InternalInfo, свойства (включая MainDataCompositionSchema), ChildObjects, реквизиты, табличные части, уникальность имён, наличие файлов форм и макетов.

Использует тот же скрипт, что и `$epf-validate` — автоопределение по типу элемента (ExternalReport).

## Параметры

| Параметр   | Обяз. | Умолч. | Описание                                      |
|------------|:-----:|---------|-------------------------------------------------|
| ObjectPath | да    | —       | Путь к корневому XML или каталогу отчёта        |
| Detailed   | нет   | —       | Подробный вывод (все проверки, включая успешные) |
| MaxErrors  | нет   | 30      | Остановиться после N ошибок                     |
| OutFile    | нет   | —       | Записать результат в файл (UTF-8 BOM)           |

## Команда

```bash
python .agents/skills/epf-validate/scripts/epf-validate.py -ObjectPath "src/МойОтчёт"
python .agents/skills/epf-validate/scripts/epf-validate.py -ObjectPath "src/МойОтчёт/МойОтчёт.xml"
```

