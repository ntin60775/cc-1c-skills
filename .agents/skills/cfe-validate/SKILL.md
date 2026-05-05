---
name: cfe-validate
description: 1C CFE extension - validate XML sources after create/edit.
---

# $cfe-validate — валидация расширения конфигурации (CFE)

Проверяет структурную корректность расширения: XML-формат, свойства, состав, заимствованные объекты. Аналог `$cf-validate`, но для расширений.

## Параметры

| Параметр      | Обяз. | Умолч. | Описание                                        |
|---------------|:-----:|---------|-------------------------------------------------|
| ExtensionPath | да    | —       | Путь к каталогу или Configuration.xml расширения |
| Detailed      | нет   | —       | Подробный вывод (все проверки, включая успешные)  |
| MaxErrors     | нет   | 30      | Остановиться после N ошибок                      |
| OutFile       | нет   | —       | Записать результат в файл                        |

## Команда

```bash
python .agents/skills/cfe-validate/scripts/cfe-validate.py -ExtensionPath "src"
python .agents/skills/cfe-validate/scripts/cfe-validate.py -ExtensionPath "src/Configuration.xml"
```
