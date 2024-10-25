# Asyncio

### Решение ModuleNotFoundError: No module named 'util'


1. Откройте файл активации виртуального окружения. На Windows это обычно файл activate.bat, находящийся в директории _.venv\Scripts._
Добавьте текущую директорию проекта в PYTHONPATH.
Откройте файл activate.bat в текстовом редакторе и добавьте следующую строку в конце файла: `set PYTHONPATH=%PYTHONPATH%;%CD%`
Здесь %CD% добавит текущую директорию (откуда запускается окружение) в переменную PYTHONPATH.

2. Вариант для VSCode: Отредактируйте launch.json В соответствии:
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceFolder}${pathSeparator}${env:PYTHONPATH}"
            }
        }
    ]
}
```

