import pytest
from unittest.mock import patch
import main

def test_add_task():
    main.tasks = []  # очищаємо список перед тестом
    with patch('builtins.input', return_value='Тестове завдання'):
        main.add_task()
    assert len(main.tasks) == 1
    assert main.tasks[0]['name'] == 'Тестове завдання'
    assert main.tasks[0]['status'] == 'New'

def test_update_status():
    main.tasks = [{'name': 'Тестове завдання', 'status': 'New'}]
    with patch('builtins.input', side_effect=['Тестове завдання', 'Done']):
        main.update_status()
    assert main.tasks[0]['status'] == 'Done'

def test_delete_task():
    main.tasks = [{'name': 'Тестове завдання', 'status': 'New'}]
    with patch('builtins.input', return_value='Тестове завдання'):
        main.delete_task()
    assert len(main.tasks) == 0


