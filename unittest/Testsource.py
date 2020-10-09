import unittest
import os
from source import showTodo, editTodo, removeTodo, insertData, checkIfFileIsEmpty, checkIfFileExists, getJson

file = 'fixtures/todo.json'
not_file = 'fixtures/this_file_doesnt_exists.json'
edited_file = 'fixtures/edited_todo.json'
deleted_file = 'fixtures/removed_todo.json'


class TestAddTodo(unittest.TestCase):
    def test_insert_data(self):
        pass


class TestShowTodo(unittest.TestCase):
    def test_file_found(self):
        """
        Determine if file exists
        :return:
        Bool
        """
        result = checkIfFileExists(not_file)
        self.assertEqual(result, False)

    def test_empty_file(self):
        """
        Determine if file is empty
        :return:
        Bool
        """
        result = checkIfFileIsEmpty(file)
        self.assertEqual(result, True)

    def test_view_data(self):
        """
        Prints content of file
        :return:
        Dict
        """
        file_dict = {"0": {"Title": "opjdaspjoao", "Description": "sdaiosdjopdias"},
                     "1": {"Title": "asdphasdi", "Description": "daohasdip"}}
        result = showTodo(file)
        self.assertDictEqual(result, file_dict)


class TestEditTodo(unittest.TestCase):
    def test_edit_todo(self):
        """
        Test that user can edit specified task
        :return:
        Dict
        """
        help_dict = getJson(edited_file)
        editTodo(file)
        result = getJson(file)
        self.assertDictEqual(result, help_dict)

    def test_edit_invalid_id_todo(self):
        """
        Test that user cant edit record which doesnt exists
        :return:
        0
        """
        result = editTodo(file)
        self.assertEqual(result, 0)


class TestRemoveTodo(unittest.TestCase):
    def test_remove_invalid_id_todo(self):
        """
        Test that user cant remove record which doesnt exists
        :return:
        0
        """
        result = removeTodo(file)
        self.assertEqual(result, 0)

    def test_remove_todo(self):
        """
        Test that user can remove record
        :return:
        Dict
        """
        help_dict = getJson(deleted_file)
        removeTodo(file)
        result = getJson(file)
        self.assertDictEqual(result, help_dict)


if __name__ == '__main__':
    unittest.main()
