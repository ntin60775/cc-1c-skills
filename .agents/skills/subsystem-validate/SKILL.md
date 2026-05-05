---
name: subsystem-validate
description: 1C subsystem - validate XML sources after create/edit.
---

# /skill:subsystem-validate — валидация подсистемы 1С

Проверяет структурную корректность XML-файла подсистемы из выгрузки конфигурации.

## Параметры

| Параметр      | Обяз. | Умолч. | Описание                                  |
|---------------|:-----:|---------|--------------------------------------------|
| SubsystemPath | да    | —       | Путь к XML-файлу подсистемы                |
| Detailed      | нет   | —       | Подробный вывод (все проверки, включая успешные) |
| MaxErrors     | нет   | 30      | Остановиться после N ошибок                |
| OutFile       | нет   | —       | Записать результат в файл                  |

## Команда

```powershell
python ".agents/skills/subsystem-validate/scripts/subsystem-validate.py" -SubsystemPath "Subsystems/Продажи"
python ".agents/skills/subsystem-validate/scripts/subsystem-validate.py" -SubsystemPath "Subsystems/Продажи.xml"
```
