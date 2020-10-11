from unittest.mock import patch
from unittest import mock
import unittest
import os

from source import showTodo, editTodo, removeTodo, \
    addTodo, checkIfFileIsEmpty, checkIfFileExists, \
    getJson, getTitle, getDesc

from counter import readFile, incValue

FILE = 'fixtures/todo.json'
NEW_FILE = 'fixtures/new_todo.json'
NOT_FILE = 'fixtures/this_file_doesnt_exists.json'
EMPTY_FILE = 'fixtures/empty.json'
EDITED_FILE = 'fixtures/edited_todo.json'
DELETED_FILE = 'fixtures/removed_todo.json'
COUNTER = 'fixtures/counter.json'


class TestCounter(unittest.TestCase):
    def test_read_counter(self):
        """
        Test if function read value from 'counter.json' and if file doesn't
        exists, it creates it
        :return:
        int
        """
        counter_value = readFile(COUNTER)
        os.remove(COUNTER)
        self.assertEqual(counter_value, 0)

    def test_inc_counter(self):
        """
        Tests if function increases value by 1 in 'counter.json'
        :return:
        int
        """
        current_value = readFile(COUNTER) + 1
        incValue(COUNTER)
        after_inc = readFile(COUNTER)
        self.assertEqual(current_value, after_inc)


class TestGetData(unittest.TestCase):
    @patch('builtins.input', return_value='test0')
    def test_input_title(self, input):
        """
        Tests if user provided data for title
        :param input:
        :return:
        string
        """
        self.assertEqual(getTitle(), 'test0')

    @patch('builtins.input', return_value='test0')
    def test_input_desc(self, input):
        """
        Tests if user provided data for description
        :param input:
        :return:
        string
        """
        self.assertEqual(getDesc(), 'test0')


class TestAddTask(unittest.TestCase):
    @mock.patch('source.addTodo', create=True)
    def test_add_todo_no_file(self, mocked_input):
        """
        Tests if task is added when file doesnt exists
        :return:
        Dict
        """
        addTodo()

    def test_add_todo(self):
        """
        Tests if task is added when file exists
        :return:
        Dict
        """
        pass


class TestShowTodo(unittest.TestCase):
    def test_file_found(self):
        """
        Determine if file exists
        :return:
        Bool
        """
        result = checkIfFileExists(NOT_FILE)
        self.assertEqual(result, False)

    def test_empty_file(self):
        """
        Determine if file is empty
        :return:
        Bool
        """
        result = checkIfFileIsEmpty(EMPTY_FILE)
        self.assertEqual(result, True)

    def test_view_data(self):
        """
        Prints content of file
        :return:
        Dict
        """
        file_dict = {"0": {"Title": "opjdaspjoao", "Description": "sdaiosdjopdias"},
                     "1": {"Title": "asdphasdi", "Description": "daohasdip"}}
        result = showTodo(FILE)
        self.assertDictEqual(result, file_dict)


class TestEditTodo(unittest.TestCase):
    def test_edit_todo(self):
        """
        Test that user can edit specified task
        :return:
        Dict
        """
        help_dict = getJson(EDITED_FILE)
        editTodo(FILE)
        result = getJson(FILE)
        self.assertDictEqual(result, help_dict)

    def test_edit_invalid_id_todo(self):
        """
        Test that user cant edit record which doesnt exists
        :return:
        0
        """
        result = editTodo(FILE)
        self.assertEqual(result, 0)


class TestRemoveTodo(unittest.TestCase):
    def test_remove_invalid_id_todo(self):
        """
        Test that user cant remove record which doesnt exists
        :return:
        0
        """
        result = removeTodo(FILE)
        self.assertEqual(result, 0)

    def test_remove_todo(self):
        """
        Test that user can remove record
        :return:
        Dict
        """
        help_dict = getJson(DELETED_FILE)
        removeTodo(FILE)
        result = getJson(FILE)
        self.assertDictEqual(result, help_dict)


if __name__ == '__main__':
    unittest.main()
